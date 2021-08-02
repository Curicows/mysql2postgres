#!/usr/bin/python3

import sys
from mysql2postgres import mysql2postgres


def m2p(argv):
    my2po = mysql2postgres().handle_args(argv)


#if __name__ == 'm2p':
m2p(sys.argv[1:])
