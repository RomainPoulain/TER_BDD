import pandas as pd
import recordlinkage as rl

# Name data for indexing
names_1 = ['alfred', 'bob', 'calvin', 'hobbes', 'rusty']
names_2 = ['alfred', 'danny', 'callum', 'hobie', 'rusty']

# Convert to DataFrames
df_a = pd.DataFrame(pd.Series(names_1, name='names'))
df_b = pd.DataFrame(pd.Series(names_2, name='names'))

# Create indexing object
indexer = rl.SortedNeighbourhoodIndex(on='names', window=3)

# Create pandas MultiIndex containing candidate links
candidate_links = indexer.index(df_a, df_b)