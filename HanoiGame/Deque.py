from QiuGuo_Linked_List import Linked_List

class Deque:

  def __init__(self):
    self._list = Linked_List()

  def __str__(self):
    return str(self._list)

  def __len__(self):
    return len(self._list)

  def push_front(self, val):
    if len(self._list) == 0:
      self._list.append_element(val)
    else:
      self._list.insert_element_at(val,0)
  
  def pop_front(self):
    if len(self._list) == 0:
      return None
    else:
      return self._list.remove_element_at(0)

  def peek_front(self):
    return self._list.get_element_at(0)
    

  def push_back(self, val):
    self._list.append_element(val)
  
  def pop_back(self):
    if len(self._list) == 0:
      return None
    else:
      return self._list.remove_element_at(len(self._list)-1)

  def peek_back(self):
    return self._list.get_element_at(len(self._list)-1)

if __name__ == '__main__':
  a = Deque()

  a.push_back(5)
  print(a)
  
  a.push_front(20)
  print(a)
  
  a.push_front(32)
  print(a)
  
  a.push_back(33)
  print(a)
  
  a.push_back(42)
  print(a)
  
  print(len(a))
  
  print(a.pop_front())
  print(a._list)
  
  print(a.peek_front())
  print(a._list)
  
  print(a.pop_back())
  print(a._list)
  
  print(a.peek_back())
  print(a._list)
  
  a.pop_back()
  a.pop_front()
  print(a.pop_front())
  print(a._list)
  
  print(a.pop_front())
  print(a.pop_back())
  print(a.peek_front())
  print(a.peek_back())
  
  print(len(a))
  
  
  
  
  
  
  
  
