import streamlit as st


def get_form_data():

    last_name = st.text_input(
        "Last Name",
        placeholder="Huang"
    )

    city = st.text_input(
        "City",
        placeholder="San Jose"
    )

    project_value = st.number_input(
        "Total Project Value",
        min_value=0,
        value=19250,
        step=100
    )

    cash_discount = st.number_input(
        "Cash Discount",
        min_value=0,
        value=1000,
        step=100
    )

    hdm_carveout = st.number_input(
        "HDM Financial Carve-out",
        min_value=0,
        value=4562,
        step=100
    )

    net_capital = (
        project_value
        - cash_discount
        - hdm_carveout
    )

    st.metric(
        "Net Capital Requirement",
        f"${net_capital:,.0f}"
    )

    return {
        "last_name": last_name,
        "city": city,
        "project_value": project_value,
        "cash_discount": cash_discount,
        "hdm_carveout": hdm_carveout,
        "net_capital": net_capital
    }
