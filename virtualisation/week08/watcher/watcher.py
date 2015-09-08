#!/usr/bin/python
from jinja2 import Environment, PackageLoader
import json
import re
import requests
import subprocess
import time

webserver_data = 'http://172.17.42.1:4001/v2/keys/services/website'
templ = Environment(loader=PackageLoader('watcher', 'templates'))

def get_servers():
    r = requests.get(webserver_data)
    data = r.json()['node']['nodes']
    if data is None:
        return []
    server_names = [json.loads(server['value'])['host'] for server in data]
    nums = re.compile('\d+-\d+-\d+-\d+')
    server_addresses = [nums.search(name).group(0).replace('-','.') for name in server_names]
    return server_addresses


def update_config(serverlist):
    template = templ.get_template('conf')
    new_config = template.render(servers=serverlist)
    f = open('/etc/nginx/nginx.conf', 'w')
    f.write(new_config)


# main 
servers = get_servers()
update_config(servers)
subprocess.call(['service', 'nginx', 'start'])

while True:
    new_servers = get_servers()
    if new_servers != servers:
        servers = new_servers
        update_config(servers)
        subprocess.call(['service', 'nginx', 'restart'])
    time.sleep(60)

