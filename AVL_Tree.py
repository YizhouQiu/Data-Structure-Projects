class AVL_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class _AVL_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
      self._value = value
      self._childleft=None
      self._childright=None
      self._height=1
    def calculate_balance(self):
      if self._childleft is None:
        left_height=0
      else:
        left_height=self._childleft._height
        
      if self._childright is None:
        right_height=0
      else:
        right_height=self._childright._height
      result = right_height - left_height
      return result 
    
    def find_min(self):
      if self._childleft is None:
        return self._value
      else:
        result_min=self._childleft.find_min()
        return result_min

  def __init__(self):
    self._root = None

# insert_element() and its private methods _insert() and balance() 
  def insert_element(self, value):  
    if self._root is None:
      self._root=AVL_Tree._AVL_Node(value)
    else:
        self._insert(value,self._root)

  def _insert(self, value, Node):
    if Node._value > value:
    #insert at left child
      if Node._childleft is None:
        Node._childleft = AVL_Tree._AVL_Node(value)
        Node._height=self._get_height(Node)
        return self._balance_insert(Node)
      else:
        Node._childleft=self._insert(value,Node._childleft)
        Node._height=self._get_height(Node)
        return self._balance_insert(Node)    
    elif Node._value == value:
      return Node
    elif Node._value < value:
    #insert at right child
      if Node._childright is None:
        Node._childright = AVL_Tree._AVL_Node(value)
        Node._height=self._get_height(Node)
        return self._balance_insert(Node)
      else:
        Node._childright=self._insert(value,Node._childright)
        Node._height=self._get_height(Node)
        return self._balance_insert(Node)
      
  def _balance_insert(self, Node):
   
    if Node.calculate_balance() == -2:
      if Node._childleft.calculate_balance()  ==-1:
        result = Node._childleft
        Node._childleft=result._childright
        result._childright=Node
        result._height=self._get_height(result)
        result._childright._height=self._get_height(result._childright)
        if Node is self._root:
          self._root=result
        return result
      elif Node._childleft.calculate_balance() == 1:
        #rotate around left child
        tmp= Node._childleft
        Node._childleft = Node._childleft._childright
        tmp._childright=Node._childleft._childleft
        Node._childleft._childleft=tmp
        #rotate 
        result = Node._childleft
        Node._childleft=result._childright
        result._childright=Node
        result._height=self._get_height(result)
        result._childright._height=self._get_height(result._childright)
        if Node is self._root:
          self._root=result
        return result 
    elif Node.calculate_balance() == 2:
      if Node._childright.calculate_balance() == 1:
        result = Node._childright
        Node._childright=result._childleft
        result._childleft=Node
        result._height=self._get_height(result)
        result._childleft._height=self._get_height(result._childleft)
        if Node is self._root:
          self._root=result
        return result
      elif Node._childright.calculate_balance() == -1:
        #rotate around left child
        tmp= Node._childright
        Node._childright = Node._childright._childleft
        tmp._childleft=Node._childright._childright
        Node._childright._childright=tmp
        #rotate 
        result = Node._childright
        Node._childright=result._childleft
        result._childleft=Node
        result._height=self._get_height(result)
        result._childleft._height=self._get_height(result._childleft)
        if Node is self._root:
          self._root=result
        return result 
    else:
      return Node
  
  def remove_element(self, value):
    if self._root is None:
      return 
    else:
      self._root=self._remove_element(value,self._root)
  def _remove_element(self,value,Node):
    
    if Node._value == value:
      if Node._childleft is None and Node._childright is None:
        return  #justify: if the Node is a leaf, return None
      elif Node._childleft is None or Node._childright is None:
        if Node._childleft is not None:
          return Node._childleft  
        else:
          return Node._childright
      else:
        value=Node._childright.find_min()
        Node._childright=self._remove_element(value,Node._childright)
        Node._value = value
        Node._height=self._get_height(Node)
        return self._balance_remove(Node)     
    else:
      if value < Node._value and Node._childleft is not None:
        Node._childleft=self._remove_element(value,Node._childleft)
      elif value > Node._value and Node._childright is not None:
        Node._childright=self._remove_element(value,Node._childright)
      Node._height=self._get_height(Node)
      return self._balance_remove(Node)
  def _balance_remove(self, Node):
    if Node.calculate_balance() == -2:
      if Node._childleft.calculate_balance()  ==-1 or \
         Node._childleft.calculate_balance() == 0:
        result = Node._childleft
        Node._childleft=result._childright
        result._childright=Node
        result._height=self._get_height(result)
        result._childright._height=self._get_height(result._childright)
        if Node is self._root:
          self._root=result
        return result
      elif Node._childleft.calculate_balance() == 1:
        #rotate around left child
        tmp= Node._childleft
        Node._childleft = Node._childleft._childright
        tmp._childright=Node._childleft._childleft
        Node._childleft._childleft=tmp
        #rotate 
        result = Node._childleft
        Node._childleft=result._childright
        result._childright=Node
        result._height=self._get_height(result)
        result._childright._height=self._get_height(result._childright)
        if Node is self._root:
          self._root=result
        return result 
    elif Node.calculate_balance() == 2:
      if Node._childright.calculate_balance() == 1 or \
         Node._childright.calculate_balance() == 0:
        result = Node._childright
        Node._childright=result._childleft
        result._childleft=Node
        result._height=self._get_height(result)
        result._childleft._height=self._get_height(result._childleft)
        if Node is self._root:
          self._root=result
        return result
      elif Node._childright.calculate_balance() == -1:
        #rotate around left child
        tmp= Node._childright
        Node._childright = Node._childright._childleft
        tmp._childleft=Node._childright._childright
        Node._childright._childright=tmp
        #rotate 
        result = Node._childright
        Node._childright=result._childleft
        result._childleft=Node
        result._height=self._get_height(result)
        result._childleft._height=self._get_height(result._childleft)
        if Node is self._root:
          self._root=result
        return result 
    else:
      return Node
