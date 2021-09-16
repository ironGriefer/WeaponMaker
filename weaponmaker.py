'''
weapon = [
    subtype,

]
'''
import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
#from pystray import MenuItem as item
#import pystray
from PIL import Image, ImageTk
import random
import time
import shutil
import ntpath

template = r"template"
dest_a = r""

def cloneDatapack():
    shutil.copytree(os.path.join(template,dest_a,"Weapons"))

def interpretWeapon(weapon):
    print("Interpreting Weapon")




class Melee:
    weapon = [

    ]
    def __init__(self, attribute, model, trigger, abil):
        self.weapon.append(attribute)
        self.weapon.append(model)
        self.weapon.append(trigger)
        self.weapon.append(abil)


class Weapon:
    ## self, <ranged, melee, projectile> [<onhit, rightclick incase of melee>, <raycast, set range, homing in case of ranged>, <linear or homing incase of projectile>]
    def __init__(self, weapontype="none", attribute="none", model="none", trigger="none", abil="none", subtype="none"):
        if weapontype == "melee":
            print("Melee Type Selected.")
            weapon = Melee(attribute,model,trigger,abil)
            interpretWeapon(weapon)


#testattributes = [

#]
#testweapon = Weapon("melee",testattributes,"111","hit","explode")


root = tk.Tk()
root.title('Minecraft Weapon Maker')
iconpath = r"resources/icon.ico"
p1 = PhotoImage(file="resources/icon.png")

root.iconphoto(False, p1)

# Set the size of the window
root.geometry("700x350")


root.mainloop()
