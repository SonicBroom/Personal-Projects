list = [1, 3, 6, 7, 10]

for i in range(len(list) - 1, 0, -1):
    if list[i] > 5:
        list.insert(i, 5)
        break

print (list)

myDictionary = {'Name': 'John', 'Age': 10, 'Pet': 'Dog'}

for key in myDictionary:
    print ('Key: ', key, '\tValue: ', myDictionary[key])

myString = "There once was a dog name Snoopy"

for aChar in myString:
    print ('String Character: ', aChar)

myList = [1, 3, 4, 7, 9, 2, 4, 6, 8 ,0]

for number in myList:
    print ('List element: ', number)
