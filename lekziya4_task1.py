
import random
guessesTaken = 0
print(" заработать, друг? Как тебя зовут?")
Name = input("Введите имя: ")
number = random.randint(1,10)

print(f"Ну тогда приступим? ‘+Name’, я загадал число от одного до 20")
while guessesTaken < 6:
    print("Как ты думаешь, какое?") #Перед функцией print() должно быть 4 пробела
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken+1
    if guess < number:
        print("Мое число больше твоего") #Перед функцией print() должно быть 8 пробелов
    if guess > number:
        print("Мое число меньше твоего")
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Превосходно  Ты угадал число с  попытки. Твой выигрыш 10 очков.")
if guess != number:
    number = str(number)
    print("Ты проиграл(")