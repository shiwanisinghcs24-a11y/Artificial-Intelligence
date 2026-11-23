def resolve(c1, c2):
    for l1 in c1:
        for l2 in c2:
            if (l1[0] != l2[0] and
                l1[1] == l2[1] and
                l1[2] == l2[2]):

                result = list(c1)
                result.remove(l1)
                result.extend(c2)
                result.remove(l2)

                return result

    return None


C1 = [
    ("~", "Food", "Peanuts"),
    ("+", "Likes", "John,Peanuts")
]

C2 = [
    ("~", "Eats", "Anil,Peanuts"),
    ("+", "Killed", "Anil"),
    ("+", "Food", "Peanuts")
]

C3 = [
    ("+", "Eats", "Anil,Peanuts")
]

C4 = [
    ("~", "Food", "Peanuts")
]

C5 = [
    ("~", "Alive", "Anil"),
    ("~", "Killed", "Anil")
]

C6 = [
    ("+", "Alive", "Anil")
]

print("Resolution Proof:")

r1 = resolve(C1, [
    ("~", "Likes", "John,Peanuts")
])
print("1.", r1)

r2 = resolve(C2, C3)
print("2.", r2)

r3 = resolve(r2, C4)
print("3.", r3)

r4 = resolve(C5, r3)
print("4.", r4)

r5 = resolve(r4, C6)
print("5.", r5)

if r5 == []:
    print("\nEmpty Clause {} obtained")
    print("Query Proved: John likes Peanuts")
else:
    print("\nQuery Not Proved")
print("Shiwani Singh 1BF24CS283")

