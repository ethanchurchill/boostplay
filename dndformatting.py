from dndread import ReadJSON


class DNDFormater():

	def __init__(self):
		self.readjson = ReadJSON()
		self.readjson.addExclusion("UA")

		self.class_categories = ["name", "source", "page", "hd", "proficiency", "spellcastingAbility", "casterProgression", "preparedSpells", "cantripProgression", 
			"spellsKnownProgression", "optionalFeatureProgression", "startingProficiencies", "startingEquipment", "multiclassing", "classTableGroups"]
		self.classes = self.readjson.getClasses(self.class_categories)
		self.feature_categories = ["name", "source", "className", "level", "entries"]
		self.features = self.readjson.getFeatures(self.feature_categories)
		self.race_categories = ["name", "source", "page", "size", "speed", "ability", "heightAndWeight", "darkvision", "traitTags", "skillProficiencies", "languageProficiencies",
			"resist", "additionalSpells", "entries", "subraces"]
		self.races = self.readjson.getRaces(self.race_categories)
		self.races = self.races[0]

	def parseProf(self, string):
		# {@item shield|phb|shields}
		if "@item" in string:
			result = (string.split('|'))[-1]
			result = result[:-1]
		else:
			result = string
		return result

	def parseVariant(self, string):
		# {@i 3rd-level barbarian {@variantrule optional class features|tce|optional feature}}
		# {@i 1st-level ranger {@variantrule optional class features|tce|optional feature}, which replaces the Natural Explorer feature}
		result = "Optional; "
		start = string.find(" replaces")
		if start == -1:
			start = string.find("}")
			result = result[:-2]
		result = result + (string[start + 1:-1])
		return result

	def parseItem(self, string):
		# {@item Herbalism kit|PHB}
		# one type of {@item artisan's tools|PHB} of your choice
		pipe = ["@item", "@filter", "@5etools", "@book", "@creature"]
		bracket = ["@dice", "@condition", "@action", "@skill", "@spell", "@sense"]
		result = string
		while(True):
			if any(((str_pipe in result) for str_pipe in pipe)) or any(((str_bracket in result) for str_bracket in bracket)):
				at_sign = result.find('@')
				if any([(result.find(word) == at_sign) for word in pipe]):
					end_char = '|'
				else:
					end_char = '}'
				result = result.replace(
					result[result.find('{'):(result.find('}')+ 1)], 
					result[(at_sign + result[at_sign:].find(' ') + 1):result.find(end_char)])
			else:
				break
		return result

	def formatArmor(self, string):
		if string == "light" or string == "medium" or string == "heavy":
			string = string + " armor"
		return string

	def formatWeapons(self, string):
		if string == "simple" or string == "martial":
			string = string + " weapons"
		return string

	def readAbility(self, string, full):
		ability = string.lower()
		if "cha" in ability: 
			if full:
				return "Charisma"
			return "CHA"
		elif "con" in ability:
			if full:
				return "Constitution"
			return "CON"
		elif "dex" in ability:
			if full:
				return "Dexterity"
			return "DEX"
		elif "int" in ability:
			if full:
				return "Intelligence"
			return "INT"
		elif "str" in ability:
			if full:
				return "Strength"
			return "STR"
		else:
			if full:
				return "Wisdom"
			return "WIS"

	def numberStr(self, number):
		number = str(number)
		if number[-1] == '1':
			if len(number) == 1 or (len(number) != 1 and number[-2] != '1'):
				return number + "st"
		elif number[-1] == '2':
			if len(number) == 1 or (len(number) > 1 and number[-2] != '1'):
				return number + "nd"
		elif number[-1] == '3':
			if len(number) == 1 or (len(number) > 1 and number[-2] != '1'):
				return number + "rd"
		return number + "th"

	def longestWordLength(self, string, font):
		length = 0
		words = string.split(' ')
		for word in words:
			if font.getlength(word) > length:
				length = font.getlength(word)
		return length

	def longestStringinListLength(self, inlist, font):
		length = 0
		for string in inlist:
			if font.getlength(string) > length:
				length = font.getlength(string)
		return length

	def parseOptFeature(self, string):
		pipe = string.find('|')
		result = string
		if pipe != -1:
			result = result[:result.find('|')]
		return result

	def getClasses(self):
		return self.classes

	def getClassFeatures(self):
		return self.features

	def getRaces(self):
		return self.races

	def getFormattedData(self, data):
		self.formatted_data = []
		for item in data:
			self.formatted_data.append(item[0])
		return self.formatted_data


