#3-3 Your Own List - Program used to print multiple statements of things I want it to say(Transport)
Transport = ["car",'motorcycle','bus','train','airplane']
message = f"Although I have many ways to get places that I like to use, my absolute favorite is most likely to be by {Transport[0].title()}."
print(message)
message = f"I will say, however even though {Transport[0]} is one of the favorite methods of transport, for longer distances I would much rather use a {Transport[1]}, because it's much faster, and I also am fairly sure that if I ever got a motorcycle it would be probably a Harley Davidson"
print(message)
message = f"I will say though as much as a {Transport[0]}, motorcycle, and plane would be fine by me I don't get much of a chance to use {Transport[3]}, because there isn't much reason to."
print(message)
#3-4 Guest List - Invite a list of people to a dinner.
Invitations = ['Zackry','Allen','Jackson']
Invite = f"About dinner today, {Invitations[2].title()} do you want to go with {Invitations[1].title()}, {Invitations[0].title()} and me?"
print(Invite)
#3-5 Changing Guest List - Someone can't make it to Dinner.
Sick = 'Zackry'
Invitations.remove(Sick)
print(Invitations)
print(f"\n{Sick.title()} can't make it to dinner today, because he got sick, and is completely stuck at home.")
New_Person = "Mason"
print(f"While {Sick.title()} most certainly can't make it to dinner today, I'm sure {New_Person.title()} can.")
print(f"{New_Person.title()}, do you want to come with {Invitations[0].title()}, {Invitations[1].title()}, to dinner?")
#Code above is only temporary, as computer is about to die.
#3-6 More Guests - Bigger Dining Table more spaces are avalible.
#Ask about "print() function.
Invitations.insert(0, 'Jeffery')
Invitations.insert(2, 'Kate')
Invitations.insert(4, "Lynn")
print(Invitations)
New_people = f"I was able to get a bigger table, so I invited {Invitations[0].title()}, {Invitations[2].title()}, and {Invitations[4].title()} to dinner."
New_Invitation = (f"{New_people} {Invitations[1].title()}, {Invitations[3].title()}, is that ok with you guys?")
print(New_Invitation)
