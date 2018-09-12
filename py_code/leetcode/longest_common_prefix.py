# coding: utf8


def longest_common_prefix(strs):
    """
    get longest common prefix
    """
    if len(strs) == 0:
        return ""

    start = strs[0]
    common_prefix = ""

    i = 0
    while i <= len(start):
        i += 1
        common_prefix = start[:i]
        for item in strs[1:]:
            if not item.startswith(common_prefix):
                return start[:(i-1)]

    return common_prefix


if __name__ == "__main__":

    print(longest_common_prefix(["abc", "abd", "abefg"]))
