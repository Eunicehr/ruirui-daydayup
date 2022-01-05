

## typora

### typora设置

![image-20220105113113077](https://s2.loli.net/2022/01/05/EAHDziuSRlwcsn7.png)

### typora图床

#### smms

- 注册smms

- 登录

- ![image-20220105135256640](https://s2.loli.net/2022/01/05/DOyz2hScJMnrZfK.png)

- ![image-20220105135359241](https://s2.loli.net/2022/01/05/YmEONs1Ut7crpdu.png)

- 生成token，复制,代会的picgo插件配置需要

  ![image-20220105135507307](https://s2.loli.net/2022/01/05/aURO4WTuErlX87e.png)

#### picgo

- 选择picgo，点击下载或更新

![image-20220105143617116](https://s2.loli.net/2022/01/05/xdpeEmtXBQOCZc3.png)

- 安装插件

  ```shell
  cd C:\Users\lenovo\AppData\Roaming\Typora\picgo\win64\
  .\picgo.exe install smms-user
  ```

- 配置picgo

打开PicGo-Core的配置文件

![image-20220105122559216](https://s2.loli.net/2022/01/05/UVnA63jtzxfQb9S.png)

按照下面的格式进行替换，Authorization中填写之前复制的token

```
{
  "picBed": {
    "current": "smms-user",
    "uploader": "smms-user",
    "smms-user": {
      "Authorization": "uuwjMOtZGgRRu6pyUxRCcNTjHdGOAQqK"
    },
    "transformer": "path"
  },
  "picgoPlugins": {
    "picgo-plugin-smms-user": true
  }
}
```



#### node.js

- 复制此路径

![image-20220105134156657](https://s2.loli.net/2022/01/05/pCMz147cJhFak3U.png)

- 添加新的环境变量

![image-20220105133154657](https://s2.loli.net/2022/01/05/q2KyTpkA1joGzV3.png)

# github

## 项目fork

- 选主题

  在http://jekyllthemes.org/中选定主题http://jekyllthemes.org/themes/jekyll-theme-yat/。选这一个主题，并进入fork

- fork

  ![image-20220105195157949](https://s2.loli.net/2022/01/05/SRxqJirFwhomOvI.png)

  

  fork完之后，项目已经复制到了gitbub仓库里

  ![image-20220105194815692](https://s2.loli.net/2022/01/05/djVLZw3qko7HKNp.png)

  

- 修改项目名

![image-20220105101423915](https://s2.loli.net/2022/01/05/zcUx6GbtIwYHi3C.png)



- 修改Branch

![image-20220105193129496](https://s2.loli.net/2022/01/05/X6u5o21g7zGEPnM.png)

### git下载与配置

1.git下载

- 下载

![image-20220105103623063](https://s2.loli.net/2022/01/05/SLwAjoqfCg6adxk.png)

![image-20220105103725326](https://s2.loli.net/2022/01/05/wgcZER6HMDhJsNf.png)

自己电脑多少位选多少位

![image-20220105103812200](https://s2.loli.net/2022/01/05/WB3HqO9kMANTl2J.png)

- 安装：点击下载好的安装包安装软件，一直点击next并且将能选上的都选上，直至出现install，点击install。

​                   安装好后鼠标右键,会多出Git GUI Here 和 Git Bash Here 两个选项 

![image-20220105104458614](https://s2.loli.net/2022/01/05/G5hsk9TF6VSwZ48.png)



2. git配置

   - 复制

   ![image-20220105105402530](https://s2.loli.net/2022/01/05/oYxQRfMrAu4pFyE.png)

   - 右击get bash,输入git clone和之前复制的内容

   ```
   git clone https://github.com/Eunicehr/ruirui-daydayup.git
   ```

   - 将压缩包解压进桌面clone出的文件夹中

     

   

### git项目同步

- 在文件夹中鼠标右键gitbash,输入三行代码

```
git add *
git commit -m "init"
git push origin master
```



## Blog

### Blog设置

- 根据注释修改文件夹中的config,记得保存



### Blog脚本

- md.py

```python
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
    filename = os.path.join('C:\Users\lenovo\Desktop\ruirui-daydayup\_posts', filename)
    f =  open(filename, "w",encoding='utf-8')
    f.write(
        f"""---
layout: post
title: "{args.name}"
date:   {datetime.now().strftime('%Y-%m-%d')}
categories: [paper]
tags: []
pinned: false
toc: true
author: ruirui-daydayup
---

 <!--more-->
        """
        )
    f.close()
    time.sleep(3)
    os.system('C:\\"Program Files"\Typora\\typora.exe {}'.format(
        filename))


```

- push.sh

```shell
git add *
git commit -m "init"
git push origin master
```

- md.sh

```python
python md.py --name $1
```







