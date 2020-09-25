#!/usr/bin/env python

import math
import numpy as np
import rospy
from Tkinter import *
import tkFont
from geometry_msgs.msg import PoseStamped


# -----------  Settings -----------
inputtopic = "/rovioli/T_G_I"

fontsize = 60
fieldwidth = 5
xl = 0.15
xm = 0.35
xr = 0.6
yt = 0.25
yx = 0.4
yy = .55
yz = .7
title = "The Shepherd's most trustworthy \nLocalization-Device-Thingy "
goals = [[45.8, 17.3, 1.4], [24.4, -1.7, 1.2], [3.2, 9.9, 1.2]]  # Mav, Rob, Map
colors = ["#cccccc", "#ff5e33", "#ffda33", "#5de146", "#888888"]
# ---------------------------------

# Init window
window = Tk()
window.title("JGameMonitor")
window.attributes('-zoomed', True)

# General
the_font = tkFont.Font(family="Lucida Grande", size=fontsize)
current_goal = 0

# Gui definition
tt = Label(window, font=the_font)
tt.config(text=title)
tt.pack(side=TOP, expand=NO, fill=X)

t1 = Label(window, text="Current:", font=the_font)
t2 = Label(window, text="Goal:", font=the_font)
w_x = Label(window, text="X [m]:", font=the_font)
w_y = Label(window, text="Y [m]:", font=the_font)
w_z = Label(window, text="Z [m]:", font=the_font)

t1.place(relx=xm, rely=yt)
t2.place(relx=xr, rely=yt)
w_x.place(relx=xl, rely=yx)
w_y.place(relx=xl, rely=yy)
w_z.place(relx=xl, rely=yz)

e_x = Entry(window, font=the_font, justify='center')
e_y = Entry(window, font=the_font, justify='center')
e_z = Entry(window, font=the_font, justify='center')
e_x2 = Entry(window, font=the_font, justify='center')
e_y2 = Entry(window, font=the_font, justify='center')
e_z2 = Entry(window, font=the_font, justify='center')

e_x.config(width=fieldwidth)
e_y.config(width=fieldwidth)
e_z.config(width=fieldwidth)
e_x2.config(width=fieldwidth)
e_y2.config(width=fieldwidth)
e_z2.config(width=fieldwidth)

e_x.place(relx=xm, rely=yx)
e_y.place(relx=xm, rely=yy)
e_z.place(relx=xm, rely=yz)
e_x2.place(relx=xr, rely=yx)
e_y2.place(relx=xr, rely=yy)
e_z2.place(relx=xr, rely=yz)


class Buttons(object):
    def __init__(self):
        self.prevBtn = Button(window, text='Prev', command=self.prev_callback, font=the_font)
        self.prevBtn.place(rely=0.95, relx=0.05, anchor=SW)
        self.nextBtn = Button(window, text='Next', command=self.next_callback, font=the_font)
        self.nextBtn.place(rely=0.95, relx=0.95, anchor=SE)
        self.tb = Entry(window, font=the_font, justify='center')
        self.tb.place(rely=0.95, relx=0.5, anchor=S)

    def next_callback(self):
        global current_goal
        global colors
        if current_goal >= 3:
            return
        current_goal = current_goal + 1
        self.prevBtn.config(bg=colors[current_goal-1])
        self.tb.config(bg=colors[current_goal])
        self.nextBtn.config(bg=colors[current_goal+1])
        e_x2.delete(0, END)
        e_y2.delete(0, END)
        e_z2.delete(0, END)
        e_x2.insert(0, goals[current_goal-1][0])
        e_y2.insert(0, goals[current_goal-1][1])
        e_z2.insert(0, goals[current_goal-1][2])
        self.tb.delete(0, END)
        self.tb.insert(0, "Flock of Sheep %i / 3" % current_goal)

    def prev_callback(self):
        global current_goal
        global colors
        if current_goal <= 1:
            return
        current_goal = current_goal - 1
        self.prevBtn.config(bg=colors[current_goal - 1])
        self.tb.config(bg=colors[current_goal],
                       text="Goal %i / 3" % current_goal)
        self.nextBtn.config(bg=colors[current_goal + 1])
        e_x2.delete(0, END)
        e_y2.delete(0, END)
        e_z2.delete(0, END)
        e_x2.insert(0, goals[current_goal - 1][0])
        e_y2.insert(0, goals[current_goal - 1][1])
        e_z2.insert(0, goals[current_goal - 1][2])


buttons = Buttons()
buttons.next_callback()


# Update
def pose_callback(msg):
    e_x.delete(0, END)
    e_y.delete(0, END)
    e_z.delete(0, END)
    e_x.insert(0, ".1f" % msg.pose.position.x)
    e_y.insert(0, ".1f" % msg.pose.position.y)
    e_z.insert(0, ".1f" % msg.pose.position.z)


# Init ros
rospy.init_node("j_game_monitor")
sub = rospy.Subscriber(inputtopic, PoseStamped, pose_callback, queue_size=100)


# Start
window.mainloop()
