
sudo apt update
sudo apt -y upgrade

sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

sudo apt -y install nodejs
sudo npm install -g yarn
sudo npm install -g pm2

mkdir ~/apps

sudo apt -y update
sudo apt -y install nginx
sudo ufw allow 'Nginx FULL'