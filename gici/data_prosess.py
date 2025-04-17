import pynmea2
import pandas as pd




import pandas as pd
import numpy as np
import argparse


def lla_to_enu(lat, lon, h, lat0, lon0, h0):
    """
    将经纬高坐标 (LLA) 转换为 ENU (东-北-天) 坐标系
    参数:
        lat, lon, h: 目标点的纬度(deg)、经度(deg)、高度(m)
        lat0, lon0, h0: 局部坐标系原点的纬度、经度、高度
    返回:
        (e, n, u): 东、北、天方向的坐标 (m)
    """
    # 将经纬度转换为弧度
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    lat0_rad = np.radians(lat0)
    lon0_rad = np.radians(lon0)

    # WGS84椭球参数
    a = 6378137.0  # 地球长半轴 (m)
    e_sq = 6.69437999013e-3  # 第一偏心率平方

    # 计算目标点相对于原点的地心坐标偏移 (ECEF)
    N = a / np.sqrt(1 - e_sq * np.sin(lat_rad)**2)
    x = (N + h) * np.cos(lat_rad) * np.cos(lon_rad)
    y = (N + h) * np.cos(lat_rad) * np.sin(lon_rad)
    z = (N * (1 - e_sq) + h) * np.sin(lat_rad)

    N0 = a / np.sqrt(1 - e_sq * np.sin(lat0_rad)**2)
    x0 = (N0 + h0) * np.cos(lat0_rad) * np.cos(lon0_rad)
    y0 = (N0 + h0) * np.cos(lat0_rad) * np.sin(lon0_rad)
    z0 = (N0 * (1 - e_sq) + h0) * np.sin(lat0_rad)

    dx = x - x0
    dy = y - y0
    dz = z - z0

    # 构建旋转矩阵 (ECEF -> ENU)
    sin_lat0 = np.sin(lat0_rad)
    cos_lat0 = np.cos(lat0_rad)
    sin_lon0 = np.sin(lon0_rad)
    cos_lon0 = np.cos(lon0_rad)

    # ENU坐标计算
    e = -sin_lon0 * dx + cos_lon0 * dy
    n = -sin_lat0 * cos_lon0 * dx - sin_lat0 * sin_lon0 * dy + cos_lat0 * dz
    u = cos_lat0 * cos_lon0 * dx + cos_lat0 * sin_lon0 * dy + sin_lat0 * dz

    return e, n, u


def pos_data_extract(input_file, output_file):
    # process RTKLIB .pos file

    # Read the file line by line, skipping headers and comments
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            if line.startswith('%') or line.strip() == '':
                continue  # Skip comments and empty lines
            parts = line.strip().split()
            
            # Case 1: If time is in "yyyy/mm/dd hh:mm:ss.sss" (UTC/GPST)
            if '/' in parts[0]:  
                time_parts = parts[1].split(':')  # Extract hh:mm:ss
                tow_s = (float(time_parts[0]) * 3600 + 
                            float(time_parts[1]) * 60 + 
                            float(time_parts[2])) - (6 * 3600 + 29 * 60 + 2) + 455342.0
            
            # Case 2: If time is already in GPS Week/TOW (e.g., "2445 345678.900")
            else:  
                tow_s = float(parts[1])
            
            lat, lon, height = map(float, parts[2:5])  # Adjust indices as needed
            # use first ground_truth lat/lon as reference
            e, n, u = lla_to_enu(lat, lon, height, 22.30155854166667, 114.19030853055555, 0)

            data.append([tow_s, e, n, u])

    # Create DataFrame and save as CSV
    df = pd.DataFrame(data, columns=['TOW_s', 'E_m', 'N_m', 'U_m'])
    df.to_csv(output_file, index=False)


def nmea_data_extract(input_file, output_file):
    # process GICI-LIB nmea-type file

    # Lists to store parsed data
    tow_s_list = []
    e_list = [] 
    n_list = []
    u_list = []

    # Read the NMEA file and parse relevant sentences (GGA for lat/lon/height)
    with open(input_file, 'r') as f:
        for line in f:
            if line.startswith('$GPGGA'):  # 仅处理GPGGA语句（包含时间、经纬度、高度）
                try:
                    msg = pynmea2.parse(line.strip())
                    # print(msg.latitude)
                    
                    # Extract data from GGA (Global Positioning System Fix Data)
                    if isinstance(msg, pynmea2.types.talker.GGA):
                        # Time of Week (TOW) may not be directly in NMEA; use timestamp if needed
                        # Note: NMEA does not provide GPS Week; you may need another source
                        tow_s = (msg.timestamp.hour * 3600 + 
                                msg.timestamp.minute * 60 + 
                                msg.timestamp.second) - (6 * 3600 + 29 * 60 + 2) + 455342.0 + 17.0
                        
                        # Append data to lists
                        tow_s_list.append(tow_s)
                        # use first ground_truth lat/lon as reference
                        e, n, u = lla_to_enu(round(msg.latitude, 9), round(msg.longitude, 9), round(msg.altitude, 9), 22.301558542, 114.190308531, 0.0)
                        e_list.append(e)
                        n_list.append(n)
                        u_list.append(u)
                        
                except pynmea2.ParseError:
                    continue  # Skip invalid lines

    # Create a DataFrame and save as CSV
    df = pd.DataFrame({
        'TOW_s': tow_s_list,
        'E_m': e_list,
        'N_m': n_list,
        'U_m': u_list
    })

    df.to_csv(output_file, index=False)


def truth_data_extract(input_file, output_file):
    # process ground truth file
    data = []
    with open(input_file, 'r') as f:
        lines = f.readlines()[2:]
        for line in lines:
            parts = line.strip().split()
            
            tow_s = float(parts[2])
            lat = float(parts[3]) + float(parts[4]) / 60 + float(parts[5]) / 3600
            lon = float(parts[6]) + float(parts[7]) / 60 + float(parts[8]) / 3600
            height = float(parts[9])
            # use first ground_truth lat/lon as reference
            e, n, u = lla_to_enu(lat, lon, height, 22.30155854166667, 114.19030853055555, 0)

            data.append([tow_s, e, n, u])

    # Create DataFrame and save as CSV
    df = pd.DataFrame(data, columns=['TOW_s', 'E_m', 'N_m', 'U_m'])
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default="pos", help="file type: pos: rtklib .pos; nmea: gici .txt; truth: ground truth file.")
    parser.add_argument("--input_file", type=str, default="20210521.medium-urban.whampoa.ublox.f9p.pos", help="input file path.")
    parser.add_argument("--output_file", type=str, default="rtk_rtklib_urban_medium_solution.csv", help="output file path.")

    args = parser.parse_args()

    if args.type == "pos":
        pos_data_extract(input_file=args.input_file, output_file=args.output_file)
    elif args.type == "nmea":
        nmea_data_extract(input_file=args.input_file, output_file=args.output_file)
    elif args.type == "truth":
        truth_data_extract(input_file=args.input_file, output_file=args.output_file)
    else:
        raise NotImplementedError