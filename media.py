#class for defining the content self variables
class MediaContent():
    #initializes self vatriables
    def __init__ (self,title,genre,rating,runtime,cast, extra=None):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.runtime = runtime
        self.cast = cast
        self.extra = extra
    def get_info(self):
        info = (self.title, self.genre, self.rating, self.runtime, self.cast) if self.extra is None else (self.title, self.genre, self.rating, self.runtime, self.cast, self.extra)
        print("get_info", info)
        return info
#gets the runtime
    def get_runtime(self):
        print("get_runtime ->", self.runtime)
        return self.runtime
#class specificly for movies
class Movie(MediaContent):
    def __init__(self, title, genre, rating, runtime, cast, year=None):
        super().__init__(title, genre, rating, runtime, cast, extra=year)
        self.year = year
#plays the movie
    def play(self):
        out = f"Now playing movie: {self.title} ({self.year})" if self.year else f"Now playing movie: {self.title}"
        print(out)
        return out
# class specificly for TV shows
class TVShow(MediaContent):
    def __init__(self, title, genre, rating, runtime, cast, seasons=None):
        super().__init__(title, genre, rating, runtime, cast, extra=seasons)
        self.seasons = seasons
#plays the TV show
    def play(self):
        out = f"Now playing TV show: {self.title} - Season count: {self.seasons}" if self.seasons is not None else f"Now playing TV show: {self.title}"
        print(out)
        return out
#class for the streaming service
class StreamingService():
    def __init__(self):
        self.available_content = []
# finds avalable content
    def avalable_content(self):
        print("avalable_content -> returning available_content list")
        return self.available_content
#adds content
    def add_content(self, content):
        print(f"add_content -> adding {content.title}")
        self.available_content.append(content)
        return True
#removes content
    def remove_content(self, content):
        if content in self.available_content:
            self.available_content.remove(content)
            print(f"remove_content -> removed {content.title}")
            return True
        print(f"remove_content -> {content.title} not found")
        return False
#watches content
    def watch(self, title):
        for content in self.available_content:
            if content.title == title:
                print(f"watch -> found {title}")
                return content.play()
        msg = f"{title} is not available on this streaming service."
        print(msg)
        return None
    