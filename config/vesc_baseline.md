# Conservative VESC commissioning baseline

This is a starting checklist, not a ready-to-flash configuration. Parameter names and safe limits depend on the exact VESC hardware, motor and battery.

## Before setup

- Confirm controller absolute voltage rating exceeds maximum charged battery voltage with margin.
- Obtain motor pole-pair count, Hall wiring, temperature-sensor type and current rating.
- Obtain battery continuous discharge, peak discharge, maximum charge/regen current and BMS cutoff behavior.
- Raise rear wheels and ensure the mechanical brake and E-stop are functional.

## Initial limits for a 2 kW / 48 V build

| Parameter | Initial value | Later ceiling after tests |
|---|---:|---:|
| Battery current max | 25–35 A | 40–45 A only if pack/controller support it |
| Motor current max | 30–40 A | 50–60 A after thermal test |
| Battery regen current | 0 to -3 A | limited by battery charge/BMS data |
| Motor brake current | -10 to -20 A | supplemental only |
| Throttle ramp-up | 2–3 s | >=1.5 s |
| Reverse speed | disabled | maximum walking pace if later enabled |
| Hard vehicle speed | 25 km/h equivalent ERPM | unchanged |

For a 16S LiFePO4 pack, a conservative starting voltage cutoff is approximately 49.6 V soft and 47.2 V hard, but replace this with the actual cell/pack manufacturer's limits and load-sag data.

## Motor setup

Use the official motor setup wizard, begin with reduced current and verify direction. FOC can provide smooth low-speed control, but third-party hardware requires cautious setup. Hall sensors are strongly preferred for controlled launch from zero speed.

## Speed limit calculation

```text
wheel_rpm = target_speed_mps / (pi × wheel_diameter_m) × 60
motor_rpm = wheel_rpm × total_reduction
ERPM = motor_rpm × pole_pairs
```

Set both forward and reverse limits; disable or severely limit reverse.

## Input fail-safe

- Calibrate idle and full throttle with margin.
- Configure out-of-range ADC as a fault/zero command.
- Add a physical pull-down near the controller input if compatible with the hardware.
- Brake input must override throttle.
- Test open-circuit, short-to-ground and short-to-supply cases with wheels raised.

## Temperature

Enable motor and controller temperature derating using actual sensor type. A reasonable initial policy is to begin derating well below the component's absolute maximum; use manufacturer data rather than generic values.
