class Publication:
  def __init__(self, title, author):
        self.title = title
        self.author = author

  def getTitle(self):
    return self.getTitle

  def getAuthor(self):
    return self.getAuthor

  def setTitle(self, title):
    return self.setTitle
  
  def setAuthor(self, author):
    return self.setAuthor

  def display_Info(self):
    return self.display_Info

class Book(Publication):
  def __init__(self, title, author, Numberofpages):
    self.Numberofpages = (Numberofpages)

  def getNumberofpages(self):
    return self.Numberofpages

  def setNumberofpages(self, Numberofpages):
    return self.Numberofpages
    if Numberofpages >= 0: 
      self.Numberofpages = Numberofpages
    else: 
      print(f'Warning! Pages cannot be zero or negative.')

class Magazine(Publication):
  def __init__(self, title, author, Issue_Number):
    self.Issue_Number = Issue_Number

  def getIssue_Number(self):
    return self.Issue_Number

  def setIssue_Number(self, Issue_Number):
    return self.int(Issue_Number)
    if Issue_number >= 0: 
      self.Numberofpages = Numberofpages
    else: 
      print(f'Warning! Issue Number cannot be zero or negative.')

#hi
PUB1 = Publication("Journal of Exp Psych9ology", "Author")
Book1 = Book("Title", "Author", 202)
Mgasin1 = Magazine("Title","Authors", 67)

print("\nPublication Information")
PUB1.display_Info()

print("\nBook Information")
Book1.setNumberofpages(-670)  
Book1.display_Info()
print(Book1.getNumberofpages())

print("\nMagazine Information")
Mgasin1.display_Info()
print(Mgasin1.getIssue_Number())


