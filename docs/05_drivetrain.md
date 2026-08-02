# 05 — Drivetrain and ratio selection

## Recommended economy drivetrain

Motor: 48 V, 2 kW MY1020D-type BLDC, approximately 4,300 rpm rated.

### Stage 1

- Motor sprocket: T8F, 11 teeth.
- Jackshaft driven sprocket: T8F, 44 teeth.
- Ratio: 4.00:1.

### Stage 2

- Jackshaft drive sprocket: #35, 12 teeth.
- Rear-axle sprocket: start with 36 teeth.
- Ratio: 3.00:1.

Total reduction: 12.00:1.

With a 300 mm tyre and 4,300 motor rpm, theoretical speed is approximately 20.3 km/h. A 32-tooth rear sprocket gives approximately 22.8 km/h, and a 40-tooth sprocket approximately 18.2 km/h. Actual loaded speed is lower; the controller remains responsible for the hard 25 km/h ceiling.

## Formulas

```text
Total ratio = (stage1 driven / stage1 drive) × (stage2 driven / stage2 drive)
Wheel rpm = motor rpm / total ratio
Speed km/h = wheel rpm × pi × wheel diameter m × 60 / 1000
Wheel torque ~= motor torque × total ratio × drivetrain efficiency
```

The included calculator evaluates alternative wheel diameters and sprockets.

## Jackshaft construction

- 20 mm keyed steel shaft, approximately 300–350 mm long.
- Two self-aligning bearing units mounted to a 5–6 mm slotted plate.
- Separate sprockets keyed or clamped to the shaft; do not weld sprockets directly to the shaft.
- Both chains independently adjustable, with at least one rigid tension adjustment per stage.
- Maintain sprocket alignment within approximately 1 mm over the sprocket face.

## Chain safety

- Enclose the top, front and driver-facing sides of both chains and sprockets.
- Guard must remain clear if a chain derails.
- No clothing, hair or fingers can reach a moving chain from the seat.
- Use a removable inspection panel secured by tools.
- Replace chain or sprocket if tight spots, hooked teeth or measurable elongation are found.

## Premium QS138 option

A QS138 70H V3 includes internal reduction and can simplify the external drive. At 48 V it must be current-limited and geared to the actual tyre diameter. The motor is substantially heavier and capable of power far beyond this project's safe envelope. Retain the 25 km/h hard limit and repeat all brake and thermal tests after installation.

## Differential options

See `docs/10_differential_options.md`. Version 1 intentionally uses a rigid axle.
