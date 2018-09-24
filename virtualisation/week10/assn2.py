import argparse
#import openstack

# create openstack connection using credentials from clouds.yml
#conn = 

# get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('operation', help='One of "report",  "up" or "down"')
args = parser.parse_args()

if args.operation == 'report':
    # print a report on instances
    pass
elif args.operation == 'up':
    # bring up various openstack resources
    pass 
elif args.operation == 'down':
    # tear down openstack resources if they are present
    pass
