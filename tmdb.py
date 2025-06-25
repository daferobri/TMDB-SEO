import os
from tmdbv3api import Account, TMDb, Movie

tmdb = TMDb()
tmdb.api_key = os.environ.get('TMDB_API_KEY')

account = Account()
details = account.details()

print('You are logged in as', details.username)

movie = Movie()

query = input('Movie to add to watchlist: ')
s = movie.search(query)
first_result = s[0]
print(f'Adding {first_result.title} to watchlist')
account.add_to_watchlist(first_result.id, "movie")