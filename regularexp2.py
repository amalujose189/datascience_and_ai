''''3️⃣ Special Sequences
6. \d

👉 Matches digits (0–9)

7. \D

👉 Matches non-digits

8. \w

👉 Matches letters, digits, underscore

9. \W

👉 Matches non-word characters

10. \s

👉 Matches whitespace (space, tab)

11. \S

👉 Matches non-whitespace

Example:

re.findall("\d+", "My number is 12345")
🔹 4️⃣ Quantifiers (Repetition)
12. *

👉 0 or more times

13. +

👉 1 or more times

14. ?

👉 0 or 1 time

15. {n}

👉 Exactly n times

16. {n,}

👉 n or more times

17. {n,m}

👉 Between n and m times

Example:

print(re.findall("a+", "aaabaaa"))
#🔹 5️⃣ Grouping & Alternation
18. ()

👉 Groups pattern
'''
import re
print(re.search("(\\d+)-(\\d+)", "123-456"))
'''19. |

👉 OR operator

re.findall("cat|dog", "cat dog cow")
🔹 6️⃣ Escape Character
20. \

👉 Used to escape special characters

Example:
To match a dot . literally:

re.findall("\\.", "file.txt")

Better way (raw string):

re.findall(r"\.", "file.txt")
🔥 Most Important Metacharacters for Interviews
.  ^  $  *  +  ?  []  {}  ()  |  \d  \w  \s'''

