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

![SetA-trajectory](https://github.com/user-attachments/assets/64629d42-5518-41bd-aad3-f5304f66d4f8)

The position with time is shown in the below figure:

![SetA-position](https://github.com/user-attachments/assets/5fd7fc7b-1558-4ad7-abbe-cee41a517dbe)

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

![SetB-trajectory](https://github.com/user-attachments/assets/e3838578-cdd8-49af-b270-6f570affc0fa)

The position with time is shown in the below figure:

![SetB-position](https://github.com/user-attachments/assets/6edbc550-44d3-4e5d-b957-23fc49ec43cf)

Please refer to the file "SetB-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. The shape of the trajectory in Set A is similar to the true trajectory while the shape of the trajectory in Set B is almost dissimilar to the true trajectory. It implies that Set A demonstrates a better accuracy than Set B.

II. Processing Speed. There is no significant change in computation time in processing Set A and Set B.

III. Robustness. In Set B from 06:34 to 06:35 abd from 06:37 to 06:41, the position of the user's receiver antenna cannot be determined in most of the time as illustrated in the position plot for Set B. Nevertheless, the user's position can almost be obtained continuously throughout the entire journey in Set A when compared to Set B. It implies that Set B demonstrates a degraded robustness. 

### 1.4 Set C

#### Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Kinematic |
| Filter Setting	(Filter Type)| Backward |
| Satellite Selection Criteria (SNR Mask)	| 0 dBHz |

Note that the parameters used in Set C are the same as those in Set A except that the Filter Type is Backward for Set C.

The trajectory generated is shown in the below figure:

![SetC-trajectory](https://github.com/user-attachments/assets/daac7c77-d4b9-49b1-8261-0ceaa3453850)

The position with time is shown in the below figure:

![SetC-position](https://github.com/user-attachments/assets/d585469a-ae19-4f7e-a818-821c28623b01)

Please refer to the file "SetC-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. For the trajectory in the straight-line wide street section, the trajectory in Set C is more close to a straight-line trajectory than Set A, implying that Set C is more accurate than Set A in this section. For the other sections, no observable accuracy differences between Set A and Set C.

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

![SetD-trajectory](https://github.com/user-attachments/assets/03b817fa-c17c-4303-bffa-323bbc76cc2a)

The position with time is shown in the below figure:

![SetD-position](https://github.com/user-attachments/assets/ad7da523-0ce5-4ae2-a256-eaf0188451e7)

Please refer to the file "SetD-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. For the trajectory in the straight-line wide street section, the trajectory in Set D is more close to a straight-line trajectory than Set A, implying that Set D is more accurate than Set A in this section. For the other sections, no observable accuracy differences between Set A and Set D.

II. Processing Speed. There is no significant change in computation time in processing Set A and Set D.

III. Robustness. The user's position can almost be obtained continuously throughout the entire journey in both Set A and Set D, which implies that both sets display similar robustness. 

### 1.6 Set E

#### Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Kinematic |
| Filter Setting	(Filter Type)| Combined - no phase reset |
| Satellite Selection Criteria (SNR Mask)	| 0 dBHz |

Note that the parameters used in Set E are the same as those in Set A except that the Filter Type is Combined for Set E.

The trajectory generated is shown in the below figure:

![SetE-trajectory](https://github.com/user-attachments/assets/a1eb1c4e-93b8-4031-a5d9-34a4216f02fa)

The position with time is shown in the below figure:

![SetE-position](https://github.com/user-attachments/assets/0c764bc6-75ab-439e-8de2-17658c396c61)

Please refer to the file "SetE-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. For the trajectory in the straight-line wide street section, the trajectory in Set E is more close to a straight-line-like trajectory than Set A, implying that Set E is more accurate than Set A in this section. For the other sections, no observable accuracy differences between Set A and Set E.

II. Processing Speed. There is no significant change in computation time in processing Set A and Set E.

III. Robustness. The user's position can almost be obtained continuously throughout the entire journey in both Set A and Set E, impling that Set A and Set E display similar robustness.

### 1.7 Set F: Parameters Tuned

| Parameters | Value |
|-----------------|-----------------|
| Position Mode	| Kinematic |
| Filter Setting	(Filter Type)| Forward |
| Satellite Selection Criteria (SNR Mask)	| 5 dBHz |

Note that the parameters used in Set F are the same as those in Set A except that the SNR Mask is 5 dBHz for Set F.

The trajectory generated is shown in the below figure:

![SetF-trajectory](https://github.com/user-attachments/assets/19be5a62-599c-4916-946b-0a1b16a3989a)

The position with time is shown in the below figure:

![SetF-position](https://github.com/user-attachments/assets/6e8f3888-c9d5-40e2-8f99-0fae424d4207)

Please refer to the file "SetF-20210521.medium-urban.whampoa.ublox.f9p.pos" for the detailed locations with time.

#### Effects of the parameter change on accuracy, processing speed and robustness

I. Accuracy. The shapes of the trajectories of both Set A and Set F are similar, implying similar accuracy between Set A and Set F.

II. Processing Speed. The processing speed is slightly faster for Set F since the signal with SNR lower than 5dBHz will be ignored, so the amount of signals that need to be processed in Set F is smaller, which eventually gives a faster computation speed.

III. Robustness. The user's position can almost be obtained continuously throughout the entire journey in both Set A and Set F, implying similar robustness.



## 2. Strengths and Limitations

Strengths: Flexibility, robustness, ease of use.

Limitations: Computational efficiency, lack of specific features.

### 2.1. Static Position with Forward Filter

#### Strengths
##### Flexibility: 
The classical static positioning methdo can be easily applied to various scenarios.
##### Robustness:
It just provides a rough location information, so its robustness is very low.
##### Ease of Use:
It can be used in a straightforward implementation and it only requires minor tuning and parameterization.

#### Limitations
##### Computational Efficiency:
It is sufficient for some simple cases, but it may become less efficient with increased data complexity.
##### Lack of Specific Features:
Does not incorporate advanced features tailored to specialized dynamic applications.

### 2.2. RTK with Forward Filter

#### Strengths
##### Flexibility: 
The RTK with forward filter is adaptable to dynamic contexts, and thus it is suitable for some real-time applications.
##### Robustness:
It can provide accurate filtering performance under varying conditions, particularly in environments with numerous signal.
##### Ease of Use:
It has a clear framework that is relatively easy to implement and integrate into real-time systems.

#### Limitations
##### Computational Efficiency:
The real-time processing requirement may require great computational resources, which may be challenging for computation resource-constrained systems.
##### Lack of Specific Features:
It may not include specific enhancements for specialized tasks beyond standard RTK applications.


### 2.3. RTK with Backward Filter

#### Strengths
##### Flexibility: 
The RTK with backward filtering process can increase the adaptability by processing data in reverse, thus providing more accurate information.
##### Robustness:
It enhances the data integrity and accuracy by re-visiting the signals, thus reducing the impact of errors.
##### Ease of Use:
Although it involves an extra processing step, the backward filter can also be easily applied.

#### Limitations
##### Computational Efficiency:
The extra backward processing step will increase the computational load, and it processes more data than forward filter. Therefore, it consumes more computational resources.
##### Lack of Specific Features:
Although it can improve the accuracy, it still falls short in addressing specific requirements, especially for those require real-time performance.

### 2.4. RTK with Combined Filter

#### Strengths
##### Flexibility: 
Obviously, RTK with combined filter can gather both the advantages of both forward and backward filtering. Hence, it is the most flexible one for a wide range of applications.
##### Robustness:
By using dual filtering techniques, it provides enhanced error mitigation and improved overall reliability.
##### Ease of Use:
Alghough it is more complex in setup, the combined approach can achieve a balance between accuracy and performance, with clear guidelines for integration.

#### Limitations
##### Computational Efficiency:
The combined processing inherently requires greater computational power, which will present great challenges in resource-constrained environments.
##### Lack of Specific Features:
Since it possesses combined filters, it cannot be easily designed to some scenarios, because it requires both the conditions with respect to forward and backward structures.



## 3. Kaggle competition

### 3.1. Model Setting and Data Storage Format Adjustment
The utilized model setting is illustrated in the figure below, where the positioning mode is "Kinematic" and the filter type is "Combined".

![4ac43a4ef3719f204dda28996e4afe1](https://github.com/user-attachments/assets/080632d8-0c94-4dc3-a241-46c4f1fdceb3)

We first updated the data storage format. Specifically, the default time format is changed to ww ssss GPST format, as illustrated in the figure below. After making this adjustment, we ran the model to save the results in the new format.

![c2c1589f8b2a3749738796ea51b41e6](https://github.com/user-attachments/assets/8b46c84c-4712-4a22-bd28-2ef7ec075d7b)

### 3.2. Data Conversion
The original format and contents of the directly saved data are displayed in the figure below. This data was then exported and saved as a .txt file.

![image](https://github.com/user-attachments/assets/78600f91-5529-4e0a-a037-dda6f938bd27)

To ensure compatibility, we developed a Python script to convert the .txt file into a .csv format file. Both the script used for the conversion and the resulting .csv file have been saved in the Kaggle_group3 folder, which has been uploaded to this project.

### 3.3. Result Submission
The positioning results in .csv format have been submitted to the Kaggle competition under the team name "Group 3." The submission details are as follows with a public score of 1.52380.

![image](https://github.com/user-attachments/assets/83b88818-5375-4b9f-a26c-5d11735f0d95)

## 4 Comparison with Other Libraries (Optional)

If time permits, test another GNSS library using the same dataset and compare based on:

Accuracy
Ease of use
Flexibility
Computational efficiency

## 5. Suggestions for Improvement

Provide recommendations to enhance:

The selected GNSS library,
The parameter tuning process
