def team_choice():
        
    choice='wrong'
    
    while choice not in ['X','O']:
          
        choice = input('Which would Player 1 like to be? (X or O): ').upper()
         
        if choice not in ['X','O']:
            print("Sorry, I don't understand, please choose X or O")
        
    global player1
    global player2
    
    if choice=='X':
        player1='X'
        player2='O'
        
    elif choice=='O':
        player1='O'
        player2='X'
    
    print(f'Player 1 is {choice} \n')
    return choice  
  
def position_choice(player):
        
    choice='wrong'
    
    while choice not in reverseguesslist:
        
        choice = input(f'{player} pick a position (1-9): ')
        
        if choice not in reverseguesslist:
            print('Sorry, invalid position')
            
    reverseguesslist.remove(choice)
    return choice
    
def position_replacement(player):
    
    user_placement = player 
    
    gameboardlist= list(gameboard)
    
    gameboardlist[game_position] = user_placement
    
    return ''.join(gameboardlist)

def win_check(team):
    
    win=False
    
    while not win:
    
        if gameboard[0]== team and gameboard[4]== team and gameboard[8]== team:
            win=True
        elif gameboard[20]== team and gameboard[24]== team and gameboard[28]== team:
            win=True
        elif gameboard[40]== team and gameboard[44]== team and gameboard[48]== team:
            win=True
        elif gameboard[0]== team and gameboard[20]== team and gameboard[40]== team:
            win=True
        elif gameboard[4]== team and gameboard[24]== team and gameboard[44]== team:
            win=True
        elif gameboard[8]== team and gameboard[28]== team and gameboard[48]== team:
            win=True
        elif gameboard[0]== team and gameboard[24]== team and gameboard[48]== team:
            win=True
        elif gameboard[8]== team and gameboard[24]== team and gameboard[40]== team:
            win=True
        else:
            break  
            
    if win==True:
        print(f'{team} has won!')
        return True

def draw_check():
    
    if len(reverseguesslist)==0:        
        print("DRAW!")
        return True

print("Welcome to Tic Tac Toe!\n")

team_choice()

print('Pick positions like this: \n1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n')

game_on = True

gameboard= '  |   |  \n---------\n  |   |  \n---------\n  |   |  \n'
position = {'1':0,'2':4,'3':8,'4':20,'5':24,'6':28,'7':40,'8':44,'9':48}
reverseguesslist= ['1','2','3','4','5','6','7','8','9']

while game_on:
    
    game_position = position[position_choice(player1)]
    
    gameboard = position_replacement(player1)
    
    print(gameboard)
    
    if win_check(player1):
        break
        
    if draw_check():
        break
    
    game_position = position[position_choice(player2)]
    
    gameboard = position_replacement(player2)
    
    print(gameboard)
    
    if win_check(player2):
        break
    
    if draw_check():
        break