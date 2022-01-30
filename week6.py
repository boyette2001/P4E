largest = 0
smallest = 0
list = [ ]

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        intnum = int(num)
        list.append(intnum)
        smallest = intnum
    except:
        print('Invalid input')
        continue
    #print(num)
    #print(list)

#print(list)

for number in list:
    if number >= largest:
        largest = number
    if number <= smallest:
        smallest = number
        
print ('Maximum is ', largest)
print ('Minimum is ', smallest)