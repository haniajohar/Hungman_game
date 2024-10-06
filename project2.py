if __name__=='__main__':
    while True:
        print("____HUNGMAN GAME____")
        print("player1")
        alphabet_list=[]
            #for english alphabets from (a-z)
       
        for i  in  range(97,123): 
            alphabet_list.append(chr(i)) 
        for i in alphabet_list:
            print(i,end=" ")
        print(" ") 
        new_list=[] 
             #to enter word 
        print("enter a letter from the given letters (To End the word press fullstop(.))")
        while True:
            
            a=input("enter  letter").lower()
            
            
            if(a in alphabet_list):
                new_list.append(a)
            elif(a=="."):
                break    
            else:
                print("error try again") 
        hidden_indices=[]   
            #to hide come of the lettrs in the list from the second player
        print("Which letters do you want to hide? Enter their index numbers (0-based):")
        
        while True:
            j = input("Enter index number (or 'done' to finish): ")
            if j.lower() == 'done':
                break
            if j.isdigit() and int(j) < len(new_list):
                hidden_indices.append(int(j))
            else:
                print("Invalid index, try again.")
         
        print("player2")
        print("guess the letter")
        #to display list for the seccond player inwhich some of the letters are hidden 
        displayed_list=[]
        for index,elements in enumerate(new_list):
            if index in hidden_indices:
                displayed_list.append("_")
            else:
                displayed_list.append(elements)
        for i in displayed_list:
            print(i,end=", ")
        attempt=0
        max_attempt=6
        #if the player guesses wrong
        hungman=[
            '''
            print("| - - - - - ")
            print("|          |")
            print("|          |")
            print("|          o ")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            ''',
            '''
            print("| - - - - - ")
            print("|          |")
            print("|          |")
            print("|          o ")
            print("|         / ")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            ''',
            '''
            print("| - - - - - ")
            print("|          |")
            print("|          |")
            print("|          o ")
            print("|         / \\")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            ''',
            '''
            print("| - - - - - ")
            print("|          |")
            print("|          |")
            print("|          o ")
            print("|         / \\")
            print("|          |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            ''',
            '''
            print("| - - - - - ")
            print("|          |")
            print("|          |")
            print("|          o ")
            print("|         / \\")
            print("|          |")
            print("|         /")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            ''',
            '''
            print("| - - - - - ")
            print("|          |")
            print("|          |")
            print("|          o ")
            print("|         / \\")
            print("|          |")
            print("|         / \\")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            ''',

        ]
        
        while(attempt<max_attempt):
            guess_correct=False
            guess=input("guess the original_letter").lower()
            for index,elements in enumerate(new_list):
               if (guess == elements)and(displayed_list[index]=="_"):
                   displayed_list[index]=elements
                   guess_correct=True
            print("word is"," ".join(displayed_list))       
            if not guess_correct:
                attempt+=1
                if (attempt==1):
                    print(hungman[0])
                elif (attempt==2):
                    print(hungman[1])
                elif (attempt==3):
                    print(hungman[2])
                elif (attempt==4) :
                    print(hungman[3])
                elif (attempt==5) :
                    print(hungman[4])
                elif (attempt==6) :
                    print(hungman[5])
                    #if the player lose the game
                    print("you lost the game")
                    break
                #if the player won the game
            if "_" not in displayed_list:
                print("congratulations you won the game")
                break
            #to give an option if you want to play again or not
        print("do you want to play again")
        choice=input("if yes press y or Y")
        if(choice=='y' or choice=='Y'):
            continue
        else:
            print("thanks")
            break