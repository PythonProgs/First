print("Hello")
done = 0
a = 0
b = 0
c = 0
d = 0
e = 0
while done < 5:
    question = input("Please choose question number 1 - 5 = ")
    if  question == "1" and a == 0:
        while a == 0:
            answera = input ("What continent is Italy in = ")
            if answera == "europe" or answera == "Europe":
                print("Correct\n")
                a = 1
                done = done + 1
            else:
                print("Wrong\n")
    elif question == "2" and b == 0:
        while b == 0:
            answerb = input("What if 4 * 5 = ")
            if answerb == "20":
                print("Correct\n")
                b = 1
                done = done + 1
            else:
                print("Wrong\n")
    elif question == "3" and c == 0:
        while c == 0:
            answerc = input("Flying Animal = ")
            if answerc == "Bird" or  answerc == "bird":
                print("Correct\n")
                c = 1
                done = done + 1
            else:
                print("Wrong\n")
    elif question == "4" and d == 0:
        while d == 0:
            answerd = input("Who wins in World War 2 = ")
            if answerd == "alliance" or answerd == "Alliance":
                print("Correct\n")
                d = 1
                done = done + 1
            else:
                print("Wrong\n")
    elif question == "5" and e == 0:
        while e == 0:
            answere = input("What is the capital city of Japan = ")
            if answere == "tokyo" or answere == "Tokyo":
                print("Correct\n")
                e = 1
                done = done + 1
            else:
                print("Wrong\n")
    elif question == "1" and a == 1:
        print("Please don't choose the same question twice\n")
    elif question == "2" and b == 1:
        print("Please don't choose the same question twice\n")
    elif question == "3" and c == 1:
        print("Please don't choose the same question twice\n")
    elif question == "4" and d == 1:
        print("Please don't choose the same question twice\n")
    elif question == "5" and e == 1:
        print("Please don't choose the same question twice\n")
    else:
        print("Please choose between 1 - 5\n")
print("Congrats, it's done!")