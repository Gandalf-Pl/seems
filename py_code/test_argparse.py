# coding: utf8
import argparse

parser = argparse.ArgumentParser(description="set config settings")

# parser.add_argument("config")
parser.add_argument(
    "-c", "--config", dest="config_file", help="config file")
args = parser.parse_args()
print args
import ipdb
ipdb.set_trace()


print args.config_file

