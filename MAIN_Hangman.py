import random
import time
import string
from hint import give_clue

with open('dictionary.txt') as f:
  words = list(f)

print("\n### Welcome to a new game of HANGMAN! ###")
time.sleep(0.8)
print("\nYour friend is in serious trouble and he needs you to save him! \n\nAre you ready to start playing...?")

start_playing = input("\nPress Y for yes or N for no\n")
start_playing = start_playing.upper()


while start_playing == 'Y':
  word = random.choice(words).strip()
  word_length = len(word)

  print("\nIn the hidden word lies the secret for saving your friend\'s life.")
  time.sleep(0.8)
  print("\nEvery wrong guess of a letter, your little friend is closer to his death!")
  time.sleep(0.8)
  print("\nYou can only guess wrong 8 times, if don't want to \'leave him hanging\'.") 

  chances_left = 8
  attempts_num = 0  


  time.sleep(0.8)
  print("\nThe hidden word is {} letters long. Fill in those blanks!".format(word_length))  
  
  word_guess = ''
  for i in range(word_length):
    word_guess += '*' 
  time.sleep(0.8)
  print("\n" + word_guess)

  time.sleep(0.6)
  print("\nDo you want to start off with a little clue?")
  with_clue = input("\nPress Y for yes or N for no\n")
  with_clue = with_clue.upper()
  if with_clue == 'Y':
    time.sleep(0.6)
    word_guess = give_clue(word)
    time.sleep(0.6)
    print("\nThere you go: " + word_guess)
    time.sleep(0.6)
    print("\nREMEMBER: The hidden word is {} letters long.".format(word_length))
    time.sleep(0.6)
  if with_clue == 'N':
    time.sleep(0.4)
    print("Alright then...")
    time.sleep(0.4)
  
  
  while word_guess != word:
    word_guess_list = [word_guess[i] for i in range(word_length)]

    
    if chances_left == 8:
      if attempts_num == 0:
        letter_guess = input("\nTry your first guess...\n")
        attempts_num += 1
      elif attempts_num > 0:
        time.sleep(0.6)
        print("\nYour progress so far: " + word_guess) # keeps the user's progress visible
        letter_guess = input("\nInsert a new letter...\n")  
        attempts_num += 1
    elif chances_left < 8 and chances_left > 1:
      time.sleep(0.6)
      print("\nYour progress so far: " + word_guess)
      time.sleep(0.4)
      letter_guess = input("\nInsert a new letter...\n")
      attempts_num += 1
    elif chances_left == 1:
      time.sleep(0.6)
      print("\nYour progress so far: " + word_guess)
      time.sleep(0.4)
      letter_guess = input("\nThis is your last chance to save your friend, he\'s entering the tunnel!!\n")
      attempts_num += 1
    else:
      print("\nYou have lost after {} attempts. Your friend is dead, and it's all on you.".format(attempts_num))
      time.sleep(0.4)
      print("\nThe word you were looking for was {}".format(word))
      time.sleep(0.4)
      print("\nDo you want to give it another go..?")
      start_playing = input("\nPress Y for yes or N for no\n")
      start_playing = start_playing.upper()
      if start_playing == 'N':
        print("\nBetter luck next time!! Bye!") 
        break

    
    time.sleep(0.6)
    letter_guess = letter_guess.upper() 
    if len(letter_guess) > 1:
      print("\nThat's cheating! You can only guess one letter at a time.")
      time.sleep(0.4)
      letter_guess = input("\nWe\'ll let that one slide, tho. Try again...\n")
    if letter_guess not in string.ascii_letters:
      print("\nSymbols are never part of words!")
      time.sleep(0.4)
      letter_guess = input("\nYou\'ll never save your friend if you don\'t take this seriously. Try again...\n")
    if letter_guess in word_guess:
      letter_guess = input("\nYou already tried that letter. Once is enough! Try again...\n")
    
    
    letter_guess = letter_guess.upper()
    if letter_guess not in word:
      chances_left -= 1
      print("\nSorry!! The letter you chose is not contained in the hidden word.")
      time.sleep(0.6)
      print("\nYou have {} chances left.".format(chances_left))
    
    if letter_guess in word:
      print("\nGreat!! The letter {} is in the hidden word.".format(letter_guess))
      time.sleep(0.6)
      for i in range(len(word_guess_list)):
        if word[i] == letter_guess:
          word_guess_list[i] = letter_guess
      word_guess = ''.join(word_guess_list) 
      
      if word_guess != word:
        time.sleep(0.6)
        print("\nYou are one step closer to saving your buddy!\n")
  
      if word_guess == word:
        time.sleep(0.6)
        print("\nYou won!!")
        time.sleep(0.6)
        print("\nYour buddy may be a bit sore in the neck, but he is now safe and sound, thanks to you!!")
        time.sleep(0.6)
        print("\nYor skills can save many mor lives!! Do you want to play another game?")
        start_playing = input("\nPress Y for yes or N for no\n")
        start_playing = start_playing.upper()
        if start_playing == 'N':
          time.sleep(0.5)
          print("\nThat's it then, maybe they can manage without you... See you next time!")
