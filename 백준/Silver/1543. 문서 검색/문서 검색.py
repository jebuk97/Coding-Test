st = input()
target = input()
cnt = 0
while (target in st) == True:
    cnt += 1
    start = st.index(target)
    st = list(st)
    st[start:start+len(target)] = '-'
    st = ''.join(st)
print(cnt)