from src.facade.movie_player_facade import MoviePlayerFacade

def main():

    movie_player = MoviePlayerFacade()
    movie_player.play_movie(
        "/path/to/movie", 
        "/path/to/subtitles"
    )

if __name__ == "__main__":
    main()