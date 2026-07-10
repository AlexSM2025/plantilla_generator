from jinja2 import Environment, FileSystemLoader
import os
import base64


def img_to_base64(path):
    with open(path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
        return f"data:image/png;base64,{encoded}"

def load_css():
    base_dir = os.path.dirname(__file__)

    css_path = os.path.join(base_dir, "styles.css")

    if not os.path.exists(css_path):
        raise FileNotFoundError(f"CSS not found at: {css_path}")

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
    hero_image = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "images", "hero_banner.png")
    )

    location_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "location.png")
    )

    calendar_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "calendar.png")
    )

    backup_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "backup.png")
    )

    piggy_bank_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "piggy-bank.png")
    )
    
    shield_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "shield.png")
    )
    
    home_energy_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "home-energy.png")
    )
    
    growth_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "growth.png")
    )
    
    leaf_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "leaf.png")
    )

    # =========================
    # FINANCIAL HIGHLIGHTS ICONS
    # =========================
    solar_panel_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "solar_panel_icon.png")
    )
    
    battery_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "battery_icon.png")
    )
    
    production_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "production_icon.png")
    )
    
    whole_home_backup_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "whole_home_backup_icon.png")
    )
    
    roof_mount_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "roof_mount_icon.png")
    )
    
    scope_document_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "scope_document_icon.png")
    )
    
    payback_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "payback_icon.png")
    )
    
    roi_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "roi_icon.png")
    )
    
    savings_dollar_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "savings_dollar_icon.png")
    )
    
    trophy_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "trophy_icon.png")
    )
    
    check_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "check_icon.png")
    )

    financing_partner_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "financing_partner.png")
    )
    
    utility_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "utility.png")
    )
    
    advisor_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "advisor.png")
    )
    
    globe_icon = img_to_base64(
        os.path.join(base_dir, "..", "..", "templates", "hdm_proposal", "assets", "icons", "globe.png")
    )


    html = template.render(

        css=css,

        maelo_logo=maelo_logo,
        bright_logo=bright_logo,
        hdm_logo=hdm_logo,

        hero_image=hero_image,

        location_icon=location_icon,
        calendar_icon=calendar_icon,
        backup_icon=backup_icon,

        piggy_bank_icon=piggy_bank_icon,
        shield_icon=shield_icon,
        home_energy_icon=home_energy_icon,
        growth_icon=growth_icon,
        leaf_icon=leaf_icon,

        solar_panel_icon=solar_panel_icon,
        battery_icon=battery_icon,
        production_icon=production_icon,
        whole_home_backup_icon=whole_home_backup_icon,
        roof_mount_icon=roof_mount_icon,
        scope_document_icon=scope_document_icon,
        
        payback_icon=payback_icon,
        roi_icon=roi_icon,
        savings_dollar_icon=savings_dollar_icon,
        
        trophy_icon=trophy_icon,
        check_icon=check_icon,

        financing_partner_icon=financing_partner_icon,
        utility_icon=utility_icon,
        advisor_icon=advisor_icon,
        globe_icon=globe_icon,

        **data
    )

    return html
