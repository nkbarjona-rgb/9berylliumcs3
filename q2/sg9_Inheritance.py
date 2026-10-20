class Publication:
  def __init__(self, title, author):
        self.title = title
        self.author = author

  def get_title(self):
    return self.title

  def get_author(self):
    return self.author

  def set_title(self, title):
    self.title = title
  
  def setAuthor(self, author):
    self.author = author

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")

class Book(Publication):
  def __init__(self, title, author, Numberofpages):
    self.Numberofpages = (Numberofpages)
    self.title = title
    self.author = author

  def getNumberofpages(self):
    return f"Number of pages: {self.Numberofpages}"

  def setNumberofpages(self, Numberofpages):
    if Numberofpages >= 0: 
      self.Numberofpages = Numberofpages
    else: 
      print(f'Warning! Pages cannot be zero or negative.')

class Magazine(Publication):
  def __init__(self, title, author, Issue_Number):
    self.Issue_Number = Issue_Number
    self.title = title
    self.author = author

  def getIssue_Number(self):
    return f"Issue Number: {self.Issue_Number}"

  def setIssue_Number(self, Issue_Number):
    return self.int(Issue_Number)
    if Issue_number >= 0: 
      self.Numberofpages = Numberofpages
    else: 
      print(f'Number of pages must be positive.')

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


