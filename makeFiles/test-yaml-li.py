import yaml

filename = 'clu.yaml'

with open(filename, 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data['spec']['topology']['nodePools'][0]['replicas'])