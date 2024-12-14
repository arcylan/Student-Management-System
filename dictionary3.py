dic1 = {1 :'one',
        2 : 'two',
        3 : 'three'}

dic2 = {4 : 'four',
        5 : 'five',
        6 : 'six'}
dic3 = {7 : 'seven',
        8 : 'eight',
        9 : 'nine'}

all1 = {**dic1,**dic2,**dic3} #kwargs(**) are used to separate the dictionairy and addes them. 
print(all1)
print(type(all1))