#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return(None, None)
    leng = (len(sentence))
    fst_lettr = sentence[0]
    return(leng, fst_lettr)
