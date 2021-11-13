#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
import re

def file_suffix(filename):
    if "." in filename:
        return filename [filename.index("."):]
    else:
        return ""

def strextract(directoryPath, suffix, allfiles):
    precompiled_regex = re.compile(r'\"[^\"]*\"')
    for root, _, filenames in os.walk(directoryPath):
        for filename in filenames:
            if (filename[0] == "." and not(allfiles)) or file_suffix(filename) != suffix :
                continue
            with open(os.path.join(root, filename)) as file:
                try:
                    for ligne in file:
                        # print(ligne)
                        between_quotes = precompiled_regex.findall(ligne)
                        for phrase in between_quotes:
                            print(phrase)
                except:
                    continue

def main():
    # build an empty parser
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=str, help="Directory from which the string extraction has to be performed recursively in all files and subdirectories")
    parser.add_argument("--suffix", "-s", type=str, default = "", help="Suffix of the files to be inspected")
    parser.add_argument("--all", "-a", default = "", help="Suffix of the files to be inspected")

    args = parser.parse_args()
    strextract(args.dir, args.suffix)

if __name__ == '__main__':
    main ()