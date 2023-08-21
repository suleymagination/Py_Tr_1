daftar_buku = ['Seven Habits', 'How to Influence People', 'Black Swan']
for buku in daftar_buku:
    print(f'\n{buku}')

print('\nPrint dengan indexing:')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah "del" dengan list comprehension:')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Black Swan']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah "del" dengan list comprehension start-stop:')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Black Swan']
del daftar_buku[0:2] # menghapus: 'Seven Habits', 'How to Influence People'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah "del" dengan list comprehension start-stop dari arah kebalikan:')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Black Swan']
del daftar_buku[0:-1] # Start : End
# menghapus: 'Seven Habits', 'How to Influence People', dan menyisakan 'Black Swan'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah "del" dengan list comprehension start-stop dengan step:')
book_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen']
del book_list[1::2] # Start : End : Step
# The `del` statement is used to delete elements from a list based on their index.
# `del book_list[1::2]` will delete every second element in the list starting from index 1 (the second element in the list).
# The elements that will be deleted are: 'Two', 'Four', 'Six', 'Eight', 'Ten', 'Twelve' and 'Fourteen'.
# The resulting list will be: `['One', 'Three', 'Five', 'Seven', 'Nine', 'Eleven', 'Thirteen']`.
for i in range(0, len(book_list)):
    print(book_list[i])

# List comprehension ini dapat digunakan untuk membuat list baru dari list yang sudah ada:
print('\nMembuat list baru dengan list comprehension start-stop dengan step:')
book_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen']
print('\nList of books with even numbers:')
even_book_list = book_list[1::2]
for i in range(0, len(even_book_list)):
    print(even_book_list[i])

book_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen']
print('\nList of books with odd numbers:')
odd_book_list = book_list[0::2]
for i in range(0, len(odd_book_list)):
    print(odd_book_list[i])
