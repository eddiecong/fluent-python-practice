# slicing part codes:
s = 'bicycle'
s1 = s[::3]
s2 = s[::-1]

s3 = s.__getitem__(slice(0, 7, 3))
print(s1 == s3)