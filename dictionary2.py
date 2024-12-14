person = {"name":"arcylan",
          "age":21,
          "country":"india"}
print(person)

person.update({"name":"jhon",
               "height":6})

print(person)
person.pop("height")
print(person)