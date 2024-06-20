# guess game
secret_number= 5
guess_count=0
guess_limit=3 # hamile 3 choti matra guess garna dine so 3 choti dine guess garna so 0 dekhi 3 samma garaune mathi 0 tala 3 haleko
while guess_count< guess_limit:
    guess = int(input("please enter a number"))
    guess_count+=1
    if guess== secret_number:
        print("you won!!")
        break  # yadi yo halena vane right huda pani  3 choti nai input magcha so break halda loop bahira lagi halcha
    else:
        if guess_count != 3:# last ma loop bahira jancha tara try again ni print garthyo ni ta so tyo print nagarna !=3 haleko
            print("try again")
    # yadi ya guess_count+=1 rakho vane (if guess_count != 2:) rakhne
else:
    print("sorry you failed")
# vitra ko else 3 choti chalcha ani 3 try samma nai ayena vane while bata baira aucha ani 
# if ,elif,else (if ko ni else huncha)
# while, else(loop ko ni else huncha)
# for, else