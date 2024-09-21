# Problem -> Collatz Conjecture: 
"""
    Pick any integer 'x' to start with. 'x' should be divided by 2 if it is even, and multiplied by 3 + 1 if it is odd. 
    No matter the initial value choosen if this method is repeated enough times the series will ultimately reach cycles {4, 2, 1}.
"""

x: int = int(input("Please choose a even number to start with: "))

def collatz_sequence(x):
  """
  Takes any number and performs the calcualation of: if 'x' is even divide by two. If 'x' is odd multiply by 3 and add 1.

  Example --> \nPlease choose a even number to start with: 23\n
                [23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1] 
  Args:
      x (_type_): Takes any integer as a paramater

  Returns:
      _type_: Returns list of numbers that will always in in 4, 2, 1
  """
  seq: list = [x]
  if x < 1:
    return []
  while x > 1:
      if x % 2 == 0:
        x = x // 2
      else:
        x = 3 * x + 1 
      seq.append(x)
  return seq

print(collatz_sequence(x))

def find_421(y):
  """
  Find how many times 4, 2, 1 starts a set of numbers in any grouping within collatz list

  Args:
      y (_type_): y is the list generated by the collatz_sequence(x) function.
  """
  pass

def find_steps():
  """
  Count how many steps it took to get from original number down to 4, 2, 1
  """
  pass