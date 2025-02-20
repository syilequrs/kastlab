def kvadrat(n):
  for i in range(1, n + 1):
    yield i * i

generator = kvadrat(int(input()))
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())

def even():
    n = int(input())
    def chetn(n):
      for i in range(0, n + 1, 2):
        yield i

    chetch = ', '.join(str(num) for num in chetn(n))
    print(chetch)

even()
    
def div34(n):
  for i in range(n+1):
    if i % 3 == 0 and i % 4 == 0:
      yield i
n = int(input())

for i in div34(n):
  print(i)

for num in div34(30):
  print(num)

def sqab(a, b):
  for i in range(a, b+1):
    yield i * i
a = int(input("a"))
b = int(input("b"))
for num in sqab(a, b):
  print(num)
        
def nt(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
for i in nt(n):
  print(i)