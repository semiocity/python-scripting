#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests
import re

def brklnk(url, depth, verbose, visited_urls, broken_links):
    # print("Visited URLs: {}\n".format(visited_urls))
    if verbose:
        print("Testing: {}".format(url), end=" ")
    head = requests.head(url, allow_redirects = True)
    visited_urls.add(url)
    if head.status_code == 200:
        if verbose:
            print("---> OK")

        if depth >= 1:
            page = requests.get(url, allow_redirects = True)
            soup = BeautifulSoup(page.content, 'html.parser')
            for link in soup.findAll("a", href=True):
                absolute_path = urljoin(url, link['href'])
                protocol = absolute_path[:absolute_path.index(":")]
                if protocol in {"http", "https"} and absolute_path not in visited_urls:
                    brklnk(absolute_path, depth-1, verbose, visited_urls, broken_links)
    else:
        if verbose:
            print("\nThis link is broken!\n")
        else:
            print("Broken link: {}".format(url))

def main():
    # build an empty parser
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="URL to look up for broken links")
    parser.add_argument("--depth", "-d", type=str, default = "1", help="Depth of recursive search (default value: 1)")
    parser.add_argument("--verbose", "-v", help="Verbose", action="store_true")
    args = parser.parse_args()
    broken_links = set()
    brklnk(args.url, int(args.depth), args.verbose, set(), broken_links)


if __name__ == '__main__':
    main ()