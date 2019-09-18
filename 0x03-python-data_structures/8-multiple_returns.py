#!/usr/bin/python3
def multiple_returns(sentence):
    leng = (len(sentence))
    if sentence is None:
        return(leng, None)

    fst_lettr = sentence[0]
    return(leng, fst_lettr)
