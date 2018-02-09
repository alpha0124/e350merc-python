#!/usr/bin/python3
numOfItems = 6;
if numOfItems < 3:
    print ("aaa")
elif 3 <= numOfItems <= 5: #between 3 & 5
    print ("bbb")
else:
    print ("ccc")
#-----------------------------------
colors = ["Red", "Blue", "Green", "Orange", "Yellow"]
sentence = '''The quick brown fox jumped over the lazy dog'''
#2 --> first index is 0
#-2 --> first reverse index is -1

#SPLICING
print (sentence[4]) #q
print (sentence[-1] + ',' + sentence[-5]) #qy
print (colors[1:4]) #['Blue', 'Green', 'Orange']
print(sentence[4:9]) #quick
print (sentence[:])
print (sentence[::])
print (sentence[::2])
print (sentence[::-2])
print (sentence[4:9:2])
print (sentence[4:-1:2]) #qikbonfxjme vrtelz o
colors[2:] = ["Black"] * 4 #['Red', 'Blue', 'Black', 'Black', 'Black', 'Black']
print (colors)

#SPLITTING
print (sentence.split("he")) #['T', ' quick brown fox jumped over t', ' lazy dog']

#JOINING
print ("-".join(colors)) #Red-Blue-Black-Black-Black-Black
print("-".join(colors).split('-')) #['Red', 'Blue', 'Black', 'Black', 'Black', 'Black']

#for loop
for eachColor in colors:
    print ('''Is ''' + eachColor + ''' your favorite color?''')

#while loop
counter = 10
i = 0
while i <= counter:
    print (str(i))
    i += 1

while counter >= 0:
    print (counter)
    counter -= 1

names = ["John", "Sean", "Alex", "David"]
while names:
    print ("Hey " + names.pop())
print (names) # list is emptied out

names.append("a") #takes only 1 item
print (names)

names = ["John", "Sean", "Alex", "David"]
print (names)
print (names.remove('Alex'))


#FUNCTIONS
print ("There are {0} TVs and {1} cars in the house".format(5,4))
