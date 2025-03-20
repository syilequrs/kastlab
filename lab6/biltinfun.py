def task1(numbers):
  return eval('*'.join(list(map(str, numbers))))
numbers = list(map(int, input().split()))
print("Product of numbers:", task1(numbers))
def task2():
  s = input()
  uppercase = sum(1 for i in s if i.isupper())
  lowercase = sum(1 for i in s if i.islower())
  print(f'{uppercase}\n{lowercase}')
task2()
def task3():
  s = input()
  print(s == s[::-1])
task3()
def task4():
  from time import sleep
  num = int(input())
  sleepTime = int(input())
  sleep(sleepTime / 1000)
  print(f'Square root of {num} after {sleepTime} miliseconds is {num**0.5}')
task4()
def task5(tup):
  return True if all(tup) else False
n = int(input())
tup = tuple(bool(int(input())) for i in range(n))
print(task5(tup))
