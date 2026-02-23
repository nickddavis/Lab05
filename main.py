from media import StreamingService, TVShow, Movie

techflix = StreamingService()

with open("input/tv_shows.txt") as f:
    shows = f.readlines()

print(f"{'*'*10}Part One--Adding TV Shows{'*'*10}")
for line in shows:
    items = line.strip("\n").split(",")
    cast = [items[5], items[6], items[7]]
    new_show = TVShow(items[0], items[1], items[2], int(items[3]), cast, int(items[4]))
    techflix.add_content(new_show)

with open("input/movies.txt") as f:
    movies = f.readlines()

print(f"{'*'*10}Part Two--Adding Movies{'*'*10}")
for line in movies:
    items = line.strip("\n").split(",")
    cast = [items[5], items[6], items[7]]
    new_movie = Movie(items[0], items[1], items[2], int(items[3]), cast, int(items[4]))
    techflix.add_content(new_movie)

print(f"{'*'*10}Part Three--Getting Info{'*'*10}")
for content in techflix.available_content:
    content.get_info()

print(f"{'*'*10}Part Four--Watching Media{'*'*10}")
techflix.watch("Dr. Who")
techflix.watch("Doctor Who")
techflix.watch("Shawshank Redemption")
techflix.watch("The Shawshank Redemption") 