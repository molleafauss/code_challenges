#!/bin/python3

import os

#
# Complete the 'betterCompression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# (done for Riot Games challenge)
#
import string


def get_next_sequence(s, pos):
    ch = s[pos]
    if ch not in string.ascii_lowercase:
        raise Exception("Error at position {}: expected lowercase letter, found {}".format(pos, ch))

    val = 0
    start = pos + 1
    end = start
    while end < len(s) and s[end] in string.digits:
        end += 1

    if start == end:
        raise Exception("Missing count at position {}: {}".format(start, s[pos:]))

    count = int(s[start:end])
    if count > 1000:
        raise Exception("Error at position {}: count exceed limit, found {}".format(start, count))

    return ch, count, end


def parse(s):
    letters = {}
    pos = 0
    while pos < len(s):
        # get char, count and next sequence position from string
        (ch, count, pos) = get_next_sequence(s, pos)
        if ch in letters:
            letters[ch] += count
        else:
            letters[ch] = count

    return letters


def betterCompression(s):
    if len(s) > 100000:
        raise Exception("String input too long: found {}, expected <= 100000".format(len(s)))

    # parse the string
    letters = parse(s)

    # format the result
    text = ""
    for ch in sorted(letters):
        text += "{}{}".format(ch, letters[ch])

    return text


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = betterCompression(s)

    fptr.write(result + '\n')

    fptr.close()
