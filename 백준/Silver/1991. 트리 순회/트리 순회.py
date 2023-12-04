n = int(input())
tree = {}
for i in range(n):
    a, b, c = input().split()
    tree[a] = [b, c]
# print(tree)
ans = ''
def pre(stt):
    global ans
    ans += stt
    if tree[stt][0] != '.':
        pre(tree[stt][0])
    if tree[stt][1] != '.':
        pre(tree[stt][1])
def mid(stt):
    global ans
    if tree[stt][0] != '.':
        mid(tree[stt][0])
    ans += stt
    if tree[stt][1] != '.':
        mid(tree[stt][1])

def post(stt):
    global ans
    if tree[stt][0] != '.':
        post(tree[stt][0])
    if tree[stt][1] != '.':
        post(tree[stt][1])
    ans += stt


pre('A')
print(ans)
ans = ''
mid('A')
print(ans)
ans = ''
post('A')
print(ans)