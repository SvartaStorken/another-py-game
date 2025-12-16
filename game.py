import random
import time

bits_score = 0
bits_array = [0, 0, 0]
attempts = 0
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
    while True:
        random_person = random.randint(0, 2)
        random_quote = random.randint(0, 2)

        the_person = person[random_person]
        if the_person in guest_questions:
            continue
        else:
            break

    if random_person == 0:
      print("***  quote:           ***")
      print(Richard_Stallman_quotes[random_quote])
    elif random_person == 1:
      print("***  quote:           ***")
      print(Linus_Torvalds_quotes[random_quote])
    elif random_person == 2:
      print("***  quote:           ***")
      print(Theo_de_Raadt_quotes[random_quote])

    print("guess which person it is:")
    print("Firstname Lastname")
    answer = input()
    time.sleep(1)

    guest_questions[attempts] = the_person

    if answer.lower() == the_person.lower():
        print("***  Right answer!    ***")
        print(the_person)
        bits_array[attempts] = 1
        time.sleep(1)

    else:
        print("***  Wrong answer     ***")
        print(the_person)

    attempts += 1
time.sleep(1)

print(*bits_array)
bit_count = 0
bit_calc = 1
calc_array = [0, 0, 0]

while bit_count < 3:
  bit_calc = bit_calc + bit_calc
  if 1 == bits_array[bit_count]:
    calc_array[bit_count] = bit_calc
    bit_count += 1
  else:
    bit_count += 1

print(*calc_array)

total_score = calc_array[0] + calc_array[1] + calc_array[2]
print(total_score)



