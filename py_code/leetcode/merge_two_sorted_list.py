# coding: utf8

class ListNode(object):
    """
    """
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


def merge_two_lists(l1, l2):
    """
    merge two sorted lists
    """
    curr = dummy = ListNode(0)

    while l1 and l2:
        if l1.val > l2.val :
            curr.next = l2
            l2 = l2.next
        else:
            curr.next = l1
            l1 = l1.next
        curr = curr.next
    curr.next = l1 or l2

    return dummy

if __name__ == "__main__":

    l1 = ListNode(0)
    l1.next = ListNode(1)
    l2 = ListNode (2)
    l2.next = ListNode(3)
    print(merge_two_lists(l1, l2))

