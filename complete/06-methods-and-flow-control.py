# create a method called bouncer that does the following:
# if the input number is 19 or higher, let them know they come come in
# otherswise let them know that they're too young
# add a method another clause for if the person is too old


def bouncer(age):
    if age < 19:
        print("There's a McDonald's play place down the street.")
    elif age < 50:
        print("You can come in")
    else:
        print(
            """
            Go gome Jerry, you have a family. 
            Come on, buddy this is the third time time this week.
            I know things aren't going well with your wife, 
            but chasing women at the club is not a healthy way to cope. 
            You reek of sadnesss and desperation,
            Even if I let you in here, you probably won't leave with anything more than 
            a couple of drinks in your face and some restraining orders.
            You need to just home and patch thigns up with Loraine.
            I'm saying this because you're my friend. 
            Trust me, you'll thank me later, now get out of here and go spend time with your kids.
          """
        )


# run the function with the the numbers: 23, 91, 13
bouncer(23)
bouncer(91)
bouncer(13)
