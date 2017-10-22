# Created by : Tochukwu Iroakazi
# Created on : oct-2017
# Created for : ICS3UR-1 
# Daily Assignment - Unit3-05
# This program displays factorial

import ui

def calculate_button_touch_up_inside(sender):
    
    integer = int(view['integer_textfield'].text)
    counter = 1 
    answer = counter 
    if integer >= 1:
      while (counter <= integer):
         answer = answer * counter
         counter = counter + 1
         view['factorial_label'].text = 'The factorial is ' + str(answer)
    else:
        view['factorial_label'].text = 'No factorial'

view = ui.load_view()
view.present('full_screen')
