import os
import scipy
import cv2 as cv
from object_detect_fun import run_object_detection
# Paths to YOLO config, weights, and classes files


config_path = 'yolov3.cfg'
weights_path = 'yolov3.weights'
classes_path = 'yolov3.txt'
All_data_dicts = []
# Directory containing images
images_directory = './Frames'

'''video = 'VID1.mp4'
cap = cv.VideoCapture(video)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
while True:
    ret, frame = cap.read()
    
    if not ret:
        print('Video ends')
        break
   
    cv.imshow('Frame',frame)
    cv.waitKey()
    #cv.imwrite()
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
data_dict = run_object_detection(frame, config_path, weights_path, classes_path)
#All_data_dicts.extend(data_dict['items'])
cap.release()'''


#file_name = 'All_results.mat'
#scipy.io.savemat(file_name,{'All_data_dicts': All_data_dicts}, appendmat= True, format = '5')
# List to store data_dicts for each run
     
'''for i, item in enumerate(os.listdir(images_directory)):
    if(i%9 == 1):
        item_path = os.path.join(images_directory, item)
        if os.path.isfile(item_path) and item.endswith(".jpg"):
            data_dict = run_object_detection(item_path, config_path, weights_path, classes_path)
            All_data_dicts.extend(data_dict['items'])
        else:
            print('Not Iframe')


#print(All_data_dicts) 
file_name = 'all_results_data.mat'
scipy.io.savemat(file_name, {'all_data_dicts': All_data_dicts}, appendmat=True, format='5')'''          






for i, item in enumerate(os.listdir(images_directory)):
    if i % 9 == 1:
        item_path = os.path.join(images_directory, item)
        if os.path.isfile(item_path) and item.endswith(".jpg"):
            data_dict = run_object_detection(item_path, config_path, weights_path, classes_path)
            items_with_i = [(i, *item_values) for item_values in data_dict.get('items', [])]
            All_data_dicts.extend(items_with_i)
            
        else:
            print('Not Iframe')

# Save all_data_dicts to a single .mat file
print(All_data_dicts)
file_name = 'all_results_data.mat'
scipy.io.savemat(file_name, {'all_data_dicts': All_data_dicts}, appendmat=True, format='5')



#file_name = 'all_results_data.mat'
#scipy.io.savemat(file_name, All_data_dicts, appendmat=True)

# Now, all_data_dicts contains the results for each image
# You can analyze or further process the data as needed
#cv.destroyAllWindows()