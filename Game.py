import pygame, random
from countryinfo import *
from country import *


def action(countries, action):
	#zoom in
	if action == "+":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0] *=1.25
					c[1] *=1.25
					c[1]-=720/8
					c[0]-=1440/8
	#zoom out
	elif action == "-":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0]+=1440/8
					c[1]+=720/8
					c[0] /=1.25
					c[1] /=1.25

	#move left
	if action == "moveL":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0] +=10
	#move right
	elif action == "moveR":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0] -=10
	#move up
	elif action == "moveU":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[1] +=10
	#move down
	elif action == "moveD":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[1] -=10
	
	return countries
	
	
	
	
	
	
	
def getInfo(size, screen):
	
	font = pygame.font.Font(None, 32)
	
	countryObjects=[]
	names = []
	c = CountryInfo()
	c = c.all()
	for key in c:
		names += [key]
	l=[0,20]
	for name in names:
		
		#loading screen
		screen.fill([30,144,255])
		screen.blit(pygame.image.load("risk.png"), [(size[0]/2)-233, 100])
		pygame.draw.rect(screen, [255, 255, 255],((size[0]/2)-236,374,470,22), 1)
		l[0]+=2
		load=pygame.Surface(l)
		screen.blit(load, [(size[0]/2)-235,375])
		
		#quit on quit
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

		#more loading screen
		try:
			text = font.render("Added: "+str(name[0].upper()+name[1:-1]+name[-1]), True, (10, 10, 10))
		except:
			text = font.render("Added: Other", True, (10, 10, 10))
		textpos = [(size[0]/2)-233, 400]
		screen.blit(text, textpos)
		
		pygame.display.flip()

		
		
		c = CountryInfo(name)
		try:
			cont=c.region()
		except:
			cont=None
		#create country object
		countryObjects+=[Country(size, name, cont)]
		try:
			#grab regions and add it to the country object
			countries = [c.geo_json()]
			country = countries[0]["features"][0]["geometry"]["coordinates"]
			for i, region in enumerate(country):
				if len(country[i]) < 2:
					countryObjects[-1].addRegions([country[i][0]])
				else:
					countryObjects[-1].addRegions([country[i]])
		except:
			pass

	#Sweden just doesn't work, so why let it?
	for country in countryObjects:
		if country.name == "sweden":
			countryObjects.remove(country)
			break

	#shift countrys over, and zoom them to a good value
	for country in countryObjects:
		for region in country.regions:
			try:
				for n in region:
					n[0] += 180
					n[0] *=4
					n[1]*=-1
					n[1] += 90
					n[1] *=4
			
			except:
				#doesn't work? Get rid of it!
				print("removed",str(country.name))
				print(region)
				countryObjects.remove(country)
	return countryObjects


	
	
