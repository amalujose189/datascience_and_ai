A={1,2,3,4,5}
B={4,5,6,7,8}
print("Union:",A|B)
print("Intersection:",A&B)
print("Difference A-B:",A-B)
print("Difference B-A:",B-A)
print("Symmetric Difference:",A^B)
#remove the comman elements



my_dic={"brand":"Ford","model":"Mustang","year":1964}
model_name=my_dic["model"]
val=my_dic.get("year")
all_keys=my_dic.keys()
all_values=my_dic.values()
all_items=my_dic.items()

my_dic["color"]="red"
my_dic.update({"year":2020})
my_dic.pop("model")
my_dic.popitem()

my_dic.pop("brand")
my_dic.popitem()
