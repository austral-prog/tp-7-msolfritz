def enumerate_list(colors):
    lista = []
    for index, s in enumerate(colors):
        if s:
           lista.append(f"{len(lista)}. {s}")
    return lista
colors = ["Red", "Green", "", "White", "Black"]
print (enumerate_list(colors))

def enumerate_backwards(list):
    lista = []
    for index, s in enumerate(list):
       if s:
          lista.append(f"{len(lista)}. {s[::-1]}")
    return lista
colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_backwards(colors))
