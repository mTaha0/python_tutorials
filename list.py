liste1 = [1, 2, 3, 4, 5]
liste2 = ["elma", "armut", "karpuz"]
liste3 = [["elma", "armut"], ["taha", "ali"], [1, 2, 3]]
print(liste3[0][1])

liste1.append(6)
liste1.pop(2) #2.indeksteki elemanı siler
liste1.pop() #listenin sonundaki elemanı siler

liste2.remove('armut') 
liste1.sort()
liste1.clear()

