
import itertools

def word(w):
    unique_combo= set()
    blank = ''
    combo_dict = {}
    max_value_keys = []
    for i in range(1,len(w)):
        for x in itertools.combinations_with_replacement(w, i):
            combo_string = blank.join(x)
            print(combo_string)
            if combo_string in w and len(combo_string)<=(len(w)/2):
                if combo_string[0:i] == w[0:i]:
                    if combo_string[0:i] == w[i:i+len(combo_string[0:i])]:
                        for x in range(0,len(w),len(x)):
                            unique_combo.add(combo_string[0:i])
                            combo_dict[combo_string[0:i]] = w.count(combo_string[0:i])

                        max_value_keys = [key for key in combo_dict.keys() if combo_dict[key] == max(combo_dict.values())]


    for sol in unique_combo:
        for z in range(0,len(w), len(sol)):
            w[0:z]
        if len(w)/w.count(sol) == len(sol):
            print('cantidad de veces que se repite en la secuencia: ' + str(w.count(sol)))
            print('extracto de texto repetido: ' + sol)
        else:
            print('cantidad de divisiones de la torta: ' + str(1))
            print('no solutions')
    print(max_value_keys)



        #la excepcion de que sean solo letras iguales



#word("abababcdcdcd")
#word("abababab")
def a(word):
    combination = {}
    for i in range(1, (len(word)//2)+1):
        if word[:i] in (word[i:]):
            if len(word)/word.count(word[:i]) == len(word[:i]):
                combination[word[:i]] = word.count(word[:i])
            else:
                pass
    max_value_keys = [count for combo, count in combination.items() if combination[combo] == max(combination.values())]
    print(max_value_keys)
    print(combination)
        #for j in range(0, len(word), i):
            #ext = word[j:j+i]
            #print(j)
            #print(ext)
    """ larg = len(word)
    for i in range(1,len(word)):
        myset = set()
        print('iter 1: '+ str(i))
        for x in range(0,(len(word)//i)):
            print('iter 2: ' + str(x))
            myset.add(word[x:x+i])
            print('extracto: ' + word[x:x+i])
        print(myset) """


a('abcabcabcabc')