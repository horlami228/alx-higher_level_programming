#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tupl = (0, None)
        return tuple

    tupl = (len(sentence), sentence[0])
    return tupl
