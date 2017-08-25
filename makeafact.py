# coding: utf-8
import argparse
from factos import facts

parser = argparse.ArgumentParser()
parser.parse_args()

fact = facts(1)

print( "Fact:\n {}\n".format(fact[0][0]))
print( "URL:\n{}".format(fact[0][1]))
print( "id:{}".format(fact[0][2]))

