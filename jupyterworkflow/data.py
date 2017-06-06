import os
from urllib.request import urlretrieve

import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('seaborn')

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data

    Parameters
    ----------
    filename : string (optional)
        location to dave the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, forces download of the data

    Returns
    -------
    data : pandas.DataFrame
        The fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv(filename, index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
