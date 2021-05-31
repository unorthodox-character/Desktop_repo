def a_fun():
    list1 = []
    eggs = {'name': 'Ankit', 'species': 'human', 'age':28}
    for i in eggs.keys():
        list1.append(i)
    return list1
list2 = ['khatte', 'vatte', 'age']
p = a_fun
print(q)
print(type(p))
for i in list2:
    print(type(i))
    if i in p:
       print('there is atleast one match')
       break
