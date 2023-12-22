#test'n
import pygame, sys, math, random
from countryinfo import *
from Country import *

works=False
while not works:
    try:
        stuffnstuff=open("Countrys.info","r")
        works=True
    except:
        works=False
        stuffnstuff=open("Countrys.info","x")
        stuffnstuff.write("making stuff be in file")
print(stuffnstuff.read())
stuffnstuff.close()

countryObjects=[]
    
pygame.init()
size = [1440, 720]
screen = pygame.display.set_mode(size)

#quit()

# MESSY SETUP

names = []
c = CountryInfo()
c = c.all()
for key in c:
    names += [key]

regions = []
for name in names:
    c = CountryInfo(name)
    countryObjects+=[Country(size, name, [random.randint(0,255),random.randint(0,255),random.randint(0,255), 255])]
    try:
        countries = [c.geo_json()]
        country = countries[0]["features"][0]["geometry"]["coordinates"]
        for i, region in enumerate(country):
            if len(country[i]) < 2:
                
                regions += [country[i][0]]
                
                countryObjects[-1].addRegions([country[i][0]])
            else:
                
                regions += [country[i]]
                
                countryObjects[-1].addRegions([country[i]])
        print("added", name)
    except:
        pass

colors = []
for i, region in enumerate(regions):
    print(i)
    try:
        for c in region:
            c[0] += 180
            c[0] *=4
            c[1] *= -1
            c[1] += 90
            c[1] *=4
            colors += [[random.randint(0,255),random.randint(0,255),random.randint(0,255), 255]]
        
        
    except:
        print("bad region") 
        print(region)
        regions.remove(region)
        
for country in countryObjects:
    try:
        for c in country.regions:
            print(c)
            c[0] += 180
            c[0] *=4
            c[1] *= -1
            c[1] += 90
            c[1] *=4
        
        
    except:
        print("\nremoved",str(region))
        print("\n\n") 
        regions.remove(region)




#END MESSY SETUP

for w in countryObjects:
    if w.regions == []:
        w.remove()
    else:
        w.prints()



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    
    
    screen.fill([30,144,255])
    for i, region in enumerate(regions):
        
        pygame.draw.polygon(screen, colors[i],  region)
        pygame.draw.polygon(screen, [0, 0, 0,255], region, 1)
    pygame.display.flip()
