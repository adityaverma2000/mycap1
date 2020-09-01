n=int(input("Enter number of elements in list:"))
list1= list(int(num)for num in input("Enter the list numbers:").strip().split())[:n]
for i in list1:
    if i>0:
        print(i,end=',')
