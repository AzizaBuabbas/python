print ("Mad libs where libs get Mad\n Start Below:")

time = input("Number:")
items = input ("Noun (plural):")
name = input ("Name:")
scream = input ("Any Sentence:")
verb = input ("Verb:")

print("\tIt was %s o'clock when I heard a knock at the door." % time)
print("\tI opened the door and there was a box full of %s  with a note saying \"From %s \" ." % (items , name.title()))
print ("Just as I closed the door I heard a scream \" %s . \"." % (scream.upper()))
print ("I froze in place and all I could do was %s ." % verb)