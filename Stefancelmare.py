text = "Stephen III of Moldavia, known as Stephen the Great (Romanian: Ștefan cel Mare [ʃteˈfan tʃel ˈmare] ; died on 2 July 1504), was voivode (or prince) of Moldavia from 1457 to 1504. He was the son of and co-ruler with Bogdan II of Moldavia who was murdered in 1451 in a conspiracy organized by his brother and Stephen's uncle Peter III Aaron who took the throne. Stephen fled to Hungary, and later to Wallachia, but with the support of Vlad III Dracula, Voivode of Wallachia, he returned to Moldavia, forcing Aaron to seek refuge in Poland in the summer of 1457. Teoctist I, Metropolitan of Moldavia, anointed Stephen prince. He attacked Poland and prevented Casimir IV Jagiellon, King of Poland, from supporting Peter Aaron, but eventually acknowledged Casimir's suzerainty in 1459. "
list=[",",".","(",")","-","[","]",";","'"]
numaratoare=0
for caracter in text:
    if caracter  in list:
        numaratoare=numaratoare +1
print("sunt" + str(numaratoare) + "de semne de punctuatie")
numaratoare=0
for caracter in text:
    if caracter==".":
        numaratoare=numaratoare +1
print("sunt" + str(numaratoare) + "fraze")
list2=["a","e","i","o","u"]
numaratoare=0
for caracter in text:
    if caracter in list2:
        numaratoare=numaratoare +1
print("sunt" + str(numaratoare) + "de vocale")
list3=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
numaratoare=0
for caracter in text:
    if caracter in list3:
        numaratoare=numaratoare +1
print("sunt" + str(numaratoare) + "de consoane")