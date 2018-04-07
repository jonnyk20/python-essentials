messageTemplate = "Hey, I'm really glad that {friend} was able to introduce us at {event}. Your office on {street} is actually on my way to {sport} practice, so if you have time on {day}, maybe I could swing by and we could talk about the {jobTitle} position."

singleWarmIntro = {
    "friend": "Carmen",
    "event": "HackerNest",
    "street": "Hastings",
    "sport": "dodgeball",
    "day": "Tuesday",
    "jobTitle": "software"
}

print("How to access a key:")
print(singleWarmIntro['friend'])
print(singleWarmIntro['event'])
print('\n--------\n')

warmIntros = [
    {
        "friend": "Carmen",
        "event": "HackerNest",
        "street": "Hastings",
        "sport": "dodgeball",
        "day": "Tuesday",
        "jobTitle": "software engineer"
    },
    {
        "friend": "Thomas",
        "event": "the React workshop",
        "street": "Columbia",
        "sport": "fencing",
        "day": "the weekend",
        "jobTitle": "project manager"
    },
    {
        "friend": "Carmen", # Again. She's the best.
        "event": "Demo Day",
        "street": "Hastings",
        "sport": "dodgeball",
        "day": "Wednesday",
        "jobTitle": "front-end developer"
    },
    {
        "friend": "David",
        "event": "Beer Pong",
        "street": "Broadway",
        "sport": "badminton",
        "day": "Friday",
        "jobTitle": "social media guru"
    }
]

for intro in warmIntros:
    friend = intro['friend']
    event = intro['event']
    street = intro['street']
    sport = intro['sport']
    day = intro['day']
    jobTitle = intro['jobTitle']
    print(messageTemplate.format(friend=friend, event=event, street=street, sport=sport, day=day, jobTitle=jobTitle))
    print('\n📨\n')

print('----\nPro mode:\n')
for intro in warmIntros:
    print(messageTemplate.format(**intro))
    print('\n📨\n')
