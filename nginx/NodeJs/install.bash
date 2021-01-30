#!/bin/bash
echo "[UBUNTU] Updating system !"

sudo apt update;
sudo apt -y upgrade;


echo "[NODE] Installing 14.x !"

sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates;
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -;

sudo apt -y install nodejs;
sudo npm install -g yarn;
sudo npm install -g pm2;

echo "[NODE] installed successfuly !"


echo "[NGINX] Installing !"

sudo apt -y update;
sudo apt -y install nginx;
sudo ufw allow 'Nginx FULL';

echo "[NGINX] installed successfuly !"


echo "[CERTBOT] Installing !"

sudo snap install core; 
sudo snap refresh core;
sudo apt-get -y remove certbot;
sudo snap install --classic certbot;
sudo ln -s /snap/bin/certbot /usr/bin/certbot;

echo "[CERTBOT] installed successfuly !"
#sudo certbot --nginx
#pm2 startup systemd

# Create your Apps
#sudo python3 script.py --d socialbot-api.blablahotel.com.br --p 3333
#sudo certbot register --non-interactive --agree-tos -m conexoes.projeto.socialbot@gmail.com