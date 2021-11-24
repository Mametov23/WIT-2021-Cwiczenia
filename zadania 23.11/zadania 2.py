from random import randint
print('Naciśnij Y, aby wziąć udział w grze W kałamarnicę i dowolną inną literę, aby zrezygnować')
print('Po kliknięciu zostaną rzucone dwie kości, liczby spadające będzie Twój numer w grze')
Y = input()

if Y == 'Y':
    print('Pierwsza kostka do gry', randint(1, 6))
    print('druga kostka do gry', randint(1, 6))
else: 
    print('Zrezygnowałeś z udziału w"gra w kałamarnicę"')