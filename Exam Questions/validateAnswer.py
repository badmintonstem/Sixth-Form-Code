def validateAnswer(answer, randomLetters):
    score = 0
    #for loop to check each letter of the answer
    for letter in answer:
        #check if letter is in the random letters list:
        if letter in randomLetters:
            #remove the letter from the random letters list so it cant be match again
            randomLetters.pop(randomLetters.index(letter))
            #increment score
            score += 1
        else:
            #if at any point the letter from the word is not in the random letters list, score is 0
            return 0
    #if for loop completed then return the score
    return score

#main program
while True:
    print(validateAnswer(input("Enter a word\n"),[x for x in 'OPXCMURETN']))