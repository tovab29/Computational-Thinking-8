# Beginning: create variables
extrovert_points = 0
introvert_points = 0

# Middle: Ask questions
awnser = input ("Being around people makes me feel A) a bit exhausting B) Like im alive!")
if awnser == "A":
    introvert_points += 1
elif awnser == "B":
    extrovert_points += 1


awnser = input ("To prepare for a night out... A) Prepare? my friends have to drag me out of the house B) call all of my friends and get dressed and ready together")
if awnser == "A":
    introvert_points += 1
elif awnser == "B":
    extrovert_points += 1


awnser = input ("When given a choice between working as part of a team or working as a group, I would prefer to... A) Work alone B) work with my friends")
if awnser == "A":
    introvert_points += 1
elif awnser == "B":
    extrovert_points += 1


awnser = input ("During parties or social gatherings, I tend to... A) find a few people to talk to B) connect and talk to new people")
if awnser == "A":
    introvert_points += 1
elif awnser == "B":
    extrovert_points += 1


awnser = input ("When I'm dealing with a personal problem, I prefer to... A) just talk to 1 close friend B) talk about it with others and ask for their help")
if awnser == "A":
    introvert_points += 1
elif awnser == "B":
    extrovert_points += 1


# End: determine results
# end of quiz:
if extrovert_points > introvert_points:
    print("you are a extrovert")
elif introvert_points > extrovert_points:
    print("your are a introvert")
