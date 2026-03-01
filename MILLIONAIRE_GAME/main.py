questions = [
    ["Who is Donald J Trump?", "Politician", "BusinessMan", "Comedian", "Joker", 2],
    ["Who is the current Prime Minister of India?", "Rahul Gandhi", "Narendra Modi", "Amit Shah", "Droupadi Murmu", 2],
    ["Who is the President of France?", "Emmanuel Macron", "Marine Le Pen", "François Hollande", "Nicolas Sarkozy", 1],
    ["Who is the current President of Argentina?", "Cristina Fernández", "Javier Milei", "Mauricio Macri", "Alberto Fernández", 2],
    ["Which country is led by Prime Minister Keir Starmer?", "Canada", "Germany", "United Kingdom", "Australia", 3]
]

prize = [1000, 10000, 50000, 100000, 1000000]
i = 0

for question in questions:
    print("\n",question[0],"\n")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}\n")

    ans = int(input("Choose option: 1 for a, 2 for b, 3 for c, 4 for d:  "))
    if(question[5] == ans):
        print("\nCorrect Answer")
    else:
        print(f"\nIncorrect, Correct answer was {question[5]}")
        print(f"Better luck next time!")
        break
    print(f"You won {prize[i]} ")
    i+=1
    