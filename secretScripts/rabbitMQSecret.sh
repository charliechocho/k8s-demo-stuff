kubectl create secret -n $1 docker-registry tanzu-rabbitmq-registry-creds --docker-server=https://registry.tanzu.vmware.com/ --docker-username='msoderberg@vmware.com' --docker-password='Th3darkhalf!'
