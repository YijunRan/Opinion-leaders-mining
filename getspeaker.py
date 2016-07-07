# -*- coding: utf-8 -*-
"""
提取发言人列表
"""
import re
import pickle
from operator import itemgetter

def re_data(strline):#使用正则表达式提取发言人
     reg = re.compile('^(?P<YMD>[^ ]*) (?P<hms>[^ ]*) (?P<speaker>[^ ]*)')
     regMatch = reg.match(strline)
     dict0 = regMatch.groupdict()
     speaker = dict0['speaker']
     return speaker

#取()中内容
def contentinbracket(c):
    if c.endswith(')'):
         p1 = re.compile(r'\(.*\)')
         tmp = str(p1.findall(c))
         tmp = tmp[3:len(tmp)-3]
    else: tmp = 'null'
    return tmp

def important_speakers(f3): #2提取重要话题发起人
    j = 0
    info_speakers = []
    info_speakers0 = []
    with open(f3) as f:
        for each_line in f:
            if each_line.startswith('---'):
                if '不' not in each_line and info_speakers0 != []:
                    info_speakers.append(info_speakers0[0])
                info_speakers0 = []
                j += 1
            elif each_line.startswith('201'):
                (part1,part2,part3) = each_line.strip('\n').split(' ',2)
                part3 = contentinbracket(part3)
                each_line = part1 +' '+ part2 +' '+ part3
                info_speakers0.append(re_data(each_line))
        return info_speakers[1:]

