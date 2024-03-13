#!/usr/bin/python2
"""Imports"""
from snakebite.client import Client

def deletedir(l):
    """Delete directories"""
    client = Client("localhost", 9000)

    for directory in l:
        try:
            del_dir = client.delete(directory, recurse=True)
            print(del_dir)
        except Exception:
            pass