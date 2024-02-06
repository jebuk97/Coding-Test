import sys
n = int(sys.stdin.readline().rstrip())
'''
2
+1
3
+2
5
+4
9
+8
17
+16
33

n*

'''
st = 2
inter = 1
for i in range(0, n):
    st += inter
    inter *= 2
print(st**2)