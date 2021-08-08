list_1=[10,20,30,40,50]
list_2=[100,200,300,400,500]
i=0
while i<len(list_1):
    b=1
    while b<=len(list_2):
        print(list_1[i],list_2[-b])
        b=b+1
        i=i+1