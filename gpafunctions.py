def gradepoint(letter, level): # Defining a gradepoint function which takes course level and letter grade 
    grade_dict = { # Defining a dictionary of letter-gradepoint pairings
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,   
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.7,
    }

    gp = (grade_dict.get(letter)) # Setting the gradepoint equal to the dictionary value that corresponds to the user's given letter grade

    if level == ("Course Level" or "Standard"): # If the default text was not changed or the user selected Standard, add no grade bumps
        pass
    elif level == "Honors": # Adding 0.5 grade bump for Honors
        gp = gp + 0.5
    elif level == "AP": # Adding 1.0 grade bump for AP class
        gp = gp + 1.0
    elif level == "IB": # Adding 1.0 grade bump for IB class
        gp = gp + 1.0
    return gp  # Returning the final gradepoint for use
