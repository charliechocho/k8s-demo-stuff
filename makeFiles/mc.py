import subprocess

def build_machine_class():
    subprocess.run('kubectl get vmclass > vmclass.txt', shell=True)
    return 'vmclass.txt'


