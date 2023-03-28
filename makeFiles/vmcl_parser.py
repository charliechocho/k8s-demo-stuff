
def mc_pull(filename, verlist):
    """Reads the vmclass.txt file and builds a dict of choices"""
    with open(filename, 'r') as tf:
        choice = 1
        for line in tf:
            data = line.split()
            if 'NAME' not in data:
                verlist[choice] = data[0]
                choice += 1
        
        return verlist

def prn_choice(verlist):
    """Iterates through the ver_list dict and prints a choice list"""
    for key, value in verlist.items():
        print(f"{key}.\t{value}")

def get_mc():
    ctrl = input('\nEnter the number of the desired control node VM Class: ')
    work = input('\nEnter the number of the desired worker node VM Class: ')
    return ctrl, work

def mc_choice(verlist, ctrl, work):
    try:
        k8s_ctrl = verlist[int(ctrl)]
    except KeyError:
        print(f'VM Class for control node is not available')
        exit()
    try:
        k8s_work = verlist[int(work)]
    except KeyError:
        print(f'VM Class for worker node is not available')
        exit()
    
    return k8s_ctrl, k8s_work
