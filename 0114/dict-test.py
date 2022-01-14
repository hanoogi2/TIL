# 딕셔너리 선언
my_home = { 
    'location':'seoul', 
    'area-code':'02',
}

# 딕셔너리 원소 접근
print(my_home['location'])
print(my_home['area-code'])
print(my_home.get('location1'))
print(my_home.get('area-code'))

# 딕셔너리 원소 변경
my_home['location'] = 'gumi'
print(my_home['location'])