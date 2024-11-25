# Exercise_Lecture_171
            # #So here a Simple rule is followed for basic mathematical operations
            # P – Parentheses
            # E – Exponentiation
            # M – Multiplication (Multiplication and division have the same precedence)
            # D – Division
            # A – Addition (Addition and subtraction have the same precedence)
            # S – Subtraction
            # print((5 + 4) * 10 / 2) #45
            # print(((5 + 4) * 10) / 2) #45
            # print((5 + 4) * (10 / 2)) #45
            # print(5 + (4 * 10) / 2) #25
            # print(5 + 4 * 10 // 2) #25

# Exercise_Lecture_187
            #Print username and protected password with its length
            # username=input("Enter your Username: ");
            # password=input('Enter your password: ');
            # password_length=len(password);
            # Protected_Pass=(password_length*'*')
            # print(f"Hi {username}, your password is {Protected_Pass} and its length is {password_length} ")

# Exercise_Lecture_189
            #What is the output of this code?
            #Before you clikc RUN, guess the output of each print statement!
                        # new_list = ['a', 'b', 'c']
                        # print(new_list[1])
                        # print(new_list[-2])
                        # print(new_list[1:3])
                        # new_list[0] = 'z'
                        # print(new_list)           # b
                                                    # b
                                                    # ['b', 'c']
                                                    # ['z', 'b', 'c']

                        # my_list = [1,2,3]
                        # bonus = my_list + [5]
                        # my_list[0] = 'z'
                        # print(my_list)
                        # print(bonus)              # ['z', 2, 3]
                                                    # [1, 2, 3, 5]

# Exercise_Lecture_190
            #1) using this list: 
            #   basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
            #   # access "Oranges" and print it:
            #   print(basket[1][1][0])

# Exercise_Lecture_192
            # Exercise List Methods
            # basket = ["Banana", "Apples", "Oranges", "Blueberries"]
            # # 1. Remove the Banana from the list
            # basket.remove('Banana')
            # # 2. Remove "Blueberries" from the list.
            # basket.remove('Blueberries')
            # # 3. Put "Kiwi" at the end of the list.
            # basket.append('Kiwi')
            # # 4. Add "Apples" at the beginning of the list
            # basket.insert(0, 'Apples')
            # # 5. Count how many apples in the basket
            # basket.count('Apples')
            # # 6. empty the basket
            # basket.clear()
            # print(basket)

# Exercise_Lecture_194
            #fix this code so that it prints a sorted list of all of our friends (alphabetical)
            # friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
            # new_friend = ['Stanley']
            # friends.extend(new_friend)
            # print(sorted(friends))

# Exercise_Lecture_213

            # is_magician = False
            # is_expert = True
            # if is_expert and is_magician:
            #   print('you are a master magician') #magician and expert
            # elif is_magician and not is_expert:
            #   print('you are getting there')     #magician but not expert
            # elif not is_magician:
            #   print('you are not a magician')    #not magician

# Exercise_Lecture_217

            # #make a counter using loop that will give us the output by adding the list items 
            # my_list = [1,2,3,4,5,6,7,8,9,10]
            # counter = 0
            # for item in my_list:
            #   counter = counter + item
            # print(counter)


# Exercise_Lecture_223
            # picture = [
            #   [0,0,0,1,0,0,0],
            #   [0,0,1,1,1,0,0],
            #   [0,1,1,1,1,1,0],
            #   [1,1,1,1,1,1,1],
            #   [0,0,0,1,0,0,0],
            #   [0,0,0,1,0,0,0]
            # ]
            # for row in picture:
            #   for pixel in row:
            #     if (pixel == 1 ):
            #       print('"*"',end='')
            #     else:
            #       print(' ',end='')
            #   print('')

# Exercise_Lecture_225
            # check for duplicates in the list
            # some_list = ['a','b','c','d','b','m','m','n']
            # duplicates = []
            # for value in some_list: 
            #   if some_list.count(value)>1:
            #     if value not in duplicates:
            #       duplicates.append(value)
            # print(duplicates)

# Exercise_Lecture_232
          #clean code
          # def is_even(num):
          #   return num % 2 == 0
          # print(is_even(21))