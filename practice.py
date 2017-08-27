
print 'test'
num = range(1,9)
def fei():
    temp = [1]
    lastTemp = []
    lastTemp2 = [0,1]
    for i in num:
        if i == 1:
            pass
        elif i == 2:
            temp = [1,1]
            lastTemp = [1,1]
            temp.append(lastTemp2[1])
        else:
            temp = [1,1]
            for j in range(len(lastTemp)-1):
                temp.insert(j + 1, lastTemp[j] + lastTemp[j+1])
            lastTemp = temp[:]
            result = reduce(lambda x,y: x+y, lastTemp2)
            lastTemp2.pop(0)
            lastTemp2.append(result)
            temp.append(result)
        pString = ''
        for k in range(len(temp)):
            pString = pString + str(temp[k]) + ' '
        print pString
        print "\n"    

def love():
    src = [[4,3,17,3],
    [1,9,11,9],
    [0,12,7,12],
    [0,13,5,13],
    [0,14,3,14],
    [0,15,1,15],
    [1,7,4,3,1,3,4,7],
    [2,6,5,5,5,6],
    [3,6,5,3,5,6],
    [5,6,4,1,4,6],
    [8,6,1,1,1,6],
    [10,11],
    [11,9],
    [12,7],
    [13,5],
    [15,1]]
    for i in range(len(src)):
        temp = src[i]
        pString = ''
        for j in range(len(temp)):
            if j%2 == 0:
                for k in range(temp[j]):
                    pString = pString + " "
            else:
                for k in range(temp[j]):
                    pString = pString + "*"
        print pString
        print '\n'


love()
