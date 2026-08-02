# 01 — System architecture

## Recommended version 1

```text
Parent key/mode switch ─┐
Brake switch ───────────┼──> controller enable / throttle inhibit
Emergency stop ─────────┘

Battery -> fuse -> service disconnect -> precharge -> main contactor -> motor controller -> BLDC motor
                                               |
                                               +-> isolated 48-to-12 V converter -> controls/lighting

Motor -> T8F chain -> jackshaft -> #35 chain -> rigid 30 mm rear axle
Hydraulic pedal -> rear caliper -> axle-mounted disc
```

## Why a rigid rear axle

A rigid axle is common on karts because it is mechanically simple, keeps both driven wheels synchronized and allows one axle-mounted brake disc to act on both rear wheels. At low speed it produces tyre scrub in tight turns, but this is preferable to introducing an unverified homemade differential into the first build.

## Why a jackshaft

Typical inexpensive 48 V / 2 kW MY1020D motors run around 4,300 rpm. A single practical kart sprocket cannot provide the approximately 11–12:1 reduction needed for 20–25 km/h with 300–350 mm tyres. A two-stage reduction permits compact sprockets, better chain clearance and easy ratio changes.

## Upgrade path

The frame reserves a motor plate and electrical space for a QS138 internal-reduction motor. The premium motor is heavier and substantially more powerful; it must remain limited to the same initial speed/current envelope until braking and chassis tests are repeated.
