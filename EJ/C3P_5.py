#3-5 Changing Guest List - Someone can't make it to Dinner.
Invitations = ['Zackry','Allen','Jackson']
Sick = 'Zackry'
Invitations.remove(Sick)
print(Invitations)
print(f"\n{Sick.title()} can't make it to dinner today, because he got sick, and is completely stuck at home.")
New_Person = "Mason"
print(f"While {Sick.title()} most certainly can't make it to dinner today, I'm sure {New_Person.title()} can.")
print(f"{New_Person.title()}, do you want to come with {Invitations[0].title()}, {Invitations[1].title()}, to dinner?")
