def index_of(word, list):
    for i in range(len(list)):
        if list[i] == word:
            return i
    return -1
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of("Black", colors))
print(index_of("Blue", colors))

def index_of_by_index(word, list, index):
    for i in range(index, len(list)):
       if list[i] == word:
          return i
    return -1

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of_by_index("Black", colors, 1))
print(index_of_by_index("Black", colors, 4))
print(index_of_by_index("Green", colors, 2))

def index_of_empty(list):
    for i in range(len(list)):
       if list[i] == "":
          return i 
    return -1

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of_empty(colors))
colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(index_of_empty(colors))

def put(word, list):
  for i in range(len(list)):
    if list[i] == "":
      list[i] = word
      return i
  return -1

colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(put("Blue", colors))
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(put("Blue", colors))

def remove(word, list):
    count = 0  
    
    for index in range(len(list)):
        if list[index] == word:  
            list[index] = ""  
            count += 1 
    return count

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(remove("Black", colors))
print(remove("Blue", colors))
