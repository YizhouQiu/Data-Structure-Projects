from Deque import Deque

class Stack:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    return str(self._dq)
    
  def __len__(self):
    return len(self._dq)

  def push(self, val):
    self._dq.push_back(val)

  def pop(self):
    return self._dq.pop_back()

  def peek(self):
    return self._dq.peek_back()

if __name__ == '__main__':
  a=Stack()
  
  a.push(3)
  print(a)
  
  a.push(4)
  print(a)
  
  a.push(11)
  print(a)
  
  print(len(a))
  
  
  print(a.pop())
  print(a)
  
  print(a.peek())
  print(a)
  
  a.pop()
  a.pop()
  print(a.peek())
  a.pop()
  print(a)
  print(a.pop())
  
  
  
  
  
  
  
