import media
import webbrowser
import fresh_tomatoes
orange=media.Movie("Orange"," True love","./img/orange.jpg",
                   "https://www.youtube.com/watch?v=sW4bXzRAj9I")
robo=media.Movie("Robot 2.O"," Robitics","./img/robo.jpg",
                 "https://www.youtube.com/watch?v=QDKY8CRe1-0&t=57s") 
brucelee=media.Movie(" BruceLee","The Fighter","./img/bruce lee.jpg",
                     "https://www.youtube.com/watch?v=gr3lFtOqkuc")
gabbar=media.Movie("Gabbar Singh", " Real hero","./img/gabber.jpg",
                   "https://www.youtube.com/watch?v=FpFoQPj4sgs");
zindagi=media.Movie("Unnadi Okate Zindagi","Friendship","./img/zindagi.jpg",
                    "https://www.youtube.com/watch?v=z678PtuCIHo")
fight_club = media.Movie(
    "Fight Club",
    " wonderful",
    "http://goo.gl/BR5nIh",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

#print(avatar.poster_image)
#avatar.showTrailer()

movies=[orange,robo,brucelee,gabbar,zindagi,fight_club]
fresh_tomatoes.open_movies_page(movies)
