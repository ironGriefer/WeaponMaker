'''
weapon = [
    subtype,

]
'''
import os
import random
import time
import PySimpleGUI as sg
import shutil
from PIL import Image

template = r"template"
dest_a = r""
iconpath = r"resources/icon.ico"




def cloneDatapack():
    shutil.copytree(os.path.join(template, dest_a, "Weapons"))


def interpretWeapon(weapon):
    print("Interpreting Weapon")

createbutton = r"gui/textures/create.png"
sg.theme("DarkGrey5")
windowlayout = [

    [sg.Button("",image_filename=createbutton,button_color=("#262626", "#262626"),border_width=0,key="-CREATEBUTTTON-")]

]

window = sg.Window("Minecraft Weapon Creator",windowlayout,size=(700,600),location=(0,0),background_color="#262626",icon="resources/icon.ico")

while True:
    event, values = window.read()
    if event == "Ok boomer." or event == sg.WIN_CLOSED:
        break
window.close()
