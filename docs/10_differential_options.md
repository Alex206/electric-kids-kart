# 10 — Differential options

## Option 1: rigid 30 mm axle — recommended

Advantages:

- Lowest part count and cost.
- Both rear wheels driven.
- One axle-mounted brake acts on both wheels.
- Easy alignment and maintenance.

Disadvantages:

- Tyre scrub and heavier steering in tight, slow turns.
- Chassis needs some torsional compliance so the inside rear tyre can unload.

For this project, these disadvantages are acceptable at 8–25 km/h.

## Option 2: purchased mechanical differential

Use a rated compact ATV/buggy/electric-trike differential rather than manufacturing bevel gears. This changes the design to two half-shafts, additional bearings/CV joints and separate wheel hubs. Confirm:

- Continuous and peak torque rating.
- Input sprocket/shaft interface.
- Half-shaft lengths and articulation.
- Brake location; a single input brake can become ineffective if a shaft fails, so wheel-end or redundant braking may be needed.
- Backlash, lubrication and enclosure.

This option improves low-speed turning but increases cost and failure modes.

## Option 3: two motors/electronic differential

Not recommended for version 1. Independent controllers require matched torque commands, watchdog behavior, direction consistency and a safe response if one controller faults. Incorrect torque split can create unintended yaw. Treat this as a later controls-engineering project after the single-motor chassis is fully validated.

## Decision

Build version 1 with the rigid axle. Reconsider a mechanical differential only if tyre scrub is unacceptable after adjusting rear track, toe, tyre pressure and chassis stiffness.
