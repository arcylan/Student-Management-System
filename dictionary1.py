#list of tuples

dic1 = dict([('name','arcylan'),
             ('age',21),
             ('education','b.tech')])
print(dic1)
print(type(dic1))

#tuple of list

dic1 = dict((['name','arcylan'],
             ['age',21],
             ['education','b.tech']))
print(dic1)
print(type(dic1))
dic1['gender'] = 'male' #adding item with key and value
print(dic1)
dic1['address'] ='pampore'
print(dic1)
dic1['age'] ='22'
print(dic1)

