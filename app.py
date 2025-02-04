import streamlit as st
from streamlit_option_menu import option_menu

from get_data import *
from render_page import *

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title="GDP dashboard",
    page_icon=":earth_americas:",
)

# -----------------------------------------------------------------------------
# Get the data

gdp_df = get_gdp_data()
unemp_data = get_unemp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
"""
# :earth_americas: The Global Stats Buffet

"""

# Add some spacing
""
""


# on_change callback
def on_change(key):
    pass


# Initialize selected3 in session_state if not already set
if "selected_option" not in st.session_state:
    st.session_state.selected_option = 0

options_list = ["GDP", "Unemployment"]

selected3 = option_menu(
    menu_title=None,
    options=options_list,
    icons=[None, None, None, None],
    menu_icon=None,
    default_index=st.session_state.selected_option,
    orientation="horizontal",
    on_change=on_change,
    key="nav_bar",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"display": "none"},
        "nav-link": {
            "font-size": "18px",
            "font-family": "sans-serif",
            "text-align": "center",
            "margin": "0px",
            "white-space": "pre-wrap",
            "border-radius": "5px",
            "--hover-color": "#eee",
            "padding": "7px",
            "color": "black",
            "background": "#f2f2f2",
        },
        "nav-link-selected": {
            "background": "linear-gradient(to right, #4A92C6 , #787FD6)",
            "font-weight": "bold",
            "color": "black",
        },
    },
)

st.session_state.selected_option = options_list.index(selected3)

if st.session_state.selected_option == 0:
    render_gdp(gdp_df)
if st.session_state.selected_option == 1:
    render_ump(unemp_data)
