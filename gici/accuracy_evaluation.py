# compute accuracy (RMSE)

import argparse
import pandas as pd
import numpy as np
import os


def main(extimated_file, algo_type):
    # 读取两个文件
    estimate_df = pd.read_csv(extimated_file)  # 估计数据
    truth_df = pd.read_csv('ground_truth.csv')        # 真值数据

    # 合并数据（仅保留时间匹配的行）
    merged_df = pd.merge(estimate_df, truth_df, on='TOW_s', suffixes=('_est', '_truth'))
    print(merged_df)

    # 计算误差（估计值 - 真值）
    merged_df['E_error'] = merged_df['E_m_est'] - merged_df['E_m_truth']
    merged_df['N_error'] = merged_df['N_m_est'] - merged_df['N_m_truth']
    merged_df['U_error'] = merged_df['U_m_est'] - merged_df['U_m_truth']

    # 计算均方根误差（RMSE）
    def rmse(series):
        return np.sqrt(np.mean(series ** 2))

    e_rmse = rmse(merged_df['E_error'])
    n_rmse = rmse(merged_df['N_error'])
    u_rmse = rmse(merged_df['U_error'])

    print(f"E方向的RMSE: {e_rmse:.4f} m")
    print(f"N方向的RMSE: {n_rmse:.4f} m")
    print(f"U方向的RMSE: {u_rmse:.4f} m")

    # 将结果保存到accuracy.csv
    results = {
        'type': [algo_type],
        'E_RMSE': [e_rmse],
        'N_RMSE': [n_rmse],
        'U_RMSE': [u_rmse]
    }

    # 如果文件存在则追加，否则创建新文件
    if os.path.exists('accuracy.csv'):
        # 追加模式，不写入列名
        pd.DataFrame(results).to_csv('accuracy.csv', mode='a', header=False, index=False)
    else:
        # 创建新文件，写入列名
        pd.DataFrame(results).to_csv('accuracy.csv', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default="gici-spp", help="the type of algorithm.")
    parser.add_argument("--file_path", type=str, default="spp_urban_medium_solution.csv", help="estimated position file.")

    args = parser.parse_args()

    main(extimated_file=args.file_path, algo_type=args.type)