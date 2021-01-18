## Install Nodejs (INSTALL_NODE.md)

## Install NGINX

```
sudo apt update
sudo apt install nginx
sudo ufw allow 'Nginx FULL'
```

### Put the configuration inside the website configuration

```
nano /etc/nginx/sites-available/example.com.br
```

#### **`example.com.br`**

```
## Handle HTTP requests
server {
    listen 80;
    server_name example.com.br wwww.example.com.br;

    # If you want serve static files
    # root /path/to/root/folder/;
    # location / {
    #     try_files $uri $uri/ =404; # Handle if the requested page is not found
    # }

    # If you want point to localhost port
    location / {
		proxy_pass http://localhost:$PORT;
	}
}
```

### Verify configs and restart

```
sudo ln -s /etc/nginx/sites-available/example.com.br /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Install pm2

```
sudo npm install -g pm2
```

### Clone repository

```
git clone https://github.com/User/project.git
```

### Install dependenicies and start project

```
cd project
yarn install
pm2 start src/server.js --name AppName # OBS: This app is running on $PORT
# pm2 start "yarn run start" --name AppName ## OR you can use an specific script to start the app
```

### Go to your server Public IP, and see your application runing!

### CertBot
- https://certbot.eff.org/lets-encrypt/ubuntufocal-nginx
## Go to your server Public IP, and see your application runing!
