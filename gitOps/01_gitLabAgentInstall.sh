helm repo add gitlab https://charts.gitlab.io
helm repo update
helm upgrade --install testk8s gitlab/gitlab-agent \
    --namespace gitlab-agent-testk8s \
    --create-namespace \
    --set image.tag=v16.9.0-rc2 \
    --set config.token=glagent-Vz41t-LekdrGQVPriDBm7CS_Nk1RzrkrMykrDL6SufGBJiCexg \
    --set config.kasAddress=wss://kas.gitlab.com
