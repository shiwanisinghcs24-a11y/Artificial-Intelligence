facts = [
    "American(Robert)",
    "Missile(T1)",
    "Owns(A,T1)",
    "Enemy(A,America)"
]

if "Missile(T1)" in facts:
    facts.append("Weapon(T1)")

if "Missile(T1)" in facts and "Owns(A,T1)" in facts:
    facts.append("Sells(Robert,T1,A)")

if "Enemy(A,America)" in facts:
    facts.append("Hostile(A)")

if ("American(Robert)" in facts and
    "Weapon(T1)" in facts and
    "Sells(Robert,T1,A)" in facts and
    "Hostile(A)" in facts):

    facts.append("Criminal(Robert)")

print("Knowledge Base:")
for fact in facts:
    print(fact)

if "Criminal(Robert)" in facts:
    print("\nRobert is Criminal")
    print("Query Proved")
else:
    print("\nQuery Not Proved")
    
print("Shiwani Singh 1BF24CS283")

