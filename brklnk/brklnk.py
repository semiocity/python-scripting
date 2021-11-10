#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests
import re


def brklnk(url):
    print(url)
    print(urlparse(url))
    # regexing4links = re.compile(r'href=\".*\"')
    page = requests.get(url, allow_redirects=True)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
    print (soup)

    links = []
    for link in soup.findAll("a", href=True):
        print("Href: {}".format(link['href']))
        absolute_path = urljoin(url, link['href'])
        links.append(absolute_path)

    broken_links = []
    for link2Btested in links:
        print ("Testing: {}".format(link2Btested))
        page = requests.get(link2Btested, allow_redirects=False)
        if page.status_code != 200:
            broken_links.append (link2Btested)

    print("Broken links: {}".format(broken_links))
    # links = re.findall(r'href=\".*\"', str(soup))
    # for ilink, link in enumerate(links):
    #     links[ilink] = url+link[6:-1]
    # print (links)
    # open("landing_page", "wt").write(page.content)
    # with open(url) as fp:
    #     soup = BeautifulSoup(fp, 'html.parser')
    # for root, _, filenames in os.walk(directoryPath):
    #     for filename in filenames:
    #         # print ("Root: {}. Filename: {}".format(root, filename))

    #         # if filename.endswith('.pyc'):
    #         #     os.remove(os.path.join(root, filename))
    #         # print ("Début chemin", os.path.join(root, filename), "Fin chemin")
    #         if filename[0]==".":
    #             continue
    #         with open(os.path.join(root, filename)) as file:
    #             print("Fichier ouvert")
    #             try:
    #                 for ligne in file:
    #                     # print(ligne)
    #                     entre_guillements = re.findall(r'\"[^\"]*\"', ligne)
    #                     for phrase in entre_guillements:
    #                         print(phrase)
    #             except:
    #                 continue

def main():
    # build an empty parser
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="URL à examiner")
    args = parser.parse_args()
    brklnk(args.url)

if __name__ == '__main__':
    main ()