#!/usr/bin/env python

import math
import numpy as np
import rospy
import Tkinter as tk
import tkinter.font as tkFont
from geometry_msgs.msg import PoseStamped


# -----------  Settings -----------
inputtopic = "/rovioli/T_G_I"

fontsize = 70
fieldwidth = 10
xl = 0.3
xr = 0.5
y1 = .4
y2 = .6
y3 = .8
title = "The Shepherd's most trustworthy \nLocalization-Device-Thingy "
# ---------------------------------

# Init window
window = tk.Tk()
window.title("JGameMonitor")
window.attributes('-zoomed', True)

# General
the_font = tkFont.Font(family="Lucida Grande", size=fontsize)

# Gui definition
t = tk.Label(window, font=the_font)
t.config(text=title)
t.pack(side=tk.TOP, expand=tk.NO, fill=tk.X)

w_x = tk.Label(window, text="X [m]:", font=the_font)
w_y = tk.Label(window, text="Y [m]:", font=the_font)
w_z = tk.Label(window, text="Z [m]:", font=the_font)

w_x.place(relx=xl, rely=y1)
w_y.place(relx=xl, rely=y2)
w_z.place(relx=xl, rely=y3)

e_x = tk.Entry(window, font=the_font)
e_y = tk.Entry(window, font=the_font)
e_z = tk.Entry(window, font=the_font)

e_x.config(width=fieldwidth)
e_y.config(width=fieldwidth)
e_z.config(width=fieldwidth)

e_x.place(relx=xr, rely=y1)
e_y.place(relx=xr, rely=y2)
e_z.place(relx=xr, rely=y3)


# Update
def pose_callback(msg):
    e_x.insert(0, str(msg.pose.position.x))
    e_y.insert(0, str(msg.pose.position.y))
    e_z.insert(0, str(msg.pose.position.z))


# Init ros
rospy.init_node("j_game_monitor")
sub = rospy.Subscriber(inputtopic, PoseStamped, pose_callback, queue_size=100)


# Start
window.mainloop()
