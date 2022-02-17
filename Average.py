Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> average=0
total=0
howManyEntered=0
howMany=int(input('How many test scores do you want to average? '))
while howManyEntered<howMany:
    testscore=int(input('Enter test score: '))
    total=total+testscore
    howManyEntered=howManyEntered+1
average=total/howMany
print ('The average for the test scores you entered is', average)
print (average)
