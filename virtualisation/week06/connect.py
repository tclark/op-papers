# A small example to show how to establish a 
# connection with an openstack project.
# Credentials are expected to be in a clouds.yaml
# file.

import openstack
from pprint import pprint

conn = openstack.connect(cloud_name='openstack')

for server in conn.compute.servers():
    pprint(server)

