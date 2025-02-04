import math
from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time.
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent / "data/gdp_data.csv"
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2023

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # -
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ["Country Code"],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        "Year",
        "GDP",
    )

    # Convert years from string to integers
    gdp_df["Year"] = pd.to_numeric(gdp_df["Year"])

    return gdp_df


@st.cache_data
def get_unemp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time.
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent / "data/unemp_data.csv"
    raw_unemp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1991
    MAX_YEAR = 2023

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # -
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    unemp_df = raw_unemp_df.melt(
        ["Country Code"],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        "Year",
        "Unemployment",
    )

    # Convert years from string to integers
    unemp_df["Year"] = pd.to_numeric(unemp_df["Year"])

    return unemp_df
