dict={"salary1":25000,"salary2":32000,"salary3":15000}

print(max(dict.values()))
print(min(dict.values()))

'''for value in dict.values:
    if (value>)'''


courses={
    "commerce": {"economics":34,"accountancy":59},
    "BCA": {"java":45,"python":78}

}
print(courses)
courses["commerce"]["economics"]=80

courses["commerce"].update({"accountancy":88})

print(courses)