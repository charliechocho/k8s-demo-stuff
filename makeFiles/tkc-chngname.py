import os
from ld_yaml import load_yaml, chng_yaml
from mc import build_machine_class
import vmcl_parser

#Clear the screen before starting the process
os.system('clear')

#put cluter yaml in variable and ask for cluster name
yamlfile = '/Users/msoderberg/h2o/k8s-demo-stuff/clusterYamls/clu.yaml'
verlist = {}

clu_name = input('What name do you want for your cluster?: ')

#check if a valid cluster name given, if so ask for number of controllers and workers
if not clu_name:
    print('You have to enter a valid cluster name!! Try again')
    exit()
else:
    ctrl_node = int(input('How many Controlplanes? (press ENTER for 1) ') or 1)
    wrk_node = int(input('How many Workernodes? (press ENTER for 1) ') or 1)

#find out what machine class available and present choices to chose from. Then change in clu.yaml
mcfile = build_machine_class()
choices = vmcl_parser.mc_pull(mcfile, verlist)
vmcl_parser.prn_choice(choices)
ctrl, work = vmcl_parser.get_mc()
ctrl_vm, work_vm = vmcl_parser.mc_choice(choices, ctrl, work)


#load cluster yaml file and change name and replica values
yml = load_yaml(yamlfile)
chng_yaml(yml, clu_name, ctrl_node, wrk_node, ctrl_vm, work_vm)
print('\n\nYour Create TKC Cluster yaml is updated and ready to go!')