#Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    cc_last_four = cc[-4:]
    cc_but_four = cc[:-4]
    length_string = len(cc_but_four)
    cc_hashed = length_string * "#"
    cc = cc_hashed + cc_last_four
    return cc

testcc= 'azhdkhf'
testcc2 = 'jefqd68fq7(564ef4qsd'
maskify(testcc2)

#WORKS

#BEST PRACTICE
# return masked string
#def maskify(cc):
    #return "#"*(len(cc)-4) + cc[-4:]