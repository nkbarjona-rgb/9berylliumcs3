# creates a class nameed publication, then initializes self, title and author attributes
class Publication: 
  def __init__(self, title, author):
        self.title = title 
        self.author = author 
    
# gets title name
  def get_title(self):
    return self.title  
    
# gets author name
  def get_author(self):
    return self.author
    
# sets up title name  
  def set_title(self, title):
    self.title = title
    
# sets authors name
  def setAuthor(self, author):
    self.author = author
    
# used to display info properly later on
  def display_info(self):
    print(f"Title: {self.title}") # to fix format for later printing
    print(f"Author: {self.author}") # to fix format for later printing
    
# creates a subclass Book within publication, initializes self title author, and adds number of pages
class Book(Publication):
  def __init__(self, title, author, Numberofpages):
    self.Numberofpages = (Numberofpages)
    self.title = title # to fix format for later 
    self.author = author # to fix format later
    
# gets number of pages
  def getNumberofpages(self):
    return f"Number of pages: {self.Numberofpages}" # to fix format for later printing
    
# gets number of pages
  def setNumberofpages(self, Numberofpages):
    if Numberofpages >= 0: # checks if number of pages is negative or zero 
      self.Numberofpages = Numberofpages
    else: 
      print(f'Warning! Pages cannot be zero or negative.')

# creates subclass magazine within publication. then initializes self, title, author, and adds issue number
class Magazine(Publication):
  def __init__(self, title, author, Issue_Number):
    self.Issue_Number = Issue_Number # to fix format for printing later 
    self.title = title  # to fix format for printing later 
    self.author = author  # to fix format for printing later 
# gets issue number
  def getIssue_Number(self):
    return f"Issue Number: {self.Issue_Number}"  # to fix format for printing later 
# gets issue number 
  def setIssue_Number(self, Issue_Number):
    return self.int(Issue_Number)
    if Issue_number >= 0: # checks if issue number is positive, negative or zero
      self.Issue_Number = Issue_Number
    else: 
      print(f'Issue Number must be positive')

#hi
PUB1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H. ")
Book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
Mgasin1 = Magazine("National Geographic","Various Authors", 202)

print("Publication Information")
PUB1.display_info()

print("\nBook Information")
Book1.setNumberofpages(-670)  
Book1.display_info()
print(Book1.getNumberofpages())

print("\nMagazine Information")
Mgasin1.display_info()
print(Mgasin1.getIssue_Number())


