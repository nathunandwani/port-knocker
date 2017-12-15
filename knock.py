#!/usr/bin/python

import sys
from socket import *
from itertools import permutations

if len(sys.argv) < 5:
    print "---------------------------------------------"
    print "               Port Knocker                  "
    print "Usage: python knock.py <ip> <p1> <p2> <p3>   "
    print "Ex: python knock.py 192.168.209.130 1 2 3    "
    print "---------------------------------------------"
    sys.exit(0)

host = sys.argv[1]
ports = permutations([int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])])

def Knockports(ports):
  for port in ports:
      try:
          s = socket(AF_INET, SOCK_STREAM)
          s.settimeout(0.1)
          s.connect_ex((host, port))
          s.close()
          print "Knocked on port " + str(port)
      except Exception, e:
          print "Error: " + str(e)

for combination in list(ports):
    print "Testing permutation: " + str(combination)
    Knockports(combination)
