import random
x = 0
cars = []
lpark = []
pplace = 0
pcount = 20
timefactor = 0.001


while True:
        time.sleep(timefactor)
        timem += 1
        if timem == 60:
            timeh += 1
            timem = 0
        print(timem)

        if timeh == 24:
            timeh = 0
            timem = 0
            timed += 1

    for u in range (pcount):
        lpark.append(pcount-u)
    lpark.reverse()
    print(lpark)

    for i in range (20):
    y = random.randint(0,10) #Ob Auto erstellt wird, wird ausgewürfelt

    if 0 == y%2:
        x = x + 1
        pplace = lpark[random.randrange(0, len(lpark), 1)]  # Parkplatznummer wird festgelegt
        lpark.remove(pplace)
        cars.append([x, pplace, 0, 0, 0])

    #for i in cars
    #   cars[]
    print(cars)
