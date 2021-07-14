from pathlib import Path

def Absolutepath(filepath):
    relative = Path(filepath)
    return relative.absolute()