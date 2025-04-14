# AAE6102 Lab Report

This lab report is jointly prepared by CUI Gege (23125624R), IP Chun Man Ben (23062929R), LAM Yat Long (23039591R), LIU Mingjiang (23133185R), YAN Xinhao (23125502R), and ZHANG Xuan (23125486R).

In this lab report, the open-source RTKLIB GNSS library is used. The dataset used is "20210521.medium-urban.whampoa.ublox.f9p.obs" provided in the UrbanNav Dataset.

## 1. Parameter Tuning and Effects

### 1.1. Parameter Settings

| Parameters | Value |
|-----------------|-----------------|
| Elevation Mask	| 15 degrees |
| Ionospheric/Tropospheric Correction	| Broadcast; Saastamoir |
| Satellite Ephemeris/clock	| Broadcast |
| Excluded Satellites (+PRN: Included)	| (Nil) |
| Satellites selected	| GPS, GLO, Galileo |

### 1.2 Set A: Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Kinematic |
| Filter Setting	(Filter Type)| Forward |
| Satellite Selection Criteria (SNR Mask)	| 0 dBHz |

The trajectory generated is shown in the below figure:

![Trajectory](https://github.com/user-attachments/assets/850f8df7-0fff-44f3-92ad-cda5ee04e87e)

The position with time is shown in the below figure:

![position](https://github.com/user-attachments/assets/09c09477-2854-4f44-9f65-0d41fe84f750)

Please refer to the file "SetA-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

Explain how parameter changes affected:

Accuracy,
Processing speed,
Robustness

## 2. Strengths and Limitations

Strengths: Flexibility, robustness, ease of use.

Limitations: Computational efficiency, lack of specific features.

## 3. Kaggle competition

Submit your positioning result and beat your classmate at Kaggle competition

## 4. Suggestions for Improvement

Provide recommendations to enhance:

The selected GNSS library,
The parameter tuning process
