"""Exemple minimal : charger le dataset et filtrer par muscle ou équipement."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
exercises = json.loads((ROOT / "data" / "exercises.json").read_text(encoding="utf-8"))


def search(target=None, equipment=None):
    return [
        e for e in exercises
        if (target is None or e["target"].lower() == target.lower())
        and (equipment is None or e["equipment"].lower() == equipment.lower())
    ]


if __name__ == "__main__":
    for e in search(target="pectorals", equipment="barbell")[:5]:
        print(e["name"], "->", ROOT / e["gif_url"])
