# coding: utf8


class Gobang(object):

    def __init__(self):
        self._width = 10
        self._length = 10
        self.black_steps = list()
        self.white_steps = list()
        self.chessboard = self.start_chessbord()

    def white_black_chooser(self, black_white):
        if black_white == "white":
            return self.white_steps
        else:
            return self.black_steps

    def start_chessbord(self):
        chessboard = list()
        for x in xrange(self._width):
            for y in xrange(self._length):
                chessboard.append((x, y))
        return chessboard

    def judge_win_or_not(self, position, black_white):
        """
        """
        row = position[0]
        col = position[1]

        if position not in self.chessboard:
            raise

        if black_white == "white":
            self.white_steps.append(position)
        else:
            self.black_steps.append(position)
        step_list = self.white_black_chooser(black_white)
        # 横向判定
        count = 0
        tmp = col - 1
        while tmp >= col - 4:
            if (row, tmp) not in step_list:
                break
            count += 1
        tmp = col + 1
        while tmp <= col + 4:
            if (row, tmp) not in step_list:
                break
            count += 1
        if count >= 5:
            return True
        # 纵向比较
        count = 0
        tmp = row - 1
        while tmp >= col - 4:
            if (tmp, col) not in step_list:
                break
            count += 1

        tmp = col + 1
        while tmp <= col + 4:
            if (tmp, col) not in step_list:
                break
            count += 1
        if count >= 5:
            return True

        # \向比较
        count = 0
        tmp_col = col
        tmp_row = row
        for i in xrange(1, 5):
            if (tmp_row+1, tmp_col-1) not in step_list:
                break
            count += 1
        count = 0
        tmp_col = col
        tmp_row = row
        for i in xrange(1, 5):
            if (tmp_row-1, tmp_col+1) not in step_list:
                break
            count += 1
        if count >= 5:
            return True

        # /向比较
        count = 0
        tmp_col = col
        tmp_row = row
        for i in xrange(1, 5):
            if (tmp_row+1, tmp_col+1) not in step_list:
                break
            count += 1
        count = 0
        tmp_col = col
        tmp_row = row
        for i in xrange(1, 5):
            if (tmp_row-1, tmp_col-1) not in step_list:
                break
            count += 1
        if count >= 5:
            return True

        return False

