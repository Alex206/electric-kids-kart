# Conservative Kelly KLS commissioning baseline

The exact application fields vary by KLS model and software version. Save the factory configuration before changing values.

## Initial values

- Battery current limit: approximately 30–35 A for first rolling tests.
- Motor/phase current: minimum practical value that launches smoothly; increase only after thermal testing.
- Throttle start/low deadband: set above measured idle noise.
- Throttle high fault: below sensor maximum so short-to-supply is detected.
- Acceleration ramp: 2–3 seconds to full command.
- Low-speed mode: about 30% of governed maximum.
- Medium mode: about 60%.
- High mode: 100% of a separately configured 25 km/h hard ceiling.
- Reverse: disabled initially.
- Regen: disabled for mechanical-brake commissioning, then introduce a very small value within battery charge limits.
- Brake switch: zero torque immediately; mechanical brake remains independent.

## Validation

Test every input state with rear wheels raised: key, E-stop, brake, throttle disconnected, Hall disconnected, mode switch, remote signal loss and controller restart. A controller fault must never produce drive torque.
