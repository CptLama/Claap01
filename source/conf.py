# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CLAAP01_PL'
copyright = '2025, Piotr Lukasiewicz'
author = 'Piotr Lukasiewicz'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'pl'

today = '25 lis 2025'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # To jest najważniejsza linia - wymusza polskie nazewnictwo w PDF
    'babel': '\\usepackage[polish]{babel}',
    
    # Opcjonalnie: To ustawienie sprawia, że rozdziały zaczynają się
    # od razu na kolejnej stronie, a nie tylko na nieparzystej (oszczędza papier/miejsce)
    'extraclassoptions': 'openany,oneside',
}