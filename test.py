from main_new import *
import os


os.system("cls")
player = make_hero(name="Искатель", money=1000)

while True:
    visit_hub(player)