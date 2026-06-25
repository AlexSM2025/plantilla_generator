# app.py

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.utils import ImageReader
import tempfile
import os

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Proposal Generator",
    layout="centered"
)

st.title("Proposal Generator")

# =========================
# FORM
# =========================

last_name = st.text_input(
    "Last Name",
    placeholder="Huang"
)

city = st.text_input(
    "City",
    placeholder="San Jose"
)


residence_line_1 = f"{last_name} Residence"

residence_line_2 = f"({city})"


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

calculated_net = (
    project_value
    - cash_discount
    - hdm_carveout
)

net_capital = st.number_input(
    "Net Capital Requirement",
    min_value=0,
    value=int(calculated_net),
    step=100
)

# =========================
# GENERATE BUTTON
# =========================

if st.button("Generate Proposal"):

    # -------------------------
    # LOAD TEMPLATE
    # -------------------------

    template = Image.open(
        "assets/images/solar_battery_hdm.png"
    ).convert("RGB")

    draw = ImageDraw.Draw(template)

    # -------------------------
    # LOAD FONTS
    # -------------------------

    font_regular = ImageFont.truetype(
        "assets/fonts/Barlow-Regular.ttf",
        28
    )

    font_bold = ImageFont.truetype(
        "assets/fonts/Barlow-Bold.ttf",
        40
    )

    font_medium = ImageFont.truetype(
        "assets/fonts/Barlow-SemiBold.ttf",
        34
    )

    # -------------------------
    # FORMAT VALUES
    # -------------------------

    project_value_text = f"${project_value:,.0f}"
    cash_discount_text = f"${cash_discount:,.0f}"
    hdm_text = f"${hdm_carveout:,.0f}"
    net_text = f"${net_capital:,.0f}"

    # -------------------------
    # DRAW TEXT
    # -------------------------

    # Residence Name
    # First line
    draw.text(
        (1370, 30),
        residence_line_1,
        fill="black",
        font=font_regular
    )
    
    # Second line
    draw.text(
        (1370, 55),
        residence_line_2,
        fill="black",
        font=font_regular
    )

    # Total Project Value
    draw.text(
        (338, 340),
        project_value_text,
        fill="black",
        font=font_bold
    )

    # Cash Discount
    draw.text(
        (1444, 424),
        cash_discount_text,
        fill="black",
        font=font_medium
    )

    # HDM Carve-Out
    draw.text(
        (1444, 517),
        hdm_text,
        fill="black",
        font=font_medium
    )

    # Net Capital Requirement
    draw.text(
        (810, 757),
        net_text,
        fill="black",
        font=font_bold
    )

    # -------------------------
    # SAVE TEMP IMAGE
    # -------------------------

    temp_image = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    )

    template.save(temp_image.name)

    # -------------------------
    # CREATE PDF
    # -------------------------

    pdf_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    c = canvas.Canvas(
        pdf_file.name,
        pagesize=landscape(template.size)
    )

    c.drawImage(
        ImageReader(temp_image.name),
        0,
        0,
        width=template.width,
        height=template.height
    )

    c.save()

    # -------------------------
    # DOWNLOAD BUTTON
    # -------------------------

    with open(pdf_file.name, "rb") as pdf:

        st.download_button(
            label="Download Proposal PDF",
            data=pdf,
            file_name="proposal.pdf",
            mime="application/pdf"
        )

    # -------------------------
    # CLEANUP
    # -------------------------

    os.unlink(temp_image.name)
    os.unlink(pdf_file.name)
