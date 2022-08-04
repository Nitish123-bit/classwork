def Last_ind(L,e):
    try:
        L.index(e)
    except:
        return 'None'
    for x in range(len(L)):
        if(L[x]==e):
            ind = x
    return ind
print( Last_ind([1, 5, 3, 5, 4], 8))