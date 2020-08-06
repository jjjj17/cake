def solution(word):
    combination = {}
    if len(word) < 200 and word != '' and word.isalpha() == True:
        for i in range(1, int(len(word)/2)+1):
            if word[:i] in (word[i:]):
                if len(word)/word.count(word[:i]) == len(word[:i]):
                    combination[word[:i]] = word.count(word[:i])
    max_value = [count for combo, count in combination.items() if combination[combo] == max(combination.values())]
    if max_value:
        return(max_value[0])
    elif len(word)<1 or word == "" or word.isalpha() == False:
        return(0)
    else:
        return(1)


print(a(''))