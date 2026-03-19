"""Session management — persists state across CLI invocations."""

import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

SESSION_FILE = os.path.expanduser("~/.cli_anything_aimarketing_session.json")
MAX_HISTORY = 10

_DEFAULTS: Dict[str, Any] = {
    "current_url": None,
    "output_dir": "./marketing-output",
    "last_audit": None,
    "history": [],
}


class Session:
    """Persistent session state for the aimarketing CLI harness."""

    def __init__(self, session_file: str = SESSION_FILE):
        self._file = session_file
        self._state: Dict[str, Any] = dict(_DEFAULTS)
        self._load()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load(self) -> None:
        if os.path.exists(self._file):
            try:
                with open(self._file, "r", encoding="utf-8") as fh:
                    data = json.load(fh)
                self._state.update(data)
            except (json.JSONDecodeError, OSError):
                self._state = dict(_DEFAULTS)

    def save(self) -> None:
        try:
            with open(self._file, "w", encoding="utf-8") as fh:
                json.dump(self._state, fh, indent=2, default=str)
        except OSError:
            pass  # non-fatal

    def clear(self) -> None:
        self._state = dict(_DEFAULTS)
        if os.path.exists(self._file):
            os.remove(self._file)

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def current_url(self) -> Optional[str]:
        return self._state.get("current_url")

    @current_url.setter
    def current_url(self, value: str) -> None:
        self._state["current_url"] = value
        self.save()

    @property
    def output_dir(self) -> str:
        return self._state.get("output_dir", "./marketing-output")

    @output_dir.setter
    def output_dir(self, value: str) -> None:
        self._state["output_dir"] = value
        self.save()

    @property
    def last_audit(self) -> Optional[Dict]:
        return self._state.get("last_audit")

    @last_audit.setter
    def last_audit(self, value: Dict) -> None:
        self._state["last_audit"] = value
        self.save()

    # ------------------------------------------------------------------
    # History
    # ------------------------------------------------------------------

    def push_history(self, command: str, url: Optional[str], summary: str) -> None:
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "command": command,
            "url": url,
            "summary": summary,
        }
        history: List = self._state.setdefault("history", [])
        history.insert(0, entry)
        self._state["history"] = history[:MAX_HISTORY]
        self.save()

    @property
    def history(self) -> List[Dict]:
        return self._state.get("history", [])

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        return dict(self._state)
