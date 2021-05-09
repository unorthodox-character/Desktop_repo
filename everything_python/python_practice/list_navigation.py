''' if u need both the list index and its items '''
def list_nav():
    spam = ['ankit', 'astha', 'maamu', 'bua']
    for i in range(len(spam)):
        p = print(f'index {i} is:',spam[i])
    return p

list_nav()