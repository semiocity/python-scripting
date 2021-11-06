#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
import re

def strextract(directoryPath):
    precompiled_regex = re.compile(r'\"[^\"]*\"')
    for root, _, filenames in os.walk(directoryPath):
        for filename in filenames:
            # print ("Root: {}. Filename: {}".format(root, filename))

            # if filename.endswith('.pyc'):
            #     os.remove(os.path.join(root, filename))
            # print ("Début chemin", os.path.join(root, filename), "Fin chemin")
            if filename[0]==".":
                continue
            with open(os.path.join(root, filename)) as file:
                try:
                    for ligne in file:
                        print(ligne)
                        between_quotes = precompiled_regex.findall(ligne)
                        for phrase in between_quotes:
                            print(phrase)
                except:
                    continue

def main():
    # build an empty parser
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=str, help="Directory from which the string extraction has to be performed recursively in all files and subdirectories")
    # parser.add_argument("-p", "--prefix", type=str, default="-- ", help="prefix to add at the beginning of every line")
    args = parser.parse_args()
    strextract(args.dir)

if __name__ == '__main__':
    main ()