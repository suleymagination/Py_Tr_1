# This code counts the number of books that have been read using a while loop.
# In each iteration of the loop, the value of book is incremented by 1
# and a message is printed to indicate that another book has been read.
# The final message displays the total number of books that have been read.
Number_of_Books = 10
book = 0
print("""Mother said: "Read all your books!" """)

while book < Number_of_Books:
    book += 1
    print(f"Book number {book} has been read")

print(f"Number of books I have read = {book}")
