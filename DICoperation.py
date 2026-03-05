my_dic={"brand":"Ford","model":"Mustang","year":1964}
model_name=my_dic["model"]
print(model_name)
val=my_dic.get("year")
print(val)
all_keys=my_dic.keys()
print(all_keys)
all_values=my_dic.values()
print(all_values)
all_items=my_dic.items()
print(all_items)

my_dic["color"]="red"
print(my_dic)
my_dic.update({"year":2020})
print(my_dic)
my_dic.pop("model")
print(my_dic)
my_dic.popitem()
print(my_dic)
#my_dic.pop("brand")
#print(my_dic)
#my_dic.popitem()

print(my_dic)
new_copy=my_dic.copy()
print(new_copy)
my_family={
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
}


