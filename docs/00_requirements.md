# 00 — Requirements

## Users and environment

- Primary drivers: one child aged 5 and one aged 13, always supervised.
- Adult commissioning driver permitted.
- Operation only on a closed, flat private area, initially dry asphalt or concrete.
- No public roads, pavements, cycle paths or shared traffic areas.

## Functional requirements

| ID | Requirement | Verification |
|---|---|---|
| F-01 | Parent-selectable 8, 15 and 25 km/h modes | GPS/roller speed test |
| F-02 | Accelerator returns to zero when released | Static inspection and energized test with wheels raised |
| F-03 | Mechanical brake stops without controller power | Coast-down and stopping test |
| F-04 | Main emergency stop removes traction power | Functional test at raised wheels and walking speed |
| F-05 | Seat and pedal reach adjustable for both children | Fit check with engine off |
| F-06 | Chain and sprockets fully guarded | Inspection probe test |
| F-07 | Reverse disabled in child mode | Functional test |
| F-08 | Battery removable without exposing live terminals | Inspection |

## Design limits

- Gross design mass: 160 kg.
- Maximum governed speed: 25 km/h.
- Initial current limit: 35 A battery current; increase only after thermal and braking tests.
- Nominal traction voltage: 48 V class.
- Maximum charged voltage for 16S LiFePO4: 58.4 V; all switching/protection devices require margin above this value.
- Target wheelbase: 1,100 mm; target overall width: 900–950 mm.

## Non-goals for version 1

- Public-road approval.
- Racing use, jumps, off-road terrain or steep slopes.
- Homemade differential gears.
- Dual-motor torque vectoring.
- Seat belt without an engineered roll cage.
- Battery-cell welding or a home-built pack for the first driving tests.
