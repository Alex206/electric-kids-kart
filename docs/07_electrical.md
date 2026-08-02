# 07 — Electrical system

## Traction circuit

```text
BAT+ -> DC fuse -> service disconnect -> main contactor -> controller B+
BAT- -----------------------------------------------------> controller B-
controller U/V/W -> motor phases
controller Hall/temperature -> motor sensors
```

Place the traction fuse as close as practical to the battery positive terminal. Use a fuse and holder explicitly rated for DC interruption above the maximum charged pack voltage; for a 16S LiFePO4 pack, select at least a 70 V DC-rated device rather than relying on a nominal 48 V label.

## Control circuit

```text
Battery -> isolated 48-to-12 V converter -> parent key -> emergency stop -> safety relay/contactor coil
                                                     |-> controller enable
Brake switch ----------------------------------------|-> throttle inhibit / brake input
Mode key --------------------------------------------|-> low/medium/high mode input
Remote fail-safe receiver ---------------------------|-> torque inhibit
```

The remote receiver is an additional parent control, not the only emergency system. Loss of radio link must inhibit torque.

## Initial component ratings

| Component | Minimum requirement |
|---|---|
| Battery | 48 V class, 0.9–1.5 kWh, documented BMS, >= 60 A continuous and >= 100 A short peak |
| Main fuse | 70 V DC or higher, initial 60–80 A after controller/battery review |
| Main contactor | >= 72 V DC switching, >= 100 A continuous, coil matched to control supply |
| Controller | 60 V minimum; 72–75 V preferred, programmable current and speed limits |
| Battery cable | 16 mm² copper for short runs; verify installation temperature and fuse coordination |
| Control wiring | 0.75–1.5 mm², separately fused at 2–5 A |
| DC/DC | Input compatible with full pack voltage; 12 V, 10 A nominal |
| Connectors | Touch-safe, polarized, vibration-resistant; no exposed XT-style live pins accessible to children |

## Precharge

Many controllers contain large input capacitors. Closing the contactor without precharge can weld contacts and damage connectors. Use a precharge resistor and verify that controller DC-bus voltage rises to at least 90% of battery voltage before closing the main contactor. The exact resistor and delay depend on controller capacitance; 100–220 ohm, 25 W is a starting range only, not a final value.

## Accelerator

- Hall-effect pedal or thumb/foot assembly with two mechanical return springs.
- Defined idle voltage and high-voltage fault limits in the controller.
- Pull-down or pull-up so an open signal wire produces zero torque/fault, never full throttle.
- Brake input overrides accelerator in hardware/controller configuration.
- Physical pedal stop prevents sensor damage.

## Battery choice

A professionally assembled pack with documented cells, BMS, continuous-current rating, temperature sensing and transport testing is preferable to assembling loose cells for the first version. LiFePO4 is preferred where a compact high-current pack from a credible builder is available. A professionally built high-current NMC/NCA pack with full BMS is safer than an undocumented marketplace LiFePO4 pack with an overstated current rating.

## Charging

- Charger chemistry and final voltage must exactly match the pack.
- Traction contactor open while charging.
- Charge on a non-combustible surface with ventilation and adult supervision.
- Do not charge a damaged, swollen, wet, frozen or unusually warm pack.
