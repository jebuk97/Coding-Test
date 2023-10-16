s = input()
s = s.lower()
al=set(s)
dic = dict()
for a in al:
    dic[a] = 0
maxi = 0
max_a = []
for i in range(0, len(s)):
    dic[s[i]] += 1

sorted_dic = sorted(dic, key = lambda x:-dic.get(x))
#sort(dic) -> 키 값들만 빠져서 정렬을 시도. get 함수는 값으로 키를 가져옴
if len(dic) == 1:
    print(sorted_dic[0].upper())
elif dic.get(sorted_dic[0]) == dic.get(sorted_dic[1]):
    print('?')
else:
    print(sorted_dic[0].upper())
