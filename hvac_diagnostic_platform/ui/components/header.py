from pathlib import Path
import base64
import streamlit as st


def load_custom_css() -> None:
    css_path = Path(__file__).resolve().parents[2] / "assets" / "styles" / "custom.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def render_sidebar_logo() -> None:
    logo_path = Path(__file__).resolve().parents[2] / "assets" / "logo" / "logo.png"
    if logo_path.exists():
        encoded = base64.b64encode(logo_path.read_bytes()).decode()
        st.sidebar.markdown(
            f"""
            <div class="sidebar-logo">
                <img src="data:image/png;base64,{encoded}" alt="Logo">
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_hero(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-title">{title}</div>
            <div class="hero-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero_image(title: str, subtitle: str, image_name: str = "hero_hvac.jpg") -> None:
    img_path = Path(__file__).resolve().parents[2] / "assets" / "images" / image_name

    if img_path.exists():
        encoded = base64.b64encode(img_path.read_bytes()).decode()
        ext = img_path.suffix.lower().replace(".", "")
        if ext == "jpg":
            ext = "jpeg"

        st.markdown(
            f"""
            <div class="hero-image">
                <img src="data:image/{ext};base64,{encoded}" alt="Hero Image">
                <div class="hero-overlay">
                    <h2>{title}</h2>
                    <p>{subtitle}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        render_hero(title, subtitle)


def render_panel_title(title: str) -> None:
    st.markdown(
        f"""
        <div class="panel-card">
            <div class="panel-title">{title}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_icon_card(title: str, icon_name: str) -> None:
    icon_path = Path(__file__).resolve().parents[2] / "assets" / "icons" / icon_name

    if icon_path.exists():
        encoded = base64.b64encode(icon_path.read_bytes()).decode()
        ext = icon_path.suffix.lower().replace(".", "")
        if ext == "jpg":
            ext = "jpeg"

        st.markdown(
            f"""
            <div class="icon-card">
                <img src="data:image/{ext};base64,{encoded}" alt="{title}">
                <div>{title}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="icon-card">
                <div style="font-size: 1.1rem; font-weight: 600;">{title}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

