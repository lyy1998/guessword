# -*- coding: cp936 -*-
import random

def readWords():
    """���ļ�words.txt�ж�ȡ���е��ʹ����������б�����"""
    f = open('words.txt')
    words = []
    for line in f.readlines():
        words.append(line.strip())
    f.close()
    return words

def generateSimplePuzzle(words):
    """
    �ӵ����б��������ѡ��һ��������Ϊ�յף���������õ��ʵ�һ��
    ��ĸ�滻Ϊ�»��ߺ󹹳����棬���յ������湹��һ��Ԫ��󷵻�
    words: �����б�
    return������ֵ�����յ������湹�ɵ�Ԫ�飬ע���յ��ǵ�һ��Ԫ�أ������ǵڶ�Ԫ��
    """
    # ��ʾ��
    # ����randomģ���һ���б������ѡ��һ��Ԫ�صķ��������֣�
    # 1. random.choice(words)���words�б����������һ��Ԫ��
    # 2. random.randint(0, len(words))���0��words�б�ĳ���
    #    �������ó��ȣ�֮�����ѡ��һ�����ֲ����أ��������ø�����
    #    ���б������������ȡ�б��е�һ��Ԫ�أ�������ȡ��Ԫ��Ҳ�����
    #    ��ȡ�ġ�
    while True:
      s = input('�����������0�������Ϊ10���Զ����»��ߡ�\n\tʲôҲ�����룬ֱ�ӽ�������')
      plzzle = "��������ʣ�"
      
      ask = []
      b = "_"
      answer = random.choice(words)
      if len(answer) < s:
          print "���ʿ��й��࣬�������¼���𰸡�"
          continue# 1. �����յ�
      for a in answer:
                  ask.append(a)
      if s == 0:
          print "��Ƥ"
          continue
      j=[]
      while True:
             
             if len(j)== s:
                 break
             p = random.randint(0, len(ask))            
             if p >= len(ask):
                 print "�Բ��𣬳�����Χ���������������У�\n����Ϊ�㽵���Ѷȣ�һ��һ�񣬶����ݣ�"
                 s = s-1
                 continue
             else:
                 ask[p] = b
                 if p not in j:
                     j.append(p)
                
             
      
             
      for stt in ask:
          plzzle += stt + " "

      tuple_1 = (answer,plzzle)# 2. ��������
    

      return tuple_1# 3. �����յ�������
    

def main():
    # ��ȡ���е���
    words = readWords()
    count, credit = 0, 0
   
    # �ظ�ִ�����²��裺
    # 1.������Ŀ�����룺puzzle = generatePuzzle(words)
    # 2.����Ļ������Ҳ²�Ĵ�
    # 3.�жϸõ����Ƿ���ڲ���ʾ��Ӧ���
    while True:
        # generate a puzzle randomly
        answer, puzzle = generateSimplePuzzle(words)
        count += 1
        print puzzle
        print ''
        guess = raw_input("���������²�ĵ��ʣ�")
        if guess == answer:
            print "���¶�����"
            credit += 1
        else:
            print "û���������Ŷ��"
            print "�յ���%s"%answer
        print "�ܹ�"+str(count)+"�����ʡ����¶���"+str(credit)+"����"

main()
