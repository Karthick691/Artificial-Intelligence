
subjects = {
    "csa17": "Artificial Intelligence",
    "csa07": "Computer Networks",
    "dsa03": "Natural Language Processing"
}

teaches = [
    ("jai", "csa17"),
    ("meena", "csa07"),
    ("ravi", "dsa03")
]

studies = [
    ("anu", "csa17"),
    ("anu", "dsa03"),
    ("kiran", "csa17"),
    ("latha", "csa07")
]

def taught_by(student):
    return [t for s, c in studies for t, code in teaches
            if s == student and c == code]

def students_of(teacher):
    return [s for t, c in teaches for s, code in studies
            if t == teacher and c == code]

def classmates(s1):
    return list(set(s2 for s, c in studies if s == s1
                    for s2, code in studies
                    if c == code and s1 != s2))

def subject_name_of(student):
    return [subjects[c] for s, c in studies if s == student]

print("Teachers of Anu:", taught_by("anu"))
print("Students of Jai:", students_of("jai"))
print("Classmates of Anu:", classmates("anu"))
print("Subjects of Anu:", subject_name_of("anu"))
