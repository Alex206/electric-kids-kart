#!/usr/bin/env python3
"""Parametric drivetrain, steering and braking calculations."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def calculations(p: dict) -> dict:
    d_m = p["rear_wheel_diameter_mm"] / 1000.0
    r1 = p["stage1_driven_teeth"] / p["stage1_drive_teeth"]
    r2 = p["stage2_driven_teeth"] / p["stage2_drive_teeth"]
    total = r1 * r2
    wheel_rpm = p["motor_rated_rpm"] / total
    no_load_wheel_rpm = p["motor_no_load_rpm"] / total
    speed = wheel_rpm * math.pi * d_m * 60 / 1000
    no_load_speed = no_load_wheel_rpm * math.pi * d_m * 60 / 1000
    wheel_torque = p["motor_rated_torque_nm"] * total * p["drivetrain_efficiency"]
    tractive_force = wheel_torque / (d_m / 2)
    acceleration = tractive_force / p["design_mass_kg"]
    v = p["max_speed_kmh"] / 3.6
    decel = p["target_deceleration_g"] * 9.81
    stop_distance = v * v / (2 * decel)
    kinetic_energy = 0.5 * p["design_mass_kg"] * v * v

    inner = math.radians(30)
    L = p["wheelbase_mm"] / 1000
    T = p["front_track_mm"] / 1000
    outer = math.atan(L / (L / math.tan(inner) + T))

    return {
        "stage1_ratio": r1,
        "stage2_ratio": r2,
        "total_ratio": total,
        "rated_speed_kmh": speed,
        "no_load_speed_kmh": no_load_speed,
        "wheel_torque_nm": wheel_torque,
        "tractive_force_n": tractive_force,
        "ideal_flat_acceleration_m_s2": acceleration,
        "stop_distance_at_max_speed_m": stop_distance,
        "kinetic_energy_at_max_speed_j": kinetic_energy,
        "ackermann_outer_angle_for_30deg_inner_deg": math.degrees(outer),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(Path(__file__).with_name("defaults.json")))
    args = parser.parse_args()
    p = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = calculations(p)
    for key, value in result.items():
        print(f"{key}: {value:.3f}" if isinstance(value, float) else f"{key}: {value}")


if __name__ == "__main__":
    main()
