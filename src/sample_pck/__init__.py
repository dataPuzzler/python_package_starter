from pathlib import Path 

repo_dir = Path(__file__).parent.parent.parent
__repo_dir__ = repo_dir

# read from file manipulated by CI Pipeline
with repo_dir.joinpath('VERSION').open() as f:
    __version__ =  f.read().strip()