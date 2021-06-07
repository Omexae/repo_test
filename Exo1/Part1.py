import somDiv
import estPremier
import estParfait
import estChanceux

print(somDiv.div(12))
print(estPremier.premier(31))
print(estParfait.parfait(6))
print(estChanceux.chance(11))

listchance = [0] * 998
listparfait = [0] * 998

for i in range(0, 998):
    listchance[i] = estChanceux.chance(i+2)
    listparfait[i] = estParfait.parfait(i+2)
    print(i)
print("Liste nombre chanceux de 2 à 1000")
for j in range(0, 998):
    print(listchance[j])
print("Liste nombre parfaits de 2 à 998")
for k in range(2, 998):
    print(listparfait[k])
