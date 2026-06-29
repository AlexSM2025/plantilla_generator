# app.py

import streamlit as st

from templates.integrated_backup.form import integrated_backup_form
from templates.integrated_backup.render import render_integrated_backup

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Proposal Generator",
    layout="centered"
)

st.title("Proposal Generator")

# =========================
# TEMPLATE SELECTION
# =========================

proposal_type = st.selectbox(
    "Proposal Type",
    [
        "Integrated Backup"
        # Más adelante:
        # "HDM Proposal"
    ]
)

# =========================
# INTEGRATED BACKUP
# =========================

if proposal_type == "Integrated Backup":

    data = integrated_backup_form()

    if st.button("Generate Proposal"):

        pdf = render_integrated_backup(data)

        st.download_button(
            label="Download Proposal PDF",
            data=pdf,
            file_name="proposal.pdf",
            mime="application/pdf"
        )

# =========================
# FUTURE TEMPLATE
# =========================

# elif proposal_type == "HDM Proposal":
#
#     data = hdm_proposal_form()
#
#     if st.button("Generate Proposal"):
#
#         pdf = render_hdm_proposal(data)
#
#         st.download_button(
#             label="Download Proposal PDF",
#             data=pdf,
#             file_name="proposal.pdf",
#             mime="application/pdf"
#         )
