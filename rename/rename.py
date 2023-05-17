# -*- coding:utf-8 -*-
# @Time : 2023/5/17 20:51
# @Author: Charlie
# @Email: charlie__william@hotmail.com
# @File : rename.py
# @Software: Visual Studio Code

import os
import argparse


def list_recursive(path, pattern_src, pattern_tar, list_source, list_target):
    for file in os.listdir(path):
        file_merged = str(os.path.join(path, file))
        if pattern_src in file:
            list_source.append(file_merged)
            list_target.append(file_merged.replace(pattern_src, pattern_tar))
        if os.path.isdir(os.path.join(os.path.abspath(path), file)):
            list_recursive(file_merged, pattern_src, pattern_tar, list_source, list_target)
    
    return list_source, list_target


def main(path, pattern_src, pattern_tar):  
    list_src = []
    list_tar = []
    list_src, list_tar = list_recursive(path, pattern_src, pattern_tar, list_src, list_tar)
    
    for idx in range(len(list_src))[::-1]:
        print(f"rename {list_src[idx]}\tto\t{list_tar[idx]}")
        os.rename(list_src[idx], list_tar[idx])

    return dict(zip(list_src, list_tar))

def arg_pars():
    parser = argparse.ArgumentParser(description='Rename the files recursively with pattern in a specific folder',
                                     epilog="Example: python rename.py -p ./ -s ABC -t abc")
    parser.add_argument('-p', '--path', dest='path', default='./', help='Choose a folder to rename, default=\'./\'')
    parser.add_argument('-s', '--pattern_source', dest='pattern_source', required=True, default=None, type=str, help='The old pattern you want to remove')
    parser.add_argument('-t', '--pattern_target', dest='pattern_target', required=True, default=None, type=str, help='The new pattern you want to keep')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = arg_pars()
    if not os.path.exists(args.path):
        print(f"Warning: The path '{args.path}' doesn't exist, please check it again.")
        exit()
    dict_rename = main(args.path, args.pattern_source, args.pattern_target)
    if not len(dict_rename):
        print(f"Warning: No file with pattern '{args.pattern_source}' was found in path '{args.path}', please check it again.")
