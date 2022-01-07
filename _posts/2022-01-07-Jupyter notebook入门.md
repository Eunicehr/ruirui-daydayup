---
layout: post
title: "github-pages"
date:   2022-01-05
categories: [python]
tags: [python]
pinned: false
toc: true
author: cute-rui
---

# Jupyter notebook入门



## 创建新笔记

1. 打开vscode，使用快捷键`ctrl+shift+P`，打开选项栏,输入jupyter,选择打开新的notebook

   ![image-20220106234750742](https://s2.loli.net/2022/01/06/DbMtr2B5Y4g3Nhv.png)

   ![image-20220107005936487](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20220107005936487.png)

2. 选择需要的python

   ![4ca62326a276c6a476dacf60697adeb](https://s2.loli.net/2022/01/07/V7nIZk5tMJTxDEi.png)![f0e647f5dba776923089316f13c258a](https://s2.loli.net/2022/01/07/8wFR7QghszTJXNP.png)

   


   > 1. jupyter 可以运行多种语言，是一种及编程和写作于一身的强大的编辑工具
   > 2. Jupyter notebook是基于Ipython内核的，在浏览器中以网页形式运行Python代码的工具，十分方便
   > 3. ipython是一个更高级的python解释器

## 单元格蓝绿两模式：命令模式、编辑模式

Jupyter notebook中，代码和文档都存在于一个个单元格中，每个单元格都有蓝色和绿色两种模式。绿色框（编辑模式）和蓝色框（命令模式）

- 命令模式（蓝色）

  可以执行键盘输入的快捷命令，如新增单元格、剪切、复制等。 `Esc` 可以从编辑模式退回到命令模式，此时单元左侧显示蓝色竖线。在命令模式下按X剪切，按C复制单元格，按Z恢复，shift+v粘贴单元格到上方，V粘贴到当前。

- 编辑模式（绿色）

  可以编辑文本和代码。选中单元并按 `Enter` 键进入编辑模式，此时单元左侧显示绿色竖线。

## 两种单元格：代码单元格和Markdown单元格

Jupyter notebook中，有两种单元格：代码单元格和Markdown单元格。

- 代码单元格

  ![image-20220107012348082](https://s2.loli.net/2022/01/07/hYxInmLyfNUaS4J.png)

可以编写代码，按 `Shift + Enter` 运行代码，其结果显示在本单元下方。代码单元左边有 `In [1]:` 这样的序列标记，方便人们查看代码的执行次序。在蓝色命令模式下，按`y`键可以将Markdown单元格转换为代码单元格。

- 

  ```
  print ("hello world")
  ```

  enter+shift运行代码，输出结果

  ![image-20220107213838826](https://s2.loli.net/2022/01/07/ivFdPf7QJU5GbTh.png)

- Markdown 单元格

  ![image-20220107012254454](https://s2.loli.net/2022/01/07/h18JN4Ynsf79H2m.png)可以对文本进行编辑、设置文本格式、插入链接、图片和数学公式等。按`Shift + Enter` 运行 markdown ，其结果显示在本单元下方。在蓝色命令模式下按`m`键可以将代码单元格转换为Markdown单元格。

  ```markdown
  # 我是Markdown一号标题
  ## 我是Markdown二号标题
  ### 我是Markdown三号标题
  >我是引用，我这行开头有一个灰色竖杠
  
  [我是外部链接，点我上百度](www.baidu.com)
  ![我是图片](https://i1.hdslb.com/bfs/face/c59e147cd3b1f6a7bb88690933499354a024b280.jpg@68w_68h.webp)
  ```

  ![image-20220107081148362](https://s2.loli.net/2022/01/07/kD3HoCqMZxWY4mT.png)

## 在Markdown中插入数学公式

- 

```markdown
这是爱因斯坦的质能转换方程$E=mc^2$，揭示了质量和能量之间的关系
```

![image-20220107081707507](https://s2.loli.net/2022/01/07/AVLdUt4cRJKqFaM.png)

![image-20220107081930500](https://s2.loli.net/2022/01/07/EWKgqwsiBhml4rA.png)

- 

```
这是一元二次方程求解公式
$$x = \frac{-b\pm \sqrt{b^2-4ac}}{2a}$$
初中数学内容
```

![image-20220107081846667](https://s2.loli.net/2022/01/07/quKAIGkD69Hp7lP.png)

## 常用快捷键

| 快捷键      | 功能                               |
| :---------- | ---------------------------------- |
| h           | 查看所有快捷键                     |
| Enter       | 从命令模式进入编辑模式             |
| Esc         | 从编辑模式退回到命令模式           |
| m           | 将代码单元格转换为Markdown单元格   |
| y           | 将Markdown单元格转换为代码单元格   |
| shift+Enter | 运行本单元格，选择下面的代码块     |
| ctrl+Enter  | 运行本单元格                       |
| alt+Enter   | 运行本单元格，在下方新建一个单元格 |
| a           | 在上方新建一个单元格（above）      |
| b           | 在下方新建一个单元格（below）      |
| d           | 删除选中的单元格（delete）         |
| x           | 剪切本单元格                       |
| c           | 复制本单元格                       |
| shift v     | 粘贴到上面                         |
| v           | 粘贴到下面                         |
| l           | 显示代码行号                       |

## 所有快捷键

- h 查看所有快捷键

  > 这些快捷键和vscode 的jupyter的快捷键有些不一样
  
  ![image-20220107005030666](https://s2.loli.net/2022/01/07/cifXIbDNk89HjOB.png)

![image-20220107005146571](https://s2.loli.net/2022/01/07/mQpDjbG1isYflon.png)

