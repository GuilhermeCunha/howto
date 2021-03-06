import subprocess
import os, errno
import argparse

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

NGINX_SITES_AVALIABLE_PATH = '/etc/nginx/sites-available'
NGINX_SITES_ENABLE_PATH = '/etc/nginx/sites-enabled'

def active_site(domain):
    print(f"Activating domain {domain}")
    os.symlink(f"/etc/nginx/sites-available/{domain}", f'/etc/nginx/sites-enabled/{domain}')
    
def add_ssl(domain):
    print(f"Adding SSL to domain {domain}")
    subprocess.call(f"sudo certbot --nginx -d {domain}", shell=True)
    
def restart_ngix():
    print(f"Restarting NGINX")
    subprocess.call(f"sudo systemctl restart nginx;", shell=True)

def read_file(path):
    f = open(path, "r")
    file_string = f.read()

    f.close()

    return file_string

def save_file(path_with_ext, content):
    print(f"Saving file in {path_with_ext}")

    file = open(path_with_ext, "w")
    file.write(content)
    file.close()

def create_site_config(domain, port, template_file = os.path.join('..', 'examples', "example.com.br")):
    file_string = read_file(template_file)
    
    file_string = file_string.replace('$PORT', str(port))
    file_string = file_string.replace('$DOMAIN', str(domain))


    return file_string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", "-d", help="domain")
    parser.add_argument("--port", "-p", help="domain")

    args = parser.parse_args()

    print(f"Creating configs to domain {args.domain} in port {args.port}")

    if(args.domain is None):
        print("domain is none")
        return
    if(args.port is None):
        print("port is none")
        return

    file_string = create_site_config(args.domain, args.port)
    
    save_file(os.path.join(NGINX_SITES_AVALIABLE_PATH, args.domain), file_string)
    active_site(args.domain)
    restart_ngix()
    add_ssl(args.domain)

if __name__ == "__main__":
    main()