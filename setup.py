from setuptools import setup, find_packages

setup(
    name='AdminCoProjet2',
    version='1.0.0',
    packages=find_packages(),
    description='Ce projet implémente une version interactive du jeu classique Pierre/Feuille/Ciseaux.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Chahan Donikian',
    author_email='chahan.donikian@cpe.fr',
    url='https://github.com/ChahanD/AdminCoProjet2',
    install_requires=[
        # Liste des dépendances de votre projet
    ],
)
