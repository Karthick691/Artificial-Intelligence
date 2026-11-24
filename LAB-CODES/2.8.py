
# Person(Name, Day, Month, Year)

persons = [
    ("arun", 12, 3, 2004),
    ("bala", 25, 7, 2003),
    ("chitra", 5, 11, 2004),
    ("divya", 18, 3, 2005),
    ("elango", 30, 1, 2003)
]

def dob(name):
    return [(d, m, y) for n, d, m, y in persons if n == name]

def born_in_year(year):
    return [n for n, d, m, y in persons if y == year]

def born_in_month(month):
    return [n for n, d, m, y in persons if m == month]

def older(p1, p2):
    a = next((d, m, y) for n, d, m, y in persons if n == p1)
    b = next((d, m, y) for n, d, m, y in persons if n == p2)
    return a[2] < b[2] or (
        a[2] == b[2] and (
            a[1] < b[1] or
            (a[1] == b[1] and a[0] < b[0])
        )
    )

print("DOB of Arun:", dob("arun"))
print("Born in 2004:", born_in_year(2004))
print("Born in March:", born_in_month(3))
print("Bala older than Arun:", older("bala", "arun"))
