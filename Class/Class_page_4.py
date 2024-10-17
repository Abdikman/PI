

class Note:

    def __init__(self, note: str = "до", is_long: bool = False):
        if is_long:
            long_note = {"до": "до-о",
                         "ре": "ре-э",
                         "ми": "ми-и",
                         "фа": "фа-а",
                         "соль": "со-оль",
                         "ля": "ля-а",
                         "си": "си-и"
                         }
            note = long_note[note]

        self.note = note
        self.is_long = is_long


    def __str__(self):
        return self.note


class LoudNote(Note):

    def __init__(self, note: str = "до", is_long: bool = False):
        super().__init__(note=note, is_long=is_long)
        self.note = self.note.upper()


class NoteWithOctave(Note):

    def __init__(self, note: str = "до", octave: str = "1 октава", is_long: bool = False):
        super().__init__(note=note, is_long=is_long)
        self.octave = octave

    def __str__(self):
        super().__str__()
        return self.note + f" ({self.octave})"

