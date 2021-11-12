#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests
import re

from requests.api import head

visited_urls = set()

def brklnk(url, depth):
    head = requests.head(url, allow_redirects=True)
    visited_urls.add(url)
    if head.status_code == 200:
        if depth >= 1:
            page = requests.get(url, allow_redirects=True)
            soup = BeautifulSoup(page.content, 'html.parser')
            for link in soup.findAll("a", href=True):
                absolute_path = urljoin(url, link['href'])
                protocol = absolute_path[:absolute_path.index(":")]
                if protocol in {"http", "https"} and absolute_path not in visited_urls:
                    brklnk(absolute_path, depth-1)
    else:
        print("Broken link: {}".format(url))


def main():
    # build an empty parser
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="URL where to look for broken links")
    parser.add_argument("--depth", "-d", type=str, default = "1", help="Depth of the recursive search")
    args = parser.parse_args()
    brklnk(args.url, int(args.depth))

if __name__ == '__main__':
    main ()