"""

	Your task, should you choose to accept it...
	Is to create a movie storage application, that will allow users to manage their movie collection 
	and find any movie they want.
	Here’s the three main features:
	• First, the application must allow to add new movies to the collection;
	• The application must allow users to view all the movies in their collection;
	• The application must also allow users to find any particular movie by any of its attributes (more info in the next page...)

"""

ben10 = {"name":"ben10", "director":"shola", "release_year":"2014", "genre":"sci-fi"}

moana = {"name":"moana", "director":"yinka", "release_year":"2020", "genre":"adventure"}

frozen = {"name":"frozen", "director":"seyi", "release_year":"2019", "genre":"adventure"}

avater = {"name":"avater", "director":"james cameron", "release_year":"2016", "genre":"sci-fi"}

avater2 = {"name":"avater the way of water", "director":"james cameron", "release_year":"2023", "genre":"sci-fi"}

kingsman = {"name":"kingsman", "director":"samuel", "release_year":"2019", "genre":"action"}

doctorstrange = {"name":"doctor strange", "director":"shola", "release_year":"2020", "genre":"sci-fi"}


movie_box = [ben10, moana, frozen, avater, avater2, kingsman, doctorstrange] #A list of dictionaraies containing movies




#========================================================================

#print(ben10.values())


# Add function
def search(param_inSearch):
	for movie in movie_box:
		movie_keys = movie.values()
		if param_inSearch in movie_keys:
			return f"Search found\nmovie_name:{movie["name"]}\nmovie_director:{movie["director"]}\nmovie_ReleaseYear:{movie["release_year"]}\nmovie_genre:{movie["genre"]}"


def view():
	all_movie = []
	for movie in movie_box:
		all_movie.append(movie["name"])

	return all_movie


def add(mov_lst):
	mov_lstDict = mov_lst[0]
	mov_lstDict = {}

	key_lst = ["name","director","release_year","genre"]
	initial = 0

	for mov in mov_lst:
		mov_lstDict[key_lst[initial]] = mov
		initial += 1

	movie_box.append(mov_lstDict)
	#return mov_lstDict


	#pass

#print(search("kingsman"))
#print(view())

#define user input function

def user_input(_add, _view, _search):
	while True:
		which_operation = input("\nwhich operation will you like to perform:\n'input add to add a movie'\n'input view to view list of movie available'\n'input search to search for a movie'\ninput q to quit application: ").strip()
		if which_operation == "q":
			print("the application has been stopped, see you some other time")
			break
			quit()
		elif which_operation == "add":
			
			mov_name = input("movie name to add? ")
			mov_director = input("name of director? ")
			mov_releaseYear = input("movie release year? ")
			mov_genre = input("movie genre? ")

			mov_lsts = [mov_name,mov_director,mov_releaseYear,mov_genre]
			add(mov_lsts)
			print("your movie has been successfully added ")
			#pass
		elif which_operation == "view":
			print(view())
			
		elif which_operation == "search":
			print(search(input("\nwhat movie wil you like to search for: ")))
			

		else:
			print("\nyou have input a totally different command i don't understand, try again:")
 
	#pass

user_input(add,view,search)