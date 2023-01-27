import random

def hangman():
    words_list = ['escape','cringe','bright','jovial','kalon','eunoia','groke','dern',
    'morosis','lacuna','perfecto','hola','unicorn','megladon','eternal','happiness','diary']
    word = random.choice(words_list)
    turns = 10
    guess_made = ""
    valid_entries = set('abcdefghijklmnopqrstuvwxyz')

    while turns > 0:
        main_word = ""
        

        for letter in word:
            if letter in guess_made:
                main_word += letter
            else:
                main_word += "_ "
                
        if main_word == word:
            print(main_word)
            print('good goin , you won ><')
            break
        elif turns == 1:
            print('only 1 turn left mate!hangman gonna die soon :/')
        

        print("Guess the right word", main_word)
        guess = input()

        if guess in valid_entries:
            guess_made += guess
        else:
            print('please enter the valid characters')
            guess = input()

        if guess not in word:
            turns -= 1

            if turns==9:
                print('9 turns left mate!')
                print('------------')
            if turns==8:
                print('8 turns left mate!')  
                print('------------')
                print('      o     ')
            if turns==7:
                print('7 turns left mate!')
                print('------------')
                print('      o     ')
                print('      |     ')
            if turns==6:
                print('6 turns left mate!')
                print('------------')
                print('      o     ')
                print('      |     ')
                print('     /      ')
            if turns==5:
                print('5 turns left mate!')
                print('------------')
                print('      o     ')
                print('      |     ')
                print('     / \    ')
            if turns==4:
                print('4 turns left mate!')
                print('------------')
                print('     \o     ')
                print('      |     ')
                print('     / \    ')
            if turns==3:
                print('3 turns left mate!')
                print('------------')
                print('     \o/    ')
                print('      |     ')
                print('     / \    ')
            if turns==2:
               print('2 turns left mate!')
               print('------------')
               print('     \o/ |  ')
               print('      |     ')
               print('     / \    ')
            if turns==1:
               print('only 1 turn left mate!hangman gonna die soon :/')
               print('------------')
               print('     \o/_|  ')
               print('      |     ')
               print('     / \    ')
            if turns==0:
               print('better luck next time')
               print('you let a kind man die')
               print('------------')
               print('      o _|  ')
               print('     /|\     ')
               print('     / \    ')
               break


name = input('enter(any char):')

print('yo! \nlets play hangman!')
print('----------------------')
print('Game rules-: \n1.You will be given 10 chances \n2.You have to guess the word to save the man from dyin')
print('----------------------')
print('good luck ^_^')
hangman()




    

  
