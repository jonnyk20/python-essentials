messageTemplate = "Hey, I'm really glad that {friend} was able to introduce us at {event}. {pronoun} the best! Your office on {street} is actually on my way to {sport} practice, so if you have time on {day}, maybe I could swing by and we could talk about the {jobTitle} position."

warmIntros = [
    {
        "friend": "Carmen",
        "event": "HackerNest",
        "gender": "female",
        "street": "Hastings",
        "sport": "dodgeball",
        "day": "Tuesday",
        "jobTitle": "software engineer"
    },
    {
        "friend": "Thomas",
        "event": "the React workshop",
        "gender": "male",
        "street": "Columbia",
        "sport": "fencing",
        "day": "Easter",
        "jobTitle": "project manager"
    },
    {
        "friend": "Carmen", # Again. She's the best.
        "event": "Demo Day",
        "gender": "female",
        "street": "Hastings",
        "sport": "dodgeball",
        "day": "Wednesday",
        "jobTitle": "front-end developer"
    },
    {
        "friend": "David",
        "event": "Beer Pong",
        "gender": "",
        "street": "Broadway",
        "sport": "badminton",
        "day": "Friday",
        "jobTitle": "social media guru"
    },
    {
        "friend": "Sam",
        "event": "Intro to Crossfit",
        "gender": "nonbinary",
        "street": "Burrard",
        "sport": "squash",
        "day": "Sunday",
        "jobTitle": "assistant to the regional manager"
    }
]

for intro in warmIntros:
    if intro["gender"] is "female":
        pronoun = "She's"
    elif intro["gender"] is "male":
        pronoun =  "He's"
    else:
        pronoun = "That person is"

    if intro["day"] is "Saturday" or intro["day"] is "Sunday":
        intro["day"] = "say, Monday or Tuesday"

    print(messageTemplate.format(**intro, pronoun=pronoun))
    print("\n📨\n")
