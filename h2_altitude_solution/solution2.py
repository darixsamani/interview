
def solution(tab):
    set_tab = set(tab)
    result = 0
    for i in set_tab:
        if tab.count(i)%2!=0:
            result = i
            break
    return result
