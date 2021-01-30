import subprocess
import os
import argparse

NGINX_SITES_AVALIABLE_PATH = '/etc/nginx/sites-available'
NGINX_SITES_ENABLE_PATH = '/etc/nginx/sites-available'

def active_site(domain):
    subprocess.call(f"sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/")

def restart_ngix():
    subprocess.call(f"sudo systemctl restart nginx")

def read_file(path):
    f = open(path, "r")
    file_string = f.read()

    f.close()

    return file_string

def save_file(path_with_ext, content):
    file = open(path_with_ext, "w")
    file.write(content)
    file.close()

def create_site_config(domain, port, template_file = "../examples/example.com.br"):
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
    if(args.domportain is None):
        print("port is none")
        return

    file_string = create_site_config(args.domain, args.port)
    save_file(os.path.join(NGINX_SITES_AVALIABLE_PATH, args.domain), file_string)
    active_site(args.domain)
    restart_ngix()

if __name__ == "__main__":
    main()