def insertion_sort(mylist):
    print(mylist)
    i=1
    while i < len(mylist):
        j = i 
        while j > 0 and mylist[j-1] > mylist[j]:
            swapval = mylist[j-1]
            mylist[j-1] = mylist[j]
            mylist[j] = swapval
            j=j-1
        i = i + 1
    return mylist

insertion = insertion_sort([64,74,1,1,23,1,45,1,67])
print(insertion)
