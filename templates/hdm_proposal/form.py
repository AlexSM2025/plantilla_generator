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

    backup_description = st.text_area(
        "Whole-Home Backup Description",
        value="With Managed Energy Consumption During Extended Outages",
        height=80
    )

    st.subheader("Installation Investment")

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        cost_of_waiting_value = st.text_input(
            "Cost of Waiting",
            placeholder="798,600"
        )

    with col2:
        status_quo_value = st.text_input(
            "Status Quo Value",
            placeholder="798,600"
        )

    with col3:
        deferred_ownership_value = st.text_input(
            "Deferred Ownership",
            placeholder="72,863"
        )

    with col4:
        direct_ownership_value = st.text_input(
            "Direct Ownership",
            placeholder="103,959"
        ) 

    data = {
        "customer_last_name": customer_last_name,
        "customer_address": customer_address,
        "customer_city": customer_city,
        "customer_state": customer_state,
        "customer_zip": customer_zip,
        "installation_target": installation_target,
        "backup_description": backup_description,
        "cost_of_waiting_value": cost_of_waiting_value,
        "status_quo_value": status_quo_value,
        "deferred_ownership_value": deferred_ownership_value,
        "direct_ownership_value": direct_ownership_value,
    }

    return data
