import os
import pandas as pd
import sqlalchemy as db
import json
from tmdbv3api import Account, TMDb, Movie

tmdb = TMDb()
tmdb.api_key = os.environ.get('TMDB_API_KEY')

account = Account()
details = account.details()

print('You are logged in as', details.username)

movie = Movie()

query = input('Movie to add to watchlist: ')

s = movie.search(query)._json.get('results', [])
for result in s:
	for key, value in result.items():
		if isinstance(value, (list, dict)):
			result[key] = json.dumps(result[key])

s_df = pd.DataFrame(s)

engine = db.create_engine('sqlite:///tmdb.db')

s_df.to_sql('movies', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
  query_result = connection.execute(db.text("SELECT * FROM movies;")).fetchall()
  print(pd.DataFrame(query_result))
