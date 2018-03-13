# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!
scores = [95, 10, 83, 95, 55, 74, 65]

def grades(scores):
    for int in scores:
        if int >= 90:
            print "Score: {}; Your grade is A".format(int)
        elif int >= 80:
            print "Score: {}; Your grade is B".format(int)
        elif int >= 70:
            print "Score: {}; Your grade is C".format(int)
        elif int >= 60:
            print "Score: {}; Your grade is D".format(int)
        elif int < 60:
            print "Score: {}; Your grade is F".format(int) 

grades(scores)