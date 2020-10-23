"""
Author: Stefano Francesco Pitton
Mail: stefanofrancesco.pitton@gmail.com
Created: 23/10/2020

Description:
------------
Implementation of test_1. The code fetch the data from a URL, parse it as JSON and then store it into a DataFrame.
For each albumId, the code print the number of pictures available.
"""
# Required libraries
import json
import urllib.request
import pandas as pd

# url
url = "https://jsonplaceholder.typicode.com/photos"

# download data
data = urllib.request.urlopen(url).read()

# parse json object
obj = json.loads(data)

# convert list into DataFrame
album_df = pd.DataFrame(obj)

# groupby albumId and compute number of pictures
pict_num_df = album_df.groupby(['albumId']).count()['id']

# print for each album the number of pictures:
for id_ in range(len(pict_num_df)):
    print('Album ID: {}, number of pictures: {}'.format(id_+1, pict_num_df.iloc[id_]))