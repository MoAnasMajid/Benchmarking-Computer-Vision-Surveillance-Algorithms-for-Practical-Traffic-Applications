# **Explanation of each part of the code**

## *Dataset Used-*

Multiple Object Tracking (MOT) dataset is a well-known benchmark in the object tracking community. It contains real-time videos captured in various scenarios. Here I have used MOT17-09-SDP dataset from one of the MOT17 datasets. This dataset contains-

i. RAW video: These are sequences of frames where the people need to be detected and tracked over multiple frames. This video is a pedestrian street scene filmed from a low angle.

ii. Ground truth annotations: These are text files that provide the true locations and identities of people at different time stamps. Each line in these  files typically includes information like frame number, object ID, bounding box coordinates, and more. 


## *Object detection and tracking-*

For real-time object detection system, I have used YOLO (You Only Look Once) algorithm . It predicts bounding boxes on each person in the frame along with the confidence score which is a estimate probability that the detected object belongs to a certain class (person in our case). Though, YOLO is used for object detection, but it's latest version YOLOv8 allows object tracking.

### **Steps-** 

1. Installing python libraries (ultralytics, opencv) and importing their packages (YOLO, cv2).

2. Loading the MOT dataset which includes the video file. From (https://motchallenge.net) ,I have used MOT17 dataset, in particularly MOT17-09-SDP dataset which includes a short 
   pedestrian street scene filmed along with the gt file. The video was downloaded from here and was provided to the code as an input.  

3. Running YOLOv8.py to apply object tracking and getting the annotated text file.

### **Code-**

https://github.com/MoAnasMajid/Benchmarking-Computer-Vision-Surveillance-Algorithms-for-Practical-Traffic-Applications/blob/main/Scripts/YOLOv8.py


## *Benchmarking-*

HOTA (Higher Order Tracking Accuracy) is a method to evaluate the performance of the object tracking algorithm.

### **Steps to compute HOTA metrics-**

1. Cloning the TrackEval github repository which is an official evaluation kit for MOT datasets.
   https://github.com/JonathonLuiten/TrackEval/tree/master

2. If we want to run tracking evaluation on our own data, we need to prepare evaluation data. Broadly, there are two steps:

i. Setup benchmark, i.e., ground-truth tracking
ii. Add tracker you want to evaluate

    ### **A. Setup benchmark-**
    
      i. Ground-truth tracking data is to be placed under TrackEval/data/gt/mot_challenge/<Your_Challenge_Name>. In our case, let’s call the new challenge as ABC-train, i.e., create a 
         directory content/TrackEval/data/gt/mot_challenge/ABC-train/ABC-01/gt.
         
      ii. Here we need to place two files in the directory- 
          i. gt.txt (one we dowloaded from the MOT17-09-SDP dataset)
          ii. seqinfo.ini file with the following contents:
             [Sequence]
             name=ABC
             seqLength= number of frames (eg. 800)
    
    ### **B. Add tracker you want to evaluate-**
    
      i. Create a directory content/TrackEval/data/trackers/mot_challenge/ABC-train where we will place our tracker outputs. Let’s call this tracker MyTracker. To add this tracker for 
         evaluation, create TrackEval/data/trackers/mot_challenge/ABC-train/MyTracker/data.
    
      ii. Now in this data folder, we are supposed to place our tracking result (the annotated text file saved after applying YOLO).


3. Run Compute HOTA metrics.py.

4. Analyze the results.

### **Code-**

https://github.com/MoAnasMajid/Benchmarking-Computer-Vision-Surveillance-Algorithms-for-Practical-Traffic-Applications/blob/main/Scripts/Compute%20HOTA%20metrics.py
