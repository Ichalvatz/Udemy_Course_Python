
movies = []


def add_movies():

    movie = {"name" : "movie_name" ,
         "director" : "movie_director" , 
         "year" : "movie_year" }
    
    movie["name"] = input("What movie do you want to add?: ")
    movie["director"] = input("Who is the director?: ")
    movie["year"] = input("What year did it come out?: ")

    movies.append(movie)


def show_movies():
    if len(movies) == 0:
        print("You have 0 movies stored")
    else:
        print("Your movies are: ")
        for movie in movies:
            print(movie["name"])


def find_movies():
    if len(movies) == 0:
        print("You have dont have any movies stored!")
        return None
    found_movies = []
    while True:
        f_choise = input("Do you want to tell me the director (Press 'd'), the year (Press 'y') or both (Press 'b'): ")

        if f_choise == "d":
            f_director = input("Who is the director?: ")
            for movie in movies:

                if f_director == movie["director"]:
                    found_movies.append(movie["name"])

            else:

                if len(found_movies) == 0:
                    print(f"No movies found from director {f_director}")
                else:
                    print(f"The movies from director {f_director} are {found_movies}")
                break

        elif f_choise == "y":
            f_year = input("What year was the movie out?: ")

            for movie in movies:

                if f_year == movie["year"]:
                    found_movies.append(movie["name"])

            else:

                if len(found_movies) == 0:
                    print(f"No movies found the year {f_year}")
                else:
                    print(f"The movies from the year {f_year} are {found_movies}")
                break

        elif f_choise == "b":
            f_director = input("Who is the director?: ")
            f_year = input("What year was the movie out?: ")

            for movie in movies:

                if f_director == movie["director"] and f_year == movie["year"]:
                    found_movies.append(movie["name"])

            else:        
                if len(found_movies) == 0:
                    print(f"No movies found from  director {f_director} from the year {f_year} ")
                else:
                    print(f"The movies from director {f_director} from the year {f_year} are {found_movies}")
                break
        else:
            print("Wrong choise please select again! ")
    
while True:

    choise = input("What do you want to do?\n Press 'a' to add movies \n Press 'l' to see your movies \n Press 'f' to find movies \n Press 'q' to exit the program\n")
    
    if choise == "q":
        print("You terminated the program")
        break
    elif choise == "a":
        add_movies()
    elif choise == "l": 
        show_movies()
    elif choise == "f":
        find_movies()
    else:
        print("Wrong input please choose again! ")
    

        