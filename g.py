""" import itertools 

def solution(s):
    if s is not None and len(s) < 200:
        for letter in s:
            print(len(s))
            if letter.find(s) < len(s):
                print(letter.find(s))
                pos = letter.find(s)
    else:
        print("wrong")
            
        
    
solution('sdgsd')
 """

 
import itertools

def word(w):
    print('solution start')
    newset = set()
    l = []
    letters = [letter for letter in w]
    blank = ''
    list_of_combos = []
    print('trabajanding')
    for i in range(1,len(w)):
        for x in itertools.combinations_with_replacement(w, i):
            l.append(x)
    print('trabajanding')
    for combo in l:
        combo_string = blank.join(combo)
        if combo_string in w and len(combo_string)<=(len(w)/2):
            list_of_combos.append(combo_string)
        newset = set(val for val in list_of_combos)
    print(newset)
    for x in newset:
        for i in range(1,len(w)):
            if x[0:i] == w[0:i]:
                #print(x[0:i])
                #print(x[i:])
                #print(w[i:])
                #print(len(w)/len(x))
                #print(w[0:i+len(x)])
                #x[0:i], w[0:i+len(x)]
                #print(w.count(x))
                abc = w.count('abc')
                thelen = len(w)
                div = abc % thelen
                print('abc count')
                print(abc)
                print('largo palabra')
                print(thelen)
                print('resto')
                print(div)


        #la excepcion de que sean solo letras iguales



word("abcabcabc")