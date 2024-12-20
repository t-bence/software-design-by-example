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

## Task 3 - Class methods and static methods

Static method: a method that belongs to the class logically, but does not have anything to do with it.

Class method: a method that gets the class (so not an instantiated object) as a first argument.

**Implement both types using dictionaries!**

Now this seems complex. How should I do it? Maybe add two fields called `classmethods` and `staticmethods` to my classes?

## Task 4 - Reporting type

Python `type` method reports the most specific type of an object, while `isinstance` determines whether an object inherits from a type either directly or indirectly. Add your own versions of both to dictionary-based objects and classes.

This seems more straightforward.

## Task 5 - Using recursion

Modify the `find` function to be recursive -- this is already the case in the code I started from, so I am skipping this part.

## Task 6 - Method caching

_Our implementation searches for the implementation of a method every time that method is called. An alternative is to add a cache to each object to save the methods that have been looked up before. For example, each object could have a special key called _cache whose value is a dictionary. The keys in that dictionary are the names of methods that have been called in the past, and the values are the functions that were found to implement those methods. Add this feature to our dictionary-based objects. How much more complex does it make the code? How much extra storage space does it need compared to repeated lookup?_
