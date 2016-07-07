# -*- coding: utf-8 -*-

from ac_ahocorasick import *
import jieba
import jieba.analyse
import re

def contentinbracket(c):# 取QQ号码
    if c.endswith(')'):
         p1 = re.compile(r'\(.*\)')
         tmp = str(p1.findall(c))
         tmp = tmp[3:len(tmp)-3]
    else: tmp = 'null'
    return tmp

def MatchResult(textFile):  #文本预处理
         key_name1 = []
         key_name2 = []
         key_name = []
         list_key = []
         value_line = []
         dic = {}
         ac = UnicodeAcAutomation()  #匹配初始化
         try:
            with open(textFile, 'r') as message:
                   for line in message:
                      #区分话题
                          if line.startswith('-----'): 
                              key_name1.append(key_name)
                              key_name2.append(dic)
                              key_name = []
                              value_line = []                  
                              continue
                           #提取聊天人
                          if line.startswith('201'): 
                              time = re.findall(r'\d{4}-\d{2}-\d{2}\s+\d{1,2}:\d{2}:\d{2}',line)
                              dele_time = line.replace(time[0], '').strip('\n')
                              dele_time = contentinbracket(dele_time)
                              key_name.append(dele_time)
                           #提取聊天人对应的内容
                          elif not line.startswith('\n'):
                              jieba.analyse.set_idf_path('idf.txt.big')
                              hh = jieba.analyse.extract_tags(line, topK = 1)
                              rr = ' '.join(hh).encode('utf-8').decode('utf-8')
                              value_line.append(rr)
                              list_tuple = zip(key_name, value_line)
                              dic = dict(list_tuple)
         except EnvironmentError:
             print 'oops'

         #回应词匹配
         for dic in key_name2:
            for key, val in dic.items():
               ac.insert(val)
               ac.build_automation()
            with open('Responsice_words.txt', 'r') as word:
                     for i in word:
                        keys = jieba.analyse.extract_tags(i, topK = 1)
                        keywords = ' '.join(keys).encode('utf-8').decode('utf-8')
                        tuple_words = ac.matchOne(keywords)
                        if tuple_words[1] != None:
                           dic[key] = tuple_words[0]
         return key_name1
        
#将数据处理成元组列表的形式
def JiaQuan():
        list1 = []
        list2 = []
        list3 = []
        data = MatchResult('2011tx3.txt')
        for dic in data:
            list1.append(dic)
        for li in list1:
            list3.append(list2)
            list2 = []
            i = 1
            for i in range(len(li)):
               if i <=1: 
                   list2.append((li[i],li[0],3.0))
               else:
                   list2.append((li[i],li[0],1.0))
        listdata = list3[2:]
##        print listdata[:10]
        return listdata
              
def WuQuan():
        list1 = []
        list2 = []
        list3 = []
        data = MatchResult('2011tx3.txt')
        for dic in data:
            list1.append(dic)
        for li in list1:
            list3.append(list2)
            list2 = []
            i = 1
            for i in range(len(li)):
                   list2.append((li[i],li[0]))
        listdata = list3[2:]
        return listdata
              

      
   
