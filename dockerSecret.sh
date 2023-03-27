kubectl create secret -n $1 docker-registry dockersecret --docker-server=registry.tanzu.dk --docker-username=msoderberg --docker-password=<passwd> --docker-email=msoderberg@vmware.com 
