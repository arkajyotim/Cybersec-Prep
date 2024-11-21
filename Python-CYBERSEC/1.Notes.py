                                          #Fundamental Data types

# int | float | complex | str | bool | list | dict | tuple | set 

#1) int
# int -> integer . Basic mathemetical operations can easily be performed
        #print (type(1+2));        <------------- int type class
        #print (1-2);
        #print (1*2);

#2) float -> float type class 
        #print (1/2);             <------------  float data type = any kind of deciaml output (more memory)

#3) complex -> mostly used in complex mathematical calculations (x+yi)

#4) string  -> string type . It is used to store textual data
                #print(type('Hello, world')); 
                #username = "something";
                #password = "something";
                #long_string="""
                #This is a multi-line string.
                #It can span multiple lines.
                #This is useful for writing long texts.
                #""";
                #print(long_string)
        # string concatination
               #print("rexon"+ " " +'yt')
        # formatted string
                #name="jhonny"
                #age=55;
                #print(f'hi {name} your age is {age}')
        # string indexes
                # selfish = '01234567';
                #            01234567
                # [start:stop:stepover]
                # print(selfish[0:8:2])
                # print(selfish[::-1]) ------> used to Reverse a String <--------
                # selfish[0]=8         ------> strings are immutable and cannot be updated/ Only memory override is possible


# 5)Boolean --> gives 0->false and 1->true
                 #print(bool(0))
         
# 6)Lists
        #Lists are mutable/changable unlike strings
                # BookList=['Harry Potter','Shakespeare']
                # print(BookList[0])
        #List Slicing:-
                # amazon_cart=['cake','biscuit','chips','snacks']
                # print(amazon_cart.[0:4])
        #list methods -> append,extend,clear,pop,insert,index,count,sort,reverse,sorted etc.
                # basket=['a','b','c','d','f','e']
                # # basket.sort();
                # # print(basket)
        #List Range
                #print(list(range(1,100)))
        #List to string conversion
                # new_sentence = " ".join(['hi','my','name','is','rexon'])
                # print(new_sentence)


# 7)Dictionary --> unordered key value pair
                # dictionary = {
                # 'a':1,
                # 'b':2,
                # 'c':3,
                # }
                # print(dictionary["a"])
        #Immutable dict values
                # user={
                #         'basket':[1,2,3],
                #         'greet':'hello',
                #         'age':20
                # }
                # print(user.get('age',55))   -----> will print age as 20 and 55 will not be overrided as dict is immutable
        #Dictionary methods: keys,values,items,clear,copy,pop,popitem,update


# 8)Tuple ----> immutable lists
                # my_tuple = (1,2,3,4,5);
                # print(my_tuple[2])
        #methods
                # hi_tuple=(1,2,3,4,5);
                # print(hi_tuple.index(2))
                # print(hi_tuple.count(2))

# 9) Sets -----> no duplicates ,immutable 

                # my_set={1,2,3,4,5,6}
                # your_set={5,6,7,8,9,10}

                #print(my_set.difference(your_set)) ---> intersection of set
                #print(my_set.discard(5)) ---> remove 5 from my_set
        #some other methods are :- .difference.update(),.intersection(),.isdisjoint(),.issubset(),.issuperset,.union()

#-----------------------------------------------------------------------------------------------------------------------------

# Math Functions

#print(round(2.6)) -> Round off to the closest integer
#print(abs(-100)) -> prints absolute values/no negative numbers


#-----------------------------------------------------------------------------------------------------------------------------

# Operator Precedence

#Also called operator priority , it follows the rule "PEMDAS"
# P – Parentheses
# E – Exponentiation
# M – Multiplication (Multiplication and division have the same precedence)
# D – Division
# A – Addition (Addition and subtraction have the same precedence)
# S – Subtraction

#-----------------------------------------------------------------------------------------------------------------------------

# MISC Information

#Note: Variables are in snake_case(all lower case with _ )
#Variable
# user_IQ = 29
# print(user_IQ)
# PI = 3.14 #Unchanging value 
# a,b,c = 1,2,3

#Binary Convertion
#print(bin(5))               #prints binary output in the form of 0b____
#print(int("0b101",2))       #the binary will be stored in memory and 2 is represented as base2 which is binary

# Statement vs Expressions
                  # iq=100  -> Statement 
                  # user_Age = iq/4 -> Expression 

#Augmented assignment operator
                  # some_value = 5;
                  # some_value += 2
                  # print(some_value)

#Escape sequence
                   #weather= "It's a \"sunny\" Day Isn't it "  <------- whatever is in between \\ is considered a string
                   #print(weather)

#Built in Functions + Methods
                  # quote='Hi there good evening'
                  # print(quote.upper())                        <------ this will print uppercase 


#Type-Conversion
                  # birth_year=input('what year were you born: ')
                  # age = 2024 - int (birth_year)
                  # print(f'your age is : {age}' )

#---------------------------------------------------------------------------------------------------------------------------------

#Logical Operators


        # if else elif :- 
                #Liscence to drive at proper age:-
                # is_old=True;
                # is_liscenced=True;

                # if is_old and is_liscenced:
                #         print('you are old and you have liscence to drive');
                # else:
                #         print('not allowed')
        # NOTE: Also here in if else statements if you enter any other value other than boolean it will automatically be converted into bool

        #Logical operators ---> < > == != <= >= and or not

        #Ternary operator (conditonal expression):-
                # is_friend=False
                # can_message='message allowed' if is_friend else 'not allowed to message'
                # print(can_message)


#LOOPS

                # for item in (1,2,3,4,5):
                #        for x in ['a','b','c']:  
                #         print(1,'c')
        
        # iterables:-
                # user={
                #         'name': 'golem',
                #         'age':5000,
                #         'can_swim':False
                # }
                # for key,value in user.items():      //key,value here is to unpack tuple dictionary
                #         print(key,value)
                # for item in user.values():
                #         print(item)
                # for item in user.keys():
                #         print(item)