#!/usr/bin/python3
def multiple_returns(sentence):
    leng = (len(sentence))

    if leng is None:
        return(leng, None)
    else:
        fst_lettr = sentence[0]
        return(leng, fst_lettr)
