import streamlit as st


def hdm_proposal_form():
    """
    Renderiza el formulario de la propuesta HDM
    y devuelve un diccionario con toda la información.
    """

    st.subheader("Customer Information")

    customer_last_name = st.text_input(
        "Last Name",
        placeholder="Smith"
    )

    customer_address = st.text_input(
        "Street Address",
        placeholder="123 Main Street"
    )

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        customer_city = st.text_input(
            "City",
            placeholder="San Diego"
        )

    with col2:
        customer_state = st.text_input(
            "State",
            placeholder="CA"
        )

    with col3:
        customer_zip = st.text_input(
            "Zip Code",
            placeholder="92101"
        )


    st.subheader("Installation")

    installation_target = st.text_input(
        "Installation Target",
        placeholder="SUMMER 2026"
    )

    data = {
        "customer_last_name": customer_last_name,
        "customer_address": customer_address,
        "customer_city": customer_city,
        "customer_state": customer_state,
        "customer_zip": customer_zip,
        "installation_target": installation_target,
    }

    return data
