import random

random.seed(5)
print(random.randint(1,100)) # Random int:  a <= x <= b
print(random.random()) # Random float:  0.0 <= x < 1.0
print(random.randrange(5)) # Random int:  0.0 <= x < b

choice_list = ["A", "B", "C", "D"]
print(random.choice(choice_list))

print(random.sample(choice_list, k=3)) # displays a list that contains any 3 of the items from choice_list

random.shuffle(choice_list)
print(choice_list)

