#!/usr/bin/python2
"""Imports"""
from snakebite.client import Client

def createdir(l):
    """Creates directories"""
    client = Client("localhost", 9000)

    for directory in l:
        create_dir = client.mkdir([directory], create_parent=True)
        print(create_dir)
