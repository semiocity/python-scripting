#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
from bs4 import BeautifulSoup
import requests

def brklnk(url):
    page = requests.get(url, allow_redirects=True)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        
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