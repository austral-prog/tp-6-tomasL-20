def remove_elements(lista):
  
    nueva_lista = lista.copy()
 
    if len(nueva_lista) > 5:
        del nueva_lista[5]
   
    if len(nueva_lista) > 4:
        del nueva_lista[4]
    
    if len(nueva_lista) > 0:
        del nueva_lista[0]

    return nueva_lista

def add_elements(lista):
    
    nueva_lista = lista.copy()
    nueva_lista.insert(0, 'Pink')
    nueva_lista.append('Yellow')

    return nueva_lista

def is_empty(lista):

    return len(lista) == 0


def check_lists(lista1, lista2):

    if len(lista1) > 2 and len(lista2) > 2:
        return lista1[2] == lista2[2]
    else:
        return False

def list_of_lists(lista_de_listas):
    
    primera = lista_de_listas[0][:2]        
    segunda = lista_de_listas[1][1:4]       
    tercera = lista_de_listas[2][-2:]        

    
    return [primera, segunda, tercera]
    
