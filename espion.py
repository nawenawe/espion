dbt = int(input())
fin = int(input())
print(f"L'espion est arrivé entre le {dbt} et le {fin}")

n = int(input())
print(f"{n} personnes sont rentrées dans la ville en tout")

nb = 0
for i in range(n):
    date = int(input())
    if date >= dbt and date <= fin:
        nb += 1


print(nb)
# print(f"La personne qui est rentree le {date} est suspicieuse")
