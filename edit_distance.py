import edit_distance

#https://en.wikipedia.org/wiki/Edit_distance
class EditDistance:
	def edit_distance(string_a, string_b):
		distance, matches = edit_distance.edit_distance(string_a, string_b)
		return distance