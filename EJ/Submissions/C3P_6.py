#3-6 More Guests - Bigger Dining Table more spaces are avalible.
Invitations = ['Zackry','Allen','Jackson']
Invitations.insert(0, 'Jeffery')
Invitations.insert(2, 'Kate')
Invitations.insert(4, "Lynn")
print(Invitations)
New_people = f"I was able to get a bigger table, so I invited {Invitations[0].title()}, {Invitations[2].title()}, and {Invitations[4].title()} to dinner."
New_Invitation = (f"{New_people} {Invitations[1].title()}, {Invitations[3].title()}, is that ok with you guys?")
print(New_Invitation)
