Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp=0
temp=int(input('Please enter the current temperature: '))
if temp>90:
    print('Wear shorts')
elif temp>70:
    print('Short sleeves are fine')
elif temp>50:
    print('Wear a jacket')
elif temp>32:
    print('Wear a heavy coat')
else:
    print('Stay inside')
