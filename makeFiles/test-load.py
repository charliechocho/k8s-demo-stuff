import yaml

filename = '/Users/msoderberg/h2o/k8s-demo-stuff/clusterYamls/clu-ubuntu.yaml'
def load_yaml(filename):
    """Load TGC yaml file"""
    with open(filename, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        print(data)

load_yaml(filename)