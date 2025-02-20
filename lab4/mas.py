from math import *

def degrad():
  deg = float(input())
  print(f'Output radians {radians(deg):.6f}')

degrad()

def trap():
  h = float(input())
  a = float(input())
  b = float(input())

  res = (1/2) * (a + b) * h
  print(f'Area = {res:.2f}')

trap()

def polyg():
  n = int(input())
  length = float(input())

  apothem = length / (2 * tan(pi/n))

  result = (n * length * apothem) / 2

  print(f'The area of the polygon is {result:.2f}')

polyg()

def para():
  length = float(input())
  height = float(input())
  result = length * height
  print(f"Area = {result:.2f}")
    
para()