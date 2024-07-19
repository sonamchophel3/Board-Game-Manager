#Name: SONAM CHOPHEL
#Student Number: 10600541

import json

with open('data.txt', 'r') as f:
    try:
        data = json.load(f)
    except:
        data = []


def inputInt(prompt):
    while True:
        try:
            fint = int(input(prompt))
            if fint >= 0:
                break
        except ValueError:
            print("Int format are only supported")
            continue
    return fint


def inputSomething(prompt):
    while True:
        a = input(prompt)
        b = a.strip()
        if b != "":
            break
        else:
            continue
    return b


def saveData(dataList):
    f = open('data.txt', 'w')
    json.dump(data, f)
    f.close()


print('Welcome to the Game Finder Admin Program.')
while True:
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()
    if choice == 'a':
        nog = inputSomething('Name of game:')
        minp = inputInt('Minimum number of players:')
        maxp = inputInt('Maximum number of players:')
        adg = inputInt('Average duration of game in minutes:')
        mrp = inputInt('Minimum recommended player age:')
        a = {}
        a["name"] = nog
        a["min_players"] = minp
        a["max_players"] = maxp
        a["duration"] = adg
        a["min_age"] = mrp
        data.append(a)
        print("Game added")
        saveData(data)
    elif choice == 'l':
        lindex = 0
        if data == []:
            print("No game saved")
        else:
            for line in data:
                print(lindex+1, ')', data[lindex]["name"])
                lindex += 1
    elif choice == 's':
        if data == []:
            print("No game saved")
        else:
            sindex = 0
            sr = 0
            s = inputSomething("Type a game name to search for:")
            for line in data:
                if s in data[sindex]["name"]:
                    print(data[sindex]["name"])
                    sindex += 1
                    sr += 1
                else:
                    continue
            if sr == 0:
                print("There is no matching search")
    elif choice == 'v':
        if data == []:
            print("No game saved")
        else:
            while True:
                vi = inputInt("Game number to view:")
                if vi >= len(data):
                    print("please enter valid index")
                    continue
                else:
                    print(data[vi])
                    break
    elif choice == 'd':
        if data == []:
            print("No game saved")
        else:
            while True:
                di = inputInt("Game number to delete:")
                if di >= len(data):
                    print("please enter valid index")
                    continue
                else:
                    del data[di]
                    print("Game deleted")
                    break
    elif choice == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
