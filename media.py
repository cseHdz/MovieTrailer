##Programmer: Carlos Hernandez
##June 15th, 2017
##Udacity - Programming Fundamentals and the Web Project 1

##The Movie class adheres to the requirements of fresh_tomatoes.py to display movies in an HTML Format

class Movie():

    ##Construct the Movie with the paratemers received
    def __init__ (self,str_title, str_storyline, str_poster_image, str_youtube_trailer):
        self.title = str_title
        self.storyline = str_storyline
        self.poster_image_url = str_poster_image
        self.trailer_youtube_url = str_youtube_trailer
        
        
