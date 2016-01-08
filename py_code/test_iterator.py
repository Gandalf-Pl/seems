# coding: utf8

class yrange(object):
    def __init__(self,start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def next(self):
        if self.start < self.end:
            i = self.start
            self.start += self.step
            return i
        else:
            raise StopIteration()

if __name__ == "__main__":
    print [item for item in yrange(1, 10, 2)]
