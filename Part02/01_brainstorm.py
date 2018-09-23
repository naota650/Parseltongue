from random import randrange

num = randrange(10)
answers = []

categories = ["basketball", "soccer", "football", "hockey"]
for x in range(4):
    print(categories[x])
    answers.append(input("enter answer: "))

print("Your answers are: ")
for x in answers:
    print("{:^80}".format(x))

