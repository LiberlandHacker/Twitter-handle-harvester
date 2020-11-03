# By Jonathan McCormick, Jr.
# Updated September 30, 2020

# Copy and paste text to be filtered
text = input("""
Copy and paste text here and
I will remove everything
that does NOT start with '@',
leaving you with only the
Twitter handles.

INPUT TEXT HERE --> """)

# Here is the list of all words from the text that begin with "@"
print("""
Here are your results:
  """)

for i in text.split():
    if i.startswith("@"):
        print(i)
