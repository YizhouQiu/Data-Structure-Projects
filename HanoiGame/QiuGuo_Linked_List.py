#Name: Yizhou Qiu and Wendy Guo
#Instructor: James Deverick
#Project2: Linked_List
#Project3 edits made by Yizhou Qiu and Clay Moughon

class Linked_List:
  
  class _Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      
      self._value = val
      self._next = None
      self._pre = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    
    self._header = self._Node(None)
    self._trailer = self._Node(None)
    self._header._next = self._trailer
    self._trailer._pre = self._header
    self._size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    
    length = 0
    current = self._header._next
    while current is not self._trailer:
      length += 1
      current = current._next
    
    return length
      

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the tail position.
    
    size = len(self)
    new_node = self._Node(val)
    if size == 0:
      self._header._next = new_node
      self._trailer._pre = new_node
      new_node._next = self._trailer
      new_node._pre = self._header
    else:
      new_node._next = self._trailer
      new_node._pre = self._trailer._pre
      self._trailer._pre._next = new_node
      self._trailer._pre = new_node
    
    self._size += 1
    

  def insert_element_at(self, val, index):
    # assuming the head position is indexed 0, add a
    # node containing val at the specified index. If 
    # the index is not a valid position within the list,
    # ignore the request. This method cannot be used
    # to add an item at the tail position.
    
    size = len(self)
    if index >= size :
      return
    if index < 0:
      return
    else:
      current = self._header
      new_node = self._Node(val)
      
      for i in range(0, index):
        current = current._next
      new_node._next = current._next
      new_node._pre = current._next._pre
      current._next._pre = new_node
      current._next = new_node
      size += 1
      self._size = size
    

  def remove_element_at(self, index):
    # assuming the head position is indexed 0, remove
    # and return the value stored in the node at the 
    # specified index. If the index is invalid, ignore
    # the request.
    
    size = len(self)
    
    if index >= size:
      return
    
    if index < 0:
      return
     
    current = self._header
    for i in range(0, index):
      current = current._next
      
    value = current._next._value
    current._next = current._next._next
    current._next._pre = current
    
    size -= 1
    self._size = size
    
    return value
      

  def get_element_at(self, index):
    # assuming the head position is indexed 0, return
    # the value stored in the node at the specified
    # index, but do not unlink it from the list.
    
    size = len(self)
    current = self._header
    
    if index >= size+1:
      return
    
    if index == 0:
      value = current._next._value
    
    else:
      for i in range(0, index+1):
        current = current._next
    
      value = current._value
    return value

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    
    size = len(self)
    
    if size == 0:
      return '[ ]' 
    else:
      string = '[ '
      current = self._header
      for i in range(0, size-1):
        current = current._next
        string = string + str(current._value) + ', '
      current = current._next
      string = string + str(current._value) + ' ]'
      return string
    
    
      
    
    

