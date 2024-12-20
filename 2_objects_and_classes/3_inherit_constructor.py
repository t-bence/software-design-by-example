import math

def shape_density(thing, weight):
    return weight / call(thing, "area")

# [shape]
def shape_new(name):
    return {
        "name": name,
        "_class": Shape
    }

Shape = {
    "density": shape_density,
    "_classname": "Shape",
    "_parent": tuple(),
    "_new": shape_new
}
# [/shape]

# here, I define a new dict called HasColor
def colored_new(color):
    return {
        "color": color,
        "_class": Colored
    }

def getcolor(thing):
    return thing["color"]

def shape_density_2(thing, weight):
    return -1

Colored = {
    "density": shape_density_2,
    "getcolor": getcolor,
    "_classname": "Colored",
    "_parent": tuple(),
    "_new": colored_new
}

def blue_new():
    return make(Colored, "blue") | {
        "_class": Blue
    }

Blue = {
    "_classname": "Blue",
    "_parent": (Colored, ),
    "_new": blue_new
}


# [make]
def make(cls, *args):
    return cls["_new"](*args)
# [/make]

def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

# [square]
def square_new(name, side):
    return make(Shape, name) | make(Blue) | {
        "side": side,
        "_class": Square
    }

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_classname": "Square",
    "_parent": (Shape, Blue),
    "_new": square_new
}
# [/square]

def circle_perimeter(thing):
    return 2 * math.pi * thing["radius"]

def circle_area(thing):
    return math.pi * thing["radius"] ** 2

def circle_new(name, radius):
    return make(Shape, name) | make(Blue) | {
        "radius": radius,
        "_class": Circle
    }

Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "_classname": "Circle",
    "_parent": (Shape, Blue),
    "_new": circle_new
}

def find(cls, method_name):
    if method_name in cls:
        return cls[method_name]
    elif not cls["_parent"]:
        return None
    else:
        methods = [find(p, method_name) for p in cls["_parent"]]
        for m in methods:
            if m is not None:
                return m # return the first one found
        return None

def call(thing, method_name, *args, **kwargs):
    method = find(thing["_class"], method_name)
    return method(thing, *args, **kwargs)

def type(thing):
    return thing["_class"]["_classname"]

def isinstance(thing, cls):
    def parentisinstance(thing, cls):
        if thing["_classname"] == cls["_classname"]:
            return True
        return any(parentisinstance(p, cls) for p in thing["_parent"])

    if cls["_classname"] == thing["_class"]["_classname"]:
        return True
    return parentisinstance(thing["_class"], cls)
    

# [call]
examples = [make(Square, "sq", 3), make(Circle, "ci", 2)]
for ex in examples:
    n = ex["name"]
    area = call(ex, "area")
    d = call(ex, "density", weight=5)
    color = call(ex, "getcolor")
    print(f"{n}: density: {d:.2f}, color: {color}")
    print(f"Type: {type(ex)}")
    print(f"Is instance of Square: {isinstance(ex, Square)}")
    print(f"Is instance of Blue: {isinstance(ex, Blue)}")
    print(f"Is instance of Colored: {isinstance(ex, Colored)}")
    print()
# [/call]
