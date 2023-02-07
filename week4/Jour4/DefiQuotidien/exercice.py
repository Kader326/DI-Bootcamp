Matrix = [
    ["7","i","3"],
    ["T","s","i"],
    ["h","%","x"],
    ["i"," ", "#"],
    ["s","M"," "],
    ["$","a"," "],
    ["#","t","%"],
    ["^","r","!"]
]

def read(liste,index,*args):
    return liste[index]
code=[]
top = 0
while top < (len(Matrix[0])):
    cpt=0
    for line in Matrix :
        char = read(line,top)
        if char.isalpha() and char != " ":
            code.append(char)
            cpt=0
        elif cpt==0:
            cpt += 1
        elif cpt==1:
            code.append(" ")
            cpt += 1

    top +=1
print("".join(code))