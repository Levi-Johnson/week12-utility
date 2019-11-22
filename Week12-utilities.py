#https://github.com/Levi-Johnson/week12-utility.git
#Levi Johnson
#CSCI 102 - Section E
#Week 11 - Part A

#Print Output
def PrintOutput(s):
    print('OUTPUT', s)

#Load File
def LoadFile(filename):
    with open(filename) as f:
        content = []
        for line in f:
            content.append(line)
        return content

#Update String
def UpdateString(s1, s2, index):
    s1 = list(s1)
    s1[index] = s2
    s1 = ''.join(s1)
    return s1

#Find Word Count
def FindWordCount(array, string):
    occurences = 0
    for i in array:
        i = i.split()
        for j in i:
            if j == string:
                occurences += 1
    return occurences

# Score Finder
def ScoreFinder(L1, L2, string):
    index = -1
    for i in range(len(L1)):
        if L1[i].lower() == string.lower():
            index = i
    if index == -1:
        print('OUTPUT player not found')
    else:
        print('OUTPUT %s got a score of %d' % (string, L2[index]))
#Union
def Union(L1, L2):
    output = []
    for i in L1:
        output.append(i)
    for i in L2:
        output.append(i)
    return output

#NotIn
def NotIn(L1, L2):
    output = []
    for i in L1:
        if i not in L2:
            output.append(i)
    return output





