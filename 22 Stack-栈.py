"""
22.0 栈（Stack）

·栈是一个数据集合，可以理解为只能在一端进行插入嚯删除操作的列表
·栈的特点：后进先出LIFO（last-in,first-out）
·栈的概念：栈顶、栈底
·栈的基本操作：
    进栈（压栈）：push
    出栈：pop
    取栈顶：gettop
·使用一般的列表结构即可实现栈
    进栈：li.append
    出栈：li.pop
    取栈顶：li[-1]

===============================================================================
===============================================================================
"""


# ========== example ==========
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())


# ========== 括号匹配问题 ==========
def brace_match(s):
    match = {'}': '{', ']': '[', ')': '('}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:  # ch in {'}',']',')'}
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:  # stack.get_top() !== match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('[{()}(){()}[]({}){}]'))
print(brace_match('()}'))
