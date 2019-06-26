ones_dict ={'0':'Zero', '1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'}
tens_dict = {'10':'Ten', '11':'Eleven', '12':'Twelve', '13':'Thirteen', '14':'Fourteen', '15':'Fifteen', '16':'Sixteen', 
             '17':'Seventeen', '18':'Eighteen', '19':'Nineteen','2':'Twenty', '3':'Thirty', '4':'Forty', '5':'Fifty', 
             '6':'Sixty', '7':'Seventy', '8':'Eighty', '9':'Ninety'}

def count_the_str_length(x):
    
    #Calculate one thousand
    if len(str(x)) == 4:
        total_sum = len('OneThousand')
    
    #Calculate hundreds
    elif len(str(x)) == 3:
        
        #Calc the full hundreds
        if str(x)[1:] == '00':
            total_sum = len(ones_dict[str(x)[0]]) + 7
   
        #Calc the rest of the hundreds
        else:  
            #First digit
            r = len(ones_dict[str(x)[0]])
        
            #Second and third digits
            if str(x)[1] == '0':
                t = len(ones_dict[str(x)[2]])

            elif str(x)[1] == '1':
                t = len(tens_dict[str(x)[1:]])
            
            else:
                if str(x)[2] == '0':
                    t = len(tens_dict[str(x)[1]])
                else:
                    z = len(tens_dict[str(x)[1]])
                    o = len(ones_dict[str(x)[2]])
                    t = z + o
            
            #Add them all together
            total_sum = r + t + 10
      
    #Calculate the tens
    elif len(str(x)) == 2:
        if str(x)[0] != '1' and str(x)[1] != '0':
            g = len(tens_dict[str(x)[0]])
            w = len(ones_dict[str(x)[1]])
            total_sum = g + w
        elif str(x)[0] != '1' and str(x)[1] == '0':
            total_sum = len(tens_dict[str(x)[0]])
        else:
            total_sum = len(tens_dict[str(x)])
    
    #Calculate the ones
    else:
        total_sum = len(ones_dict[str(x)])
        
    return total_sum
  
num_length_list = []

for i in range(1,1001):
    h = count_the_str_length(i)
    num_length_list.append(h)
  
print(sum(num_length_list)
#21124
