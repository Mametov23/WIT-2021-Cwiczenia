
type = input("Napisz Typ(prykład: `trivia`, `math`, `date`, lub `year`): ")
if type == 'trivia' or type == 'math' or type == 'date' or type == 'year':
    print('type jest zapisano')
elif not (type == 'trivia' or type == 'math' or type == 'date'):
    type = 'trivia'
    print('the default type is trivia')
number = input("Napisz number(jeśli 'type' data to napisz w formularzu mouth / day): ")


print(type)
print(number)