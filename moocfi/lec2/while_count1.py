number = int(input("give a number between 1-10 :"))
while number <= 10:
    if number < 1:
        print("give a valid input!")
        break
    print(number)
    number += 1 #if we don't update variable to converge then while gets trapped in infinite loop
print("Execuation Complete.")


num = int(input("give a number between 5-50 :"))
while 5 <= num <= 50 and num != 10: 
    #we are using break within condition
    print(f'{num}')
    num += 1
print("Finish!")
