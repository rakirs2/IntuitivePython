Invitations = ['Zackry','Allen','Jackson']
#3-7 Shrinking Guest List: New dining table won't arrive in time, so you can only take 2 people.
a = "I can only invite 2 people,"
message = " because the table won't arrive in time, sorry I had to do this last minute, but I won't be able to have you come over for dinner on Friday, "
apology = ", I'm so sorry about this, and I hope there is no hard feelings about it."
Cant_come = Invitations.pop(0)
print(f"{a}{message}{Cant_come}, I'm so sorry about this, and I hope there is no hard feelings about it.")
#I made "apology" after I already made the code above.^
Cant_come = Invitations.pop(1)
print(f"{a}{message}{Cant_come}{apology}")
Cant_come = Invitations.pop(2)
print(f"{a}{message}{Cant_come}{apology}")
print(f"I'm sorry to tell you, but the bigger table I wanted to take wasn't able to get there in time, so it's going to be me, you and {Invitations[0].title()}")
print(f"I wish I had better news, but me, you and {Invitations[1].title()} were the only ones that could make it to dinner, because the table I wanted to get wasn't avaliable, meaning that I had to uninvite the rest of our friends that were supposed to come to dinner.")
del Invitations[0]
del Invitations[0]
print(Invitations)
