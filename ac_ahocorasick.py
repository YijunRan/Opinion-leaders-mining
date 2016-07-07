#-*- coding:utf-8 -*-

KIND = 16

class Node():
    static = 0
    def __init__(self):
        self.fail = None
        self.next = [None]*KIND
        self.end = False
        self.word = None
        Node.static += 1

class AcAutomation():
    def __init__(self):
        self.root = Node()
        self.queue = []
        
    def getIndex(self, char):
        return ord(char)#返回一个代表unicode的整数
    
    def insert(self, string):
        p = self.root
##        p.next = [None]*KIND
        for char in string:
            index = self.getIndex(char)
            if p.next[index] == None:
                p.next[index] = Node()
            p = p.next[index]
        p.end = True
        p.word = string
        
    def build_automation(self):
        self.root.fail = None
        self.queue.append(self.root)
        while len(self.queue)!= 0:
            parent = self.queue[0]
            self.queue.pop(0)
            for i, child in enumerate(parent.next):
##                self.queue = []
                if child == None:
                    continue
                if parent == self.root:
                    child.fail = self.root
                else:
                    failp = parent.fail
                    while failp != None:
                        if failp.next[i] != None:
                            child.fail = failp.next[i]
                            break
                        failp = failp.fail
                    if failp == None:
                        child.fail = self.root
                self.queue.append(child)
                
    def matchOne(self, string):
        p = self.root
        for char in string:
            index = self.getIndex(char)
            while p.next[index] == None and p != self.root:
                p = p.fail
            if p.next[index] == None:
                p = self.root
            else:
                p = p.next[index]
            if p.end:
                return True, p.word
        return False, None
    
    


class UnicodeAcAutomation():
    def __init__(self,encoding='utf-8'):
        self.ac = AcAutomation()
        self.encoding = encoding
        
    def getAcString(self, string):
        string = bytearray(string.encode(self.encoding))
        ac_string = ''
        for byte in string:
            ac_string += chr(byte%16)
            ac_string += chr(byte/16)
        return ac_string
    
    def insert(self, string):
        if type(string) != unicode:
            raise Exception('UnicodeAcAutomation:: insert type not unicode')
        ac_string = self.getAcString(string)
        self.ac.insert(ac_string)

    def build_automation(self):
        self.ac.build_automation()
    
    def matchOne(self, string):
        if type(string) != unicode:
            raise Exception('UnicodeAcAutomation:: insert type not unicode')
        ac_string = self.getAcString(string)
        retcode, ret = self.ac.matchOne(ac_string)
        if ret != None:
            s = ''
            for i in range(len(ret)/2):
                s += chr(ord(ret[2*i])+ ord(ret[2*i+1])*16)
            ret = s.decode('utf-8')
        return retcode, ret
    
