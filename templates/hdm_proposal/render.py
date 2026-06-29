from jinja2 import Environment, FileSystemLoader
import os
import base64


# =========================
# CONVERT IMAGE TO BASE64
# =========================
def img_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()


# =========================
# RENDER PAGE 1
# =========================
def render_page1(data):
    """
    Renderiza la Página 1 del Proposal HDM.
    Retorna HTML listo para Streamlit o PDF.
    """

    base_dir = os.path.dirname(__file__)

    env = Environment(
        loader=FileSystemLoader(base_dir)
    )

    template = env.get_template("page1.html")

    # =========================
    # LOGOS (BASE64)
    # =========================
    maelo_logo = img_to_base64(
        os.path.join(base_dir, "../../assets/logos/maelo_logo.png")
    )

    bright_logo = img_to_base64(
        os.path.join(base_dir, "../../assets/logos/bright_energy_logo.png")
    )

    hdm_logo = img_to_base64(
        os.path.join(base_dir, "../../assets/logos/hdm_logo.png")
    )

    # =========================
    # RENDER HTML
    # =========================
    html = template.render(

        # Logos (BASE64 strings)
        maelo_logo=maelo_logo,
        bright_logo=bright_logo,
        hdm_logo=hdm_logo,

        # Form data
        **data
    )

    return html
