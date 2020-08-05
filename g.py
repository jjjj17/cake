
import itertools

def word(w):
    print('solution start')
    unique_combo= set()
    l = []
    letters = [letter for letter in w]
    blank = ''
    list_of_combos = []
    print('trabajanding')
    for i in range(1,len(w)):
        for x in itertools.combinations_with_replacement(w, i):
            combo_string = blank.join(x)
            if combo_string in w and len(combo_string)<=(len(w)/2): #bugueado porque hay de len mayor
                if combo_string[0:i] == w[0:i]: #ojo que estoy usando el mismo numero en los dos loops, genera combos de tamaño i y recorre de tamaño i igual
                    if combo_string[0:i] == w[i:i+len(combo_string[0:i])]:
                        unique_combo.add(combo_string[0:i])
    for sol in unique_combo:
        if len(w)/w.count(sol) == len(sol):
            print(w.count(sol))
            print(sol)
        else:
            print(1)
            print('no solutions')
                        #list_of_combos.append(combo_string)
    #unique_combos = set(list_of_combos)
    #print(unique_combos)

"""     print('trabajanding')
    print(len(l))
    for combo in l:
        combo_string = blank.join(combo)
        if combo_string in w and len(combo_string)<=(len(w)/2):
            list_of_combos.append(combo_string)
        newset = set(val for val in list_of_combos)
    print(newset)
    for x in newset:
        for i in range(1,len(w)):
            if x[0:i] == w[0:i]:
                if x[0:i] == w[i:i+len(x)]:
                    print('yes!')
                    print(w.count(x[0:i]))
        if len(w)/w.count(x) == len(x):
            print(w.count(x)) """



        #la excepcion de que sean solo letras iguales



word("abababababab")