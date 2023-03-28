import os
from mc import build_machine_class

filename = build_machine_class()
ver_list = {}

def mc_pull():
    with open(filename, 'r') as tf:
        choice = 1
        for line in tf:
            data = line.split()
            if 'NAME' not in data:
                ver_list[choice] = data[0]
                choice += 1

def prn_choice():
    for key, value in ver_list.items():
        print(f"{key}.\t{value}")

def mc_choice(ctrl, work):
    try: 
        k8s_ver = ver_list[int(mc_image)]
        return k8s_ver
    except KeyError:
        print(f'VM Class {mc_image} is not available')
        


    
mc_pull()
prn_choice()
mc = mc_choice()
print(mc)