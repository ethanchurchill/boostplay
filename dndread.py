import json
import urllib.request

class ReadJSON():
	def __init__(self):
		self.filestart = "assets/dnd_jsons/"
		self.excluded = []

	# Private function in dndread that takes a category (ie. languages, races, classes, etc.) and a 
	# jsonfile and reads said json file and returns a list of names that appear in the file.
	def __getValues(self, inkeys, category, jsonfile):
		with open(self.filestart + category + '/' + jsonfile, encoding="utf8") as f:
			unfltr_results = json.load(f)

		fltr_results = []
		count = 0
		for result in unfltr_results:
			result_keys = result.keys()
			no_exclusion_found = True
			result_items = result.items()
			for key, value in result_items:
				if key == "source":
					for string in self.excluded:
						if string in value:
							no_exclusion_found = False
							break
					if not no_exclusion_found:
						break
			if no_exclusion_found:
				fltr_results.append([])
				for key in inkeys:
					fltr_results[count].append(result.get(key, []))
				count = count + 1
					
		return fltr_results

	# Public function to add a string to the list of excluded strings when reading json files.
	def addExclusion(self, string):
		self.excluded.append(string)

	def getExclusions(self):
		return self.excluded

	# Public function getLanguages returns a list of language values based upon input key for DnD 5e.
	def getLanguages(self, keys):
		languages = []
		for key in keys:
			languages.append(self.__getValues(key, "languages", "5e_languages.json"))
		return languages

	# ...
	def getBackgrounds(self, keys):
		backgrounds = []
		for key in keys:
			backgrounds.append(self.__getValues(key, "backgrounds", "5e_backgrounds.json"))
		return backgrounds

	# ...
	def getSubclasses(self, keys):
		subclasses = []
		for key in keys:
			subclasses.append((
				self.__getValues(key, "subclasses", "5e_artificer_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_barbarian_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_bard_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_cleric_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_druid_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_fighter_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_monk_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_paladin_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_ranger_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_rogue_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_sorcerer_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_warlock_subclasses.json") + 
				self.__getValues(key, "subclasses", "5e_wizard_subclasses.json")))
		return subclasses

	def getFeaturesArtificer(self, keys):
		return self.__getValues(keys, "classes", "5e_artificer_features.json")

	def getFeaturesBarbarian(self, keys):
		return self.__getValues(keys, "classes", "5e_barbarian_features.json")

	def getFeaturesBard(self, keys):
		return self.__getValues(keys, "classes", "5e_bard_features.json")

	def getFeaturesCleric(self, keys):
		return self.__getValues(keys, "classes", "5e_cleric_features.json")

	def getFeaturesDruid(self, keys):
		return self.__getValues(keys, "classes", "5e_druid_features.json")

	def getFeaturesFighter(self, keys):
		return self.__getValues(keys, "classes", "5e_fighter_features.json")

	def getFeaturesMonk(self, keys):
		return self.__getValues(keys, "classes", "5e_monk_features.json")

	def getFeaturesPaladin(self, keys):
		return self.__getValues(keys, "classes", "5e_paladin_features.json")

	def getFeaturesRanger(self, keys):
		return self.__getValues(keys, "classes", "5e_ranger_features.json")

	def getFeaturesRogue(self, keys):
		return self.__getValues(keys, "classes", "5e_rogue_features.json")

	def getFeaturesSorcerer(self, keys):
		return self.__getValues(keys, "classes", "5e_sorcerer_features.json")

	def getFeaturesWarlock(self, keys):
		return self.__getValues(keys, "classes", "5e_warlock_features.json")

	def getFeaturesWizard(self, keys):
		return self.__getValues(keys, "classes", "5e_wizard_features.json")

	# ...
	def getFeatures(self, keys):
		features = []
		features.append(self.__getValues(keys, "classes", "5e_artificer_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_barbarian_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_bard_features.json")) 
		features.append(self.__getValues(keys, "classes", "5e_cleric_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_druid_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_fighter_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_monk_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_paladin_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_ranger_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_rogue_features.json"))
		features.append(self.__getValues(keys, "classes", "5e_sorcerer_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_warlock_features.json"))  
		features.append(self.__getValues(keys, "classes", "5e_wizard_features.json"))
		return features

	def getClassArtificer(self, keys):
		return self.__getValues(keys, "classes", "5e_class_artificer.json")

	def getClassBarbarian(self, keys):
		return self.__getValues(keys, "classes", "5e_class_barbarian.json")

	def getClassBard(self, keys):
		return self.__getValues(keys, "classes", "5e_class_bard.json")

	def getClassCleric(self, keys):
		return self.__getValues(keys, "classes", "5e_class_cleric.json")

	def getClassDruid(self, keys):
		return self.__getValues(keys, "classes", "5e_class_druid.json")

	def getClassFighter(self, keys):
		return self.__getValues(keys, "classes", "5e_class_fighter.json")

	def getClassMonk(self, keys):
		return self.__getValues(keys, "classes", "5e_class_monk.json")

	def getClassPaladin(self, keys):
		return self.__getValues(keys, "classes", "5e_class_paladin.json")

	def getClassRanger(self, keys):
		return self.__getValues(keys, "classes", "5e_class_ranger.json")

	def getClassRogue(self, keys):
		return self.__getValues(keys, "classes", "5e_class_rogue.json")

	def getClassSorcerer(self, keys):
		return self.__getValues(keys, "classes", "5e_class_sorcerer.json")

	def getClassWarlock(self, keys):
		return self.__getValues(keys, "classes", "5e_class_warlock.json")

	def getClassWizard(self, keys):
		return self.__getValues(keys, "classes", "5e_class_wizard.json")

	# ...
	def getClasses(self, keys):
		classes = []
		classes.append(self.__getValues(keys, "classes", "5e_class_artificer.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_barbarian.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_bard.json")) 
		classes.append(self.__getValues(keys, "classes", "5e_class_cleric.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_druid.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_fighter.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_monk.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_paladin.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_ranger.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_rogue.json"))
		classes.append(self.__getValues(keys, "classes", "5e_class_sorcerer.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_warlock.json"))  
		classes.append(self.__getValues(keys, "classes", "5e_class_wizard.json"))
		return classes

	# ...
	def getRaces(self, keys):
		races = []
		races.append(self.__getValues(keys, "races", "5e_races.json"))
		return races
		
	# ...
	def getFeats(self, keys):
		feats = []
		for key in keys:
			feats.append(self.__getValues(key, "feats", "5e_feats.json"))
		return feats

	# ...
	def getItems(self, keys):
		items = []
		for key in keys:
			items.append(self.__getValues(key, "items", "5e_items.json"))
		return items

	# ...
	def getSpells(self, keys):
		spells = []
		for key in keys:
			spells.append((
				self.__getValues(key, "spells", "5e_spells_ai.json") + 
				self.__getValues(key, "spells", "5e_spells_egw.json") + 
				self.__getValues(key, "spells", "5e_spells_ggr.json") +
				self.__getValues(key, "spells", "5e_spells_idrotf.json") + 
				self.__getValues(key, "spells", "5e_spells_phb.json") + 
				self.__getValues(key, "spells", "5e_spells_tce.json") +
				self.__getValues(key, "spells", "5e_spells_xge.json")))
		return spells

# temp = ReadJSON()
# ns = ["name", "source"]
# classes = temp.getClasses(ns)
# for i in range(len(classes[0])):
# 	if "UA" not in classes[1][i]:
# 		print(classes[0][i] + " " + classes[1][i])

# print()
# subclasses = temp.getSubclasses(["subclassShortName"])
# for subclass in subclasses:
# 	print(subclass)
