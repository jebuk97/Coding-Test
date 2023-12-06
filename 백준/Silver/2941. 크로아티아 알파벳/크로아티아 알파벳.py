ch = input()
ch_al = set(("c=", 'c-', "dz=", "d-", "lj", "nj", "s=", "z="))
ans = len(ch)
for i in range(len(ch)-1):
    if (ch[i:i+2] in ch_al) == True:
        ch = list(ch)
        ch[i:i+2] = '--'
        ch = ''.join(ch)
        ans -= 1
        continue
    if ch[i] == "d" and i <= len(ch)-2:
        if (ch[i:i + 3] in ch_al) == True:
            ch = list(ch)
            ch[i:i+3] = '---'
            ch = ''.join(ch)
            ans -= 2
print(ans)