import yaml

def load_yaml(filename):
    """Load TGC yaml file"""
    with open(filename, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
         
def chng_yaml(yml, clu_name, ctrl_node, wrk_node):
    """Takes input through name and changes value in yml file"""
    with open(filename, 'w') as file:
        yml['metadata']['name'] = clu_name
        yml['spec']['topology']['controlPlane']['replicas'] = ctrl_node
        yml['spec']['topology']['nodePools'][0]['replicas'] = wrk_node
        yaml.dump(yml, file)