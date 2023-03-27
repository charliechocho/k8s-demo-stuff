from yaml import load_yaml, chng_yaml

#put cluter yaml in variable and ask for cluster name
filename = '/Users/msoderberg/h2o/k8s-demo-stuff/clusterYamls/clu.yaml'
clu_name = input('What name do you want for your cluster?: ')

#check if a valid cluster name given, if so ask for number of controllers and workers
if not clu_name:
    print('You have to enter a valid cluster name!! Try again')
    exit()
else:
    ctrl_node = int(input('How many Controlplanes? (press ENTER for 1) ') or 1)
    wrk_node = int(input('How many Workernodes? (press ENTER for 1) ') or 1)

#load cluster yaml file and change name and replica values
yml = load_yaml(filename)
chng_yaml(yml, clu_name, ctrl_node, wrk_node)