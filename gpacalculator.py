import time, os
from tkinter import *
from gpafunctions import gradepoint


# Defining the root widget (window) and giving it a title and a set of dimensions
root = Tk()
root.title("GPA Calculator")
root.geometry("500x500")

# Prepping three input fields and the values that correspond
letter_grade = StringVar()
letter_grade.set("Letter Grade")

course = StringVar()
course.set("Course Name")

level = StringVar()
level.set("Course Level")

# Creating list "buckets" for user's data
courses = []
grades = []
levels = []

labels = []

# Clearing any lingering transcripts
if os.path.exists("transcript.txt"):
        os.remove("transcript.txt")


def add_course():
    try: # Trying to send the user's letter grade and course level to gradepoint to be calculated... (l. 64)
        number_grade = gradepoint(letter_grade.get(), level.get())

        # Adding user's values to data "buckets"
        grades.append(number_grade)
        courses.append(course.get())
        levels.append(level.get())

        # Resetting to default values for our entries
        letter_grade.set("Letter Grade")
        course.set("Course Name")
        level.set("Course Level")

        for x in range(len(courses)):  # For every course in all our courses,
            if levels[x] == "Course Level":  # Just sweeping the default input into our preferred "Standard" input
                levels[x] = "Standard"
            if grades[x] is not None:  # Data validation! Making sure we actually have a grade to print. If not...
                coursetext = f"{levels[x]}: {courses[x]} | {grades[x]}"
                courselabel = Label(root, text=coursetext)
                courselabel.grid(row=x+1)
            else:  
                # ... then we create and place an error message
                errorlabel = Label(root, text="Error! Please enter a grade.")
                errorlabel.grid(row=x+1)

                time.sleep(3) # Error message on screen for three seconds
                errorlabel.destroy() # Error message destroyed

        labels.append(courselabel) # Adding the label w/ course information to the list of labels we have
        calc_button.grid(row=50, column=2)  # Grids the Calc GPA Button only after a course has been added

    # ...but if they don't work, we send an error to the terminal.
    except:
        print("Error! Please enter a grade.")
    
        # Resetting default values
        letter_grade.set("Letter Grade")
        course.set("Course Name")
        level.set("Course Level")

def calc():
    gpa = sum(grades)/len(grades) # GPA = the sum of all the gradepoints / how many grades there are

    # Creating and placing a label with the GPA
    gpa_label = Label(root, text="GPA: " + str(round(gpa, 2))) # Bonus tip: round() is a built-in, rounds our GPA to two decimal points
    gpa_label.grid(row=1, column=1) 

    labels.append(gpa_label) # Adds the GPA label to the list of all the labels we have

    # Disables the Calc GPA button and Add Course Buttons
    calc_button["state"] = "disabled"
    add_button["state"] = "disabled"

    print_button.grid(row=51, column=1) # Places the Print Transcript button only after there is a GPA to print


def print_transcript():
    # Creates a transcript.txt file if it doesn't exist
    transcript = open("transcript.txt", "w")
    # For every label, writing its text to the transcript.txt file
    for label in labels:
        transcript.writelines((label.cget("text") + "\n"))
    transcript.close() # Closing the transcript file afterwards #bestpractices
    print_button["state"] = "disabled" # Disabling the print_button after use


def reset():
    # Removing all labels on screen
    for label in labels:
        label.destroy()
    
    # Emptying courses, grades, and levels lists
    courses.clear()
    grades.clear()
    levels.clear()
    
    # Setting all button states back to normal
    calc_button["state"] = "normal"
    add_button["state"] = "normal"
    print_button["state"] = "normal"

    # If we have an existing transcript, deleting it
    if os.path.exists("transcript.txt"):
        os.remove("transcript.txt")
    

# Creating and placing a course entry field
course_entry = Entry(root, textvariable=course, width=20, borderwidth=1)
course_entry.grid(row=0, column=0)

# Creating and placing a grade entry dropdown
grade_options = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
grade_dropdown = OptionMenu(root, letter_grade, *grade_options)
grade_dropdown.grid(row=0, column=1)

# Creating and placing a course level dropdown
level_options = ["Standard", "AP", "IB", "Honors"]
level_dropdown = OptionMenu(root, level, *level_options)
level_dropdown.grid(row=0, column=2)

# Creating and placing an add course button
add_button = Button(root, text="Add Course", command=add_course)
add_button.grid(row=50, column=0)

# Creating buttons to calculate GPA and print results to transcript
calc_button = Button(root, text="Calculate GPA", command=calc)
print_button = Button(root, text="Write to Transcript", command=print_transcript)

# Creating and a clear all fields button
clear_button = Button(root, text="Clear", command=reset)
clear_button.grid(row=50, column=1)

root.mainloop()
