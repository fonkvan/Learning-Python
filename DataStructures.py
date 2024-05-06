from collections import deque

#the default list can act as a stack very easily (FILO)
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

#list is not efficient for queue (FIFO), so from collections import deque
#designed to have fast appends and pops from both ends
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue)

#list comprehesions
#assume we want to make a list of squares
squares=[]
#for x in range(10):
#    squares.append(x**2)
#print(squares)
#problem with this is that x still exists afterwards. a better way would be like this:
#squares = list(map(lambda x : x**2, range(10)))
#or better yet:
squares = [x**2 for x in range(10)] #concise, easily readable

#combs = []
#for x in [1,2,3]:
#    for y in [3,1,4]:
#        if x != y:
#            combs.append((x, y))
#the above is equivalent to this:
points = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y] #i actually love this format
print(points)

#can easily flatten a list as well
vec = [[1,2,3],[4,5,6],[7,8,9]]
print(vec)
flattened = [num for elem in vec for num in elem]
print(flattened)

#can also do something complex like this:

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

#however it is better to use built in functions when possible. zip works well here
betterTransposed = list(zip(*matrix))
print(betterTransposed) #note that zip makes tuples so it is a bit different than above

#note: You can use del to delete specific elements in a list or even slices of a list, as well as variables all together
#tuples are immutable, but can contain mutable objects such as lists
tup = ([1,2,3],[4,5,6])
#and you can nest them
newTup = (tup, [7,8,9])
print(newTup)
#this is valid cause the list is mutable
newTup[1][0] = 8
print(newTup)
#this isn't because tuples are immutable
#newTup[0] = (0,0,0)
emptyTuple = ()
singleton = ("hello",) #need the comma to make this a tuple
altMethod = "hello", #tuples don't need the parentheses, only when combining tuples like newTup above
print(singleton)

#the way we make tuples is called tuple packing
t = 12345, 54321, 'hello'
print(t)
#below is called sequence unpacking
x, y, z = t #basically easier to type that x = t[0], y=t[1], z=t[2]
print(x)
print(y)
print(z)

#sets - an unordered collection with no duplicate items. supports mathematical
#operations like union, intersection, difference, and symmetric difference
basket = {'banana', 'apple', 'orange', 'grape', 'apple', 'pineapple', 'grape'}
print(basket) #note that the duplicates are removed
#an empty set must be created using set(). {} creates an empty dictionary
#fast membership testing in sets:
print('orange' in basket)
print('dragonfruit' in basket)
#can also create sets using set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

#dictionary: 'associative memory', basically a key-value pair. keys must be unique within a single dictionary
#if you store a value with a key, and that key already exists, the old value will be overwritten with the new key.
#it is an error to extract a value using a non-existent key (so I'm assuming you must check if the key exists first)
#list(d) on a dictionary creates a list of the keys in the dictionary, this is unsorted. can create sorted list of 
#keys using sorted(d)
dictA = {'jack':427, 'jill':529}
dictA['guido'] = 948
print(dictA)
print(dictA['jack'])
print('donovan' in dictA)
print('jill' in dictA)
print(sorted(dictA))
#can build dictionaries from sequences of key value pairs using dict constructor
dictB = dict([('sape', 4139), ('guido', 4127), ('jack', 1234)])
print(dictB)
#can also use dictionary comprehensions
squaresDictionary = {x : x**2 for x in range(11)}
print(squaresDictionary)
#for simple strings, keys can be treated as if using keyword arguments
dictC = dict(jack=123,jill=456,bob=789)
print(dictC)
print(dictC['jack'])

#can get both key and value from dictionary at same time using items()
for x, y in squaresDictionary.items():
    print(x, y)

#if you want to mutate a dictionary while looping over it, you should use keys() func, cause it creates a copy
#at least that's what Raymond Hettinger says in his video but ended up having to do the below instead of using keys
#for k in dictC.copy():
#    if k.startswith('j'):
#        del dictC[k]
#print(dictC)

#could also have just created a new dictionary using dictionary comprehension
dictC = {k : dictC[k] for k in dictC if not k.startswith('j')}

#when looping a sequence (list, tuple, range), can get position and value and same time using enumerate()
for x,y in enumerate(t):
    print(x,y)

#can loop over two sequences at once using zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}?  It is {a}.')

#can loop a sequence in reverse
for i in reversed(range(1, 10, 1)):
    print(i)

#or sorted ordered
for f in sorted(basket):
    print(f)

#using set() on a sequence eliminates duplicates. can use sorted in comination with it to loop over unique elements in sorted order
#basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
#for f in sorted(set(basket)):
#    print(f)

#usually simpler/safer to create a new list rather than changing old list
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = [num for num in raw_data if not math.isnan(num)]
print(filtered_data)
#this is the way that the python tutorial did it, above is the way I rewrote it:
#filtered_data = []
#for value in raw_data:
#    if not math.isnan(value):
#        filtered_data.append(value)

#can compare sequences. Comparisons use lexicographical ordering: compare first two items, equal go to next two, until a comparison
#is determined. examples:
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
#comparing objects of different type is legal as long as the objects have appropriate comparison methods

#call function until a sentinel value
#blocks = []
#while True:
#   block = f.read(32)
#   if block == '':
#       break
#   blocks.append(block)

#better way to call function until sentinel value
#also with is the 'new' way to open files as opposed to try-finally clauses
from functools import partial
with open('TestTextFile.txt', encoding = 'utf-8') as f:
    blocks = []
    for block in iter(partial(f.read, 32), ""):
        blocks.append(block)
    print(blocks)
    f.close()
#old way, skipping some stuff from above
#f=open(TestTextFile.txt)
#try:
#   data = f.read()
#finally:
#   f.close

#grouping things into a dictionary
names = ['raymond', 'rachel', 'jim', 'bob', 'john', 'roger', 'melissa', 'judith']

#slow
d1 = {}
for name in names:
    key = name[0]
    if key not in d1: #have to check if it's not in there before adding it because otherwise get a KeyError
        d1[key] = []
    d1[key].append(name)
print(d1)

#fast
from collections import defaultdict
d2 = defaultdict(list) #defaultdict calls default_factory instead of raising KeyError when key is not in dict.
#default_factory sets the value type as whatever is passed in to defaultdict()
for name in names:
    key = name[0]
    d2[key].append(name)
print(dict(d2)) #technically still a dict but some different behaviors/printing so convert it to dict

#ex2 of defaultdict
d3 = defaultdict(int)
for name in names:
    key = name[0]
    d3[key] += 1
print(dict(d3)) #now we have a dictionary that counts how many names start with each letter

#don't do this
s=names[0]
for name in names[1:]:
    s += ", " + name
#print(s)

#do this instead
print(', '.join(names))

from functools import cache
#first time we do say factorial(10), it will make 11 recursive calls
#but then say after that we do factorial(5), no recursive calls are made, because the values are cached
#factorial(12) would give 2 more recursive calls, thanks to the previously cached values
#also cache is thread safe holy 
@cache 
def factorial(n):
    return n * factorial(n-1) if n else 1 #this works cause 0 is false in python so if n == 0 it will hit the else and return 1

#can get rid of temporary contexts
from decimal import *
old_context = getcontext().copy()
getcontext().prec = 50
print(Decimal(355) / Decimal(113))
setcontext(old_context)

#we don't wanna do that. we do the below instead
with localcontext(Context(prec=50)):
    print(Decimal(355)/Decimal(113))

#locks, used to need to do a try-finally and in the finally release the lock, but instead we just do
#i like this cause it's similar ideology to RAII
#with lock:
#   ...whatever we do inside lock