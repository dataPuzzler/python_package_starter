from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Sample Package",
    install_requires=[
        "numpy",
        "requests",
        "multilevel_py >= 0.2.0" 
    ],
    extras_require={
        "dotenv": ["python-dotenv"],
    },
)