#in_order() and its private method _in_order():  
  def in_order(self):
    
    if self._root is None:
      return "[ ]"
    else:
      result_string="[ "
      result_string= self._in_order(self._root,result_string)
      result_string= result_string[:-2]
      result_string= result_string + " ]"
      return result_string
    
  def _in_order(self, Node,result_string): 
    
    if Node._childleft is None:
      result_string += (str(Node._value)+ ", ")
      if Node._childright is not None:
        result_string = self._in_order(Node._childright,result_string)
      return result_string    
    else:
      result_string=self._in_order(Node._childleft,result_string)
      result_string += (str(Node._value)+ ", ")
      if Node._childright is not None:
          result_string=self._in_order(Node._childright,result_string)
      return result_string

      
# pre_order() and its private method _pre_order():  
  def pre_order(self):
    
    if self._root is None:
      return "[ ]"
    else:
      result_string = "[ "
      result_string = self._pre_order(self._root,result_string)
      result_string = result_string[:-2]
      result_string += " ]"
      return result_string
    
  def _pre_order(self,Node,result_string): 
    
    result_string += (str(Node._value) + ", ")
    if Node._childleft is not None:
      result_string = self._pre_order(Node._childleft, result_string)
    if Node._childright is not None:
      result_string = self._pre_order(Node._childright,result_string)
    return result_string
      

#post_order() and its private method _post_order():     
  def post_order(self):
    if self._root is None:
      return "[ ]"
    else:
      result_string = "[ "
      result_string = self._post_order(self._root, result_string)
      result_string = result_string[:-2]
      result_string += " ]"
      return result_string
  
  def _post_order(self,Node,result_string):
    if Node._childleft is None:
      if Node._childright is not None:
        result_string = self._post_order(Node._childright,result_string)
      result_string += (str(Node._value)+ ", ")
      return result_string
    else:
      result_string=self._post_order(Node._childleft,result_string)
      if Node._childright is not None:
          result_string=self._post_order(Node._childright,result_string)    
      result_string += (str(Node._value)+ ", ")
      return result_string
    
    
#get_height() and its private method _get_height()
  def get_height(self):
    if self._root is None:
      return 0
    else:
      return self._get_height(self._root)
  def _get_height(self,Node):
    if Node is None:
      return 0
    if Node._childleft is None and Node._childright is None:
      return 1
    else:
      Node_height=1 + max(self._get_height(Node._childleft),\
                      self._get_height(Node._childright))
      return Node_height
    
    
#method for printing 
  def __str__(self):
    return self.in_order()

print("TestcaseA")
#does the tree function correctly if the tree is empty
tree=AVL_Tree()
print("Expected: [ ] \n  Actual:",str(tree.in_order()))
print("Expected: [ ] \n  Actual:",str(tree.pre_order()))
print("Expected: [ ] \n  Actual:",str(tree.post_order()))
print("Expected: None \n  Actual:",str(tree.remove_element(389089)))
print("Expected: 0 \n  Actual:",str(tree.get_height()))
print("----------------------")
print()

