# SPDX-FileCopyrightText: 2026 The HeiChips Contributors
# SPDX-License-Identifier: Apache-2.0
#
# Draw the "Three-Stage Ring Oscillator with Output Buffer" exercise figure
# with schemdraw, following inverter/scripts/sizing/sizing_inverter.ipynb.
# Three inverters form the ring, the fourth inverter buffers the ring node.

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

    ring_in = elm.Line().right().length(0.75)
    n1 = logic.Not().anchor('in1').label(r'$1$', loc='bottom', ofst=0.15)
    elm.Line().at(n1.out).right().length(0.75)
    n2 = logic.Not().anchor('in1').label(r'$2$', loc='bottom', ofst=0.15)
    elm.Line().at(n2.out).right().length(0.75)
    n3 = logic.Not().anchor('in1').label(r'$3$', loc='bottom', ofst=0.15)
    osc = elm.Line().at(n3.out).right().length(1.0).dot()
    elm.Line().at(osc.end).right().length(1.0)
    n4 = logic.Not().anchor('in1').label(r'$4$ (output buffer)', loc='bottom', ofst=0.15)
    elm.Line().at(n4.out).right().length(0.75)
    elm.Dot(open=True).label(r'$V_\mathrm{out}$', loc='right', ofst=0.15)

    # Feedback wire from the ring node back to the input of the first stage
    elm.Line().at(osc.end).up().length(2.0).label(r'osc', loc='right', ofst=0.15)
    elm.Line().left().tox(ring_in.start)
    elm.Line().down().toy(ring_in.start)

    # Save the schematic
    d.save(str(FIG_DIR / "exercise_ring_oscillator.svg"))
    d.save(str(FIG_DIR / "exercise_ring_oscillator.pdf"))
