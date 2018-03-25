#sucht nach Modulen in modules.txt
def scanM():
    f = open("modules.txt", "r")
    l = []
    m1 = []
    m2 = []
    liste = f.read().splitlines()
    for line in liste:
        m1 = m1 +  [line.split(",")[0]]
        m2 = m2 + [line.split(",")[1]]
    l = l + [m1,m2]
    f.close()
    return l
