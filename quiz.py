# Trivia quiz

print("This is a quiz that test your knowledge on video games")

'''
'''
name= input("Enter your name: ")
print("Hello, ", name, "Are you ready to start the quiz?")

print("There wil be 7 questions in this quiz. Each question is multiple choice. ")
print("You have the option to choose A, B, C, or D.")
print(" ~~~~~~~~~~~~~~~ ")
# set the score of the quiz to 0
score = 0
score = int(score)

# question 1
print("Question 1: What was the most popular Nintendo DS (excluding the 3DS/2DS) game made?")

print("A: Mario Kart")
print("B: Super Mario 64 DS")
print("C: Prince of Persia ")
print("D: Legend of Zelda")


Q1answer="A" # the right answer to question 1
Q1response= input("Your answer: ")

if Q1response=="A" or Q1response=="a":
      print("Correct answer", Q1answer)
      score= score +10
elif Q1response != "B, C, D" or Q1response != 'b, c, d':
    print("Incorrect")
    score=score -5

