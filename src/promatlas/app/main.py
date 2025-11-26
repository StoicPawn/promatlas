"""Entry point for the PromAtlas Streamlit application."""

import streamlit as st

from promatlas.config import get_settings


def main() -> None:
    """Render the PromAtlas landing page."""

    settings = get_settings()
    st.set_page_config(page_title="PromAtlas", layout="wide")
    st.title("PromAtlas")
    st.write(
        """
        Piattaforma unificata di rischio territoriale e settoriale basata su dati open.
        Usa i menu laterali per navigare i moduli (in sviluppo).
        """
    )

    st.info(
        f"Database analitico previsto in: {settings.database_path} \n"
        "Esegui gli script di download/ETL per popolare i dati."
    )


if __name__ == "__main__":
    main()
