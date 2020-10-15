#importo random para usarlo mas adelante
import random

def get_def_and_pop(word_list,word_dict):
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = word_dict.get(word)
    return word, definition


#una funcion para separar la palabra y la definicion
#aca la magia para pasar el split a dos variables
#indicando separado por , y que sea tomada solo la primer una vez.
def get_word_and_definition(rawstring):
    word, definition = rawstring.split(',',1)
    return word,  definition


fh = open("Vocabulary_list.csv","r")
wd_list = fh.readlines()
print(wd_list)

#para eliminar los duplicados se podria
#iterar por la lista, pero pasando
#la lista a un set, con una linea de codigo se 
#eliminan todos los duplicados.

#primero borramos la primer linea de la lista, y
#luego instanaciamos un set pasandole la lista en el constructor.
#ese set lo pasamos a un nuevo archivo de texto.

wd_list.pop(0) #borro la primer linea.
wd_set = set(wd_list) #el set se instancia con la lista, duplicados eliminados.
fh = open("Vocabulary_set.csv","w") #creo manejador de archivos con
#el nombre del archvo y en modo escritura.
#ahora a escribir la lineas de en el archvo.
fh.writelines(wd_set)

word_dict = dict() #instancia un diccionario.
for rawstring in wd_set:
    word,definition = get_word_and_definition(rawstring)
    word_dict[word]= definition


wd_list = list(word_dict)

for rawstring in wd_set:
    word,definition = get_word_and_definition(rawstring)
    word_dict[word] = definition

while True:
    wd_list = list(word_dict)
    choice_list = []
    
    for x in range(4):
        word,definition =  get_def_and_pop(wd_list, word_dict)
        choice_list.append(definition)
    random.shuffle(choice_list)
    print(word)
    print("---------------------")
   
    for idx, choice in enumerate(choice_list):
        print(idx+1,choice)
    choice = int(input('Enter 1, 2, 3 or 4, 0 to exit'))
    if choice_list[choice - 1] == definition:
        print("Correct! \n")
    elif choice == 0:
        exit(0)
    else:
        print("Incorrect")