import random, string, json, csv, ast, re, sys
from datetime import datetime
from secrets import choice
import random
import string

def intlist():
    randlst = [[]]
    for i in range(10):
        lst = [random.randint(-100, 100) for i in range(random.randint(1, 10))]
        randlst.append(lst)
    return randlst

def nestedlist():
    return [genericlist() for i in range(random.randint(1, 5))]

def genericlist():
    n = random.randint(0, 2)
    if n == 0:
        lst = strlist()
    elif n == 1:
        lst = intlist()
    else:
        lst = tuplelist()
    return lst

def tuplelist():
    randlst = [[]]
    for i in range(10):
        randlst.append(randtuple())
    return randlst

def strlist():
    randlst = [[]]
    for i in range(10):
        randlst.append(randstr())
    return randlst

def boollist():
    randlst = [[]]
    for i in range(10):
        lst = [random.choice([True, False]) for i in range(random.randint(1, 10))]
        randlst.append(lst)
    return randlst

def datetimestr():
    return [str(datetime.today()) for i in range(10)]

def randset():
    randlst = [{}]
    for i in range(10):
        lst = set([random.randint(-100, 100) for i in range(random.randint(1, 10))])
        randlst.append(lst)
    return randlst

def randdatetime():
    return [datetime.today() for i in range(10)]

def intstr():
    randlst = ['']
    for i in range(10):
        randlst.append(''.join([choice(string.digits) for _ in range(random.randint(1, 10))]))
    return randlst

def nesteddict():
    randlst = [dict()]
    for i in range(10):
        ilst, slst = genericdict()[1], genericdict()[2]
        intdict = dict.fromkeys((0 + i for i in range(random.randint(1, 10))), ilst)
        intdict[0 + random.randrange(random.randint(1, 10))] = slst
        randlst.append(intdict)
    return randlst

def listdict():
    randlst = [dict()]
    for i in range(10):
        ilst, slst = randint(), randstr()
        intdict = dict.fromkeys((0 + i for i in range(random.randint(1, 10))), ilst)
        intdict[0 + random.randrange(random.randint(1, 10))] = slst
        randlst.append(intdict)
    return randlst

def intdict():
    randlst = [dict()]
    for i in range(10):
        intdict = dict.fromkeys((0 + i for i in range(random.randint(1, 10))), 0)
        intdict[0 + random.randrange(random.randint(1, 10))] = 1
        randlst.append(intdict)
    return randlst

def strdict():
    randlst = [dict()]
    for i in range(10):
        strdict = dict.fromkeys(("key" + str(i) for i in range(random.randint(1, 10))), 'value1')
        strdict["key" + str(random.randrange(random.randint(1, 10)))] = 'value2'
        randlst.append(strdict)
    return randlst

def randfloat():
    randlst = [random.uniform(-100,100) for i in range(10)]
    randlst.extend([-1.0, 0, 1.0])
    return randlst

def randint():
    randlst = [random.randint(-100,100) for i in range(10)]
    randlst.extend([-1, 0, 1])
    return randlst

def randstr():
    randlst = ['']
    for i in range(10):
        randlst.append(''.join([choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(random.randint(1, 10))]))
    return randlst

def any():
    n = random.randint(0, 10)
    if n == 0:
        lst = strlist()
    elif n == 1:
        lst = randint()
    elif n == 2:
        lst = randstr()
    elif n == 3:
        lst = strdict()
    elif n == 4:
        lst = randset()
    elif n == 5:
        lst = randtuple()
    else:
        lst = randdatetime()
    return lst

def randtuple():
    randlst = [tuple()]
    for i in range(10):
        lst = tuple([random.randint(-100, 100) for i in range(random.randint(1, 10))])
        randlst.append(lst)
    return randlst

def genericdict():
    n = random.randint(0, 2)
    if n == 0:
        dct = strdict()
    elif n == 1:
        dct = intdict()
    else:
        dct = listdict()
    return dct

def dictlist():
    randlst = [[]]
    for i in range(10):
        randlst.append(genericdict())
    return randlst