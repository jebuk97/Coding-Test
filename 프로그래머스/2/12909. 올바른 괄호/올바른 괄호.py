from collections import deque
def solution(s):
    answer = True
    st = deque()
    for i in s:
        if i == '(':
            st.append('(')
        else:
            try:
                st.pop()
            except:
                return False
    if len(st) > 0:
        return False
    else:
        return True