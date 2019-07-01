temp_file = open('FILEPATH')
names_list = temp_file.read().replace('"','').split(',')
names_list.sort()

alpha_values = {'A':1,'B':2, 'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
               'P':16,'Q':17,'R':18, 'S':19,'T':20,'U':21,'V':22,'W':23, 'X':24, 'Y':25, 'Z':26}

def letter_val(name):
    return sum([alpha_values[x] for x in name]) * (names_list.index(name) + 1)
    
names_score_list =[]

for item in names_list:
    value = letter_val(item)
    names_score_list.append(value)
    
print(sum(names_score_list))
#871198282
