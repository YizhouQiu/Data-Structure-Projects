from Deque import Deque

class Queue:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    return str(self._dq)

  def __len__(self):
    return len(self._dq)

  def enqueue(self, val):
    self._dq.push_back(val)

  def dequeue(self):
    return self._dq.pop_front()

if __name__ == '__main__':
  #TODO test cases here
  
  a = Queue()
  
  a.enqueue(45)
  print(a)
  
  a.enqueue(81)
  print(a)
  
  a.dequeue()
  print(a)
  
  a.dequeue()
  print(a)
  
  a.dequeue()
  print(a)
  
  a.enqueue(10)
  print(a)
  
  a.enqueue(5)
  print(a)
  
  print(len(a))
