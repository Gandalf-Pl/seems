# coding: utf8


class Test(object):

    @staticmethod
    def test():
        print "this is static method in Test Class"


if __name__ == "__main__":

    print "start test"
    test = Test()
    test.test()
    print "after test"
