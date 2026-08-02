# 12 — Procurement and price comparison

Prices observed on 1 August 2026. Treat prices and availability as snapshots; verify before ordering. Safety-critical selection is based on documented ratings and compatibility, not lowest price.

## Budget scenarios

| Scenario | Current range | Typical target |
|---|---:|---:|
| Economy prototype | EUR 1,900–2,500 | EUR 2,200 |
| Recommended family build | EUR 2,600–3,400 | EUR 3,000 |
| Premium QS138 build | EUR 3,600–4,500 | EUR 4,000 |

The full recommended line-item BOM totals approximately EUR 3,318. Existing steel and wheels, a lower-cost but inspected steering set, or already-owned protective equipment can reduce that amount.

## Drive motor options

| Tier | Product | Observed price | Comment | Source |
|---|---|---:|---|---|
| Economy | MY1020D 48 V 2 kW brushless motor only | EUR 149.99 | German seller; verify shaft, Hall connector and exact rated rpm | [Happy Motorparts](https://happy-motorparts.de/Elektromotor-48-Volt-DC-2000-Watt-MY1020D-brushless-buerstenlos) |
| Economy kit | VEVOR MY1020D-type 48 V 2 kW kit | EUR 143.99 | Includes basic controller/throttle; use included controller only for bench/prototype unless limits and fail-safes are verified | [VEVOR](https://eur.vevor.com/brushless-dc-motor-c_11227/vevor-electric-brushless-dc-motor-brushless-electric-motor-48v-2000w-controller-p_010400593330) |
| Premium | QS138 70H V3 internal-reduction motor | EUR 449–599 | Heavy, very high capability; use only with conservative limits | [Vector eBike](https://vectorebike.com/de/products/qs138-70h-v3) |
| Premium kit | QS138 V3 + Votol EM150 | EUR 990 | More power than required; not the initial recommendation | [Gruber Parts](https://gruber-parts.com/products/qs-138-c70h-3000w-mid-und-votol-em-150-controller) |

## Controller options

| Product | Observed price | Strengths | Caveats | Source |
|---|---:|---|---|---|
| Kelly KLS7212S, 24–72 V, 120 A peak | EUR 187–322 | EV-oriented, Hall support, programmable current/voltage, regen | Vendor pricing differs; programming cable may be extra | [Kelly Controller EU](https://kellycontroller.eu/index.php?dispatch=products.view&product_id=3002) |
| Flipsky dual 75100 VESC-based | USD 172 listed | Flexible open tooling, regen and telemetry | Dual controller unnecessary; hardware-specific VESC settings and phase-filter warning must be followed | [Flipsky](https://flipsky.net/products/flipsky-dual-75100-with-aluminum-pcb-based-on-vesc-for-electric-skateboard-electric-scooter-ebike-speed-controller) |

Recommended first choice: Kelly KLS7212S or another documented single-channel EV controller with Hall sensors, brake input and programmable limits. VESC remains an excellent engineering option if configured and validated carefully.

## Battery options

| Product | Observed price | Comment | Source |
|---|---:|---|---|
| Professionally built 48 V 20 Ah 100 A Li-ion softpack | EUR 613 | Berlin-built, documented Samsung cells, BMS options and transport/safety testing; chemistry is not LiFePO4 | [Dan-Tech Energy](https://shop.danenergy.com/de/products/li-ion-battery-softpack-13s4p-48v-20ah-100a) |
| Custom 16S LiFePO4 25–30 Ah, >=80 A BMS | budget EUR 650–900 | Preferred chemistry, but obtain from a credible pack builder with exact continuous-current and temperature data | supplier quotation required |
| 48 V 20 Ah scooter replacement pack | EUR 519–529 | Capacity known; current capability is not stated on the listing and must be confirmed before use | [epowerfun](https://epowerfun.de/48V-20AH-Akku-960Wh-inkl.BMS-Platine-ePF-Pulse/201075) |

Do not buy a pack solely from an advertised `100 A` headline. Require continuous current, peak duration, cell model, BMS cutoff behavior, charge current, temperature sensing, dimensions, weight and charger specification.

## Kart mechanical parts

| Item | Observed price | Source |
|---|---:|---|
| 30 mm × 950 mm OTK rear axle | EUR 163.95 | [KartKings](https://kartkings.de/products/otk-hinterachse-typ-n-30x950mm) |
| 30 mm axle bearing | EUR 12.80 each | [Prespo](https://www.prespo.de/hinterachsaufbau/achslager/) |
| 30 mm brake-disc carrier | EUR 34.70–39.90 | [DK Kartshop](https://www.dk-kartshop.de/hinterachse-und-zubehoer/bremsscheibenaufnahme-30mm-silber.html?language=de) |
| Complete 150 cc kart steering set | EUR 184.79 | [Motokay](https://www.motokay.de/weiteres-zubehoer/lenker/lenkerzubehoer/moturo-lenkrad-fuer-150ccm-go-kart_6236050_184519) |
| Generic 110 cc steering assembly | about EUR 62.70–64 | [ManoMano](https://www.manomano.de/p/lenkung-lenkgetriebe-spurstange-montage-set-for-go-kart-110cc-89475848) |

The generic steering set is cheaper but its geometry and material quality need physical inspection. A kart-specific set from a known supplier is the preferred baseline.

## Electrical protection examples

| Item | Observed price | Requirement note | Source |
|---|---:|---|---|
| 48-to-12 V, 10 A converter | EUR 23.80 | Confirm input range includes fully charged pack | [Power & Storage](https://www.power-and-storage.de/shop/DC-DC-Wandler-48V-zu-12V-10A-p174773330) |
| 80 A MEGA fuse example | EUR 9.16 | Listing is 58 V; select a version with adequate margin, preferably >=70 V DC | [Service Döbeln](https://www.service-doebeln.de/shop/de/MEGA-Sicherungen-80A-58V-fuer-48V-Systeme.html) |

## Purchase order

Buy in this order to avoid incompatible parts:

1. Measure existing wheels and steel.
2. Select front spindles/steering kit and rear axle/hubs.
3. Select matched brake kit and carriers.
4. Freeze wheel diameter and calculate gearing.
5. Select motor/controller as a compatible pair.
6. Select battery based on controller current and physical envelope.
7. Select fuse, contactor, precharge and charger from the final battery voltage/current data.
8. Buy steel plates, bearings, sprockets, chain and guards after the interfaces are known.
