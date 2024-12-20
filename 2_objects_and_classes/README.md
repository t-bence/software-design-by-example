# 2 - Objects and classes

This chapter explains objects and classes, and how they are built up. Plus it hints at why you have the `self` keyword in Python.

## Task 1 - Named arguments

Add handling of named arguments to the `call` function.

This is really simple, I just had to add `**kwargs` to the `call` function.

## Task 2 - Multiple inheritance

I created a `Colored` class as well. This has a method called `getcolor`, which will return the color. It also has a method `shape_density`, that has the same name as a function defined in the `Shape` class, but this one always returns `-1`. This is created so to illustrate method resolution. The `_parent` field was changed, now it is a tuple, that can store more parent classes. And the `find` method was changed, too: it looks for a method in the current class now, and then loops through the parent classes as well. It will find all methods with the expected name, and then return the lowest-leftmost one in the tree of superclasses. So, which method is used, depends currently on the order in which the superclasses are written, which is probably not good.

Also, imagine the following. There is a `Child` class that inherits from two classes:

`Child(Parent1(Grandparent), Parent2)`

 If now `Grandparent` and `Parent2` both define the same method, the one from `Grandparent` will be called, even though it is one level higher, again, probably not ideal.
