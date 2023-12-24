import pygame, random
from countryinfo import *
from country import *


def action(countries, action):
	if action == "+":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0] *=1.25
					c[1] *=1.25
					c[1]-=720/8
					c[0]-=1440/8
	
	elif action == "-":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0]+=1440/8
					c[1]+=720/8
					c[0] /=1.25
					c[1] /=1.25

	
	if action == "moveL":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0] +=10

	elif action == "moveR":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0] -=10

	elif action == "moveU":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[1] +=10
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
		screen.fill([30,144,255])
		screen.blit(pygame.image.load("risk.png"), [(size[0]/2)-233, 100])
		pygame.draw.rect(screen, [255, 255, 255],((size[0]/2)-236,374,470,22), 1)
		l[0]+=2
		load=pygame.Surface(l)
		screen.blit(load, [(size[0]/2)-235,375])
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

		
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
		countryObjects+=[Country(size, name, cont)]
		try:
			countries = [c.geo_json()]
			country = countries[0]["features"][0]["geometry"]["coordinates"]
			for i, region in enumerate(country):
				if len(country[i]) < 2:
					countryObjects[-1].addRegions([country[i][0]])
				else:
					countryObjects[-1].addRegions([country[i]])
		except:
			pass

	for country in countryObjects:
		if country.name == "sweden":
			countryObjects.remove(country)
			break

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
				print("removed",str(country.name))
				print(region)
				countryObjects.remove(country)
	return countryObjects


	
	
