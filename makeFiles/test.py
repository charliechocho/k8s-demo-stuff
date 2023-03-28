filename = 'vmclass.txt'
verlist = {}

with open(filename, 'r')as f:
    choice = 1
    for line in f:
        data = line.split()
        verlist[choice] = data[0]
        choice += 1

for key, value in verlist.items():
    print(f"{key}\t{value}")


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

ctrl, work = get_mc()
k8s_ctrl, k8s_work = mc_choice(verlist, ctrl, work)

print(f"{k8s_ctrl}\n{k8s_work}")