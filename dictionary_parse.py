"""
INPUT:
numUsers=3
userVideosWatched={
	"Fred" : ["mass", "world", "stress"],
	"Jenie" : ["happy", "pride"],
	"Rone" : ["alexander"]
}
numGenres=3
videoGeneres={
	"Horror": ["mass", "stress"]
	"Comedy": ["happy"],
	"Romance": ["wprld", "alexander", "pride"]
}

OUTPUT:
{
	"Fred": ["Horror"],
	"Jenie": ["Comedy", "Romance"],
	"Rone": ["Romance"]
}
"""


def parseMyDict(numUsers, userVideosWatched, numGenres, videoGeneres):
	output_dict={}
	# print()
	genre_list=[]
	ptr=0
	build_genre_dict={}
	for key, values in videoGeneres.items():
		# print(key, values)
		genre_list.append(key)
		for value in values:
			build_genre_dict[value]=ptr
		ptr+=1
	print(build_genre_dict)
	print(genre_list)
	for key, values in userVideosWatched.items():
		user_array=[]
		for value in values:
			user_array.append(build_genre_dict[value])
		output_dict[key]=user_array

	print(output_dict)




if __name__=="__main__":
	userVideosWatched={
	"Fred" : ["mass", "world", "stress"],
	"Jenie" : ["happy", "pride"],
	"Rone" : ["alexander"]
		}
	videoGeneres={
	"Horror": ["mass", "stress"],
	"Comedy": ["happy"],
	"Romance": ["world", "alexander", "pride"]
		}
	parseMyDict(3, userVideosWatched,  3, videoGeneres)