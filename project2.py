# Initializing dictionary
book = {}

# Add a book
def add_book(name, author):
    book[name] = author
    print(f'Added {name} with a author name {author}')

# Update a book
def update_book(name, author):
    if name in book:
        book[name] = author
        print(f'{name}\'s author name have been updated to {author}')
    else:
        print(f'{name} is not found!')

# Delete a book
def delete_book(name):
    if name in book:
        del book[name]
        print(f'{name} has been successfully deleted')
    else:
        print(f'{name} is not found!')

# View all books
def display_all_book():
    if book:
        for name, author in book.items():
            print(f'{name} : {author}')
    else:
        print('No books found/added')

# Main function
def main():
    while True:
        print('\nBook Management System')
        print('1. Add Book')
        print('2. Update Book')
        print('3. Delete Book')
        print('4. display Book')
        print('5. Exit')

        choice = int(input('Enter your choice: '))
        
        if choice == 1:
            name = input('Enter Book name: ')
            author = input('Enter author name: ')
            add_book(name, author)
        
        elif choice == 2:
            name = input('Enter Book name: ')
            author = input('Enter author name: ')
            update_book(name, author)
        
        elif choice == 3:
            name = input('Enter Book name: ')
            delete_book(name)
        
        elif choice == 4:
            display_all_book()
        
        elif choice == 5:
            print('Close the program')
            break
        
        else:
            print('Invalid choice. Please try again.')

# Run the main function
main()