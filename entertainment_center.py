# Programmer: Carlos Hernandez
# June 15th, 2017
# Udacity - Programming Fundamentals and the Web Project 1

# Import the classes used in entertainment_center
import fresh_tomatoes
import media


# Create instances of the Movie class
gladiator = media.Movie("Gladiator",
                        "The story of a commander made\
                        gladiator who defeats Caesar",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")  # noqa

legendsFall = media.Movie("Legends of The Fall",
                          "The story of three brothers and their father living\
                          in the wilderness and how their lives\
                          are affected by nature, history, war and love",
                          "https://upload.wikimedia.org/wikipedia/en/1/1d/Legendsoffallposter.jpg",  # noqa
                          "https://www.youtube.com/watch?v=fSTyL-KbUM0")

gangsNY = media.Movie("Gangs of New York",
                    "The story of an irish immigrant avenging his\
                    father during the early days of US",
                    "http://t2.gstatic.com/images?q=tbn:ANd9GcQH5q3fv0sN6sIFmBTb7Wqn4pb_fymvhj8aM_PpYgBHAizH8GWv",  # noqa
                    "https://www.youtube.com/watch?v=qHVUPri5tjA")


# Create a list with the movies
movies = [gladiator, legendsFall, gangsNY]


# Display the movies using the fresh_tomatoes class
fresh_tomatoes.open_movies_page(movies)
