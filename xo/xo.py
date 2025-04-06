import random

def make_step(game,x,y):
    flag = True
    if game[x][y] == '':
        game[x][y] = 'x'
        flag = win_check(game)   
        if flag:
            while True:
                x = random.randint(-1,2)
                y = random.randint(-1,2)
                if game[x][y] == '':
                    game[x][y] = 'o'
                    flag = win_check(game)
                    break  
    else:
        print("Данная ячейка уже занята")
    return game, flag

def win_check(game):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != '':
            print(f'Выйграл {game[i][0]}')
            return False
        if game[0][i] == game[1][i] == game[2][i] != '':
            print(f'Выйграл {game[i][0]}')
            return False
    if (game[0][0] == game[1][1] == game[2][2] != '') or \
        (game[0][2] == game[1][1] == game[2][0] != ''):
            print(f'Выйграл {game[1][1]}')
            return False
    counter = 0
    for i in game:
        if '' in i:
            counter += 1
    if counter == 0:
        print("Ничья")
        return False
    return True
        
def main():
    game = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    flag = True

    while flag:
        x,y = map(int,input().split())
        game, flag = make_step(game,x,y)
        for i in range(3):
            print(game[i])
 
        

if __name__ == '__main__':
    main()
