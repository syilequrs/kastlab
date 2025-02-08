import math
#ex1
def ounces(grams):
  return 28.3495231 * grams
print(ounces(int(input())))
#ex2
def celcisus(fahrenfarenheitaheithet):
  return (5/9) * (fahrenfarenheitaheithet-32)
print(celcisus(float(input())))
#ex3
def solve(numheads, numlegs):
  for chick in range(numheads+1):
    rab = numheads - chick
    if(2 * chick + 4 * rab) == numlegs:
      print(chick, rab)
      return
numheads, numlegs = map(int, input().split())
solve(numheads, numlegs)
#ex4
def filter_prime(nums: list):
    def isPrime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return False if n == 1 else True
    return list(filter(lambda x: isPrime(x), nums))
#ex5
from itertools import permutations
def str_permutations(s):
    for p in permutations(s):
        print(''.join(p))
str_permutations(str(input()))
#ex6
def changeOrder(s):
    return ' '.join(reversed(s.split()))

rev = changeOrder(str(input()))
print(rev)
#ex7
def has_33(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 3 and nums[i+1] == 3:
      return True
  return False
nums = [1, 2, 3, 3, 4]
print(has_33(nums))
#ex8
def spy_game(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
      return True
  return False
muns = [1,2,4,0,0,7,5]
print (spy_game(muns))
#ex9
from math import pi
def volume(radius):
  return (4/3) * pi * (radius**3)
r = int(input())
print(volume(r))
#ex10
def uniqueList(arr):
  n = []
  for i in arr:
    if i not in n:
      n.append(i) 
  return n
#ex11
def palindrom_ili_net(s):
  return True if s == s[::-1] else False
#ex12
def ihstogram(arr):
  for i in arr:
    print('*' * i)
#ex13 yahoo
from random import randint
def ugadayka():
  random = randint(1, 20)
  name = input("Hello! What is your name?\n")
  print(f"Well {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
  numbah_of_thies = 0
  while True:
    num = int(input())
    numbah_of_thies += 1
    if num < random:
        print('Your guess is too low.\nTake a guess.')
    elif num > random:
        print('Your guess is too high.\nTake a guess.')
    else:
        print(f'Good job, {name}! You guessed my number in {numbah_of_thies} guesses!')
        break
