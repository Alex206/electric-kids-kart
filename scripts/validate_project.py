#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "docs/02_safety.md",
    "docs/07_electrical.md",
    "docs/09_commissioning.md",
    "calculations/defaults.json",
    "cad/frame.scad",
    "bom/bom.csv",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("Missing required files:", *missing, sep="\n- ")
    sys.exit(1)

p = json.loads((ROOT / "calculations/defaults.json").read_text())
assert p["max_speed_kmh"] <= 25, "Baseline speed must not exceed 25 km/h"
assert p["design_mass_kg"] >= 150, "Design mass unexpectedly low"
assert p["stage1_drive_teeth"] > 0 and p["stage2_drive_teeth"] > 0
print("Project validation passed")
