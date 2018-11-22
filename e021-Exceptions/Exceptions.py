print("##################### 1 #####################")
exam_note = -5
"""
if exam_note<0 or exam_note>10:
    raise ValueError("The note must be between 0 and 10")
else:
    print("The exam note is %d" % (exam_note))
"""

"""
output:
    Traceback (most recent call last):
      File ".../Python/e021-Exceptions/Exceptions.py", line 5, in <module>
        raise ValueError("The note must be between 0 and 10")
    ValueError: The note must be between 0 and 10
"""


print("##################### 2 #####################")
exam_note = -5

def print_exam_note(exam_note):
    if exam_note<0 or exam_note>10:
        raise ValueError("The note must be between 0 and 10")
    else:
        print("The exam note is %d" % (exam_note))

try:
    print_exam_note(exam_note)
except ValueError as NoteError:
    print(NoteError)


"""
output:
    The note must be between 0 and 10
"""


print("##################### 3 #####################")
class ExamNoteError(Exception):
    def __init__(self, exam_note):
        self.exam_note = exam_note

    def __str__(self):
        return "Note not valid, %s, the note must be between 0 and 10" % str(self.exam_note)


exam_note = -5

def print_exam_note(exam_note):
    if exam_note<0 or exam_note>10:
        raise ExamNoteError(exam_note)
    else:
        print("The exam note is %d" % (exam_note))

try:
    print_exam_note(exam_note)
except ExamNoteError as NoteError:
    print(NoteError)


"""
output:
    Note not valid, -5, the note must be between 0 and 10
"""


print("##################### 4 #####################")
exam_note = -5

try:
    assert(exam_note>0 and exam_note<10)
except AssertionError:
    print("Note not valid")

"""
output:
    Note not valid
"""


