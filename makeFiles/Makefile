include Makefile.env

#This Makefile requires an argument that sets the user in order to login to clusters and Supervisor Cluster
#Ex. </> make Makefile USER={dev} or {admin}
#If you want to login to or create a cluster you also need to supply the NS=<namespace> argument

ifeq ($(USER), dev)
 	PASSWD ?= $(USER_PASSWORD)
 	CLU_USER ?= $(DEV_USER)
else ifeq ($(USER), admin)
 	PASSWD ?= $(SUPERVISOR_PASSWORD)
 	CLU_USER ?= $(ADMIN_USER)
else ifeq ($(USER), lab_admin)
	PASSWD ?= $(LAB_SUPER_PWD)
	CLU_USER ?= $(ADMIN_USER)
else ifeq ($(USER), lab_user)
	PASSWD ?= $(LAB_USER_PWD)
	CLU_USER ?= $(LAB_USER)
endif

export KUBECTL_VSPHERE_PASSWORD ?= $(PASSWD)

login:
	@#logs in to the supervisor cluster
	@echo "Loggar in som $(CLU_USER) på TKC"
	@kubectl vsphere login --server $(SUPERVISOR_CLU) -u $(CLU_USER) --insecure-skip-tls-verify

login-lab:
	@#logs in to the lab supervisor cluster
	@echo "Loggar in som $(CLU_USER) på TKC"
	@kubectl vsphere login --server $(LAB_SUPER_CLU) -u $(CLU_USER) --insecure-skip-tls-verify

logout:
	@#logs out from the vSphere w. Tanzu Session
	@echo "Loggar Ut Från Alla vSphere Kluster"
	@kubectl vsphere logout

login-clu:
	@#requries 2 arguments - "CLU" and "USER"
	@echo "$(CLU_USER) Loggar In På Kluster $(CLU)"
	@kubectl vsphere login --server $(SUPERVISOR_CLU) -u $(CLU_USER) --insecure-skip-tls-verify --tanzu-kubernetes-cluster-name $(CLU)
	@kubectx $(CLU)
	@kubectl get nodes

login-lab-clu:
	@#requries 2 arguments - "CLU" and "USER"
	@echo "$(CLU_USER) Loggar In På Kluster $(CLU)"
	@kubectl vsphere login --server $(LAB_SUPER_CLU) -u $(CLU_USER) --insecure-skip-tls-verify --tanzu-kubernetes-cluster-name $(CLU)
	@kubectx $(CLU)
	@kubectl get nodes

clu-create:
	@#create a TKC cluster
	@echo "Creating New TKC in Namespace $(NS)"
	@kubectx $(NS)
	@kubectl apply -f $(APP_ROOT)/clusterYamls/clu.yaml

clu-delete:
	@#deletes a TKC cluster! Make sure you run tkc-chyaml and give the correct name of the cluster to delete
	@echo "Deleting TKC in Namespace $(NS)"
	@kubectx $(NS)
	@kubectl delete -f $(APP_ROOT)/clusterYamls/clu.yaml

allow:
	@#this is creating an allowing role and rolebinding to allow deploy on the cluster in question 
	@echo "Creating Allow Deploy Rule"
	@kubectl apply -f $(APP_ROOT)/configYamls/allow-runasnonroot-clusterrole.yaml

certman-inst:
	@#this installs certmanager on a cluster, make sure you have HELM installed
	@echo "Installing Certmanager On The Current Cluster Using HELM"
	@helm repo update
	@helm install cert-manager jetstack/cert-manager --namespace cert-manager \
	--create-namespace --version $(CERTMAN_VER) --set installCRDs=true
	
tkc-chyaml: chyaml/bin/activate
	@echo "Let's you name your next cluster to be deleted or created"
	@# assumes you have the clu.yaml file prepped 
	@# In order to run this you need a Python Venv(Virtual environment) craeted in the working directory
	@# of the Makefile. This is done by writing this command:
	@# </> python3 -m venv chyaml </> 
	@# </> source chyaml/bin/activate </> 
	@# Then install the requirements in the requirements.txt file like this:
	@# </> pip install -r requirements.txt </> - This is to install the PyYaml module
	@# You also need to change the path to the clu.yaml file for the filenam vaiable in the python code.
	@./chyaml/bin/python3 tkc-chngname.py


	


