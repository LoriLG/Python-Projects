def mySort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
             if list[i]>list[i+1]:
                 list[i],list[i+1] = list[i+1],list[i]
    
               
list1 =[67,45,2,13,1,998]
list2 = [89,23,33,45,10,12,45,45,45]


mySort(list1)
mySort(list2)

print(list1)
print ('\n')
print(list2)

        
        
