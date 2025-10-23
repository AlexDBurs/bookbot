
def word_counter(file_contents):
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count

#Dado un string, arma un diccionario con formato letra:numero de repeticiones
def letter_counter(file_contents):
    word_list = file_contents.lower().split()
    letter_dict = {}
    for word in word_list:
        for letter in word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

#Función auxiliar para utilizar en dict_sorter(). Es la forma en la que se toman los valores para sortear
def letter_dict_list_sorter_key(dict):
     return dict['num']

#Dado un diccionario cn formato letra:numero de repeticiones, devuelve una lista de diccionarios ordenada por numero de repeticiones
def dict_sorter(letter_dict):
    letter_dict_list = []
    for key in letter_dict:
        if key.isalpha():
            letter_dict_list.append({'name':key, 'num':letter_dict[key]})

    letter_dict_list.sort(reverse = True, key = letter_dict_list_sorter_key)
    return letter_dict_list