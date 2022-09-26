#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A Python script that takes in a URL
@author: Bashir AmirKano
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
