from os import environ
from typing import Any
from pathlib import Path
from dotenv import load_dotenv

class XdgBaseDirs:
    defaults = {
        "config": "$HOME/.config/",
        "data": "$HOME/.local/share/",
        "state": "$HOME/.local/state/",
        "cache": "$HOME/.cache/",
        "runtime": "/run/user/$UID"
    }
    def __init__(self, name: str|None = None):
        self._name: str|None = name

    def get(
        self,
        arg: str,
        file: str|None = None,
        alt_name: str|None = None,
        default: Any = None
    ) -> Path|Any:
        name =  alt_name or self._name or ""
        file = file or ""
        
        var = self.getvar(arg, default)
        if var == default:
            return var
        else:
            return Path(var).joinpath(name, file)

    def getvar(self, arg: str, default: None|Any = Any) -> str|Any:
        xdg_default = self.defaults.get(arg, None)

        return environ.get(arg, xdg_default) or default


def make_eckname(module: str, name: str) -> tuple[str, str]:
    mdl_name = environ.get("APP", "eckermann").title()

    return
