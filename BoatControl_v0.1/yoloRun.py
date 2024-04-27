# YOLOv5 module import
import cv2
import gpioSet as gs
import torch

# YOLOv5 model load
model = torch.hub.load('','custom','best.pt',source='local')

# Webcam Open
cap = cv2.VideoCapture(0)

# Webcam Frame set
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

# Webcam FPS set
cap.set(cv2.CAP_PROP_FPS,60)

# Webcam In_Buffersize set
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)

# target_object = bottle(39)
target_obj = [0,1,2]

while True:
    # Frame read
    ret, frame = cap.read()
    
    if ret:
        # Detect Object use YOLOv5
        results = model(frame, size=70)
        # Target Check
        target_results = [result for result in results.pred[0] if result[-1] in target_obj]
        # Visualize results
        frame_with_results = results.render(target_results)[0]
        # Results Visualization
        cv2.imshow('YOLOv5 Object Detection',frame_with_results)
        if not target_results:
            print("No target object")
            gs.setIntegratedControl(3) 
        else:
            # Convert XY_Position to integers
            for result in target_results:
                result[0:4].int()
            # Find best object
            target_results.sort(key=lambda x:-x[4])
            print(target_results[0])
            x_min = target_results[0][0]
            x_max = target_results[0][2]

            if (x_min>1 and x_max<639):
                print("Object in position")
                gs.setIntegratedControl(5)

    # Press 'q' Out
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
        
# Out Webcam
cap.release()
cv2.destroyAllWindows()
