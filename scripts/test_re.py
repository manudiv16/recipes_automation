import re 

text = """
# jfjfjf jfjfj jfsk sk  kskslskd  jsksdf slkfd
"""

pattern = re.compile(r'# ((\w*) *(\w*))*')

matches = pattern.findall(text)
print(matches)

def cosas():
    hola = (1,2,3,4,5)
    for i in hola:
        yield i
    


def fun():
    


fun()