input_text = input() #input text from the user

#to get the number of letters in the input
letters = 0 
for i in range(len(input_text)):
   if(input_text[i].isalnum()):
       letters += 1

length = len(input_text.split()) #splits the tex input into a list and gets it length
string = str(length) #converts to string
words = int(string) #converts to integer and stores in the words variable

#splits the tex input into a list w/ period and gets it length
period = len(input_text.split("."))

#function to determine a sentence
def sentence(string):
   s_count = 0
   end = False
   s_end = {'?', '!', '.'} #end symbols
   for c in string:
       if c in s_end:
           if not end:
               end = True
               s_count += 1
           continue
       end = False
   return s_count #return the sentence count

#perform the function call
sentences = sentence(input_text) 

L = letters / words * 100 #average number of letters per 100 words in the text
S = sentences / words * 100 #average number of sentences per 100 words in the text

coleman_liau = 0.0588 * L - 0.296 * S - 15.8 #Coleman-Liau's Formula
computed = round(coleman_liau) #rounded to the nearest integer

#if else statement on the computed value and result
if computed < 1:
   result = "Before Grade 1"
elif computed == 1:
   result = "Grade 1"
elif computed == 2:
   result = "Grade 2"
elif computed == 3:
   result = "Grade 3"
elif computed == 4:
   result = "Grade 4"
elif computed == 5:
   result = "Grade 5"
elif computed == 6:
   result = "Grade 6"
elif computed == 7:
   result = "Grade 7"
elif computed == 8:
   result = "Grade 8"
elif computed == 9:
   result = "Grade 9"
elif computed == 10:
   result = "Grade 10"
elif computed == 11:
   result = "Grade 11"
elif computed == 12:
   result = "Grade 12"
elif computed == 13:
   result = "Grade 13"
elif computed == 14:
   result = "Grade 14"
elif computed == 15:
   result = "Grade 15"
elif computed >= 16:
   result = "Grade 16+"

print(result) #print the result corresponding to the computed value

