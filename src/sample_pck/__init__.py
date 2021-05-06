from pathlib import Path 

repo_dir = Path(__file__).parent.parent.parent
__repo_dir__ = repo_dir

# read from file manipulated by CI Pipeline
__version__ =  repo_dir.joinpath('VERSION').open().read().strip()