# [x][0]: name
# [x][1]: source
# [x][2]: page
# [x][3]: hd
# [x][4]: proficiency
# [x][5]: spellcastingAbility
# [x][6]: casterProgression
# [x][7]: preparedSpells
# [x][8]: cantripProgression
# [x][9]: spellsKnownProgression
# [x][10]: optionalFeatureProgression
# [x][11]: startingProficiencies
# [x][12]: startingEquipment
# [x][13]: multiclassing
# [x][14]: classTableGroups

	def formatClasses(self):
		self.formatted_classes = []

		# Getting rid of unnecessary structure in array
		for item in self.classes:
			self.formatted_classes.append(item[0])

		
		for class_array in self.formatted_classes:
			# Getting rid of hit dice fluff
			class_array[3] = class_array[3]['faces']

			# Making ability full word for saving throws (ex. int --> Intelligence)
			class_array[4][0] = self.readAbility(class_array[4][0], True)
			class_array[4][1] = self.readAbility(class_array[4][1], True)

			# Making spellcasting ability full word (ex. int --> Intelligence) 
			if class_array[5] != []:
				class_array[5] = self.readAbility(class_array[5], True)

			# Making caster progression tag capitalized (ex. full --> Full)
			if class_array[6] != []:
				class_array[6] = class_array[6].capitalize()
			# Formatting proficiencies to be readable
			if class_array[11] != []:
				if "armor" in class_array[11]:
					armor = []
					for item in class_array[11]["armor"]:
						if "proficiency" in item:
							item = item["proficiency"]
						armor.append(self.formatArmor(self.parseProf(item)))
					class_array[11]["armor"] = armor

				if "weapons" in class_array[11]:
					weapons = []
					for item in class_array[11]["weapons"]:
						if "proficiency" in item:
							item = item["proficiency"]
						weapons.append(self.formatWeapons(self.parseProf(item)))
					class_array[11]["weapons"] = weapons

				if "tools" in class_array[11]:
					tools = []
					for item in class_array[11]["tools"]:
						if "proficiency" in item:
							item = item["proficiency"]
						tools.append(self.parseItem(item))
					class_array[11]["tools"] = tools

				# if "skills" in self.active_class[11]:
				# 	skills = []
				# 	i = -1
				# 	for skill_table in self.active_class[11]["skills"]:
				# 		skills.append("")
				# 		i = i + 1
				# 		skill_count = skill_table["choose"]["count"]
				# 		if len(skill_table["choose"]["from"]) == 18:
				# 			skills[i] = skills[i] + " Choose any " + str(skill_count)
				# 			break
				# 		skills[i] = skills[i] + " Choose " + str(skill_count) + " from"
				# 		for item in skill_table["choose"]["from"]:
				# 			if "proficiency" in item:
				# 				item = item["proficiency"]
				# 			parsed_skill = self.parseProf(item).split(' ')
				# 			for word in parsed_skill:
				# 				if (self.reg_font.getbbox(skills[i] + " " + word))[2] > (self.width - skills_displacement - self.margin):
				# 					skills.append("")
				# 					i = i + 1
				# 					skills_displacement = self.width - self.prof_line
				# 				skills[i] = skills[i] + " " + word
				# 			skills[i] = skills[i] + ","

				# 		skills[i] = skills[i][:-1]
				# 		first = True
				# 		skills_displacement = (self.width - self.prof_line) + self.bold_font.getlength("Skills: ")





		return self.formatted_classes

