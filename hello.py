str = input("Enter Your Sentence >>> ")
print(str)
word = input("Enter character You want to extract >>> ")
first_1 = str.find(word)
print(first_1)
second_2 = str.find (word,first_1+1)
print(second_2)
third_3 = str.find(word,second_2+1)
print(third_3)
fourth_4 =str.find(word,third_3+1)
print(fourth_4)
fifth_5 = str.find(word,fourth_4+1)
print(fifth_5)
sixth_6 = str.find(word,fifth_5+1)
print(sixth_6)
seventh_7= str.find(word,sixth_6+1)
print(seventh_7)