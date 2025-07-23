MENU_PROMPT="/n Enter 'a' to add movie, 'l' to list movies, 'f' to find movie by title,'q' to quit: "
movies=[]

def add_movie():
    title = input("Enter a name of movie: ")
    director = input("Enter name of director of movie: ")
    year = int(input("Enter a year in which movie released: "))
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def show_movie():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    search_title=input("Enter a movie title you're looking for: ")
    for movie in movies:
        if movie["title"]==search_title:
            print_movie(movie)


def menu():
    selection=input(MENU_PROMPT)
    while selection!='q':
        if selection=='a':
            add_movie()
        elif selection=='l':
            show_movie()
        elif selection=='f':
            find_movie()
        else:
            print("Unknown command. Please try again.")
        selection=input(MENU_PROMPT)

menu()