from pathlib import Path

def Absolute_path(filepath):
    relative = Path(filepath)
    return relative.absolute()