
'''for and if usecase in a list '''

lists = ['ankit', 'astha', 'maamu', 'bua']
print('enter ur name')
naam = input() #to see if input name exist in the list
for names in lists:
    if naam == names:
        print('welcome to the family!!')
        break
else:# ELSE clause is being used in the for loop 
    print('u r not included')