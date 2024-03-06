# Per recepire le modifiche di OpenProject

git fetch upstream
git merge upstream/main

# OpenProject Deploy

Recipes and examples for deploying OpenProject.

* [Docker Compose](./compose/)
* [Kubernetes](./kubernetes/)

# Se non sono già state create, creo le cartelle per i volumi
sudo mkdir -p /var/lib/openproject/{pgdata,assets}

sudo nano /etc/hosts
# e aggiungo
# 127.0.0.1     inva-openproject.com


# Creo il container e lo avvio in background (al posto di -d metto -it lo apro in background)

docker run -d -p 80:80 --name openproject \
  -e OPENPROJECT_SECRET_KEY_BASE=secret \
  -e OPENPROJECT_HOST__NAME=inva-openproject.com \
  -e OPENPROJECT_HTTPS=false \
  -v /var/lib/openproject/pgdata:/var/openproject/pgdata \
  -v /var/lib/openproject/assets:/var/openproject/assets \
  openproject/community:13

# dopo un po è disponibile (qualche minuto)
<http://inva-openproject.com>

# Primo accesso admin admin e poi si sceglie lo user
admin invaadmin2020

# per stoppare
docker stop openproject

# per riavviare 
docker start openproject

# per rimuovere tutto 
docker rm openproject
