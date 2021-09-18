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
import roman
from PIL import Image

template = r"template"
dest_a = r""
iconpath = r"resources/icon.ico"


class JAWGAttribute:
    def __init__(self, attribute, amount="1", operation="amount", slot="mainhand"):
        self.attribute = attribute
        self.amount = amount
        self.operation = operation
        self.slot = slot


class JAWGEnchantment:
    def __init__(self, enchantment, lvl=1, display="uhasfhhdjsfjhlsdffdhdfhfghdfa343w4asd"):
        if display == "uhasfhhdjsfjhlsdffdhdfhfghdfa343w4asd":
            self.display = enchantment
        else:
            self.display = display
        self.enchantment = enchantment
        self.lvl = lvl


class JAWGText:
    def connecter(self, text, arg):

        prop = {
            "text": text,
            "italic": "false"
        }
        for iterate in arg.keys():
            prop[iterate] = str(arg[iterate]).lower()
        self.data = json.dumps(prop)

    def update(self, text, **kwargs):
        self.connecter(text, kwargs)

    def __init__(self, text, **kwargs):
        self.connecter(text, kwargs)


class JAWGItem:
    def __init__(self, base_item="", name=JAWGText(""), lore=[], count=1, enchantments=[], attributes=[], data=[]):
        self.base_item = base_item
        self.name = name
        self.lore = lore
        self.count = count
        self.enchantments = enchantments
        self.attributes = attributes
        self.data = data
        translations = {
            "max_health": "Max Health"
        }
        def getTranslation(phrase):
            try:
                d = translations[phrase]
                return d
            except:
                return phrase
        if "minecraft:" not in base_item:
            base_item = "minecraft:" + base_item
        data.append("HideFlags:127")
        for enchant in enchantments:
            loreaddon = JAWGText(enchant.display.capitalize() + " " + roman.toRoman(int(enchant.lvl)))
            lore.append(loreaddon)
        slots = {}
        def addToTable(table,value):
            newtable = table.copy()

            newtable.append(value)
            return newtable
        for attribute in attributes:
            if attribute.slot not in slots:
                slots[attribute.slot] = []
            slots[attribute.slot] = addToTable(slots[attribute.slot], attribute)
        loreaddon = []
        for key in slots:
            loreaddon.append(JAWGText(("When on " + key.capitalize() + ":"),color="white"))
            for value in slots[key]:
                loreaddon.append(JAWGText("+" + value.amount + " " + getTranslation(value.attribute),color="blue"))
        for i in loreaddon:
            lore.append(i)





a = "{display:{Lore:["
e = JAWGItem("golden_sword", enchantments=[JAWGEnchantment("sharpness", "13", "COOL")], attributes=[JAWGAttribute(attribute="max_health",slot="head"),JAWGAttribute(attribute="max_healeth",slot="legs"),JAWGAttribute(attribute="max_fhealth",slot="legs"),JAWGAttribute(attribute="maxe_health",slot="head")])
for i in e.lore:
    a = a + "'" + i.data + "',"
a = a[:-1]
a = a + "]}}"
print(a)


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
