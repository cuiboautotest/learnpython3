'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, node):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(node)
        while self.s2:
            self.s1.append(self.s2.pop())
    def pop(self):
        return self.s1.pop()
