# Libraries
import os
import pandas as pd
from arcgis.gis import GIS
from arcgis.layers import Service
from dotenv import load_dotenv
load_dotenv()

# API Authentication
# We Dont Need to login for a public Project
gis=GIS()

# Access a hosted Data Source and Query USA data
src_url = os.getenv('src_url')
fl = Service(src_url)
fset_usa = fl.query(where=os.getenv('country'))
fset_usa.sdf.to_csv(os.getenv('covid_data_out'))

# Get USA Country level Boundaries
us_states_item = gis.content.get(os.getenv('content'))
us_states_flayer = us_states_item.layers[0]
us_states_df = us_states_flayer.query(as_df=True)
us_states_df.to_csv(os.getenv('country_data_out'))
