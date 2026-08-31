---
title: Motorless solid-state cooler uses heat to cool itself; could recycle processor
  heat into cooling — shape-memory alloy films could turn data center exhaust into
  refrigeration
source_url: https://www.tomshardware.com/tech-industry/manufacturing/motorless-solid-state-cooler-uses-heat-to-cool-itself-could-recycle-processor-heat-into-cooling-shape-memory-alloy-films-could-turn-data-center-exhaust-into-refrigeration
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-31T16:07:53Z'
published: '2026-08-31T00:00:00Z'
description: Device could potentially help cool data centers without electricity
image: https://cdn.mos.cms.futurecdn.net/KqBokvkVTxM9Mkyjj2L4t-1280-80.jpg
---

![elastocaloric cooling](https://cdn.mos.cms.futurecdn.net/KqBokvkVTxM9Mkyjj2L4t.jpg) 

A team of scientists in Germany and Japan has demonstrated a solid-state cooling system that uses heat to generate the mechanical work required for refrigeration, potentially opening a route to processors and data centers that recycle some of their own waste heat for cooling. Developed by researchers at the Karlsruhe Institute of Technology (KIT) and the University of Tsukuba, the system — detailed in Nature Energy on August 28 — replaces the electrically powered actuator normally required for elastocaloric cooling with a heat-responsive shape-memory alloy, allowing the cooling cycle to run from an external heat source rather than a motor.

The prototype combines two ultra-thin metal films that serve as an actuator and a refrigerant. A 22-micrometer titanium-nickel (TiNi) shape-memory film contracts when heated, converting thermal energy into mechanical motion. This motion stretches and releases a 26.5-micrometer titanium-nickel-iron (TiNiFe) refrigerant film, triggering a reversible phase transition that produces cooling. In laboratory tests, Joule heating the actuator to 86°C produced a 12.9 K temperature span across the refrigerant film — the difference between its hottest and coldest states during the cooling cycle — and a 4.0 K span across the assembled cooling device, measured between its hot and cold sides. When the researchers replaced the resistance heating with an external 130°C heat source, the prototype still maintained a 2.2 K device-level temperature span, demonstrating that an external thermal source could drive the cooling mechanism.

Conventional refrigeration and air conditioning systems mostly use vapor-compression cooling. A compressor raises the pressure and temperature of a refrigerant, which then dumps heat in a condenser before expanding and evaporating at low pressure to absorb heat from the space being cooled. The technology is mature and efficient, but requires an electrically driven compressor and relies on refrigerants with significant global warming potential.

Solid-state cooling moves heat without the conventional compressor-and-refrigerant loop. Thermoelectric coolers, for example, use electrical current to create a temperature difference across semiconductor materials and are already common in compact electronics. However, the researchers note that thermoelectric devices typically reach only 10% to 15% of the theoretical reversed-Carnot efficiency limit, roughly one-quarter that of modern vapor-compression systems.

Elastocaloric cooling takes a different route. Certain shape-memory alloys change crystal structure when mechanically loaded and unloaded. Applying stress induces a phase transition that releases latent heat and warms the material. Once that heat is rejected, releasing the load reverses the transition, causing the material to absorb heat and cool. The solid alloy effectively becomes the refrigerant.

The problem is that the material still has to be repeatedly stretched and released. Existing elastocaloric systems generally use motors, hydraulic systems, or electromechanical actuators to provide the required force, adding electrical consumption, bulk, and mechanical complexity — particularly troublesome for miniature coolers. Instead, the KIT-Tsukuba team made one shape-memory alloy drive another. Heating the TiNi actuator film causes it to recover its original shape and contract. Mechanically coupled to the TiNiFe refrigerant film, that contraction supplies the force required for the cooling cycle. As the actuator heats and cools, it loads and unloads the refrigerant without an electric motor.

Broken down further, the system works as follows: the researchers take a shape-memory alloy (TiNiFe refrigerant film) that cools when released after being stretched. Instead of using a mechanical system to repeatedly stretch and release that alloy, they use another shape-memory alloy (TiNi) that contracts when heated and mechanically couple it to its cooling counterpart. When the TiNi is heated, it contracts, stretching and “loading” the refrigerant film. Once the heat is removed, the TiNi relaxes, releasing the film and triggering the phase transition that causes it to cool. Under cyclic heating, the TiNi alloy therefore provides the repeated stretching and releasing motion the TiNiFe requires for elastocaloric cooling.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The thermal actuator delivered a force-to-displacement ratio of 14.5 N/mm, compared with 1.1 N/mm for a commercial electromechanical actuator the researchers used as a reference. The thin films also provide a high surface-to-volume ratio for rapid heat transfer. Under Joule-heated actuation, the integrated device reached a steady 4.0 K temperature span after 20 cycles and a specific cooling power of 4.43 W/g. When driven from the external heat source, those figures fell to 2.2 K and 3.32 W/g, respectively.

This external-heat result is the real proof of concept. While the technology is still an early-stage laboratory experiment, a scaled, perfected version could have interesting implications. Typically, the heat the system needs to operate is generated from electricity or another form of energy. However, an ideal scenario would be to repurpose existing waste heat — a setup already attainable in data centers. Therefore, the technology has the potential to cool processors using the heat they generate!

However, applying it as a data center cooling technology is far from the technology's current state. The prototype produced just 2.09 milliwatts of cooling power at zero temperature lift. That is nowhere near the heat loads of modern processors, much less AI accelerators or data-center racks. The researchers also cite relatively slow actuation, limited strain rate, and the current heat-exchanger geometry among the factors constraining performance. There also needs to be a way to make the heating cyclical.

The team is now working to connect multiple films in parallel to increase cooling capacity. Further progress will require scaling the active material, improving heat transfer and operating frequency, and proving long-term durability. For now, the researchers have demonstrated the underlying energy chain in which heat can be converted into mechanical motion, and that motion can be turned into useful cooling without an electric motor driving the refrigeration cycle.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
