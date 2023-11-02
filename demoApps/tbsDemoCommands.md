tbsDemoCommands.txt
Let's hava a look at the cluster and the TBS installation
kubectl get ns
kubectl get all -n build-service

Create the image using build packs:
kubectl create ns tele2 
kp secret create my-registry-creds --registry registry.tanzu.dk --registry-user msoderberg -n tele2

kp image create hello-tele2 --tag registry.tanzu.dk/app-images/hello-tele2 --local-path ./hello-tele2 --env BP_JVM_VERSION=17 -n tele2 --wait

Let's check the build logs

tanzu build-service build logs my-image

Create deployment for out Tele2 app

kubectl create -n hello-tele2-deploy.yaml
kubectl create -n hello-tele2-svc.yaml

Let's patch the image and redeploy

kp image patch hello-tele2 --local-path ./hello-tele2

kubectl create -n hello-tele2-deploy.yaml