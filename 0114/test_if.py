dust = 50

# if
if dust > 50:
    print('50초과')

# if~else
if dust > 50:
    print('50초과')
else:
    print('50이하')

# if ~ elif ~ else
if dust > 150:
    print('매우나쁨')
elif dust > 80:  # dust <= 150 and dust > 80
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')