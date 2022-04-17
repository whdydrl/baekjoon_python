words = input().upper()
set_words = list(set(words))

cnt_list = []
for x in set_words :
    cnt = words.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(set_words[max_index])