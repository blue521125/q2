'''
#06 Philip Excalibur P. Fullante
Computer Science 3 - Q2
October 16, 2026 Friday
'''
class Publication:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def get_title(self):
        print("Title:",self.title)
        
    def get_author(self):
        print("Author:",self.author)
        
    def set_title(self,title):
        self.title = title
        
    def set_author(self,author):
        self.author = author
        
    def display_info(self):
        self.get_title()
        self.get_author()


class Book(Publication):
    def __init__(self,title,author,number_pages):
        super().__init__(title,author)
        self.number_pages = number_pages
        
    def get_number_of_pages(self):
        print("Number of Pages:",self.number_pages)
        
    def display_info(self):
        self.get_title()
        self.get_author()
        self.get_number_of_pages()
    
    def set_number_of_pages(self,number_pages):
        if number_pages <= 0:
            print('Number of pages must be positive.')
        else:
            self.number_pages = number_pages


class Magazine(Publication):
    def __init__(self,title,author,issue_number):
        super().__init__(title,author)
        self.issue_number = issue_number
    
    def get_issue_number(self):
        print("Issue Number:",self.issue_number)
    
    def display_info(self):
        self.get_title()
        self.get_author()
        self.get_issue_number()
    
    def set_issue_number(self,issue_number):
        if issue_number <= 0:
            print('Issue number must be positive.')
        else:
            self.issue_number = issue_number


pub1 = Publication("How to be stupid","Stupidy Stupington")
boo1 = Book("Become the best minecrafter!!11!","Noob1234",645)
mag1 = Magazine("Hottest Teens Ever?!","New Jersey Times",3751903)

print("Publishing Information:")
pub1.set_title("I am Stupid")
pub1.display_info()

print("\nBook Information:")
boo1.set_number_of_pages(-343)
boo1.display_info()

print("\nMagazine Information:")
mag1.set_issue_number(4870932)
mag1.display_info()
