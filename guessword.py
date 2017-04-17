# -*- coding: cp936 -*-
import random

def readWords():
    """从文件words.txt中读取所有单词构建出单词列表并返回"""
    f = open('words.txt')
    words = []
    for line in f.readlines():
        words.append(line.strip())
    f.close()
    return words

def generateSimplePuzzle(words):
    """
    从单词列表中随机挑选出一个单词作为谜底，并随机将该单词的一个
    字母替换为下划线后构成谜面，将谜底与谜面构成一个元组后返回
    words: 单词列表
    return（返回值）：谜底与谜面构成的元组，注意谜底是第一个元素，谜面是第二元素
    """
    # 提示：
    # 利用random模块从一个列表中随机选择一个元素的方法有两种：
    # 1. random.choice(words)会从words列表中随机返回一个元素
    # 2. random.randint(0, len(words))会从0到words列表的长度
    #    （包括该长度）之间随机选出一个数字并返回，可以利用该数字
    #    和列表的索引操作获取列表中的一个元素，这样获取的元素也是随机
    #    获取的。
    while True:
      s = input('输入任意大于0，最大数为10，以定义下划线。\n\t什么也不输入，直接结束程序。')
      plzzle = "猜这个单词："
      
      ask = []
      b = "_"
      answer = random.choice(words)
      if len(answer) < s:
          print "单词空行过多，即将重新计算答案。"
          continue# 1. 生成谜底
      for a in answer:
                  ask.append(a)
      if s == 0:
          print "调皮"
          continue
      j=[]
      while True:
             
             if len(j)== s:
                 break
             p = random.randint(0, len(ask))            
             if p >= len(ask):
                 print "对不起，超出范围，正在重新生成中！\n正在为你降低难度，一次一格，多多包容！"
                 s = s-1
                 continue
             else:
                 ask[p] = b
                 if p not in j:
                     j.append(p)
                
             
      
             
      for stt in ask:
          plzzle += stt + " "

      tuple_1 = (answer,plzzle)# 2. 生成谜面
    

      return tuple_1# 3. 返回谜底与谜面
    

def main():
    # 读取所有单词
    words = readWords()
    count, credit = 0, 0
   
    # 重复执行以下步骤：
    # 1.生成题目，代码：puzzle = generatePuzzle(words)
    # 2.从屏幕接受玩家猜测的词
    # 3.判断该单词是否存在并显示相应结果
    while True:
        # generate a puzzle randomly
        answer, puzzle = generateSimplePuzzle(words)
        count += 1
        print puzzle
        print ''
        guess = raw_input("请输入您猜测的单词：")
        if guess == answer:
            print "您猜对啦！"
            credit += 1
        else:
            print "没有这个单词哦！"
            print "谜底是%s"%answer
        print "总共"+str(count)+"个单词。您猜对了"+str(credit)+"个！"

main()
