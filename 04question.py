def check_guess(guess, answer):
    global score

    if guess.lower() == answer.lower():
        print('correct answer')
        score = score + 1
    else:
        print('wrong answer')
    print('Score :', score)

print('Guess the riddle')
score = 0

#open question file
q_file = open('04question.txt')
q_content = q_file.read()
#print(q_content)

#open answer file
a_file = open('04answer.txt')
a_content = a_file.read()
#print(a_content)

question = q_content.splitlines()
answer = a_content.splitlines()

#print(question)
#print(answer)

#for i in range(4):
for i in range(len(question)):
    #print(question[i])
    #print(answer[i])
    guess = input(question[i])
    check_guess(guess, answer[i])

