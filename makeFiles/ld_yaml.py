import yaml
# filename = '/Users/msoderberg/h2o/k8s-demo-stuff/clusterYamls/clu.yaml'
def load_yaml(filename):
    """Load TGC yaml file"""
    with open(filename, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
         
def chng_yaml(filename, yml, clu_name, ctrl_node, wrk_node, cp_vm, wn_vm, tkr_os):
    """Takes input through name and changes value in yml file"""
    with open(filename, 'w') as file:
        yml['metadata']['name'] = clu_name
        yml['metadata']['annotations']['run.tanzu.vmware.com/resolve-os-image'] = f'os-name={tkr_os}'
        yml['spec']['topology']['controlPlane']['replicas'] = ctrl_node
        yml['spec']['topology']['controlPlane']['vmClass'] = cp_vm
        yml['spec']['topology']['nodePools'][0]['replicas'] = wrk_node
        yml['spec']['topology']['nodePools'][0]['vmClass'] = wn_vm
        yaml.dump(yml, file, sort_keys=False)