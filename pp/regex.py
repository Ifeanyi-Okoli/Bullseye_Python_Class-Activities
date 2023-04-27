"""
[abc] >>> this is simply matching the characters a, b, or c.

[^abc] >>> this is matching any character except a, b, or c.

[a - z] >>> this is matching any character between a and z, including a and z.

[a - zA - Z] >>> this is matching any character between a and z, or A and Z.

[^a - zA - Z] >>> this is matching any character except between a and z, or A and Z.

[0 - 9] >>> this is matching any digit between 0 and 9.

[^0 - 9] >>> this is matching any character except between 0 and 9.

[0 - 9a - zA - Z] >>> this is matching any character between 0 and 9, or a and z, or A and Z.

[0 - 9a - zA - Z_] >>> this is matching any character between 0 and 9, or a and z, or A and Z, or _. (underscore)

[0 - 9a - zA - Z_@] >>> this is matching any character between 0 and 9, or a and z, or A and Z, or _, or @.

#=========REGEX QUANTIFIERS====================

[ ]? >>> this is matching 0 or 1 occurrence of the pattern to its left.

[ ]* >>> this is matching 0 or more occurrences of the pattern to its left.

[ ]+ >>> this is matching 1 or more occurrences of the pattern to its left.

[ ]{ n } >>> this is matching exactly n number of occurrences of the pattern to its left.

[ ]{ n, } >>> this is matching at least n occurrences of the pattern to its left.

[ ]{ n, m } >>> this is matching at least n and at most m occurrences of the pattern to its left.

#===============REGEX METACHARACTERS================

\d >>> this is matching any decimal digit. This is equivalent to the set class [0-9].

\D >>> this is matching any non-digit character. This is equivalent to the set class [^0-9].

\w >>> this is matching any alphanumeric character. This is equivalent to the set class [a-zA-Z0-9_].
\W >>> this is matching any non-alphanumeric character. This is equivalent to the set class [^a-zA-Z0-9_].

\ s >>> this is matching any whitespace character. This is equivalent to the set class [ \t\n\r\f\v].

\ >>> tells the computer to treat the following characters as search pattern.
"""

#task checking that a mobile number starts with either 8 or 9 and is 10 digits long

val = [89][0-9]{9}


#First character uppercase, contains only letters, and only 1 digit is allowed in the middle

[A-Z][a-z]*[0-9][a-z]*

#email
#[a-zA-Z0-9_\.\-] >>> handles the first part of the email address before the @ symbol. It should contain alphanumeric characters, underscores, dots, and hyphens. Because dot and hyphens are special characters in regex, we use \ to escape them and make the computer to see them as search literals instead of special characters.
#+ >>> tells the computer to match one or more occurrences of the pattern to its left. Meaning it can repeat the pattern as many times as possible.
#@ >>> matches the @ symbol.
#[a-z]+ >>> matches one or more occurrences of the pattern to its left. Meaning it can repeat the pattern as many times as possible. This is for the part that comes after the @ symbol.
# [\.] >>> matches the dot symbol.
# [a-z]{2,3} >>> matches 2 to 3 occurrences of the pattern to its left. Meaning it can repeat the pattern 2 to 3 times. This is for the last part of the email address.
[a-zA-Z0-9_\.\-]+@[a-z]+\.[a-z]{2,3} 

[a-zA-Z0-9_\.\-]+[@][a-z]+[\.][a-z]{2,3}