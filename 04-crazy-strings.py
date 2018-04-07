"""
This whole exercise will use the same variables. These shouldn't change.
"""

friend = "Carmen"
event = "HackerNest"
street = "Hastings"
sport = "dodgeball"
day = "Tuesday"
jobTitle = "software engineer"


"""
Plan #1: Concatenation

    Let's just chop the message up, and then splice the variables in where we want them.
    This is quite inconvenient, because we need to take the whole string apart and then
    Frankenstein it back together.

    In this case, the trade-off isn't TOO bad... But we have better ways.
"""

terriblePlan = "Hey, I'm really glad that " +  friend + " was able to introduce us at " + event + ". Your office on " + street + " is actually on my way to " + sport + " practice, so if you have time on " + day +", maybe I could swing by and we could talk about the " + jobTitle + " position."

print("This is a terrible plan that works:")
print(terriblePlan)
print("\n--------\n")

"""
Plan #2: Replace

    Maybe we can just have placeholder words in the message, and then replace them with other words.
    I know that I want to replace 'person' with the name of a person, and 'event' with the name of an event.
    Replace comes in handy alot, but you can run into trouble without realizing it.

    What if this phrase is in your message?:

        'I think person is a really good person.'

    You'll end up with this message by accident:

        'I think Carmen is a really good Carmen.'

    A clever developer might start using some sort of convention in their templates to
    make sure that sort of thing doesn't happen:

        'I think [PERSON] is a really good person.'
        'I think !!!PERSON is a really good person.'
        'I think _person_ is a really good person.'

    That's a neat idea, and is actually really similar to our better plans... But our
    better plans circumvent the need to outsmart the text.

    Also, it's kind of a drag writing so many lines like that.
"""

badPlan = "Hey, I'm really glad that friend was able to introduce us at event. Your office on street is actually on my way to sport practice, so if you have time on day, maybe I could swing by and we could talk about the jobTitle position."

badPlan = badPlan.replace('friend', friend)
badPlan = badPlan.replace('event', event)
badPlan = badPlan.replace('street', street)
badPlan = badPlan.replace('sport', sport)
badPlan = badPlan.replace('day', day)
badPlan = badPlan.replace('jobTitle', jobTitle)

print("This is a slightly less terrible plan that works:")
print(badPlan)
print("\n--------\n")


"""
Plan #3: String formatting

    This is the ideal way to manipulate strings programmatically. String formatting is
    much more flexible and reliable than the methods above.
"""
print("{}bc{}fghijklmno{}qrs{}uvwxyz".format('a','de','p','t')) # Empty braces: Read the arguments in order
print("Batman and {sidekick}".format(sidekick='Robin'))

betterPlan = "Hey, I'm really glad that {friend} was able to introduce us at {event}. Your office on {street} is actually on my way to {sport} practice, so if you have time on {day}, maybe I could swing by and we could talk about the {jobTitle} position."
betterOutcome = betterPlan.format(friend=friend, event=event, street=street, sport=sport, day=day, jobTitle=jobTitle)
# betterPlan.format(**locals()) # <-- Pro mode.
print("\n--------\n")
print("Regular string formatting:")
print(betterOutcome)


print("\n--------\n")
print("Literal string formatting:")
# This is called 'literal string interpolation.' When you do it this way, it takes out the .format(blahblah) step.
literalBetterPlan = f"Hey, I'm really glad that {friend} was able to introduce us at {event}. Your office on {street} is actually on my way to {sport} practice, so if you have time on {day}, maybe I could swing by and we could talk about the {jobTitle} position."

print(literalBetterPlan)
