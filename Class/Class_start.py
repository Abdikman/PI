from Class_page_4 import *

# do = Note("до", True)
# sol = Note("соль", True)
# doo = Note("до")
#
# print(do, sol, doo)

PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]

print(LoudNote(PITCHES[5]), LoudNote(PITCHES[5], True))

print(NoteWithOctave(PITCHES[2], "первая октава", True))

