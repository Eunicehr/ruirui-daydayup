r'''
Author       : ruirui-daydayup
Date         : 2022-1-04 14:27:47
LastEditors  : ruirui-daydayup
LastEditTime : 2021-1-5 16:07:10
FilePath     : \DeepLabV3Plus-Pytorchd:\blog\md.py
'''
import os
from datetime import datetime
import argparse
import time

datetime.now().strftime('%Y-%m-%d')
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name",type=str,required=True,help="文件名")
    args=parser.parse_args()
    return args

if __name__=="__main__":
    args=get_args()
    filename = datetime.now().strftime('%Y-%m-%d')+"-"+args.name+".md"
    filename = os.path.join('_posts', filename)
    f =  open(filename, "w",encoding='utf-8')
    f.write(
        f"""---
layout: post
title: "{args.name}"
date:   {datetime.now().strftime('%Y-%m-%d')}
categories: []
tags: []
pinned: false
toc: true
author: cute-rui
---

        """
        )
    f.close()
    time.sleep(3)
    os.system('C:\\"Program Files"\Typora\\typora.exe {}'.format(
        filename))
