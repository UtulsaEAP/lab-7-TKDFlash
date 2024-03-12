"""
Sean Killian
Thursday @ 2pm
"""

def courseGrade():

     # TODO: Declare any necessary variables here.
    midterm_1_tot = 0
    midterm_2_tot = 0
    midterm_3_tot = 0

    student_grade = [] 
    # TODO: Read a file name from the user and read the tsv file here.

    input_file = input()
    try:
        with open(input_file, 'r') as file:
            for line in file:
                # split the name and exams up
                last_name, first_name, midterm_1, midterm_2, midterm_3 = line.strip().split()
 
                #make grades into ints
                midterm_1 = int(midterm_1)
                midterm_2 = int(midterm_2)
                midterm_3 = int(midterm_3)
               
                #get avg and letter grade
                average = (midterm_1 + midterm_2 + midterm_3)/3
                if average >= 90:
                    letter_grade = 'A'
                elif 80 <= average < 90:
                    letter_grade = 'B'
                elif 70 <= average < 80:
                    letter_grade = 'C'
                elif 60 <= average < 70:
                    letter_grade = 'D'
                else:
                    letter_grade = 'F'
                student_grade.append((last_name, first_name, midterm_1, midterm_2, midterm_3, letter_grade))

                #add to total class test totals
                midterm_1_tot += midterm_1
                midterm_2_tot += midterm_2
                midterm_3_tot += midterm_3
    except:
        print('File not found')
        return

    #get class average per exam
    number_of_students = len(student_grade)
    avg_midterm_1 = midterm_1_tot / number_of_students
    avg_midterm_2 = midterm_2_tot / number_of_students
    avg_midterm_3 = midterm_3_tot / number_of_students

    # TODO: Compute student grades and exam averages, then output results to a text file here.

    #name based on which TSV file
    if  input_file == "./Problem 3/StudentInfo.tsv":
        output_file = "./report.txt"
    elif input_file == "./Problem 3/StudentInfo1.tsv":
        output_file = "./report1.txt"
    else:
        output_file = "./report2.txt"

    #actual ouput    
    with open(output_file, 'w') as output_file:
        for student in student_grade:
            output_file.write('\t'.join(map(str, student)) + '\n')

        output_file.write(f'\nAverages: midterm1{avg_midterm_1: .2f}, midterm2{avg_midterm_2: .2f}, final{avg_midterm_3: .2f}')  

if __name__ == "__main__":

    courseGrade()