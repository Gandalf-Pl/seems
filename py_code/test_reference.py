# coding: utf8
"""
Q: How are arguments passed-by reference or by value?
A: The short answer is 'neither', actually it is called 'call by object' or
   'call by sharing'. The values of these references are to the functions,
   As result you can not change the value of the reference but you can modify
   the object if it is mutable. Remember numbers, strings and tuples are
   immutable, list and dict are mutable.Actually I this python is passed-by
   reference. In python, everything is object, arguments just names for
   objects.
"""


def test_dict(dict1):
    print id(dict1)
    print dict1.get("name", "")
    dict1.update({"b": "test2"})


def test_tuple(tuple1):
    print id(tuple1)
    print tuple1


if __name__ == "__main__":

    a = dict(name="test1", city=[1, 2])
    print id(a)
    print a
    test_dict(a)
    print a

    b = (1, 2, 3)
    print id(b)
    test_tuple(b)
