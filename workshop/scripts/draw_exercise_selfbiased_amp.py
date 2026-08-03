# SPDX-FileCopyrightText: 2026 The HeiChips Contributors
# SPDX-License-Identifier: Apache-2.0
#
# Draw the "Self-Biased Single-Ended Inverter Amplifier" exercise figure
# with schemdraw, following inverter/scripts/sizing/sizing_inverter.ipynb.
# The inverter is drawn as a symbol, the focus is the feedback resistor R_f
# closing the dc loop from vout to vin.

from pathlib import Path

import matplotlib
matplotlib.rcParams.update({
    "text.usetex": True,
    "font.family": "lmodern"
})
import schemdraw as sd
import schemdraw.elements as elm
import schemdraw.logic as logic
sd.svgconfig.svg2 = False

FIG_DIR = Path(__file__).resolve().parent.parent / "fig"

with sd.Drawing(show=False) as d:
    d.config(unit=2, fontsize=16)

    elm.Dot(open=True).label(r'$V_\mathrm{in}$', loc='left', ofst=0.15)
    dot_in = elm.Line().right().length(1.0).dot()
    elm.Line().at(dot_in.end).right().length(0.75)
    inv = logic.Not().anchor('in1')
    out_node = elm.Line().at(inv.out).right().length(1.0).dot()
    elm.Line().at(out_node.end).right().length(1.0)
    elm.Dot(open=True).label(r'$V_\mathrm{out}$', loc='right', ofst=0.15)

    # Feedback resistor R_f from the input node over the inverter to the output node
    elm.Line().at(dot_in.end).up().length(1.25)
    elm.Resistor().right().tox(out_node.end).label(r'$R_\mathrm{f}$', loc='top', ofst=0.15)
    elm.Line().down().toy(out_node.end)

    # Save the schematic
    d.save(str(FIG_DIR / "exercise_selfbiased_amp.svg"))
    d.save(str(FIG_DIR / "exercise_selfbiased_amp.pdf"))
