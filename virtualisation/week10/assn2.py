import argparse
import openstack

# create openstack connection using credentials from clouds.yml
#conn = 

# get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('operation', help='Either "up" or "down"')
args = parser.parse_args()

if args.operation == "up":
    # bring up various openstack resources
    pass 
elif args.operation == 'down':
    # tear down openstack resources if they are present
    pass
