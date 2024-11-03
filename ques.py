sec="chelsea"
guess= ""
time_count= 0
limit = 3
out=False

while guess != sec and not (out):
    if time_count < limit:
        
       guess= input("Enter a guess: ")
       time_count += 1
    else:
       out=True
if out:
      print("You ran out of guesses. The secret code was " + sec)
else:

 print("Congratulations, you guessed the correct word!")

    