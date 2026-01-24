import time
import random
from epuck import EPuckCom, EPuckIP, epuck   #makesure you have pyserial installed

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# def cam_bytes_to_image(mode, data, width, height):

    # if (mode == epuck.CAM_MODE_RGB565):
    #     npdata = np.frombuffer(data, dtype=">i2")    # camera is big endian, 16 bit per pixel.
    #     npdata = npdata.astype(np.uint32)            #expand to 32 bit to make room for unpacking.
    #     alpha = 0xFF000000     #ALPHA is MSB, all set to 1
    #     r = ((npdata & 0xF800) >> 8)    # mask out top 5 bits, then shift right to make it the LSB of the 32 bit
    #     g = ((npdata & 0x07E0) << 5)         # mask out middle 6 bits, then shift a little left to make it the 2nd LSB
    #     b = ((npdata & 0x001F) << 19)        # mask out the bottom 5 bits, then shift it all the way left to be the 3rd LSB
    #     arr = alpha + r + g + b
    #     return Image.frombuffer('RGBA', (width, height), arr, 'raw', 'RGBA', 0, 1)  

    # if (mode == epuck.CAM_MODE_GREY):
    #     npdata = np.frombuffer(data, np.uint8)    # camera is big endian, 16 bit per pixel.
    #     return Image.frombuffer('L', (width, height), npdata, 'raw', 'L', 0, 1)    

def epuck_test():

    epuckcomm = EPuckCom("COM10", debug=False)
    #epuckcomm = epuck.EPuckIP("192.168.229.106", debug=True)
    if (not epuckcomm.connect()):
        print("Could not connect, quitting")
        return

    epuckcomm.enable_sensors = True
    #epuckcomm.enable_camera = True
    epuckcomm.send_command() # enable sensor stream.
    time.sleep(0.5)  #give time for the robot to get the request


    distance = 20 #cm
    wheel_rad=2.05 #cm
    steps_to_complete_wheel_cycle= 20*50
    cir= 2 * 3.14 * wheel_rad
    cir_needed= distance/cir
    step_needed = round(cir_needed * steps_to_complete_wheel_cycle)

    ini_left_step= epuckcomm.state.sens_left_motor_steps
    ini_right_step= epuckcomm.state.sens_right_motor_steps

    epuckcomm.state.act_left_motor_speed = 500
    epuckcomm.state.act_right_motor_speed = 500
    epuckcomm.send_command()

    while True:
        epuckcomm.data_update()
        
        left_step= epuckcomm.state.sens_left_motor_steps - ini_left_step
        right_step= epuckcomm.state.sens_right_motor_steps - ini_right_step
        #print("[Moving Forward] Left Step: " + str(left_step)+ ":: Right Step:" +str(right_step)+ " :: Step Needed: " +str(step_needed))

        if left_step >= step_needed or right_step >= step_needed:
            print("[Done] " + str(distance)+" cm reached!!")
            break

        time.sleep(0.05)
    
    

    epuckcomm.stop_all()
    epuckcomm.close()
    
    
epuck_test()