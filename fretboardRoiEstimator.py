import cv2
import numpy as np


class FretboardRoiEstimator():
    
    hasFretboardKeyPoints = False
    fretboardKeyPoints = np.array(0)
    fretboardKeyPointsImage = np.array(0)

    
   
    
    def roiSelector(self, frame):
        r = cv2.selectROI(frame)
        
        # Crop image
        roi = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        
        return roi
        
        
    def detectORBKeypoints(self, frame):
        
        # Initiate ORB detector
        orb = cv2.ORB_create()
        
        # find the keypoints with ORB
        kp = orb.detect(frame,None)
        
        # compute the descriptors with ORB
        kp, des = orb.compute(frame, kp)
        
        self.fretboardKeyPoints = kp
        self.hasFretboardKeyPoints = True

        # draw only keypoints location,not size and orientation
        self.fretboardKeyPointsImage = cv2.drawKeypoints(frame, kp, None, color=(0,255,0), flags=0)
    
    
    def detectSIFTKeypoints(self, frame):
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        #initialize SIFT object
        sift = cv2.SIFT_create()
        
        kp = sift.detect(gray,None)
        self.fretboardKeyPoints = kp
        self.hasFretboardKeyPoints = True
        
        self.fretboardKeyPointsImage = cv2.drawKeypoints(frame,kp, None, color=(0,255,0),flags=0)
        
    
    #return keypoints of fretboard if available
    def getFretboardKeypoints(self):
        if self.hasFretboardKeyPoints:
            return self.fretboardKeyPoints
    
    #return keypoints image of fretboard if available
    def getFretboardKeypointsImage(self):
        if self.hasFretboardKeyPoints:
            return self.fretboardKeyPointsImage
        

    