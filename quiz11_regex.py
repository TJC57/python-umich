#Quiz Regular Expressions

#1 - Which of the following regular expressions would extract 'uct.ac.za' from this string using re.findall?
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#Finds results where start with @ and matches any non-whitespace character one or more times.
result = re.findall('@(\S+)', line)

#2 - Which of the following is the way we match the "start of line" in a regular expression?
#^

#3 - What would the following mean in a regular expression? [a-z0-9]
# Match a lowercase letter or a digit

#4 - What is the type of the return value of the re.findall() method?
# A list of strings

#5 - What is the 'wild card' character in a regular expression (character that matches any character)?
# . since it matches any character, but * repeats the character 0 or more times.

#6 - What is the difference between the + and * character in regular expressions?
# The + matches at least 1 character and the * matches 0 or more.

#7 - What does the [0-9]+ match in regular expression?
# One or more digits

#8 - What does the following Python sequence print out?
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y
# ['From: Using the :'] because this search is greedy.

#9 - What character do you add to the + or * to indicate that the match is to be done in a non-greedy manner?
# ?

#10 - Given the following text: "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008", what would regular expression '\S+?@\S+' match?
# stephen.marquard@uct.ac.za
