# coding: utf-8
import argparse
from factos import facts

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=int, default=1, help='Number of facts to display')
parser.add_argument('-i', action='store_true')
args = parser.parse_args()

facts = facts(args.f)
count = 0
for fact in facts:
    count += 1
    print('[{}]\nfact: {}\n url: {}\n reddit_id: {}\n'.format(count,fact[0],fact[1], fact[2]))

