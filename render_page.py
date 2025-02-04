import math

import streamlit as st


def render_gdp(gdp_df):
    min_value = gdp_df["Year"].min()
    max_value = gdp_df["Year"].max()

    from_year, to_year = st.slider(
        "Which years are you interested in?",
        min_value=min_value,
        max_value=max_value,
        value=[min_value, max_value],
    )

    countries = gdp_df["Country Code"].unique()

    if not len(countries):
        st.warning("Select at least one country")

    selected_countries = st.multiselect(
        "Which countries would you like to view?",
        countries,
        ["DEU", "FRA", "GBR", "BRA", "MEX", "JPN"],
    )

    ""
    ""
    ""

    # Filter the data
    filtered_gdp_df = gdp_df[
        (gdp_df["Country Code"].isin(selected_countries))
        & (gdp_df["Year"] <= to_year)
        & (from_year <= gdp_df["Year"])
    ]

    st.header("GDP over time", divider="gray")

    ""

    st.line_chart(
        filtered_gdp_df,
        x="Year",
        y="GDP",
        color="Country Code",
    )

    ""
    ""

    first_year = gdp_df[gdp_df["Year"] == from_year]
    last_year = gdp_df[gdp_df["Year"] == to_year]

    st.header(f"GDP in {to_year}", divider="gray")

    ""

    cols = st.columns(4)

    for i, country in enumerate(selected_countries):
        col = cols[i % len(cols)]

        with col:
            first_gdp = (
                first_year[first_year["Country Code"] == country]["GDP"].iat[0]
                / 1000000000
            )
            last_gdp = (
                last_year[last_year["Country Code"] == country]["GDP"].iat[0]
                / 1000000000
            )

            if math.isnan(first_gdp):
                growth = "n/a"
                delta_color = "off"
            else:
                growth = f"{last_gdp / first_gdp:,.2f}x"
                delta_color = "normal"

            st.metric(
                label=f"{country} GDP",
                value=f"{last_gdp:,.0f}B",
                delta=growth,
                delta_color=delta_color,
                border=True,
            )


def render_ump(unemp_data):
    min_value = unemp_data["Year"].min()
    max_value = unemp_data["Year"].max()

    from_year, to_year = st.slider(
        "Which years are you interested in?",
        min_value=min_value,
        max_value=max_value,
        value=[min_value, max_value],
    )

    countries = unemp_data["Country Code"].unique()

    if not len(countries):
        st.warning("Select at least one country")

    selected_countries = st.multiselect(
        "Which countries would you like to view?",
        countries,
        ["DEU", "FRA", "GBR", "BRA", "MEX", "JPN"],
    )

    ""
    ""
    ""

    # Filter the data
    filtered_gdp_df = unemp_data[
        (unemp_data["Country Code"].isin(selected_countries))
        & (unemp_data["Year"] <= to_year)
        & (from_year <= unemp_data["Year"])
    ]

    st.header("Unemployment over time", divider="gray")

    ""

    st.line_chart(
        filtered_gdp_df,
        x="Year",
        y="Unemployment",
        color="Country Code",
    )

    ""
    ""

    first_year = unemp_data[unemp_data["Year"] == from_year]
    last_year = unemp_data[unemp_data["Year"] == to_year]

    st.header(f"Unemployment in {to_year}", divider="gray")

    ""

    cols = st.columns(4)

    for i, country in enumerate(selected_countries):
        col = cols[i % len(cols)]  # Distributes columns evenly

        with col:
            # Extract unemployment values for the first and last year
            first_unemployment = first_year[first_year["Country Code"] == country][
                "Unemployment"
            ].values
            last_unemployment = last_year[last_year["Country Code"] == country][
                "Unemployment"
            ].values

            # Handle missing values safely
            if (
                len(first_unemployment) == 0
                or len(last_unemployment) == 0
                or math.isnan(first_unemployment[0])
                or math.isnan(last_unemployment[0])
            ):
                growth = "n/a"
                delta_color = "off"
                last_value = "n/a"
            else:
                first_unemployment = first_unemployment[0]
                last_unemployment = last_unemployment[0]

                # Calculate growth
                if first_unemployment == 0:
                    growth = "n/a"  # Avoid division by zero
                else:
                    growth = f"{(last_unemployment - first_unemployment):,.2f}%"

                delta_color = "inverse"
                last_value = f"{last_unemployment:,.3f}%"

            # Display unemployment metric
            st.metric(
                label=f"{country} Unemployment",
                value=last_value,
                delta=growth,
                delta_color=delta_color,
                border=True,
            )


def render_pop():
    st.write("Pop")
