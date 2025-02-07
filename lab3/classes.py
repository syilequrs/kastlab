import math
#ex1
class strungi:

    def __init__(self):
        self.string = ''
        
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())
strg = strungi()
strg.getString()
strg.printString()
#ex2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length ** 2
obj = Square(int(input()))
print(obj.area())

#ex3
class Rectangle(Shape):
  def __init__(self, length, width):
    super().__init__()
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width
#ex4
class Point:
  def __init__(self, x, y) -> None:
     self.x = x
     self.y = y

  def show(self):
    print(f"x = {self.x}, y = {self.y}")

  def move(self, x1, y1):
      self.x = x1
      self.y = y1
    
  def dist(self, x1, y1):
    distance = ((x1 - self.x)**2 + (y1 - self.y)**2) ** 0.5
    print(f"distance between points: {distance}")
#ex5
class Account:
  def __init__(self, owner='', balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount > self.balance:
      raise(BaseException('You cant withdraw more than you have'))
 
    else: 
      self.balance -= amount
      return amount
#ex6
def primeFilter(nums):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return list(filter(lambda x: isPrime(x), nums))
