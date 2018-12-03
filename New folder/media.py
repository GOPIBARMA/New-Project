import webbrowser
class Movie():
    def __init__(self,movie_title,movie_storyline,movie_poster_image,youtube_trailer_url):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image=movie_poster_image
        self.trailer_youtube_url=youtube_trailer_url
        
    
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
