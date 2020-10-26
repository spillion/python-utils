#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re


def findcontent(str1):
    re1 = re.search(r'(?:\w+\.|\w+)+(?=\.\w+}})', str1)
    re2 = re.search(r'\w+(?=}})', str1)
    re3 = re.search(r'{{(?:\w+\.)+', str1)
    if re1:
        # {{ getDeepValue1(jcxxData.CYLXRY.RYXB,'VALUE','无')}}
        print("原来" + str1)
        pattern = re3.group(0)
        repl1 = '{{getDeepValue('+re1.group(0)+",'"
        repl2 = re2.group(0) + "','无')"
        new1 = re.sub(r'{{(?:\w+\.)+', repl1, str1)
        new2 = re.sub(r'\w+(?=}})', repl2, new1)
        print("现在" + new2)
        print('\n')
    else:
        return 0;
    return new2


file2 = open("C:\\Users\\kedacom\\Desktop\\1.txt", "w",  encoding='utf-8')
with open("C:\\Users\\kedacom\\Desktop\\新建文本文档.txt", 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line1 = line.strip('\n')
        new1 = findcontent(line1)
        if new1:
            line1 = new1
        file2.write(line1)
        # 把末尾的'\n'删掉

file2.close()

# re1 = re.search(r'\w+(?=}})', '{{scope.row.WD}}')
# re2 = re.search(r'(?:\w+\.|\w+)+(?=\.\w+}})', '{{ VALUE.han}}')
# print(re1.group(0))
# print(re2.group(0))
