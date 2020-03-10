# Multi-type_vehicles_detection at intersection
According to YOLOv3 and SORT algorithms, counting multi-type vehicles. Implemented by Pytorch.  
Detecting and tracking the vehicles in \["bicycle","bus","car","motorbike","truck"].

The purpose of this code is to monitor the traffic at inersetion and its turning movement. It will automatically identify enty and exit intersection of vechile with its class and time period required from entry to exit. 

Yolo3 is used to for object detecion to identify the vechile in 5 class - bicycle, bus, car, motorbike, truck. To identify the tuning movement of vechile coodinate of centre of boundin box is printed with vechile identification no and class of vechile in every frame. Data cleaning will be done in python to increase the accuracy of model. After cleaning the data minimum distance of start and end frame is extracted out and minimum distance between line and point is calculated from the intersection defined boundary condition. Assign the vechile stating and end intersection according to result

## Reference
- yolov3-darknet  https://github.com/pjreddie/darknet
- yolov3-pytorch  https://github.com/eriklindernoren/PyTorch-YOLOv3
- sort https://github.com/abewley/sort

## Dependencies
- ubuntu/windows
- cuda>=10.0
- python>=3.6
- `pip3 install -r requirements.txt`

## Usage
1. Download the pre-trained yolov3 weight file [here](https://pjreddie.com/media/files/yolov3.weights) and put it into `weights` directory;  
2. Run `python3 app.py` ;
3. Select video and double click the image to select area, and then start;
4. After detecting and tracking, the result video and file are saved under `results` directory, the line of `results.txt` with format \[videoName,id,objectName] for each vehicle.

## Demo




