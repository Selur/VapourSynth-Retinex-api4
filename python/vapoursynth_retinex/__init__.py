"""Ships the Retinex VapourSynth plugin and installs it into the autoload directory."""
import os
import shutil
import sys
from pathlib import Path

_EXTENSIONS = {'win32': '.dll', 'darwin': '.dylib'}


def plugin_path() -> Path:
    """Path of the plugin binary bundled in this package."""
    ext = _EXTENSIONS.get(sys.platform, '.so')
    for f in Path(__file__).resolve().parent.iterdir():
        if f.suffix == ext and 'retinex' in f.name.lower():
            return f
    raise FileNotFoundError('Retinex plugin binary not found in ' + str(Path(__file__).parent))


def autoload_dir() -> Path:
    """Per-user VapourSynth plugin autoload directory."""
    if sys.platform == 'win32':
        return Path(os.environ['APPDATA']) / 'VapourSynth' / 'plugins64'
    if sys.platform == 'darwin':
        return Path.home() / 'Library' / 'Application Support' / 'VapourSynth' / 'plugins'
    return Path(os.environ.get('XDG_CONFIG_HOME') or Path.home() / '.config') / 'vapoursynth' / 'plugins'


def install(directory=None) -> Path:
    """Copy the plugin into the autoload directory (or `directory`) and return the destination."""
    src = plugin_path()
    dest_dir = Path(directory) if directory else autoload_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    shutil.copy2(src, dest)
    return dest


def uninstall(directory=None) -> bool:
    """Remove the plugin from the autoload directory. Returns whether a file was removed."""
    dest = (Path(directory) if directory else autoload_dir()) / plugin_path().name
    if dest.exists():
        dest.unlink()
        return True
    return False
