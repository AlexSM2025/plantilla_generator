from jinja2 import Environment, FileSystemLoader
import os


def render_page1(data):
    """
    Renderiza la Página 1 del Proposal HDM.
    Retorna el HTML listo para mostrarse o convertirlo a PDF.
    """

    base_dir = os.path.dirname(__file__)

    env = Environment(
        loader=FileSystemLoader(base_dir)
    )

    template = env.get_template("page1.html")

    html = template.render(

        # Logos
        maelo_logo="assets/logos/maelo_logo.png",
        bright_logo="assets/logos/bright_energy_logo.png",
        hdm_logo="assets/logos/hdm_logo.png",

        # Variables del formulario
        **data
    )

    return html
