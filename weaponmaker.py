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
import json
from PIL import Image

template = r"template"
dest_a = r""
iconpath = r"resources/icon.ico"

def JAWGText(text="",color="white",italics=False,bold=False,underlined=False,strikethrough=False,mystery=False):
    def boolToString(bool):
        if bool == True:
            bool = "true"
        else:
            bool = "false"
        return bool

    string = '{"name":"' + text + '","bold":"'+boolToString(bold)+'"}'
    return string



print(JAWGText("DAyda"))

class JAWGItem(
    base_item="minecraft:golden_sword",
    lore=[
        [JAWGText("This sword is pretty cool",bold=True,italics=False)]
    ]):
    print("")


def cloneDatapack():
    shutil.copytree(os.path.join(template, dest_a, "Weapons"))


def interpretWeapon(weapon):
    print("Interpreting Weapon")

createbutton = r"gui/textures/create.png"
sg.theme("DarkGrey5")

preview = []

rightside = [

    [sg.Frame("PREVIEW",preview,size=(305, 350),font=("Minercraftory"))],
    [sg.Button("",image_filename=createbutton,button_color=("#262626", "#262626"),border_width=0,key="-CREATEBUTTTON-")]

]
leftside = [
    [sg.Text("Ttext")]
]

windowlayout = [

    [sg.Column(leftside,size=(340,590)),sg.Column(rightside,size=(340,590),vertical_alignment="bottom")]


]

window = sg.Window("Minecraft Weapon Creator",windowlayout,size=(700,600),location=(0,0),background_color="#262626",icon="resources/icon.ico")

while True:
    event, values = window.read()
    if event == "Ok boomer." or event == sg.WIN_CLOSED:
        break
window.close()
