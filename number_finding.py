number = ['2','3','4','6','10','20','100']
number = [int(a) for a in number]
print(number)
#target = print(input("Enter the target word or no: "))

range_of_list = len(number)

halved = range_of_list//2

while True:
    range_of_list = len(number)
    halved = range_of_list//2


    if target == number[:halved]:
        print("found it")
    for a in number[:halved]:
        if target != a:
            number = a.split(',')
        else:
            print("found it" , a)

'''


for a in number[:halved]:
    if  == target:
        print("Found" , a)

for a in number[halved:range_of_list]:
    if a == target:
        print("Found" , a)
    else:
        range_of_list2 = len(a)

'''
