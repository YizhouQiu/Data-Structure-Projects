# Austin Pearce and Yizhou Qiu
# Project 1: Classes, Objects, and Arrays
# CSCI 241: Data Structures
# Section: MW 2:00 - 3:20
# Instructor: James Deverick
# This program includes two classes, Score and Scoreboard. Score includes the
# methods add_points, subtract_points, get_player_name, get_multiplier, 
# increment_multiplier, get_score, get_level, get_lives, lose_life, gain_life,
# and a string method. Scoreboard includes the methods update and 
# print_scoreboard. There are also several test cases in order to check the
# influence on the values returned or used by several other methods.


class Score:

  def __init__(self, player_name):
    # The required attributes
    self._player_name = player_name
    self._current_score = 0
    self._current_level = 0
    self._current_multiplier = 1
    self._lives_remaining = 3

  # The required methods
  def add_points(self, amount):
    # Implement this method by adding the number of points specified by 
    # amount times the current Multiplier value to the currentScore. 
    # If the new score value should result in the level changing, 
    # then change currentLevel.
    # Return the new value of currentScore.
    
    currentScore = self._current_score
    currentMultiplier = self._current_multiplier
    currentLevel = self._current_level
    
    currentScore = (amount) * (currentMultiplier) + (currentScore)
    
    while currentScore >= (2**currentLevel) * 10000:
      currentLevel += 1
    
    self._current_level = currentLevel
    self._current_score = currentScore
    
    return self._current_score
      
  def subtract_points(self, amount):
    # Resets currentMultipler to 1. 
    # Subtract the number of points specified by amount 
    # from currentScore, and update currentLevel if necessary.
    # Return the new value of currentScore.
    
    self._current_multiplier = 1
    
    currentScore = self._current_score
    currentLevel = self._current_level
    
    if currentScore >= amount:
      currentScore = currentScore - amount
    elif currentScore < amount:
      currentScore = 0
    
    if currentScore != 0:
      while currentScore < (2**(currentLevel-1)) * 10000:
	if currentLevel == 0:
	  currentLevel = 0
	else:
	  currentLevel -= 1
    else:
      currentLevel = 0
    
    self._current_level = currentLevel
    self._current_score = currentScore
    
    return self._current_score
  
  def get_player_name(self):
    # Return the name of the player associated with this object.
    
    return self._player_name

  def get_multiplier(self):
    # Return the current value of the multiplier attribute.
    
    return self._current_multiplier

  def increment_multiplier(self):
    # Increase the value of currentMultiplier by one.
    # Return the new value of currentMultiplier.
    
    currentMultiplier = self._current_multiplier 
    
    currentMultiplier += 1
    
    self._current_multiplier = currentMultiplier
    
    return self._current_multiplier

  def get_score(self):
    # Return the current value of the score attribute.
    
    return self._current_score

  def get_level(self):
    # Return the current value of the level attribute.
    
    return self._current_level

  def get_lives(self):
    # Return the number of lives remaining.
    
    return self._lives_remaining

  def lose_life(self):
    # Decrement the number of lives remaining. 
    # If, after you have decremented the lives attributes, that attribute
    # has a positive value, return True, indicating play can continue.
    # If the number is zero, return false, indicating that the game is over.
    
    livesRemaining = self._lives_remaining
    
    livesRemaining -= 1
    
    self._lives_remaining = livesRemaining
    
    if self._lives_remaining > 0:
      return True
    else:
      return False
   
    
  def gain_life(self):
    # Increase the current value of the lives attribute by one.
    
    livesRemaining = self._lives_remaining
    
    livesRemaining += 1
    
    self._lives_remaining = livesRemaining
    
    return self._lives_remaining

  def __str__(self):
    return self._player_name + ' SCORE: ' + str(self._current_score) +\
        ' LVL: '+ str(self._current_level) +\
        ' MULT: ' + str(self._current_multiplier) +\
        ' LIVES: ' + str(self._lives_remaining)

class Scoreboard:

  def __init__(self, capacity):
    self._high_scores = [None] * capacity
    self._entries = 0

  def update(self, candidate_score):
    # If candidate_score has a score value higher than the lowest
    # score in the Scoreboard, add it at the correct position.
    
    highScores = self._high_scores
      
    for i in range(len(highScores)):
      if highScores[i] != None:
	if candidate_score.get_score() > highScores[i].get_score():
	  temp = highScores[i]
	  highScores[i] = candidate_score
	  for k in range(i+1,len(highScores)): 
	    temp2 = highScores[k]
	    highScores[k] = temp
	    temp = temp2
	  break 
      elif highScores[i] == None:
	highScores[i] = candidate_score 
	break      
	
	  
  def print_scoreboard(self):
    # Take advantage of the fact that the Score object implements the
    # __str__() method, and can therefore be passed directly to print().
    # Use this to print the current score board.
    
    highScores = self._high_scores
    
    for i in range(len(highScores)):
      if highScores[i] != None:
	print highScores[i]

