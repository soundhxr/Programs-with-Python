class question:
    def __init__(self, q, a):
        self.q =q
        self.a = a
lvl = input('Choose level of difficulty\npress e for easy, press d for difficult: ')
while lvl.lower() != 'e' and lvl.lower() != 'd':
    print('invalid input\n')
    lvl = input('Choose level of difficulty\npress e for easy, press d for difficult: ')
    continue
easy=[
    question("\nName the capital of India - ", "delhi"),
    question("Name an organ in the human body which reads the same backward and forward - ", "eye")
]
difficult=[
    question("\nIn a group of 10 people, each person gives handshake to every other person. How many handshakes in total will take place? - ", "45"),
    question("ISRO was set up in which year? - ", "1969")
]
def runtest(lst):
    score = 0
    for Q in lst:
        answer = input(Q.q)
        if answer.lower() == Q.a:
            print("correct!\n")
            score += 1
        else:
            print('Oops, the correct answer is', Q.a.capitalize(), end='\n\n')

    print('You got', score, "out of", len(lst), 'correct')
if lvl.lower() == 'e':
    runtest(easy)
elif lvl.lower() == 'd':
    runtest(difficult)


