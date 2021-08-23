import time

import cv2
import numpy as np
start=time.time()
cap=cv2.VideoCapture(0)

whT=320#width, height of targetq
confThreshold=0.5 #50%
nmsThreshold =0.3 # should be lower in value

classesFile='coco.names'
classNames=[]
with open(classesFile,'rt') as f:
    classNames=f.read().rstrip('\n').split('\n') #extracts all the information based on  new line from coco.names


print(classNames)
print(len(classNames))

modelConfiguration='yolo-v3.cfg'
modelWeights='yolov3 .weights'

net=cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def findObjects(outputs,img):
    hT, wT, cT=img.shape
    bounding_box=[]
    classIds=[]
    confidence_val=[]

    for output in outputs: #we have 3 outputs, go to each output and call each of the box
        for detection in output:  # find the probability of the object in the image
            scores=detection[5:] # leave the first 5 values because after them only the 80 classes begin
            classId=np.argmax(scores) #class of maximum value
            confidence=scores[classId] # confidence score of the class having max value
            if confidence> confThreshold:
                w,h = int(detection[2]*wT), int(detection[3]*hT)
                x,y = int((detection[0]*wT)-w/2), int((detection[1]*hT)-h/2)
                bounding_box.append([x,y,w,h])
                classIds.append(classId)
                confidence_val.append(float(confidence))

    print(len(bounding_box))
    indices= cv2.dnn.NMSBoxes(bounding_box,confidence_val,confThreshold,nmsThreshold) # non-max supression in case there are more than 1 bounding box for the same object

    print(indices)

    for i in indices:
        i=i[0] # to take the first element
        box= bounding_box[i]
        x,y,w,h=box[0],box[1],box[2],box[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(img,f'{classNames[classIds[i]].upper()} {int(confidence_val[i]*100)}%',
                    (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)



while True:
    ret,img=cap.read()

    blob=cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop=False)
    net.setInput(blob)

    layerNames=net.getLayerNames()
    #print(layerNames)
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()] # it loops through the layer numbers to print the layer name
    #print(outputNames)

    #print(net.getUnconnectedOutLayers()) #output layers

    outputs=net.forward(outputNames)
    #print(outputs[0].shape) # number of  different outputs in which the bounding boxes can be found
    #print(outputs[1].shape)
    #print(outputs[2].shape)

    # the array that we get on outputing the shape are the number of bounding boxes that can be found in the layers, like layer 1- 300, layer 2-1200, layer 3-4800)
    # 85 is because of center x, center y, width, height and confidence values of the object and the rest 80 are classes in coco.names

    #print(outputs[0][0])
    findObjects(outputs,img)





    cv2.imshow('Image',img)

    #exiting the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# closing the window
end=time.time()-start
print("Total time taken",end,"s")
cv2.destroyAllWindows()
cap.release()
