sentence = "Python is Awesome"
for x in sentence.split():
    if any(char.isupper() for char in x):
        print(x[::-1].capitalize(), end=" ")
    else:
        print(x[::-1], end=" ")