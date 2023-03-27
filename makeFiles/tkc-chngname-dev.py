import yaml

filename = 'clu.yaml'
clu_name = input('What name do you want for your cluster?: ')

if not clu_name:
    print('You have to enter a valid cluster name!! Try again')
    exit()

def load_yaml():
    """Load TGC yaml file"""
    with open(filename, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
         
def chng_yaml(yml, clu_name):
    """Takes input through name and changes value in yml file"""
    with open(filename, 'w') as file:
        yml['metadata']['name'] = clu_name
        yaml.dump(yml, file)

yml = load_yaml()
chng_yaml(yml, clu_name)