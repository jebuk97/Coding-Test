def solution(numbers, target):
    answer = 0
    st = [(0, numbers[0]), (0, -numbers[0])]
    while len(st) > 0:
        cur_index, summ = st.pop()
        if cur_index == len(numbers)-1:
            if summ == target:
                answer+=1
            continue
        st.append((cur_index+1, summ+numbers[cur_index+1]))
        st.append((cur_index+1, summ-numbers[cur_index+1]))
    
    return answer