class Poly_Val:

  def __init__(self, coef, exp):
    self._coefficient = coef
    self._exponent = exp

  def get_coefficient(self):
    return self._coefficient

  def get_exponent(self):
    return self._exponent

  def __str__(self):
    return str(self._coefficient) + 'x^' + str(self._exponent)

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods ignore your
  # requests when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location?
  
  #test appending an item to empty linked list and size increment:  
  test_1 = Linked_List()
  test_1.append_element(3)
  print("test appending an item to empty linked list and size increment:")
  print("Expect = [3] Size: 1")
  print("Actual = " + str(test_1))
  
  #test appending an item to nonempty linked list and size increment
  test_1.append_element(100)
  print("")
  print("test appending an item to nonempty linked list, size increment:")
  print("Expect = [3, 100] Size: 2")  
  print("Actual = " + str(test_1))
  
  #testing inserting element in a empty linked list:
  test_3 = Linked_List()
  test_3.insert_element_at(3,0)
  print("")
  print("test inserting element in a empty linked list:")
  print("Expect = [ ] Size: 0")
  print("Actual = " + str(test_3))
  
  #test inserting element at index=0 and increasing the size 
  #by one:
  test_1.insert_element_at(22,0)
  print("")
  print("test inserting element at index=0 and increasing the size by one:")
  print("Expect = [22, 3, 100] Size: 3")  
  print("Actual = " + str(test_1))
  
  #test inserting element at another valid index and increasing the 
  #size by one
  test_1.insert_element_at(45,1)
  print("")
  print("test inserting element at another valid index=1 and increasing the\
  size by one:")
  print("Expect = [22, 45, 3, 100] Size: 4")  
  print("Actual = " + str(test_1))

  #test inserting at tail position
  test_1.insert_element_at(87,3)
  print("")
  print("test inserting at tail position:")
  print("Expect = [22, 45, 3, 100] Size: 4")  
  print("Actual = " + str(test_1))
  
  #test inserting at invalid index
  test_1.insert_element_at(102, 7)
  print("")
  print("test inserting at invalid index=7:")
  print("Expect = [22, 45, 3, 100] Size: 4")    
  print("Actual = " + str(test_1))
  
  #test removing an item at a valid index and decreasing the size 
  #by one
  test_1.remove_element_at(0)
  print("")
  print("test removing an item at a valid index=0 and decreasing the size by\
  one:")
  print("Expect = [45, 3, 100] Size: 3")    
  print("Actual = " + str(test_1))
  
  #test removing an item at invalid index 
  test_1.remove_element_at(9)
  print("")
  print("test removing an item at invalid index=9:")
  print("Expect = [45, 3, 100] Size: 3")    
  print("Actual = " + str(test_1))
  
  #test getting an element stored in the node at index 0 but do not unlink
  #it from the list
  print("")
  print("test getting an element stored in the node at index=0 but do not\
  unlink it from the list:")
  print("Expect = 45, [45, 3, 100] Size: 3")
  print("Actual = " + str(test_1.get_element_at(0)) + ", " + str(test_1))
  
  #test getting an element stored in the node at a valid index=3 but do not
  #unlink it from the list
  print("")
  print("test getting an element stored in the node at a valid index=3 but do\
  not unlink it from the list:")
  print("Expect = 3, [45, 3, 100] Size: 3")
  print("Actual = " + str(test_1.get_element_at(1)) + ", " + str(test_1)) 
  
  #test getting an element stored in the node at another valid index but do not
  #unlink it from the list
  print("")
  print("test getting an element stored in the node at valid index=2\
  but do not unlink it from the list:")
  print("Expect = 100, [45, 3, 100] Size: 3")
  print("Actual = " + str(test_1.get_element_at(2)) + ", " + str(test_1))
  
  #test getting an element stored in the node at an invalid index
  print("")
  print("test getting an element stored in the node at an invalid index=3:")
  print("Expect = None, [45, 3, 100] Size: 3")
  print("Actual = " + str(test_1.get_element_at(7)) + ", " + str(test_1))
  
  #test getting an element when the node's value is None
  test_1.append_element(None)
  print('')
  print("test getting an element when the node's value is NOne:")
  print("Expect = None, [45, 3, 100, None] Size: 4")
  print("Actual = " + str(test_1.get_element_at(3)) + ", " + str(test_1))

  #test getting an element from an empty linked list
  test_1.remove_element_at(2)
  test_1.remove_element_at(1)
  test_1.remove_element_at(0)
  test_1.remove_element_at(0)  
  print("")
  print("test getting an element from an empty linked list:")
  print("Expect = None, [ ] Size: 0")
  print("Actual = " + str(test_1.get_element_at(7)) + ", " + str(test_1))
  

  #test if length return the number of values stored in the list:
  test_2 = Linked_List()
  test_2.append_element(12)
  test_2.append_element(31)
  print('')
  print("test if length returns the number of values stored in the list:")
  print("Expect: [12, 31] Size: 2 Length = 2")
  print("Actual: " + str(test_2) + " Length = " + str(len(test_2)))
  
  #test if length return the number of values stored in \
  #the list
  test_2.append_element(None)
  test_2.insert_element_at(82,1)
  print('')
  print("test if length returns the number of values stored in the linked\
  list")
  print("Expect: [12, 82, 31, None] Size: 4 Length = 4")
  print("Actual: " + str(test_2) + " Length = " + str(len(test_2)))
  
  
  # The following code should appear after your tests for your
  # linked list class.

  p1 = Linked_List()
  p1.append_element(Poly_Val(10,1012))
  p1.append_element(Poly_Val(5,14))
  p1.append_element(Poly_Val(1,0))
  p2 = Linked_List()
  p2.append_element(Poly_Val(3,1990))
  p2.append_element(Poly_Val(-2,14))
  p2.append_element(Poly_Val(11,1))
  p2.append_element(Poly_Val(5,0))

  p3 = Linked_List()

  # here, create the Poly_Val objects that should comprise p3
  # and add them to the list. Make sure that p3 is constructed
  # correctly regardless of the contents of p1 and p2. Try
  # building different polynomials for p1 and p2 and ensure that
  # they sum correctly.
  i = 0
  n = 0
  coef_3 = 0
  expo_3 = 0
  while i < len(p1) and n < len(p2):
    current_1 = p1.get_element_at(i)
    current_2 = p2.get_element_at(n)
    if current_1.get_exponent() < current_2.get_exponent():
      coef_3 = current_2.get_coefficient()
      expo_3 = current_2.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      n += 1
    elif current_1.get_exponent() > current_2.get_exponent():
      coef_3 = current_1.get_coefficient()
      expo_3 = current_1.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      i += 1
    else:
      coef_3 = current_1.get_coefficient() + current_2.get_coefficient()
      expo_3 = current_1.get_exponent()
      n += 1
      i += 1
      p3.append_element(Poly_Val(coef_3,expo_3))
  
  while p1.get_element_at(i) is not p1.get_element_at(len(p1)):
    coef_3 = p1.get_element_at(i).get_coefficient()
    expo_3 = p1.get_element_at(i).get_exponent()
    i += 1
    p3.append_element(Poly_Val(coef_3,expo_3))
    
  while p2.get_element_at(n) is not p2.get_element_at(len(p2)):
    coef_3 = p2.get_element_at(n).get_coefficient()
    expo_3 = p2.get_element_at(n).get_exponent()
    n += 1
    p3.append_element(Poly_Val(coef_3,expo_3))
  
  print('')
  print("The result for adding up p1 and p2 is:")
  print("Expect = [3x^1990, 10x^1012, 3x^14, 11x^1, 6x^0] Size: 5")  
  print("Actual = " + str(p3))
  
  #Test adding up two polynomials which have no same exponent:
  p1 = Linked_List()
  p1.append_element(Poly_Val(10,1012))
  p1.append_element(Poly_Val(5,14))
  p1.append_element(Poly_Val(1,0))
  p2 = Linked_List()
  p2.append_element(Poly_Val(3,1990))
  p2.append_element(Poly_Val(-2,13))
  p2.append_element(Poly_Val(11,2))
  p2.append_element(Poly_Val(5,1))
  
  p3 = Linked_List()
  i = 0
  n = 0
  coef_3 = 0
  expo_3 = 0
  while i < len(p1) and n < len(p2):
    current_1 = p1.get_element_at(i)
    current_2 = p2.get_element_at(n)
    if current_1.get_exponent() < current_2.get_exponent():
      coef_3 = current_2.get_coefficient()
      expo_3 = current_2.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      n += 1
    elif current_1.get_exponent() > current_2.get_exponent():
      coef_3 = current_1.get_coefficient()
      expo_3 = current_1.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      i += 1
    else:
      coef_3 = current_1.get_coefficient() + current_2.get_coefficient()
      expo_3 = current_1.get_exponent()
      n += 1
      i += 1
      p3.append_element(Poly_Val(coef_3,expo_3))
  
  while p1.get_element_at(i) is not p1.get_element_at(len(p1)):
    coef_3 = p1.get_element_at(i).get_coefficient()
    expo_3 = p1.get_element_at(i).get_exponent()
    i += 1
    p3.append_element(Poly_Val(coef_3,expo_3))
    
  while p2.get_element_at(n) is not p2.get_element_at(len(p2)):
    coef_3 = p2.get_element_at(n).get_coefficient()
    expo_3 = p2.get_element_at(n).get_exponent()
    n += 1
    p3.append_element(Poly_Val(coef_3,expo_3))  
  
  print('')
  print("Test adding polynomials which have no same exponent:")
  print("Expect = [3x^1990, 10x^1012, 5x^14, -2x^13, 11x^2, 5x^1, 1x^0]\
  Size: 7")
  print("Actual = " + str(p3))
  
  #Test adding up two polynomials which have same number of terms and same 
  #exponent too:
  p1 = Linked_List()
  p1.append_element(Poly_Val(2,4))
  p1.append_element(Poly_Val(2,3))
  p1.append_element(Poly_Val(2,2))
  p1.append_element(Poly_Val(2,1))  
  p2 = Linked_List()
  p2.append_element(Poly_Val(2,4))
  p2.append_element(Poly_Val(2,3))
  p2.append_element(Poly_Val(2,2))
  p2.append_element(Poly_Val(2,1))
    
  p3 = Linked_List()
  i = 0
  n = 0
  coef_3 = 0
  expo_3 = 0
  while i < len(p1) and n < len(p2):
    current_1 = p1.get_element_at(i)
    current_2 = p2.get_element_at(n)
    if current_1.get_exponent() < current_2.get_exponent():
      coef_3 = current_2.get_coefficient()
      expo_3 = current_2.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      n += 1
    elif current_1.get_exponent() > current_2.get_exponent():
      coef_3 = current_1.get_coefficient()
      expo_3 = current_1.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      i += 1
    else:
      coef_3 = current_1.get_coefficient() + current_2.get_coefficient()
      expo_3 = current_1.get_exponent()
      n += 1
      i += 1
      p3.append_element(Poly_Val(coef_3,expo_3))
    
  while p1.get_element_at(i) is not p1.get_element_at(len(p1)):
    coef_3 = p1.get_element_at(i).get_coefficient()
    expo_3 = p1.get_element_at(i).get_exponent()
    i += 1
    p3.append_element(Poly_Val(coef_3,expo_3))
      
  while p2.get_element_at(n) is not p2.get_element_at(len(p2)):
    coef_3 = p2.get_element_at(n).get_coefficient()
    expo_3 = p2.get_element_at(n).get_exponent()
    n += 1
    p3.append_element(Poly_Val(coef_3,expo_3))  
    
  print('')
  print("Test adding polynomials which have same numbers of terms and\
  same exponent too:")
  print("Expect = [4x^4, 4x^3, 4x^2, 4x^1] Size: 4")
  print("Actual = " + str(p3))
  
  #Test adding up two polynomials which have big difference in regard of number
  #of terms
  p1 = Linked_List()
  p1.append_element(Poly_Val(2,4))  
  p2 = Linked_List()
  p2.append_element(Poly_Val(2,7))
  p2.append_element(Poly_Val(2,6))
  p2.append_element(Poly_Val(2,5))
  p2.append_element(Poly_Val(2,4))
  p2.append_element(Poly_Val(2,3))
  p2.append_element(Poly_Val(2,2))
  p2.append_element(Poly_Val(2,1))
      
  p3 = Linked_List()
  i = 0
  n = 0
  coef_3 = 0
  expo_3 = 0
  while i < len(p1) and n < len(p2):
    current_1 = p1.get_element_at(i)
    current_2 = p2.get_element_at(n)
    if current_1.get_exponent() < current_2.get_exponent():
      coef_3 = current_2.get_coefficient()
      expo_3 = current_2.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      n += 1
    elif current_1.get_exponent() > current_2.get_exponent():
      coef_3 = current_1.get_coefficient()
      expo_3 = current_1.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      i += 1
    else:
      coef_3 = current_1.get_coefficient() + current_2.get_coefficient()
      expo_3 = current_1.get_exponent()
      n += 1
      i += 1
      p3.append_element(Poly_Val(coef_3,expo_3))
      
  while p1.get_element_at(i) is not p1.get_element_at(len(p1)):
    coef_3 = p1.get_element_at(i).get_coefficient()
    expo_3 = p1.get_element_at(i).get_exponent()
    i += 1
    p3.append_element(Poly_Val(coef_3,expo_3))
    
  while p2.get_element_at(n) is not p2.get_element_at(len(p2)):
    coef_3 = p2.get_element_at(n).get_coefficient()
    expo_3 = p2.get_element_at(n).get_exponent()
    n += 1
    p3.append_element(Poly_Val(coef_3,expo_3))  
      
  print('')
  print("Test adding up two polynomials which have big difference in\
  regard of terms")
  print("Expect = [2x^7, 2x^6, 2x^5, 4x^4, 2x^3, 2x^2, 2x^1] Size: 7")
  print("Actual = " + str(p3))  
  
  #Test adding up one polynomial with a another 0 terms polynomial
  p1 = Linked_List()
  p2 = Linked_List()
  p2.append_element(Poly_Val(2,7))
  p2.append_element(Poly_Val(2,6))
  p2.append_element(Poly_Val(2,5))
  p2.append_element(Poly_Val(2,4))
  p2.append_element(Poly_Val(2,3))
  p2.append_element(Poly_Val(2,2))
  p2.append_element(Poly_Val(2,1))
    
  p3 = Linked_List()
  i = 0
  n = 0
  coef_3 = 0
  expo_3 = 0
  while i < len(p1) and n < len(p2):
    current_1 = p1.get_element_at(i)
    current_2 = p2.get_element_at(n)
    if current_1.get_exponent() < current_2.get_exponent():
      coef_3 = current_2.get_coefficient()
      expo_3 = current_2.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      n += 1
    elif current_1.get_exponent() > current_2.get_exponent():
      coef_3 = current_1.get_coefficient()
      expo_3 = current_1.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      i += 1
    else:
      coef_3 = current_1.get_coefficient() + current_2.get_coefficient()
      expo_3 = current_1.get_exponent()
      n += 1
      i += 1
      p3.append_element(Poly_Val(coef_3,expo_3))
    
  while p1.get_element_at(i) is not p1.get_element_at(len(p1)):
    coef_3 = p1.get_element_at(i).get_coefficient()
    expo_3 = p1.get_element_at(i).get_exponent()
    i += 1
    p3.append_element(Poly_Val(coef_3,expo_3))
      
  while p2.get_element_at(n) is not p2.get_element_at(len(p2)):
    coef_3 = p2.get_element_at(n).get_coefficient()
    expo_3 = p2.get_element_at(n).get_exponent()
    n += 1
    p3.append_element(Poly_Val(coef_3,expo_3))  
    
  print('')
  print("Test adding up one polynomial with a another 0 terms polynomial:") 
  print("Expect = [2x^7, 2x^6, 2x^5, 2x^4, 2x^3, 2x^2, 2x^1] Size: 7")
  print("Actual = " + str(p3))
  
  #Test adding up two 0 terms polynomials
  p1 = Linked_List()
  p2 = Linked_List()
    
  p3 = Linked_List()
  i = 0
  n = 0
  coef_3 = 0
  expo_3 = 0
  while i < len(p1) and n < len(p2):
    current_1 = p1.get_element_at(i)
    current_2 = p2.get_element_at(n)
    if current_1.get_exponent() < current_2.get_exponent():
      coef_3 = current_2.get_coefficient()
      expo_3 = current_2.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      n += 1
    elif current_1.get_exponent() > current_2.get_exponent():
      coef_3 = current_1.get_coefficient()
      expo_3 = current_1.get_exponent()
      p3.append_element(Poly_Val(coef_3, expo_3))
      i += 1
    else:
      coef_3 = current_1.get_coefficient() + current_2.get_coefficient()
      expo_3 = current_1.get_exponent()
      n += 1
      i += 1
      p3.append_element(Poly_Val(coef_3,expo_3))
    
  while p1.get_element_at(i) is not p1.get_element_at(len(p1)):
    coef_3 = p1.get_element_at(i).get_coefficient()
    expo_3 = p1.get_element_at(i).get_exponent()
    i += 1
    p3.append_element(Poly_Val(coef_3,expo_3))
      
  while p2.get_element_at(n) is not p2.get_element_at(len(p2)):
    coef_3 = p2.get_element_at(n).get_coefficient()
    expo_3 = p2.get_element_at(n).get_exponent()
    n += 1
    p3.append_element(Poly_Val(coef_3,expo_3))  
    
  print('')
  print("Test adding up two 0 terms polynomials:") 
  print("Expect = [ ] Size: 0")
  print("Actual = " + str(p3))  
  
    
  