# app.py

import streamlit as st

from templates.integrated_backup.form import integrated_backup_form
from templates.integrated_backup.render import render_integrated_backup
from templates.hdm_proposal.render import render_page1
from templates.hdm_proposal.form import hdm_proposal_form

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
        "Integrated Backup",
        "HDM Proposal",
        "Propel Proposal"
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
# HDM PROPOSAL
# =========================

elif proposal_type == "HDM Proposal":

    data = hdm_proposal_form()

    html = render_page1(data)
    
    st.components.v1.html(
        html,
        width=1400,
        height=900,
        scrolling=True
    )
#
#     data = hdm_proposal_form()
#
     if st.button("Generate Proposal"):
         #pdf = render_hdm_proposal(data)
         pdf = render_page1(data)

         st.download_button(
             label="Download Proposal PDF",
             data=pdf,
             file_name="HDM_proposal.pdf",
             mime="application/pdf"
         )

# =========================
# PROPEL PROPOSAL
# =========================

#elif proposal_type == "Propel Proposal":

    #data = propel_proposal_form()

    #html = render_page1(data)
    
    #st.components.v1.html(
        #html,
        #width=1400,
        #height=900,
        #scrolling=True
    #)

#     data = hdm_proposal_form()
#
#     if st.button("Generate Proposal"):
#         pdf = render_hdm_proposal(data)
#
#         st.download_button(
#             label="Download Proposal PDF",
#             data=pdf,
#             file_name="HDM_proposal.pdf",
#             mime="application/pdf"
#         )