print("TestcaseB")
#if the insert_element() method works correctly?
#if the in_order() method works correctly?
#if the pre_order() method works correctly?
#if the post_order() method works correctly?
tree.insert_element(80)
tree.insert_element(120)
tree.insert_element(40)
tree.insert_element(50)
tree.insert_element(20)
print("Expected: [ 20, 40, 50, 80, 120 ] \n  Actual:",str(tree.in_order()))
print("Expected: [ 80, 40, 20, 50, 120 ] \n  Actual:",str(tree.pre_order()))
print("Expected: [ 20, 50, 40, 120, 80 ] \n  Actual:",str(tree.post_order()))
print("Expected: 3 \n  Actual:",str(tree.get_height()))
print("----------------------")
print()

print("TestcaseC")
#tests for imbalance during insertion
print("Left-left imbalance")
tree.insert_element(10)
print("Expected: [ 10, 20, 40, 50, 80, 120 ] \n  Actual:",str(tree.in_order()))
print("Expected: [ 40, 20, 10, 80, 50, 120 ] \n  Actual:",str(tree.pre_order()))
print("Expected: [ 10, 20, 50, 120, 80, 40 ] \n  Actual:",str(tree.post_order()))
print("Expected: 3 \n  Actual:",str(tree.get_height()))
print()

print("Left-right imbalance")
tree.insert_element(15)
print("Expected: [ 10, 15, 20, 40, 50, 80, 120 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 40, 15, 10, 20, 80, 50, 120 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 10, 20, 15, 50, 120, 80, 40 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 3 \n  Actual:",str(tree.get_height()))
print()

print("Right-right imbalance")
tree.insert_element(140)
tree.insert_element(160)
print("Expected: [ 10, 15, 20, 40, 50, 80, 120, 140, 160 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 40, 15, 10, 20, 80, 50, 140, 120, 160 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 10, 20, 15, 50, 120, 160, 140, 80, 40 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 4 \n  Actual:",str(tree.get_height()))

print("Right-left imbalance")
tree.insert_element(125)
print("Expected: [ 10, 15, 20, 40, 50, 80, 120, 125, 140, 160 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 40, 15, 10, 20, 120, 80, 50, 140, 125, 160 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 10, 20, 15, 50, 80, 125, 160, 140, 120, 40 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 4 \n  Actual:",str(tree.get_height()))
print("----------------------")
print()

print("TestcaseD")
tree.remove_element(1000)
print("Expected: [ 10, 15, 20, 40, 50, 80, 120, 125, 140, 160 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 40, 15, 10, 20, 120, 80, 50, 140, 125, 160 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 10, 20, 15, 50, 80, 125, 160, 140, 120, 40 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 4 \n  Actual:",str(tree.get_height()))
print()
tree.insert_element(125)
print("Expected: [ 10, 15, 20, 40, 50, 80, 120, 125, 140, 160 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 40, 15, 10, 20, 120, 80, 50, 140, 125, 160 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 10, 20, 15, 50, 80, 125, 160, 140, 120, 40 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 4 \n  Actual:",str(tree.get_height()))
print("----------------------")
print()

print("TestcaseE")
#tests for imbalance during removal
print("Right-right imbalance")
tree.remove_element(10)
tree.remove_element(20)
print("Expected: [ 15, 40, 50, 80, 120, 125, 140, 160 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 120, 40, 15, 80, 50, 140, 125, 160 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 15, 50, 80, 40, 125, 160, 140, 120 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 4 \n  Actual:",str(tree.get_height()))

print()
print("Right-left imbalance")
tree.remove_element(15)
print("Expected: [ 40, 50, 80, 120, 125, 140, 160 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 120, 50, 40, 80, 140, 125, 160 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 40, 80, 50, 125, 160, 140, 120 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 3 \n  Actual:",str(tree.get_height()))
print()

print("Left-left imbalance")
tree.insert_element(30)
tree.remove_element(80)
print("Expected: [ 30, 40, 50, 120, 125, 140, 160 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 120, 40, 30, 50, 140, 125, 160 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 30, 50, 40, 125, 160, 140, 120 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 3 \n  Actual:",str(tree.get_height()))
print()

print("Left-right imbalance")
tree.insert_element(60)
tree.remove_element(160)
tree.remove_element(125)
print("Expected: [ 30, 40, 50, 60, 120, 140 ] \n  Actual:",\
      str(tree.in_order()))
print("Expected: [ 50, 40, 30, 120, 60, 140 ] \n  Actual:", \
      str(tree.pre_order()))
print("Expected: [ 30, 40, 60, 140, 120, 50 ] \n  Actual:",\
      str(tree.post_order()))
print("Expected: 3 \n  Actual:",str(tree.get_height()))
print("----------------------")
print()