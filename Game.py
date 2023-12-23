import pygame, random
from countryinfo import *
from country import *


def action(countries, action):
	if action == "+":
		for country in countries:
			for region in country.regions:
				for c in region:
					'''c[1]-=720/2
					c[0]-=1440/2'''
					c[0] *=1.25
					c[1] *=1.25
	
	elif action == "-":
		for country in countries:
			for region in country.regions:
				for c in region:
					c[0] /=1.25
					c[1] /=1.25
					'''c[0]+=1440/2
					c[1]+=720/2'''
	
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
	
	
	
	
	
	
	
def getInfo(size):
	countryObjects=[]
	names = []
	c = CountryInfo()
	c = c.all()
	for key in c:
		names += [key]

	for name in names:
		c = CountryInfo(name)
		countryObjects+=[Country(size, name)]
		try:
			countries = [c.geo_json()]
			country = countries[0]["features"][0]["geometry"]["coordinates"]
			for i, region in enumerate(country):
				if len(country[i]) < 2:
					countryObjects[-1].addRegions([country[i][0]])
				else:
					countryObjects[-1].addRegions([country[i]])
			print("added", name)
		except Exception as e:
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


	
	
