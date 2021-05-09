s = '8' * 70
while s.find('2222') != -1 or s.find('8888') != -1:
    if s.find('2222') != -1:
        s = s.replace('2222', '88', 1)
    else:
        s = s.replace('8888', '22', 1)
print(s)