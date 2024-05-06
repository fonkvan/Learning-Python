from enum import Enum
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

color = Color(input("Enter choice of red blue or green"))

match color:
    case Color.RED: #for named constants must use dotted name to prevent being interpreted as capture variable
        print("Seeing red")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("Feeling blue")