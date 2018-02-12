exam_score = 65
student_present = True
if (exam_score > 89 and student_present) :
    print('A')
else:
    if (exam_score > 79 and student_present) :
        print('B')
    else:
        if (exam_score > 69 and student_present) :
            print('C')
        else:
            if (exam_score > 59 and student_present) :
                print('D')
            else:
                print('F')
