#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
import re

def strextract(directoryPath):
    for root, _, filenames in os.walk(directoryPath):
        for filename in filenames:
            print ("Root: {}. Filename: {}".format(root, filename))

            # if filename.endswith('.pyc'):
            #     os.remove(os.path.join(root, filename))
            print ("Début chemin", os.path.join(root, filename), "Fin chemin")
            with open(os.path.join(root, filename)) as file:
                print("Fichier ouvert")
                try:
                    for ligne in file:
                        # print(ligne)
                        entre_guillements = re.findall(r'\"[^\"]*\"', ligne)
                        for phrase in entre_guillements:
                            print(phrase)
                except:
                    continue

def main():
    # build an empty parser
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=str, help="Directory")
    # parser.add_argument("-p", "--prefix", type=str, default="-- ", help="prefix to add at the beginning of every line")
    args = parser.parse_args()
    strextract(args.dir)

if __name__ == '__main__':
    main ()