if __name__ == '__main__':
  # Your test code goes here.
  # Create multiple Score objects, test the methods thoroughly.
  # Be careful not to make assumptions about how the methods behave or what
  # order things happen in.
  # Finally, create a Scoreboard instance and add your score objects
  # to it, printing it each time to ensure that they are ordered correctly.
  
  # TESTING FOR CLASS SCORE
  # Testing for add_points
  #EXPECTED:
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  test1 = Score("Steve")
  test1.add_points(60000)
  print("")
  print("Testing for add_points: ")
  print("")   
  print (test1)
    
  # Testing for add_points with multiplier and increment_multiplier
  #EXPECTED:
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  test2 = Score("Abby")
  test2.increment_multiplier()    
  test2.add_points(20000)
  print("")
  print("Testing for add_points, Multiplier and increment_multiplier: ")
  print("")   
  print(test2)
    
  #Testing for add_points for upper bounds of level
  #EXPECTED:
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3
  test3 = Score("Richard")
  test3.add_points(19999)
  print("")
  print("Testing for add_points, Upper Bounds of Level: ")
  print("")   
  print(test3)
    
  #Testing for add_points for lower bounds of level
  #EXPECTED:
  #  Emily SCORE: 10000 LVL: 1 MULT: 1 LIVES: 3
  test4 = Score("Emily")
  test4.add_points(10000)
  print("")
  print("Testing for add_points, Lower Bounds of Level: ")
  print("")   
  print(test4)
    
  #Testing for subtract_points
  #EXPECTED:
  #  Benjamin SCORE: 20000 LVL: 2 MULT: 1 LIVES: 3
  test5 = Score("Benjamin")
  test5.add_points(40000)
  test5.subtract_points(20000)
  print("")
  print("Testing for subtract_points: ")
  print("")   
  print(test5)
    
  #Testing for subtract_points with multiplier returning to 1
  #EXPECTED:
  #  Theresa SCORE: 130000 LVL: 4 MULT: 1 LIVES: 3
  test6 = Score("Theresa")
  test6.increment_multiplier()
  test6.add_points(80000)
  test6.subtract_points(30000)
  print("")
  print("Testing for subtract_points, Multiplier Returning to 1: ")
  print("")   
  print(test6)
    
  #Testing for subtract_points for more than current score
  #EXPECTED:
  #  Tom SCORE: 0 LVL: 0 MULT: 1 LIVES: 3
  test7 = Score("Tom")
  test7.add_points(40000)
  test7.subtract_points(60000)
  print("")
  print("Testing for subtract_points, Greater Than Current Score: ")
  print("")   
  print(test7)
    
  #Testing for subtract_points for equal to current score
  #EXPECTED:
  #  Beth SCORE: 0 LVL: 0 MULT: 1 LIVES: 3
  test8 = Score("Beth")
  test8.add_points(40000)
  test8.subtract_points(40000)
  print("")
  print("Testing for subtract_points, Equal to Current Score: ")
  print("")   
  print(test8)
    
  #Testing for get_player_name
  #EXPECTED:
  #  Test name: Steve
  test_name = test1.get_player_name()
  print("")
  print("Testing for get_player_name: ")
  print("")   
  print("Test name: " + test_name)
    
  #Testing for get_multiplier
  #EXPECTED:
  #  Test multiplier: 2
  test_multiplier = test2.get_multiplier()
  print("")
  print("Testing for get_multiplier: ")
  print("")   
  print("Test multiplier: " + str(test_multiplier))
    
  #Testing for get_score
  #EXPECTED
  #  Test score: 19999
  test_score = test3.get_score()
  print("")
  print("Testing for get_score: ")
  print("")   
  print("Test score: " + str(test_score))
    
  #Testing for get_level
  #EXPECTED:
  #  Test level: 2
  test_level = test5.get_level()
  print("")
  print("Testing for get_level: ")
  print("")   
  print("Test level: " + str(test_level))
    
  #Testing for lose_life
  #EXPECTED:
  #  James SCORE: 0 LVL: 0 MULT: 1 LIVES: 2
  test9 = Score("James")
  test9.lose_life()
  print("")
  print("Testing for lose_life: ")
  print("")   
  print(test9)
    
  #Testing for lose_life, losing all lives
  #EXPECTED:
  #  Game continue: True
  #  Game continue: True
  #  Game continue: False
  #  Jenna SCORE: 0 LVL: 0 MULT: 1 LIVES: 0
  test10 = Score("Jenna")
  test_lose = test10.lose_life()
  print("")
  print("Testing for lose_life, Losing All Lives: ")
  print("")   
  print("Game continue: " + str(test_lose))
  test_lose = test10.lose_life()
  print("Game continue: " + str(test_lose))
  test_lose = test10.lose_life()
  print("Game continue: " + str(test_lose))
  print(test10)
    
  #Testing for gain_life
  #EXPECTED:
  #  Schleeeeeeer SCORE: 50000 LVL: 3 MULT: 1 LIVES: 4
  test11 = Score("Schleeeeeeer")
  test11.add_points(50000)
  test11.gain_life()
  print("")
  print("Testing gain_life: ")
  print("")   
  print(test11)
    
  #Testing for get_lives
  #EXPECTED:
  #  Test lives: 4
  test_lives = test11.get_lives()
  print("")
  print("Testing get_lives: ")
  print("")  
  print("Test lives: " + str(test_lives))  
  
  
  #TESTING FOR CLASS SCOREBOARD
  #Testing for building initial scoreboard
  #EXPECTED:
  #  Nothing will print becuase there are no objects in the scoreboard.
  print("")
  print("Building the Initial Scorebaord: ")
  scoreBoard = Scoreboard(5)
  scoreBoard.print_scoreboard()
  print("Nothing will print becuase there are no objects in the scoreboard.")
  
  #Testing for first update scoreboard
  #EXPECTED:
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3
  print("")
  print("First Update to Scoreboard: ")
  print("")  
  test_update = Scoreboard(5)
  test_update.update(test3)
  test_update.print_scoreboard()
  
  #Testing for second update scoreboard
  #EXPECTED:
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3  
  print("")
  print("Second Update to Scoreboard: ")
  print("")  
  test_update.update(test2)
  test_update.print_scoreboard()
  
  #Testing for third update scoreboard
  #EXPECTED:
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3  
  print("")
  print("Third Update to Scoreboard: ")
  print("")  
  test_update.update(test1)
  test_update.print_scoreboard()
  
  #Testing for fourth update scoreboard
  #EXPECTED:
  #  Theresa SCORE: 130000 LVL: 4 MULT: 1 LIVES: 3
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3  
  print("")
  print("Fourth Update to Scoreboard: ")
  print("")  
  test_update.update(test6)
  test_update.print_scoreboard()
  
  #Testing for fifth update scoreboard
  #EXPECTED: 
  #  Theresa SCORE: 130000 LVL: 4 MULT: 1 LIVES: 3
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3
  #  Tom SCORE: 0 LVL: 0 MULT: 1 LIVES: 3  
  print("")
  print("Fifth Update to Scoreboard: ")
  print("")  
  test_update.update(test7)
  test_update.print_scoreboard()
  
  #Testing for overloading scoreboard, inadequate score
  #EXPECTD: 
  #  Theresa SCORE: 130000 LVL: 4 MULT: 1 LIVES: 3
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3
  #  Tom SCORE: 0 LVL: 0 MULT: 1 LIVES: 3  
  print("")
  print("Overloading Scoreboard: Inadequate Score: ")
  print("")  
  test_update.update(test8)
  test_update.print_scoreboard()
  
  #Testing for overloading scoreboard, pushing a score off the end
  #EXPECTED:
  #  Theresa SCORE: 130000 LVL: 4 MULT: 1 LIVES: 3
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3
  #  Emily SCORE: 10000 LVL: 1 MULT: 1 LIVES: 3
  print("")
  print("Overloading Scoreboard: Inserting in End: ")
  print("")  
  test_update.update(test4)
  test_update.print_scoreboard()
  
  #Testing for overloading scoreboard, inserting score into middle of scoreboard
  #EXPECTED: 
  #  Theresa SCORE: 130000 LVL: 4 MULT: 1 LIVES: 3
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  #  Schleeeeeeer SCORE: 50000 LVL: 3 MULT: 1 LIVES: 4
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Richard SCORE: 19999 LVL: 1 MULT: 1 LIVES: 3  
  print("")
  print("Overloading Scoreboard: Inserting in Middle: ")
  print("")
  test_update.update(test11)
  test_update.print_scoreboard()
  
  #Testing for same scores on scoreboard
  # EXPECTED: 
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Tom SCORE: 0 LVL: 0 MULT: 1 LIVES: 3   
  print("")
  print("Testing for Same Score on Scoreboard, Part 1: ")
  print("") 
  test_same = Scoreboard(5)
  test_same.update(test1)
  test_same.update(test2)
  test_same.update(test7)
  test_same.print_scoreboard()
  # EXPECTED: 
  #  Steve SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
  #  Abby SCORE: 40000 LVL: 3 MULT: 2 LIVES: 3
  #  Tom SCORE: 0 LVL: 0 MULT: 1 LIVES: 3
  #  Beth SCORE: 0 LVL: 0 MULT: 1 LIVES: 3   
  print("")
  print("Testing for Same Score on Scoreboard, Part 2: ")
  print("")   
  test_same.update(test8)
  test_same.print_scoreboard() 
    