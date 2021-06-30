import sys
 
# class definitions here




class Record:
    """Represent a record."""
    def __init__(self, ...):
        # 1. Define the formal parameters so that a Record can be instantiated
        #    by calling Record('meal', 'breakfast', -50).
        # 2. Initialize the attributes from the parameters. The attribute
        #    names should start with an underscore (e.g. self._amount)
 
    # Define getter methods for each attribute with @property decorator.
    # Example usage:
    # >>> record = Record('meal', 'breakfast', -50)
    # >>> record.amount
    # -50
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        # 1. Read from 'records.txt' or prompt for initial amount of money.
        # 2. Initialize the attributes (self._records and self._initial_money)
        #    from the file or user input.
 
    def add(self, record, category):
        
        # 2. Convert the string into a Record instance.
        # 3. Check if the category is valid. For this step, the predefined
        #    categories have to be passed in through the parameter.
        # 4. Add the Record into self._records if the category is valid.
 
    def view(self):
        # 1. Print all the records and report the balance.
 
    def delete(self, ...):
        # 1. Define the formal parameter.
        # 2. Delete the specified record from self._records.
 
    def find(self, ...):
        # 1. Define the formal parameter to accept a non-nested list
        #    (returned from find_subcategories)
        # 2. Print the records whose category is in the list passed in
        #    and report the total amount of money of the listed records.
 
    def save(self):
        # 1. Write the initial money and all the records to 'records.txt'.
class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        # 1. Initialize self._categories as a nested list.
 
    def view(self, ...):
        # 1. Define the formal parameters so that this method
        #    can be called recursively.
        # 2. Recursively print the categories with indentation.
        # 3. Alternatively, define an inner function to do the recursion.
 
    def is_category_valid(self, ...):
        # 1. Define the formal parameters so that a category name can be
        #    passed in and the method can be called recursively.
        # 2. Recursively check if the category name is in self._categories.
        # 3. Alternatively, define an inner function to do the recursion.
 
    def find_subcategories(self, ...):
        # 1. Define the formal parameters so that a category name can be
        #    passed in and the method can be called recursively.
        # 2. Recursively find the target category and call the
        #    self._flatten method to get the subcategories into a flat list.
        # 3. Alternatively, define an inner function to do the recursion.
 
    def _flatten(self, ...):
        # 1. Define the formal parameters so that this method
        #    can be called recursively.
        # 2. Recursively call self._flatten and return the flat list.
        # 3. (FYI) The method name starts with an underscore to indicate that
        #    it is not intended to be called outside the class.
        # 4. Alternatively, put flatten as an inner function of
        #    find_subcategories.

 
categories = Categories()
records = Records()
 
while True:
    command = input('\nWhat do you want to do (add / ...)? ')
    if command == 'add':
        record = input('Add an expense or income record with ...:\n')
        records.add(record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)
    elif command == 'view categories':
        categories.view()
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')
