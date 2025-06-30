#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple

tuple1=('kevin', 12 , 1.1 , True)
print (tuple1)
tuple2=(1,2,3,4,5)
print( tuple2)
tuple3=tuple2 + (9,)
print (tuple3)
tuple4= (1,1,1)
print (tuple4 .count(1))
tuple5= (1,2,3,4,5,6,7,8,9,10)
print (tuple5[:5])


#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.

numbers_given=(1,2,3,3,2,1)
if numbers_given == numbers_given[::-1]:
    print('the tuple is a Palindrome')
else:
    print('Its not a Palindrome')


#Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.
weather=(1, 0, 0, 0, 1, 1, 0)
ranny=0
sunny=0
for i in weather:
    if i == 1:
     ranny= ranny+1
    else:
       sunny= sunny+1

print('the ranny days are',ranny,'And the sunny days are',sunny)
if ranny<sunny:
   print('its an sunny season/week')
else:
   print('its an ranny season/week')


