# Created by : Tochukwu Iroakazi
# Created on : oct-2017
# Created for : ICS3UR-1 
# Daily Assignment - Unit3-04
# This program displays leap year


import ui

def check_touch_up_inside(sender):
    
    
    year_type = int(view['year_textfield'].text)
    
    if year_type % 4 == 0:
       view['show_label'].text = str(year_type) + ' is a leap year!'
    else:
       view['show_label'].text = str(year_type) + ' is not a leap year!'
    
    
    if year_type % 100 == 0:
       if year_type % 400 == 0:
          view['show_label'].text = str(year_type) + ' is a leap year!'
       
       else:
          view['show_label'].text = str(year_type) + ' is not a leap year!'
       

view = ui.load_view()
view.present('full_screen')
