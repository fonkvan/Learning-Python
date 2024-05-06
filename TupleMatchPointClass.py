class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0): #can get rid fo this x=x stuff by using __match_args__
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

if __name__ == "__main__":
    a=Point(0,0)
    b=Point()
    c=Point(5,3)
    i = 7
    d=Point(i, i)
    where_is(a)
    where_is(b)
    where_is("c")
    where_is(c)
    where_is(d)