ones_dict ={'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', 
            '7':'seven', '8':'eight', '9':'nine'}

tens_dict = {'1':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', 
             '17':'seventeen', '18':'eighteen', '19':'nineteen', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', 
             '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}

def stringify_ones(x):
    return ones_dict[x]

def stringify_tens(x):
    if x == '10':
        return 'ten'
    elif x[0] == '1':
        return tens_dict[x]
    elif x[1] == '0':
        return tens_dict[x[0]]
    else:
        return tens_dict[x[0]] + ones_dict[x[1]]

def stringify_hundreds(x):
    if x[1:] == '00':
        return ones_dict[x[0]] + 'hundred'
    elif x[1] == '0' and x[2] != 0:
        return ones_dict[x[0]] + 'hundredAnd' + ones_dict[x[2]]
    else:
        return ones_dict[x[0]] + 'hundredAnd' + stringify_tens(x[1:])

def stringify_number(x):
    
    num_string = str(x)
    
    if len(num_string) == 3:
        stringed_num = stringify_hundreds(num_string)
    elif len(num_string) == 2:
        stringed_num = stringify_tens(num_string)
    else:
        stringed_num = stringify_ones(num_string)
    return stringed_num

def calc_num_str_len(x):    
    if len(str(x)) == 4:
        num_length = len('oneThousand')
    else:
        num_length = len(stringify_number(x))
    return num_length
  
base_num = 0

for x in range(1,1001):
    base_num += calc_num_str_len(x)

print(base_num)
