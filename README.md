# Electric Kids Kart

Parametric design and build documentation for a small electric go-kart intended for two supervised drivers aged approximately 5 and 13.

> **Status: pre-fabrication design draft.** Do not cut steel or order the axle, steering, brake, sprockets, or battery until the measurements in `docs/11_measurements_needed.md` have been completed.

## Baseline architecture

- 48 V nominal traction system; controller rated for at least 60 V, preferably 72–75 V.
- 2 kW BLDC motor for the first build; premium upgrade path to a QS138 3 kW motor operated with conservative current limits.
- 30 mm rigid rear axle with chain drive; no differential in version 1.
- Two-stage reduction for the high-speed MY1020D motor: T8F motor-to-jackshaft, then #35 chain jackshaft-to-axle.
- Hydraulic rear disc brake as the primary brake. Regeneration is supplemental only.
- Three parent-controlled operating modes: approximately 8, 15 and 25 km/h.
- Adjustable seat and pedal box to accommodate the large height difference between the two children.
- Use only on closed private property. No public-road operation.

## Design targets

| Parameter | Target |
|---|---:|
| Maximum governed speed | 25 km/h |
| Child mode | 8 km/h |
| Youth mode | 15 km/h |
| Design gross mass | 160 kg |
| Nominal motor power | 2 kW |
| Battery energy | 0.9–1.5 kWh |
| Dry stopping distance at 25 km/h | <= 6.5 m, excluding reaction time |
| Ground clearance | >= 60 mm |

## Repository map

- `docs/` — requirements, safety, frame, steering, drivetrain, brakes, electrical system, build sequence and test plan.
- `cad/frame.scad` — editable parametric OpenSCAD model.
- `cad/frame_preview.stl` and `cad/frame_preview.glb` — generated preview geometry.
- `drawings/` — frame plan, steering geometry and wiring diagram in SVG.
- `bom/bom.xlsx` and `bom/bom.csv` — purchasing list, cost scenarios and calculation inputs.
- `calculations/kart_calc.py` — speed, ratio, tractive-force and stopping calculations.
- `config/` — conservative initial settings for VESC and Kelly controllers.

## Important safety boundaries

- A mechanical brake must stop the kart without electrical assistance.
- Do not install a seat belt unless a properly engineered roll structure is also fitted. An open kart without a roll cage should not restrain the driver into the vehicle during a rollover.
- The accelerator must have a return spring, an idle switch or plausibility check, a defined electrical fail-safe, and a physical stop.
- The main battery fuse must be mounted close to the battery positive terminal and be DC-rated above the pack's maximum charged voltage.
- All rotating chains, sprockets, the brake disc, axle keys and electrical terminals must be guarded.
- First tests are performed by an adult, then at walking speed, before either child drives.

## Estimated project cost

The current realistic range is approximately:

- Economy prototype: **EUR 1,900–2,500**, using existing wheels/steel and carefully inspected generic parts.
- Recommended family build: **EUR 2,600–3,400**, using a documented controller, high-current battery, kart steering/brake parts and robust electrical protection.
- Premium QS138 build: **EUR 3,600–4,500**.

The complete recommended line-item BOM currently totals about **EUR 3,318** before substituting existing material or lower-cost compatible alternatives.

Prices are snapshots and shipping can materially change totals. See `docs/12_procurement.md` and the spreadsheet.

## Next required input

Record the wheel diameters, hub interfaces, steel profile dimensions and expected tallest/heaviest driver in `docs/11_measurements_needed.md`. The CAD and sprocket selection are intentionally parameterized around those values.
