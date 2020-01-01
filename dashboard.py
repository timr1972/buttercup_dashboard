from graphics import *
from random import seed
from random import randint

import time

# Define Globals
global rpm_cell_count
global rpm_orange_line
global rpm_red_line
global rpm_max_power
global rect
global rpm_display_num
global speed_display_num
global prev_rpm

# Set Variables
seed(1)
prev_rpm = 199
rect = [""]
rpm_cell_count = 20
rpm_orange_line = 0.80
rpm_red_line = 0.90
rpm_max_power = 6500

# Draw the window
win = GraphWin('Buttercup Dashboard v1.0 01/01/20', 640, 450)
win.setBackground('black')
win_division = win.getWidth()/6
rpm_display_lbl = Text(Point(win_division * 2, 25), 'RPM')
rpm_display_num = Text(Point(win_division * 4, 25), '0000')
speed_display_num = Text(Point(win_division * 3, 380), '___')
info_display = Rectangle(Point(150, 180), Point(490, 280)) # 30 pixels wide


def draw_dash():

    rpm_display_lbl.setTextColor('snow1')
    rpm_display_lbl.setStyle('bold')
    rpm_display_lbl.setSize(30)
    rpm_display_lbl.draw(win)

    rpm_display_num.setTextColor('red')
    rpm_display_num.setStyle('bold')
    rpm_display_num.setSize(30)
    rpm_display_num.draw(win)

    speed_display_num.setTextColor('yellow1')
    speed_display_num.setStyle('bold')
    speed_display_num.setSize(36)
    speed_display_num.draw(win)

    info_display.setFill('green4')
    info_display.setOutline('white')
    info_display.draw(win)
    
    return 1

def draw_fuel():
    # 30 pixels wide 50-80
    # 130 pixels hihg 290-420
    rect_fuel = Rectangle(Point(50, 290), Point(80, 420))
    rect_fuel.setFill('grey')
    rect_fuel.setOutline('white')
    fuel_display_1 = Text(Point(35, 290), 'Full')
    fuel_display_1.setTextColor('snow1')
    fuel_display_1.setSize(8)
    fuel_display_2 = Text(Point(35, 322), '3/4')
    fuel_display_2.setTextColor('snow1')
    fuel_display_2.setSize(8)
    fuel_display_3 = Text(Point(35, 355), '1/2')
    fuel_display_3.setTextColor('snow1')
    fuel_display_3.setSize(8)
    fuel_display_4 = Text(Point(35, 387), '1/4')
    fuel_display_4.setTextColor('snow1')
    fuel_display_4.setSize(8)    
    fuel_display_lbl = Text(Point(65, 435), 'Fuel')
    fuel_display_lbl.setTextColor('orange1')
    fuel_display_lbl.setStyle('bold')
    fuel_display_lbl.setSize(15)    
    rect_fuel.draw(win)
    fuel_display_1.draw(win)
    fuel_display_2.draw(win)
    fuel_display_3.draw(win)
    fuel_display_4.draw(win)  
    fuel_display_lbl.draw(win)
    return rect_fuel

def draw_temp():
    # 420 to 450 wide -> 560 to 590
    rect_temp = Rectangle(Point(560, 290), Point(590, 420))
    rect_temp.setOutline('white')
    rect_temp.setFill('grey')
    temp_display_1 = Text(Point(605, 290), '120')
    temp_display_1.setTextColor('snow1')
    temp_display_1.setSize(10)
    temp_display_2 = Text(Point(605, 355), '90')
    temp_display_2.setTextColor('snow1')
    temp_display_2.setSize(10)
    temp_display_3 = Text(Point(605, 400), '30')
    temp_display_3.setTextColor('snow1')
    temp_display_3.setSize(10)
    temp_display_lbl = Text(Point(575, 435), 'Temp')
    temp_display_lbl.setTextColor('orange1')
    temp_display_lbl.setStyle('bold')
    temp_display_lbl.setSize(15)

    rect_temp.draw(win)
    temp_display_1.draw(win)
    temp_display_2.draw(win)
    temp_display_3.draw(win)
    temp_display_lbl.draw(win)
    return rect_temp
    
def draw_rpm(f1, f2, f3, fQty):
    if ((fQty * 10) + f1) > 500:
        return "Bar Chart Exceeded Bounds"
    
    bar_count=0
    bar_pos=f1
    bar_pos = 40
    block_size = 27
    block_space = block_size + 1
    while bar_count < fQty:
        rect.append(Rectangle(Point(bar_pos, f2), Point(bar_pos+block_size, f3)))
        bar_pos = bar_pos + block_space
        bar_count = bar_count + 1
        rect[bar_count].setFill("lightgrey")
        rect[bar_count].draw(win)
    return "RPM Drawn"


def test_rpm():
    # Run a wipe once to test display    
    x=1
    while x<rpm_cell_count+1:
        if x < rpm_cell_count * rpm_orange_line:
            rect[x].setFill("green1")
        else:
            if x < rpm_cell_count * rpm_red_line:
                rect[x].setFill("orange1")
            else:
                rect[x].setFill("red1")
        x = x + 1
    while x>1:
        x = x - 1
        rect[x].setFill("lightgrey")

def show_speed(speed):
    speed_display_num.setText(speed)
    
def plot_rpm(old_rpm2, rpm):
    '''
    rpm is provided as a value from 0 to 9999
    take rpm as % of rpm_max_power
    '''
    rpm_display_num.setText(rpm) # Show RPM as value in text
    old_rpm_percentage = old_rpm2 / rpm_max_power 
    old_rpm_display = round(rpm_cell_count * old_rpm_percentage) # work out old display value
    rpm_percentage = rpm / rpm_max_power
    rpm_display = round(rpm_cell_count * rpm_percentage) # work out new display value
    x = old_rpm_display # Set start value to old RPM
    if old_rpm2 < rpm:
        # We have received a higher RPM
        while x < rpm_display:
            if x < rpm_cell_count * rpm_orange_line:
                rect[x].setFill("green1")
            else:
                if x < rpm_cell_count * rpm_red_line:
                    rect[x].setFill("orange1")
                else:
                    rect[x].setFill("red1")
            x=x+1
            
    if old_rpm2 > rpm:
        # We have received a lower RPM
        while x>rpm_display:
            x = x - 1
            rect[x].setFill("lightgrey")
    
print(draw_rpm(50,50,100,rpm_cell_count)) # Draw the RPM
print(draw_fuel())
print(draw_temp())
print(draw_dash())
test_rpm() # Test the RPM

print("Running random values to RPM")
for loopcount in range (50):
    rpm = randint(200, 6450)
    plot_rpm(prev_rpm, rpm)
    show_speed(round(rpm/10))
    prev_rpm = rpm
    time.sleep(0.05)
plot_rpm(prev_rpm, 850)
speed_display_num.setText(0)

print("Complete")