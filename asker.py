from random import choice

questions = ["Why is the sky blue?: ", "Why is there a face on the moon?: ",
                     "Where are all the dinosaurs: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "I don't know":
    answer = input("tell again?: ").strip().lower()

input("Is it the right answer: ")

input("Say bye to me: ")
