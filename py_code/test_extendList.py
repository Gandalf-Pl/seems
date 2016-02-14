# coding: utf8


def extendList(val, list=[]):
    list.append(val)
    return list


def extendString(val, str=""):
    str += val
    return str


if __name__ == "__main__":
    list1 = extendList(10)
    list2 = extendList(123, [])
    list3 = extendList("a")

    # 在函数参数中定义的表达式(expressions)的默认值在函数
    # 定义的时候被定义，而不是在调用的时候
    print "list1 is {}".format(list1)
    print "list2 is {}".format(list2)
    print "list3 is {}".format(list3)

    str1 = extendString("a")
    str2 = extendString("b", "")
    str3 = extendString("c")

    print "str1 is {}".format(str1)
    print "str2 is {}".format(str2)
    print "str3 is {}".format(str3)

