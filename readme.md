# **Explanation of each part of the code**

##Dataset Used-

Multiple Object Tracking (MOT) dataset is a well-known benchmark in the object tracking community. It contains real-time videos captured in various scenarios. Here I have used MOT17-09-SDP dataset from one of the MOT17 datasets. This dataset contains-

i. RAW video: These are sequences of frames where the people need to be detected and tracked over multiple frames. This video is a pedestrian street scene filmed from a low angle.

ii. Ground truth annotations: These are text files that provide the true locations and identities of people at different time stamps. Each line in these  files typically includes information like frame number, object ID, bounding box coordinates, and more. 

##Object detection and tracking-

For real-time object detection system, I have used YOLO (You Only Look Once) algorithm . It predicts bounding boxes on each person in the frame along with the confidence score which is a estimate probability that the detected object belongs to a certain class (person in our case). Though, YOLO is used for object detection, but it's latest version YOLOv8 allows object tracking.

**Steps-** 
i. Installing python libraries (ultralytics, opencv) and importing their packages (YOLO, cv2).
ii. Loading the MOT dataset which includes the video file.
iii. Loading the model (yolov8n.pt).
iv. Preprocessing the data to get the video properties.
v. Creating an annotated txt file to get the data of each detected frame and tracking it across multiple time stamps.
vi. Running model on each frame using while loop.
vii. Saving the annotated file.

**Code-**
https://github.com/MoAnasMajid/Benchmarking-Computer-Vision-Surveillance-Algorithms-for-Practical-Traffic-Applications/blob/main/YOLOv8%20model

##Benchmarking-

HOTA (Higher Order Tracking Accuracy) is a method to evaluate the performance of the object tracking algorithm.

**Steps to compute HOTA metrics-**
i. Preparing Evaluation data. Placing the ground truth annotated text file and YOLO model predicted file on the TrackEval's gt and trackers folders.
ii. Cloning the TrackEval github repository which is an official evaluation kit for MOT datasets.
iii. Running TrackEval's run_mot_challenge script which can run various benchmarks. 
iv. Analyzing the results.

**Code-**
https://github.com/MoAnasMajid/Benchmarking-Computer-Vision-Surveillance-Algorithms-for-Practical-Traffic-Applications/blob/main/Computing%20HOTA%20metrics
