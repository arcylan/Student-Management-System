dict = {1 : "one",
        2 : "two",
        3 : "three"}
for i in dict.values():
    print(i)



dict = {1 : "one",
        2 : "two",
        3 : "three"}
for i,j in dict.items():
    print(i,"=",j )



dict = {78 : "HTTP",
        89 : "STTP",
        100 : "LocalHost"}
for i in dict.items():
    print(f"{i[0]} : {i[1]}")    