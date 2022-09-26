#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
- Python script that takes in a URL
@author: Bashir AmirKano 
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
