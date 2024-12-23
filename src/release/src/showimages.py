#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

import gsdevice




def main(argv):
    folder_num = {'grab': 1, 'collision': 2}
    cls = sys.argv[1]
    
    folder_num = folder_num[cls]
    
    # the device ID can change after unplugging and changing the usb ports.
    # on linux run, v4l2-ctl --list-devices, in the terminal to get the device ID for camera
    dev = gsdevice.Camera("GelSight Mini")
    dev.connect()
    

    video_num = 0
    image_num = 0 
    SAVE = False
    try:
        while dev.while_condition:
            # get the roi image
            f1 = dev.get_image()
         
            bigframe = cv2.resize(f1, (f1.shape[1]*2, f1.shape[0]*2))
            cv2.imshow('Image', bigframe)

            key_code = cv2.waitKey(1)
            if key_code == ord('q'):
                break
            elif key_code == ord('s'):
                folder_path = '/media/abml/MA-Data/release_data/' + str(folder_num) + '/' + str(video_num) + '/'
                check_make_clear_folder(folder_path)
                SAVE = True
                
            elif key_code == ord('p'):
                SAVE = False
                print(str(image_num) + ' images in the folder ' + str(folder_num) +'/'+str(video_num))
                video_num += 1
                image_num = 0          
                     
            if SAVE:
                save_path = folder_path + str(time.time()) + '.jpg'
                cv2.imwrite(save_path, bigframe)
                image_num += 1
                print('saving image ' + save_path)
                
                
                
                
                
                
    except KeyboardInterrupt:
            print('Interrupted!')
            dev.stop_video()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(sys.argv[1:])
