# program to interchange first and last element in list'
def swaplist(list):
    size = len(list)

    #swapping
    temp = list[0]
    list[0] = list[size-1]
    list[size-1] = temp
    return list


lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
print(swaplist(lst))
