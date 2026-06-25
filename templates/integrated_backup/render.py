from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.utils import ImageReader

from .config import FIELDS

import tempfile
import os
import io


def render_integrated_backup(data):

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
    # FORMAT TEXT
    # -------------------------

    residence_line_1 = f"{data['last_name']} Residence"
    residence_line_2 = f"({data['city']})"

    project_value_text = f"${data['project_value']:,.0f}"
    cash_discount_text = f"${data['cash_discount']:,.0f}"
    hdm_text = f"${data['hdm_carveout']:,.0f}"
    net_text = f"${data['net_capital']:,.0f}"

    # -------------------------
    # DRAW TEXT
    # -------------------------

    draw.text(
        (
            FIELDS["residence_line_1"]["x"],
            FIELDS["residence_line_1"]["y"]
        ),
        residence_line_1,
        fill="black",
        font=font_regular
    )

    draw.text(
        (
            FIELDS["residence_line_2"]["x"],
            FIELDS["residence_line_2"]["y"]
        ),
        residence_line_2,
        fill="black",
        font=font_regular
    )

    draw.text(
        (
            FIELDS["project_value"]["x"],
            FIELDS["project_value"]["y"]
        ),
        project_value_text,
        fill="black",
        font=font_bold
    )

    draw.text(
        (
            FIELDS["cash_discount"]["x"],
            FIELDS["cash_discount"]["y"]
        ),
        cash_discount_text,
        fill="black",
        font=font_medium
    )

    draw.text(
        (
            FIELDS["hdm_carveout"]["x"],
            FIELDS["hdm_carveout"]["y"]
        ),
        hdm_text,
        fill="black",
        font=font_medium
    )

    draw.text(
        (
            FIELDS["net_capital"]["x"],
            FIELDS["net_capital"]["y"]
        ),
        net_text,
        fill="black",
        font=font_bold
    )

    # -------------------------
    # TEMP IMAGE
    # -------------------------

    temp_image = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    )

    template.save(temp_image.name)

    # -------------------------
    # PDF
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
    # RETURN BYTES
    # -------------------------

    with open(pdf_file.name, "rb") as pdf:
        pdf_bytes = io.BytesIO(pdf.read())

    os.unlink(temp_image.name)
    os.unlink(pdf_file.name)

    return pdf_bytes
