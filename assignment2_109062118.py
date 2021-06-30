import sys

def initialize():
    try:
        fh = open('records.txt')
        money = int(fh.readline())
        x = fh.readline()
        s = x.split(' ')
        record = [f'{s[0]} money']
        for x in fh.readlines():
            x = x.strip('\n')
            record.append(x)
        fh.close()
    except: 
        while 1:
            try:
                money = input('How much money do you have?')
                record = ["basic money"]
                money = int(money)
                break
            except:
                print("input an integer please!!") 
    return money, record

def initialize_categories():
    s = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    return s
def view_categories(categories,prefix=()):
    if type(categories) == list:
        i=0
        for x in categories:
            if type(x) != list:
                i+=1
            view_categories(x,prefix+(i,))
    else :
        s = ' '*4*(len(prefix)-1)
        s += '.'.join(map(str,prefix))
        s += ' '+categories
        print(s)
def add(records,initial_money):
    x = input("Add an expense or income record with description and amount:\n")
    records.append(x)
    x = x.split(' ')
    initial_money += int(x[1])  
    return records,initial_money

def view(initial_money, records):
    print("Here's your expense and income records:")
    print("Description        Amount")
    print("================== =======")
    for i in records:
        pr = i.split(' ')
        print(f'{pr[0]}',end='')
        space = 19-int(len(pr[0]))
        for j in range(0,space):
            print(' ',end='')
        print(f'{pr[1]}')
    print("================== =======")
    print('Now you have %d dollars.'%initial_money)

def delete(records,initial_money):
        while 1:
            try:
                bede = int(input('which Description in the list do you want to delete?\n'))
                if bede>int(len(records)):
                    print("the list doesn't exist!!")
                    continue
                break
            except:
                print("please enter a integer")
        x = records[bede].split(' ')
        initial_money -= int(x[1])
        for i in range(bede,len(records)-1):
            records[i] = records[i+1]
        records.pop()
        return records,initial_money


def save(initial_money, records): 
    with open('records.txt', 'w') as f:
        f.write(f'{initial_money}\n')
        for i in records:
            f.write(f'{i}\n')


initial_money, records = initialize()

categories = initialize_categories()

while True:
    command = input('\nWhat do you want to do (add/view/delete/exit)?')
    if command == 'add':
        records,initial_money = add(records,initial_money)
    elif command == 'view':
        view(initial_money, records)
    elif command == 'delete':
        records,initial_money = delete(records,initial_money)
    elif command == 'exit':
        save(initial_money, records)
        break
    elif command == 'view categories':
        view_categories(categories,())
    else:
        sys.stderr.write('Invalid command. Try again.\n')
