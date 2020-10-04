"""
23.0 队列（Queue）

23.0.1 队列
·队列是一个数据结合，仅允许在列表的一端进行插入，另一端进行删除
·进行插入的一端称为队尾（rear），插入动作称为进队或入队
·进行删除的一端称为队头（front），删除动作称为出队
·队列的性质：先进先出FIFO（first-in,first-out）
-------------------------------------------------------------------------------
23.0.2 队列的实现方式：环形队列

·环形队列：
当队尾/队首指针 rear/front == Maxsize - 1时，再前进一个位置就自动到0
队首指针前进1：front = (front + 1) % Maxsize
队尾指针前进1：rear = (rear + 1) % Maxsize
队空条件：rear == front
队满条件：（rear + 1）% Maxsize == front
-------------------------------------------------------------------------------
23.0.3 双向队列

·双向队列的两端都支持进队和出队操作
·双向队列的基本操作：队首进队、队首出队、队尾进队、队尾出队
-------------------------------------------------------------------------------
23.0.4 Python队列内置模块

·使用方法：from collections import deque
    创建队列：queue = deque(）
    进队：qppend()
    出队：popleft()
    双向队列队首进队：appendleft()
    双向队列队尾出队：pop()

===============================================================================
===============================================================================
"""


# ========== example ==========
class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue id filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue id empty.")

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


# q = Queue(5)
# for i in range(4):
#     q.push(i)
# print(q.is_filled())
# print(q.pop())
# q.push(4)
# print(q.queue)


# ========== deque ==========
from collections import deque


# q = deque([1, 2, 3, 4, 5], 5)
# q.append(6)  # 队尾进队
# print(q.popleft())  # 队首出队

# 用于双向队列
# q.appendleft(1)  # 队首进队
# q.pop()  # 队尾出队


def tail(n):  # 打印文件最后n行
    with open('23 Queue-队列.txt', 'r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='')
