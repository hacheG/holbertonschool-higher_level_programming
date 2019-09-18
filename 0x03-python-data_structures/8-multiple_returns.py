#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return
    leng = (len(sentence))
    fst_lettr = sentence[0]
    return(leng, fst_lettr)
