kubectl create secret -n $1 docker-registry regsecret --docker-server=https://registry.tanzu.vmware.com/ --docker-username='msoderberg@vmware.com' --docker-password='Th3darkhalf!'
