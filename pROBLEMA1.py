with open("input.txt",'r') as i:
    list1=list(eval(i.readline()))
print(list1)
list2=sorted(list1)
print(list2)
listrev=sorted(list1)
listrev.sort(reverse=True)
print(listrev)
print('numărul de elemente din listă = ',len(list1))
print('elementul MAX = ',max(list1))
print('elementul MIN = ',min(list1))
list3=list1
list3.append(111)
print(list3)
list4=list1
list4.insert(1,222)
list4=list4[0:len(list4)-1]
print(list4)