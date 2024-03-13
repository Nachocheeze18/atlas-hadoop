#!/usr/bin/python2
"""Imports"""
from snakebite.client import Client


def download(l):
    """retrieves from the HDFS files listed
    in l and store them"""
    client = Client('localhost', 9000)

    for directory in l:
        dw_load = client.copyToLocal([directory], '/tmp')
        print(dw_load)
