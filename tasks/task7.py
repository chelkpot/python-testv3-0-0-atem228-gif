s = input().strip()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
a = (a + 7) % 10
b = (b + 7) % 10
c = (c + 7) % 10
d = (d + 7) % 10
a, c = c, a
b, d = d, b
result = str(a) + str(b) + str(c) + str(d)
print(result)