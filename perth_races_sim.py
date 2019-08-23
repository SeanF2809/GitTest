import random
import time

print ('PERTH RACES SIMULATOR')
print ('')
print ('You will be asked to pick your horse, please do so with 1,2 or 3: ')
print('')
print ('Horse1 - Dickless Harry, 2/1')
print ('Horse2 - Kneeless Kevin, 5/1')
print ('Horse3 - Pushing up Daisys, 10/1')
bank = 100


while bank > 0:
    print('Your Remaing bank is: ', bank)
    print('')
    horse_selection = int(input('Please Select your horse, if you are ready to quit type "exit": '))
    if horse_selection == "exit":
        exit()
        
    
    print('')
    bet_value = int(input('Please Place your Bet Value: '))
    print('')
    bank = bank - bet_value

    random_horse = random.randint(1,100)

    print('THE HORSES ARE RUNNING, PREPARE YOURSELF FOR SOME COMENTARY')
    time.sleep(2)
    print ('DICKLESS HARRY IS TRYING TO HUMP THE RAIL')
    time.sleep(2)
    print ('KNEELESS KEVIN IS REPORTEDLY REALLY BAD AT TWISTER')
    time.sleep(2)
    print('PUSHING UP DAISYS... LOOKS LIKE ITS PUSHING UP DAISYS')
    time.sleep(2)

    if random_horse <=50 and horse_selection ==1:
        print ('Dickless Harry has won the race!!')
        bet_wind = bet_value * 2
        bank = bank + bet_wind
         
    elif random_horse >= 51 and random_horse <= 80 and horse_selection ==2:
        print ('Kneeless Kevin has won the race!!')
        bet_wink = bet_value * 5
        bank = bank + bet_wink 
            
    elif random_horse >= 81 and random_horse <=100 and horse_selection ==3:
        print ('Pushing up Daisys has won the race!!')
        bet_winp = bet_value * 10
        bank = bank + bet_winp     
      
    elif bank == 0:
        print ('You have run out of money, your significant other and/or bank manager is going to kill you')
        print ('Game Over')
        time.sleep(1)
        break
    else:
        print ('Better Luck Next Time')
        if random_horse <=50:
            print ('Dickless Harry won the race, the sod')
        if random_horse >=51 and random_horse <=80:
            print ('Kneeless Kevin won the race, total bastard')
        if random_horse >=80 and random_horse <=100:
            print ('Pushing up Daisys won... how?')
            

   
        
    
        




