import random
def guess_number():
    random_number = random.choice([i for i in range(100)])
    u  = int(input('Напиши число: '))
    us = False 
    while us == False: 
        if random_number > u:
            print( "Za nisko!")
            u  = int(input('Напиши число: '))
            us = False
        elif random_number < u:
            print( "Za wysoko!")
            u  = int(input('Напиши число: '))
            us = False
        elif random_number == u:
            us = True
            print( "Brawo!")

def count_chars():
    word = input('Напиши слово: ')
    seen = ""

    for c in word:
        if c not in seen:
            print(f"{c}: {word.count(c)}")
            seen += c
            
count_chars()