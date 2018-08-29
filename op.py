def isdir(i):
    if(i=='N' or i=='S' or i=='E' or i=='W'):
        return 1
    else:
        return 0
intx = inty = finx = finy = 0

inp = input('').split(' ')
intx = int(inp[0])
inty = int(inp[1])

directions = str(input(r''))
for i in range(0,len(directions)):
    if(isdir(directions[i].upper())):
        tempspc = i + 1
        tempi = i
        for tempi in range(tempspc, len(directions)):
            if(directions[tempi]==','):
                tempi -= 1
                break
        val = directions[tempspc:tempi+1]
        val = int(val)
        if(directions[i]=='N'):
            finy += val
        if(directions[i]=='S'):
            finy -= val
        if(directions[i]=='E'):
            finx += val
        if(directions[i]=='W'):
            finx -= val
pytho = ((finx-intx)**2 + (finy-inty)**2)**(0.5)
print(finx,finy)
print(pytho)
