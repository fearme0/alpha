#sucht nach Befehlen in commands.txt
def scanC():
    f = open("commands.txt", "r")
    C = {}
    for line in f:
        k, v = line.strip().split(':')
        C[k.strip()] = v.strip()
    f.close()
    return C
