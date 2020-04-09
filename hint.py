import random

def give_clue(word):
  hinti1 = random.randrange(len(word))
  hinti2 = random.randrange(len(word))
  
  def replace_all(hinti):
    for i in range(len(word)):
      if word[i] == word[hinti]:
        cluelist[i] = word[hinti]
    return cluelist
  
  while hinti2 == hinti1:
    hinti2 = random.randrange(len(word))
  
  cluelist = ['*' for i in range(len(word))]
  cluelist = replace_all(hinti1)
  if len(word) > 8:
    cluelist = replace_all(hinti2)
      
  return ''.join(cluelist)
