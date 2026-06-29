from jinja2 import Environment, FileSystemLoader
import os
import base64


def img_to_base64(path):
    with open(path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
        return f"data:image/png;base64,{encoded}"

def load_css():
    base_dir = os.path.dirname(__file__)
    css_path = os.path.join(base_dir, "../../styles.css")

    with open(css_path, "r", encoding="utf-8") as f:
        return f.read()


def render_page1(data):

    base_dir = os.path.dirname(__file__)
    css = load_css()

    env = Environment(
        loader=FileSystemLoader(base_dir)
    )

    template = env.get_template("page1.html")

    # =========================
    # RUTAS CORRECTAS (CLAVE)
    # =========================
    assets_dir = os.path.abspath(
        os.path.join(base_dir, "..", "..", "assets", "logos")
    )

    maelo_logo = img_to_base64(os.path.join(assets_dir, "maelo_logo.png"))
    bright_logo = img_to_base64(os.path.join(assets_dir, "bright_logo.png"))
    hdm_logo = img_to_base64(os.path.join(assets_dir, "hdm_logo.png"))

    html = template.render(

        css=css,

        maelo_logo=maelo_logo,
        bright_logo=bright_logo,
        hdm_logo=hdm_logo,

        **data
    )

    return html
