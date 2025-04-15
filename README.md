# AAE6102 Lab Report

This lab report is jointly prepared by CUI Gege (23125624R), IP Chun Man Ben (23062929R), LAM Yat Long (23039591R), LIU Mingjiang (23133185R), YAN Xinhao (23125502R), and ZHANG Xuan (23125486R).

In this lab report, the open-source RTKLIB GNSS library is used. The dataset used is "20210521.medium-urban.whampoa.ublox.f9p.obs" provided in the UrbanNav Dataset. The trajectory of this dataset is shown in the below figure:

![UrbanNav-HK-Deep-Urban-1](https://github.com/user-attachments/assets/16f5c656-2b12-437b-ac82-0fb8d51c76dd)

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

We consider Set A as the baseline to investigate how the changes in parameter affect accuracy, processing speed and robustness. Please refer to the file "SetA-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time for Set A.

### 1.3 Set B
#### Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Static |
| Filter Setting	(Filter Type)| Forward |
| Satellite Selection Criteria (SNR Mask)	| 0 dBHz |

Note that the parameters used in Set B are the same as those in Set A except that the position mode is static for Set B.

The trajectory generated is shown in the below figure:

![trajectory-b](https://github.com/user-attachments/assets/5948cf0d-7697-4f18-95e1-7f58acba76b1)

The position with time is shown in the below figure:

![position-b](https://github.com/user-attachments/assets/7a441eb3-5cc7-48ae-b395-a1ce035cb930)

Please refer to the file "SetB-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. The shape of the trajectory in Set A is similar to the true trajectory while the shape of the trajectory in Set B is almost dissimilar to the true trajectory. It implies that Set A demonstrates a better accuracy than Set B.

II. Processing Speed. There is no significant change in computation time in processing Set A and Set B.

III. Robustness. In Set B from 06:33 to 06:50, the position of the user's receiver antenna cannot be determined in most of the time as illustrated in the position plot for Set B. Nevertheless, the user's position can almost be obtained continuously throughout the entire journey in Set A when compared to Set B. It implies that Set B demonstrates a degraded robustness. 

### 1.4 Set C

#### Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Kinematic |
| Filter Setting	(Filter Type)| Backward |
| Satellite Selection Criteria (SNR Mask)	| 0 dBHz |

Note that the parameters used in Set C are the same as those in Set A except that the Filter Type is Backward for Set C.

The trajectory generated is shown in the below figure:

![trajectory-c](https://github.com/user-attachments/assets/f878b14c-f5f3-47e2-9069-c3fd681f237b)

The position with time is shown in the below figure:

![position-c](https://github.com/user-attachments/assets/dbf89072-ea2e-4b65-9077-e702c247945c)

Please refer to the file "SetC-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. Two shape tips can be observed in the bottom right corner of the trajectory in Set A corresponding to the presence of tall building while the accuracy of Set C near the tall building (located near the bottom right corner) performs better than Set A. For the remaining proportion of the trajectory plots, both Set A and Set C has a relative high accuracy in open street environment and a small degraded accuracy for the environments with medium-height buildings and narrow streets. However, the accuracy of Set C in the wide street is worse than Set A.

II. Processing Speed. There is no significant change in computation time in processing Set A and Set C.

III. Robustness. The user's position can almost be obtained continuously throughout the entire journey in both Set A and Set C, which implies that both sets display similar robustness. 

### 1.5 Set D

#### Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Kinematic |
| Filter Setting	(Filter Type)| Combined |
| Satellite Selection Criteria (SNR Mask)	| 0 dBHz |

Note that the parameters used in Set D are the same as those in Set A except that the Filter Type is Combined for Set D.

The trajectory generated is shown in the below figure:

![trajectory-d](https://github.com/user-attachments/assets/0ae429e8-9985-4451-ad60-5f8870d0f600)

The position with time is shown in the below figure:

![position-d](https://github.com/user-attachments/assets/d19e8518-9919-40a5-aec4-a0ed81ccaf59)

Please refer to the file "SetD-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. Two shape tips can be observed in the bottom right corner of the trajectory in Set A corresponding to the presence of tall building while the accuracy of Set D near the tall building (located near the bottom right corner) performs better than Set A. For the remaining proportion of the trajectory plots, both Set A and Set D has a relative high accuracy in open street environment and a small degraded accuracy for the environments with medium-height buildings and narrow streets. However, the accuracy of Set D in the wide street is worse than Set A.

II. Processing Speed. There is no significant change in computation time in processing Set A and Set D.

III. Robustness. The user's position can almost be obtained continuously throughout the entire journey in both Set A and Set D. However, shape chances can hardly be observed in E-W plot and N-S plot for Set D while shape changes can be observed between 06:51 and 06:52 in Set A. However, shape changes in u-D plot can be observed in both Set A and Set D. Therefore, Set D has a slightly better robustness than Set A. 

### 1.6 Set E

#### Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Kinematic |
| Filter Setting	(Filter Type)| Combined - no phase reset |
| Satellite Selection Criteria (SNR Mask)	| 0 dBHz |

Note that the parameters used in Set E are the same as those in Set A except that the Filter Type is Combined for Set E.

The trajectory generated is shown in the below figure:

![trajectory-e](https://github.com/user-attachments/assets/99c02ea0-31cc-4835-a2a2-7aaaa6e7c2d6)

The position with time is shown in the below figure:

![position-e](https://github.com/user-attachments/assets/fa4bbb73-8ebc-4226-bec2-a30fc9685ef2)

Please refer to the file "SetE-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. Two shape tips can be observed in the bottom right corner of the trajectory in Set A corresponding to the presence of tall building while the accuracy of Set E near the tall building (located near the bottom right corner) performs better than Set A. For the remaining proportion of the trajectory plots, both Set A and Set E has a relative high accuracy in open street environment and a small degraded accuracy for the environments with medium-height buildings and narrow streets. However, the accuracy of Set E in the wide street is worse than Set A.

II. Processing Speed. There is no significant change in computation time in processing Set A and Set E.

III. Robustness. The user's position can almost be obtained continuously throughout the entire journey in both Set A and Set E. However, shape chances can hardly be observed in E-W plot and N-S plot for Set E while shape changes can be observed between 06:51 and 06:52 in Set A. However, shape changes in u-D plot can be observed in both Set A and Set E. Therefore, Set E has a slightly better robustness than Set A. 

### 1.7 Set F: Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Kinematic |
| Filter Setting	(Filter Type)| Forward |
| Satellite Selection Criteria (SNR Mask)	| 5 dBHz |

Note that the parameters used in Set F are the same as those in Set A except that the SNR Mask is 5 dBHz for Set F.

The trajectory generated is shown in the below figure:

![trajectory-f](https://github.com/user-attachments/assets/f2fe51a0-4d60-4801-8a68-02045cb6583a)

The position with time is shown in the below figure:

![position-f](https://github.com/user-attachments/assets/16740e02-97c3-445f-878e-c823d3bcd00a)

Please refer to the file "SetF-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. The shapes of the trajectories of both Set A and Set F are similar, and both exhibit sinigificant error with tall building, small error with medium-height building or narrow streets, and excellent accuracy in wide street. It implies that the accuracy of the both sets are similar.

II. Processing Speed. There is no significant change in computation time in processing Set A and Set F.

III. Robustness. The user's position can almost be obtained continuously throughout the entire journey in both Set A and Set F. However, shape chances can hardly be observed in E-W plot and N-S plot for Set F while shape changes can be observed between 06:51 and 06:52 in Set A. However, shape changes in u-D plot can be observed in both Set A and Set F. Therefore, Set F has a slightly better robustness than Set A. 



## 2. Strengths and Limitations

Strengths: Flexibility, robustness, ease of use.

Limitations: Computational efficiency, lack of specific features.

### 2.1. Static Position with Forward Filter

#### Strengths
##### Flexibility: 
Can be readily applied in static environments. It is very simple to deploy it in various scenarios.
##### Robustness:
Provides a reliable and consistent filtering approach that can handle moderate noise levels.
##### Ease of Use:
Straightforward implementation that requires minimal tuning and parameterization.

#### Limitations
##### Computational Efficiency:
While sufficient for simpler scenarios, the approach may become less efficient with increased data complexity.
##### Lack of Specific Features:
Does not incorporate advanced features tailored to specialized dynamic applications.

### 2.2. RTK with Forward Filter

#### Strengths
##### Flexibility: 
Can be readily applied in static environments. It is very simple to deploy it in various scenarios.
##### Robustness:
Provides a reliable and consistent filtering approach that can handle moderate noise levels.
##### Ease of Use:
Straightforward implementation that requires minimal tuning and parameterization.

#### Limitations
##### Computational Efficiency:
While sufficient for simpler scenarios, the approach may become less efficient with increased data complexity.
##### Lack of Specific Features:
Does not incorporate advanced features tailored to specialized dynamic applications.


### 2.3. RTK with Backward Filter

#### Strengths
##### Flexibility: 
Can be readily applied in static environments. It is very simple to deploy it in various scenarios.
##### Robustness:
Provides a reliable and consistent filtering approach that can handle moderate noise levels.
##### Ease of Use:
Straightforward implementation that requires minimal tuning and parameterization.

#### Limitations
##### Computational Efficiency:
While sufficient for simpler scenarios, the approach may become less efficient with increased data complexity.
##### Lack of Specific Features:
Does not incorporate advanced features tailored to specialized dynamic applications.

### 2.4. RTK with Combined Filter

#### Strengths
##### Flexibility: 
Can be readily applied in static environments. It is very simple to deploy it in various scenarios.
##### Robustness:
Provides a reliable and consistent filtering approach that can handle moderate noise levels.
##### Ease of Use:
Straightforward implementation that requires minimal tuning and parameterization.

#### Limitations
##### Computational Efficiency:
While sufficient for simpler scenarios, the approach may become less efficient with increased data complexity.
##### Lack of Specific Features:
Does not incorporate advanced features tailored to specialized dynamic applications.



## 3. Kaggle competition

Submit your positioning result and beat your classmate at Kaggle competition

## 4. Suggestions for Improvement

Provide recommendations to enhance:

The selected GNSS library,
The parameter tuning process
