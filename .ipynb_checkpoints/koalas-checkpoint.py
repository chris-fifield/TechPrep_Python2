# Functions for processing student data.

# return a letter ranking based on a given student grade.
def getLetterGrade(grade):
        
    if grade >= 90: # Final grade equal to or greater than 90 is an "A+"
        return("A+")
    
    if grade >=80: # Final grade equal to or greater than 80 is an "A"
        return("A")

    if grade >=70: # Final grade equal to or greater than 70 is a "B"
        return("B")
    
    if grade >=60: # Final grade equal to or greater than 60 is a "C"
        return("C")
    
    if grade > 55: # Final grade greater than 55 is a "D"
        return("D")
    else:
        return("F") # Final grade less than or equal to 55 is an "F"