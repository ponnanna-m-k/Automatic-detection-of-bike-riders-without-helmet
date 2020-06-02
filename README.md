# Automatic Detection of bike riders without helmet

Automatic Detection of bike riders without helmet is an application which is used to check if a motorcyclist is wearing a helmet or not using OpenCV and also with the help of cascade classifiers. The accuracy of this particular application is not upto the mark as of now. Looking forward for improvement.

# Phase-I: Detection Bike-riders 
This phase involves detection of bike-riders in a frame.  This phase involves two steps : feature extraction and classification. 
1) Feature Extraction : Object classification requires some suitable representation of visual features. HOG and SIFT are proven to be efficient for object detection. 
2) Classification: After feature extraction, next step is to classify them as ‘bike-riders’ vs ‘other’ objects. Thus, this requires a binary classifier. Any binary classifier can be used here, however we choose SVM due to its robustness in classification performance even when trained from less number of feature vectors . 

# Phase-II: Detection of Bike-riders Without Helmet 
After the bike-riders are detected in the previous phase, the next step is to determine if bike rider is using a helmet or not. Usual face detection algorithms would not be sufficient for this phase due to following reasons :

i) Low resolution poses a great challenge to capture facial details such as eyes, nose, mouth. 
ii) Angle of movement of bike may be at obtuse angles. In such cases, face may not be visible at all. 

So proposed framework detects region around head and then proceed to determine whether bike-rider is using helmet or not. In order to locate the head of bike-rider, proposed framework uses the fact that appropriate location of helmet will probably be in upper areas of bike rider. 
