import random
import json
import datetime
secret = random.randint(1, 5)
guess = 0
attempts = 0


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    #a = score_file.read()
    #score_list = json.loads(a)
    #print("Top scores: " + str(score_list))

#for score_dict in score_list:
    #print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + ", name: " + score_dict.get("name") + ", wrong guesses: " + str(score_dict.get("wrong")))


def myFunc(e):
    return e['attempts']
score_list.sort(key=myFunc)

for score_dict in score_list:
    print (score_dict)

wrong = []
while guess != secret:
    guess = int(input ("guess the number :"))
    attempts += 1 #attemps = attemps +1

    if guess == secret:
        print ("bieeeeeeeeen!")
        print ("Attempts needed: " + str(attempts))

        current_time = str(datetime.datetime.now())
        name = input("what's your name?")
        score_data= {"attempts": attempts, "date": str(current_time), "name": name, "wrong": str(wrong)}
        print ("hasta pronto" +" "+score_data ["name"])
        score_list.append(score_data)

        with open("score_list.txt", "w")as score_file:
            score_file.write(json.dumps(score_list))
        break


    elif guess > secret:
        print ("más pequeño")


    elif guess < secret:
        print ("más grande")

    else:
        print ("It's not " + str(guess) + " try again!")

    wrong.append(guess)