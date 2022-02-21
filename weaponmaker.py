'''
weapon = [
    subtype,

]
'''

from asyncio import constants
import math
import os
import random
import time
import PySimpleGUI as sg
import shutil
import json
import roman
from PIL import Image
import re
def toNBT(jsonDict):
    jsonStr = json.dumps(jsonDict, separators=(',', ':'))
    temp = re.sub(r'"(\w+)"\s*:', lambda n:re.sub(r'"','', n.group()), jsonStr)
    re.sub(r'[\\][\"]', '', temp)
    re.sub(r'[\"][\\]', '', temp)
    re.sub(r'[\\][\"]', '', temp)
    re.sub(r'[\"][f][a][l][s][e][\"]', 'DAVID2', temp) ##i litterally have no clue how to use regex m.n
    return re.sub(r'[\:][\"][t][r][u][e][\"]', 'JACOB2', temp)
    
template = r"template"
dest_a = r""
iconpath = r"resources/icon.ico"


class Operation:
    Amount = 0
    Percentage = 1
    Multiplicative = 2
    


class bool:
    def __init__(self, bool):
        self.data = None
        if bool == True:
            self.data = "true"
        if bool == False:
            self.data = "false" ##TODO when i do the string parser thingym, make this work with it.

        
class Attribute:
    def getRandomUUID(self):
        ##TODO please help i have no fricking clue how to make UUIDs god help me
        return [random.randrange(-999999999, 999999999),random.randrange(-999999999, 999999999),random.randrange(-999999999, 999999999),random.randrange(-999999999, 999999999)]
    def __init__(self, attribute, amount=1, slot='mainhand',operation=1,displayName=None):
        self.data = {
            "AttributeName":attribute,
            "Name":attribute,
            "Amount":amount,
            "Slot":slot,
            "Operation":operation,
            "UUID":self.getRandomUUID() ##TODO the actual format is [I;-424044772,753420940,-1259457086,1257445437], while this is just [-424044772,753420940,-1259457086,1257445437], need to add that I; to the beginning
        }
        
class Text:
    def __init__(self,text = "you forgot to put text bozo", italics = False, bold = False, underline = False, strikethrough = False, color="white"):
        if text == None:
            return
        italics = bool(italics)
        bold = bool(bold)
        underline = bool(underline)
        strikethrough = bool(strikethrough)

        self.data = {"\"text\"":text}
        self.data["\"italics\""] = italics.data
        self.data["\"bold\""] = bold.data
        self.data["\"underline\""] = underline.data ##TODO make a condense function, for example, underline = false is not nessasary because underline is false by default.
        self.data["\"strikethrough\""] = strikethrough.data
        self.data["\"color\""] = color

class Item:
    def __init__(self, item="golden_sword", name=Text(), lore=[], enchantments=[], attributes=[], count=1, data={}):
        self.item = item
        self.name = name
        self.lore = lore
        self.attributes = attributes
        self.enchantments = enchantments ## almost forgot to add this lol
        self.count = count
        self.data = data
        self.nbt = {
            "display":{
                "Name": name.data,
                "Lore":lore
            },
            "HideFlags":127
        }

        ##TAKE CARE OF ATTRIBUTES
        attribute_translations = {
            "max_health": "Max Health",
            "follow_range": "Mob Follow Range",
            "knockback_resistance": "Knockback Resistance",
            "movement_speed": "Speed",
            "attack_damage": "Attack Damage",
            "armor": "Armor",
            "armor_toughness": "Armor Toughness",
            "attack_speed": "Attack Speed",
            "luck": "Luck"
        }
        hand_translations = {
            "mainhand": "Main Hand",
            "offhand": "Off hand",
            "feet": "Feet",
            "legs": "Legs",
            "chest": "Body",
            "head": "Head",
        }
        loreaddon = None
        if attributes != []:
            self.nbt["AttributeModifiers"] = []
            for attribute in attributes:
                self.nbt["AttributeModifiers"].append(attribute.data)
                self.nbt["display"]["Lore"].append([Text(text="When on ",color='gray').data, Text(text=hand_translations[attribute.data['Slot']], color='gray').data])
                   
        
        
        
        ##self.nbt = self.nbt | data ##TODO merging of dictonarys is too greedy so i disabled it

        

item = Item(item="diamond_sword",name=Text("this is a constructer"),data={"display":{"Name":{"text":"This is data"}}})
print(toNBT(item.nbt))

def cloneDatapack():
    shutil.copytree(os.path.join(template, dest_a, "Weapons"))


def interpretWeapon(weapon):
    print("Interpreting Weapon")


createbutton = r"gui/textures/create.png"
sg.theme("DarkGrey5")

preview = []

rightside = [

    [sg.Frame("PREVIEW", preview, size=(305, 350), font=("Minercraftory"))],
    [sg.Button("", image_filename=createbutton, button_color=("#262626", "#262626"), border_width=0,
               key="-CREATEBUTTTON-")]

]
leftside = [
    [sg.Text("Ttext")]
]

windowlayout = [

    [sg.Column(leftside, size=(340, 590)), sg.Column(rightside, size=(340, 590), vertical_alignment="bottom")]

]

window = sg.Window("Minecraft Weapon Creator", windowlayout, size=(700, 600), location=(0, 0),
                   background_color="#262626", icon="resources/icon.ico")

while True:
    event, values = window.read()
    if event == "Ok boomer." or event == sg.WIN_CLOSED:
        break
window.close()
