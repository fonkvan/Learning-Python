def burgerShop(kind, *args, **keywords):
    print(f"Do you have any {kind}s?")
    print(f"Sorry, we're out of {kind}s")
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

burgerShop("Juicy Lucy", 
           "Damn that sucks",
           "Yes, it does suck",
           "Well what else do you have?",
           "Actually nvm imma go somewhere else",
           Owner="Brent",
           Cook="Adam",
           Customer="Bobby")

#note that parameters with *name go into a tuple (all 4 quotes after juicy lucy)
#all parameters with **name go into a dictionary

#def foo(name, **kwds):
#   return 'name' in kwds
#this results in a collision with name parameter and the one in kwds, ex:
#foo(1, **{"name":2})
#TyperError: foo() got multiple values for argument 'name'

#solution is to use a positional only argument for name:
def foo(name, /, **kwds):
    return "name" in kwds

print(foo(1, **{"name":2})) #** is used here to 'unpack' the argument list. can also be done for tuples using *
#this is done for when the tuple or dictionary is already available such as this example. 
#the example all the way at the top, in tuple and dictionary weren't 'packed' so they didn't need unpacked, they could just be typed
print(foo(1, name=2)) #this way seems a little more ambiguous than the one directly above