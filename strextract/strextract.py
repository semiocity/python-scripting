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

def strextract(directoryPath, suffix, allfiles, path_required):
    precompiled_regex = re.compile(r'\"[^\"]*\"')
    for root, _, filenames in os.walk(directoryPath):
        for filename in filenames:

            if filename.startswith(".") and not(allfiles):
                continue            
            if suffix and not filename.endswith(suffix) :
                continue

            with open(os.path.join(root, filename)) as file:
                try:
                    for ligne in file:
                        # print(ligne)
                        matching_list = precompiled_regex.findall(ligne)
                        for phrase in matching_list:
                            print("{}{}".format("{}\t".format(os.path.join(root, filename)) if path_required else "" ,phrase))
                except:
                    continue

def main():
    # build an empty parser
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=str, help="Directory from which the string extraction has to be performed recursively in all files and subdirectories")
    parser.add_argument("--suffix", "-s", type=str, default = "", help="Suffix of the files to be inspected")
    parser.add_argument("--all", "-a", default = False, help = "Also inspect hidden files", action="store_true")
    parser.add_argument("--path", "-p", default = False, help = "Display full path of the file being inspected", action="store_true")

    args = parser.parse_args()
    strextract(args.dir, args.suffix, args.all, args.path)

if __name__ == '__main__':
    main ()