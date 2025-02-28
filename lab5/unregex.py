import re
def ab():
    pattern = re.compile(r'ab*')
    text = input()
    print("YES" if pattern.search(text) else "NO")
ab()
def abb():
    pattern = re.compile(r'ab{2,3}')
    text = input()
    print("YES" if pattern.search(text) else "NO")
ab()
def lowtoscore():
    pattern = re.compile(r'[a-z]+\_')
    text = input()
    print(pattern.findall(text))
lowtoscore()
def Ull():
    pattern = re.compile(r'[A-Z]{1}[a-z]+')
    text = input()
    print(pattern.findall(text))
Ull()
def aendb():
    pattern = re.compile(r'a.+b\Z')
    text = input()
    print("YES" if pattern.search(text) else "NO")
aendb()
def nocomdotcol():
    pattern = re.compile(r'[ ,.]')
    text = input()
    print(pattern.sub(':', text))
nocomdotcol()
def snakfun():
    def snake_to_camel(snake_case):
        return re.sub(r"_([a-z])", lambda s: s.group(1).upper(), snake_case)
    snakeCase = input()
    camelCase = snake_to_camel(snakeCase)
    print(camelCase)
snakfun()
def split():
    text = input()
    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())
split()

def inspac():
    text = input()
    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())
inspac()
def camtos():
    def camelToSnake(snake_case):
        return re.sub(r"\B([A-Z])", lambda s: '_'+s.group(1), snake_case).lower()
    camelCase = input()
    snakeCase = camelToSnake(camelCase)
    print(snakeCase)
camtos()
