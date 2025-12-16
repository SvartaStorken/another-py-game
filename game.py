import random
import time

bits_score = 0
bits_array = [0, 0, 0]
attempts = -1
guest_questions = ["x", "x", "x"]
the_person = "x"


#Richard Stallman arrays
Richard_Stallman_quotes = ["Sharing is good, and with digital technology, sharing is easy.", "Proprietary software is an injustice.", "Ubuntu of course is a non-free distro, and I wouldn't recommend that anyone use it"]
#Linus Torvalds
Linus_Torvalds_quotes = ["In real open source, you have the right to control your own destiny.", "Talk is cheap. Show me the code.", "See, you not only have to be a good coder to create a system like Linux, you have to be a sneaky bastard too."]
#Theo de Raadt
Theo_de_Raadt_quotes = ["It's the little things that make Freedom become Not Freedom.", "Linux people do what they do because they hate Microsoft. We do what we do because we love Unix.", "This is a software monopoly but at least it was written by people who care about security, so it's not like Microsoft's monopoly."]

person = ["Richard Stallman", "Linus Torvalds", "Theo de Raadt"]

print("***  Welcome          ***")
time.sleep(1)
print("***  to               ***")
time.sleep(1)
print("***  Another py Game  ***")
time.sleep(1)
print("***  How is           ***")
time.sleep(1)
print("***  This person?     ***")
time.sleep(1)
print("***                   ***")
time.sleep(1)

while attempts < 3:
    value = "false"
    print("loop1")

    while attempts < 3:
      print("loop2")

      random_person = random.randint(0, 2)
      random_quote = random.randint(0, 2)
    

      if random_person == 0:
        print("***  quote:           ***")
        print(Richard_Stallman_quotes[random_quote])
      elif random_person == 1:
        print("***  quote:           ***")
        print(Linus_Torvalds_quotes[random_quote])
      elif random_person == 2:
        print("***  quote:           ***")
        print(Theo_de_Raadt_quotes[random_quote])

      the_person = person[random_person]
      print(the_person)
      print(guest_questions[attempts])

      if the_person in guest_questions:
        print("looping")
      else:
        break

  print("guess which person it is:")
  print("Firstname Lastname")
  answer = input()
  attempts += 1
  guest_questions[attempts] = [the_person]

  if answer.lower() == the_person.lower():
    print("***  Right answer!    ***")
    print(the_person)
    bits_array[attempts] = 1

  else:
    print("***  Wrong answer     ***")
    print(the_person)

  if attempts == 2:
    break
time.sleep(1)

print(*bits_array)
print(*guest_questions)