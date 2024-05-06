def printpoint(point):
    """This string literal is a document string. It's optional, must be first, and describes what the function does (not here tho).\n
    It even gets added to the
    VSCode Tooltip! ('VSCode Tooltip' not on a separate line because there wasn't a new line char added)\n
    Wowzers"""
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"X={x}")
        case (0, y):
            print(f"Y={y}")
        case (x, y):
            print(f"X={x}, Y={y}") #basically ensuring the type here with a 'catch-all'


if __name__ == "__main__":
    printpoint((0,0))
    printpoint(6)
    printpoint("math")
    printpoint((5,4))
    printpoint((3,0))
    printpoint((0,9))
