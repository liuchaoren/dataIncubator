'''
extract and plot the data of amazon customer review information
'''

from pandas import *
import numpy as ny
import sys
from sets import Set
import json

businessFilename = '/Users/Chaoren/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json'
review = '/Users/Chaoren/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json'

foodbyCountryorRegion = ['Swiss', 'Canadian', 'Arabian', 'Austrian', 'Belgian', 'German', 'Chinese', 'Shanghainese',
	'Dim Sum', 'Cantonese', 'Szechuan', 'Taiwanese', 'French', 'Italian', 'Russian', 'Polish', 'Irish', 'American', 'Czech', 'African', 'Singaporean',
	'Turkish', 'Korean', 'Soul', 'Brazilian', 'Latin', 'Indian', 'Iberian', 'Egyptian', 'Ukrainian', 'Japanese', 'Spanish', 'Portuguese', 'Mexican']


def jsonFileExtractor(jfile):
	alllines = open(jfile).readlines()
	extractList = []
	for eachline in alllines:
		extractList.append(json.loads(eachline))
	return extractList


# def categoryExtractor(extractList):
# 	categories = Set([])
# 	for eachitem in extractList:
# 		if "Restaurants" in eachitem["categories"]:
# 			categories.update(eachitem["categories"])
# 	return categories


def aggregateByCountries(extractList):
	businesses = []
	for eachitem in extractList:
		if "Restaurants" in eachitem["categories"]:
			for eachcate in eachitem["categories"]:
				for eachcountry in foodbyCountryorRegion:
					if eachcountry in eachcate:
						# categories[eachcountry].update(str(eachitem['business_id']))
						if eachcountry in ['Dim Sum', 'Cantonese', 'Szechuan', 'Taiwanese']:
							eachcountry == 'Chinese'
						elif eachcountry in ['Soul']:
							eachcountry == 'Korean'
						businesses.append({'business_id': eachitem['business_id'], 'city': eachitem['city'], 'state': eachitem['state'], 'stars': eachitem['stars'], 'review_count': eachitem['review_count'], 'style': eachcountry})
	dataReturn = DataFrame(businesses)
	# dataReturn.index = dataReturn.business_id
	# del dataReturn['business_id']
	return dataReturn


def updateReview(businessInfo, reviewfile):
	review = jsonFileExtractor(reviewfile)
	businessCollector = {}
	for eachreview in review:
		votes = eachreview['votes']['funny'] + eachreview['votes']['useful'] + eachreview['votes']['cool']
		if businessCollector.has_key(eachreview['business_id']):
			businessCollector[eachreview['business_id']] += votes
		else:
			businessCollector[eachreview['business_id']] = votes

	reviews = []
	for eachbusiness in businessInfo.business_id:
		if businessCollector.has_key(eachbusiness):
			reviews.append(businessCollector[eachbusiness])
		else:
			reviews.append(0)
	businessInfo['reviewadd'] = reviews
	return businessInfo


if __name__ == '__main__':
	businessExtracted = jsonFileExtractor(businessFilename)
	businessInfo = aggregateByCountries(businessExtracted)
	businessInfoReviewAdd = updateReview(businessInfo, review)
	businessInPits = businessInfo[businessInfo['city'] == 'Pittsburgh']
	starsInPits = businessInPits.groupby(by='style')['stars'].mean()
	reviewnum = businessInPits.groupby(by='style')['review_count'].mean()
	reviewAddInPits = businessInPits.groupby(by='style')['reviewadd'].mean()
	gainbynum = reviewnum / starsInPits
	gainbyvote = (reviewAddInPits + reviewnum) / starsInPits
	gainbynum.plot(kind='bar')
	ylabel("popularity/rating")
	tight_layout()
	gainbyvote.plot(kind='bar')
	ylabel("popularity/rating")
	tight_layout()





	# targetIndex = businessInfo['business_id'] == 'uYKwS-biARKgBkk5rY_PaQ'].index





