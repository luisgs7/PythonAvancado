s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}

s1.add(7)
s1.update('1')
s3 = s1 & s2
s4 = s2 - s1
s5 = s1 ^ s2

print(s3)
print(s4)
print(s5)
