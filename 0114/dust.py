dust = 70

# 150초과
if dust > 151:
    print('매우나쁨')
# 81 ~ 150
elif 80 < dust and dust <= 150: # dust > 80
    print('나쁨')
# 31 ~ 80
elif 30 < dust <= 80: # dust > 30
    print('보통')
# 30 이하
else:
    print('좋음')