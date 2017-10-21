# Created by : Tochukwu Iroakazi
# Created on : oct-2017
# Created for : ICS3UR-1 
# Daily Assignment - Unit3-05
# This program displays walking man

import ui
import time

@ui.in_background  

def start_touch_up_inside(sender):
    #
    counter = 1
    while counter <= 10:
        if counter == 1:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk1.png')
        elif counter == 2:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk2.png')
        elif counter == 3:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk3.png')
        elif counter == 4:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk4.png')
        elif counter == 5:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk5.png')
        elif counter == 6:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk6.png')
        elif counter == 7:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk7.png')
        elif counter == 8:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk8.png')
        elif counter == 9:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk9.png')
        elif counter == 10:
            view['man_walking_image_view'].image = ui.Image.named('./Resources/walk10.png')
        
        counter = counter + 1
        time.sleep(0.1)
        

view = ui.load_view()
view.present('full_screen')
