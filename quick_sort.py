def quick_sort(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    less,equal,high=[],[],[]
    for i in L:
        if i<pivot:
            less.append(i)
        elif i>pivot:
            high.append(i)
        else:
            equal.append(i)
    sorted_list=quick_sort(less)+equal+quick_sort(high)
    return sorted_list
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
