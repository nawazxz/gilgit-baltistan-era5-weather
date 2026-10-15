#!/usr/bin/env python3
"""
GB Climate Report — large poster format, single column, easy to read.
"""

import os
HERE = os.path.dirname(os.path.abspath(__file__))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import textwrap

OUT = os.path.join(HERE, "GB_Climate_Report.png")

def draw_report():
    # Wide, moderately tall — 2400 x 3400 px at 100 dpi
    fig, ax = plt.subplots(figsize=(24, 34), facecolor="white")
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 34)
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)

    Y = [33.4]  # mutable cursor, top-down

    def gap(g=0.18):
        Y[0] -= g

    def hline(color="#dddddd", lw=1):
        ax.plot([0.5, 23.5], [Y[0], Y[0]], color=color, lw=lw, zorder=2)

    def banner(text, sub=None, bg="#1a252f", fg="white", subfg="#aab7b8",
               height=0.65, fontsize=22):
        rect = mpatches.FancyBboxPatch(
            (0.2, Y[0] - height), 23.6, height,
            boxstyle="square,pad=0", fc=bg, ec="none", zorder=1
        )
        ax.add_patch(rect)
        ty = Y[0] - height * (0.38 if sub else 0.50)
        ax.text(12, ty, text, ha="center", va="center",
                fontsize=fontsize, fontweight="bold", color=fg, zorder=2)
        if sub:
            ax.text(12, Y[0] - height * 0.72, sub,
                    ha="center", va="center",
                    fontsize=13, color=subfg, zorder=2)
        Y[0] -= height

    def section_header(num, topic, color, height=0.52):
        rect = mpatches.FancyBboxPatch(
            (0.2, Y[0] - height), 23.6, height,
            boxstyle="square,pad=0", fc=color, ec="none", zorder=1
        )
        ax.add_patch(rect)
        ax.text(0.65, Y[0] - height * 0.50,
                f"{num}   {topic}",
                ha="left", va="center",
                fontsize=20, fontweight="bold", color="white", zorder=2)
        Y[0] -= height

    def headline(text, color, height=0.40):
        rect = mpatches.FancyBboxPatch(
            (0.2, Y[0] - height), 23.6, height,
            boxstyle="square,pad=0", fc=color, ec="none", zorder=1
        )
        ax.add_patch(rect)
        ax.text(0.65, Y[0] - height * 0.52, text,
                ha="left", va="center",
                fontsize=14, fontweight="bold",
                color=darken(color), style="italic", zorder=2,
                wrap=True)
        Y[0] -= height

    def reason(num, title, body, num_color, indent=0.65):
        # Calculate lines needed
        lines = textwrap.wrap(body, 95)
        height = 0.38 + len(lines) * 0.185

        # Number
        ax.text(indent, Y[0] - 0.18,
                f"{num}.", ha="left", va="top",
                fontsize=19, fontweight="bold", color=num_color)
        # Title
        ax.text(indent + 0.55, Y[0] - 0.18,
                title, ha="left", va="top",
                fontsize=17, fontweight="bold", color="#111111")
        # Body — each line manually
        for li, line in enumerate(lines):
            ax.text(indent + 0.55, Y[0] - 0.42 - li * 0.185,
                    line, ha="left", va="top",
                    fontsize=14, color="#333333")

        Y[0] -= height
        # Light divider
        ax.plot([0.5, 23.5], [Y[0] + 0.04, Y[0] + 0.04],
                color="#eeeeee", lw=1)

    def stat_row(stats):
        height = 0.80
        n = len(stats)
        cw = 23.6 / n
        for i, (label, value, color) in enumerate(stats):
            x0 = 0.2 + i * cw
            rect = mpatches.FancyBboxPatch(
                (x0, Y[0] - height), cw - 0.05, height,
                boxstyle="square,pad=0",
                fc="#2c3e50" if i % 2 == 0 else "#263545",
                ec="none", zorder=1
            )
            ax.add_patch(rect)
            cx = x0 + cw * 0.5
            ax.text(cx, Y[0] - 0.18, label,
                    ha="center", va="top", fontsize=11.5,
                    color="#aab7b8", fontweight="bold", zorder=2)
            ax.text(cx, Y[0] - 0.48, value,
                    ha="center", va="top", fontsize=16,
                    color=color, fontweight="bold", zorder=2)
        Y[0] -= height

    def conclusion_box(title, body, bg, left, width):
        lines = textwrap.wrap(body, 38)
        height = 0.55 + len(lines) * 0.195
        rect = mpatches.FancyBboxPatch(
            (left, Y[0] - height), width - 0.12, height,
            boxstyle="square,pad=0.15", fc=bg, ec="#dddddd", lw=1, zorder=1
        )
        ax.add_patch(rect)
        ax.text(left + 0.22, Y[0] - 0.22, title,
                ha="left", va="top", fontsize=15,
                color="#1a252f", fontweight="bold", zorder=2)
        for li, line in enumerate(lines):
            ax.text(left + 0.22, Y[0] - 0.50 - li * 0.195,
                    line, ha="left", va="top",
                    fontsize=12.5, color="#333333", zorder=2)
        return height

    def darken(hex_color, factor=0.5):
        hex_color = hex_color.lstrip("#")
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        return f"#{int(r*factor):02x}{int(g*factor):02x}{int(b*factor):02x}"

    # ── TITLE ─────────────────────────────────────────────────────────────────
    banner(
        "GILGIT-BALTISTAN  CLIMATE CHANGE REPORT   1990 – 2024",
        sub="What is changing in GB weather and why it is happening  |  "
            "35 years of corrected satellite data  |  5 weather stations",
        height=0.72, fontsize=21
    )
    gap(0.12)

    # ── STATS ─────────────────────────────────────────────────────────────────
    stat_row([
        ("Real warming rate",   "+0.08°C / decade",  "#e74c3c"),
        ("Broken data claimed", "+1.42°C / decade",  "#888888"),
        ("Rainfall 1990-2016",  "Down at all 5",     "#3498db"),
        ("Low-elev snowfall",   "Down 12 – 18%",     "#9b59b6"),
        ("Fastest warming",     "Gilgit & Chilas",   "#e67e22"),
        ("Most stable",         "Khunjerab 4693m",   "#27ae60"),
    ])
    gap(0.20)

    # ═══════════════════════════════════════════════════════════════════════════
    #  01  TEMPERATURE
    # ═══════════════════════════════════════════════════════════════════════════
    section_header("01", "TEMPERATURE", "#c0392b")
    gap(0.06)
    ax.text(0.65, Y[0],
            "+0.08°C per decade over 1990-2024 after fixing the data, likely an underestimate",
            ha="left", va="top", fontsize=15, fontweight="bold",
            color="#c0392b", style="italic")
    Y[0] -= 0.32
    gap(0.06)

    reason(1, "Global Greenhouse Gases",
           "Burning coal, oil and gas worldwide traps heat in the atmosphere. The Hindu Kush Himalaya "
           "warms roughly twice as fast as the global average because cold thin air at altitude "
           "amplifies any extra heat from greenhouse gases.",
           "#c0392b")
    gap(0.06)
    reason(2, "Low Valleys Warmed Fastest Here",
           "In the clean 1990-2016 record, Gilgit (+0.34°C per decade) and Chilas (+0.23°C) warmed "
           "fastest, while Skardu, Hunza and Khunjerab barely moved. Studies usually find high "
           "mountains warming faster, so treat these station-level numbers from a coarse grid with care.",
           "#c0392b")
    gap(0.06)
    reason(3, "Black Carbon on Snow",
           "Soot from vehicles and crop burning in Pakistan and India drifts into GB on the wind "
           "and settles on glaciers. Dark soot absorbs sunlight instead of reflecting it, "
           "accelerating snowmelt and raising local temperatures above the natural rate.",
           "#c0392b")
    gap(0.06)
    reason(4, "Shrinking Snow Cover",
           "As snow shrinks each decade, bare dark rock is exposed underneath. Rock absorbs far "
           "more heat than white snow. This creates a cycle where less snow leads to more warming, "
           "which leads to even less snow the following year.",
           "#c0392b")
    gap(0.22)

    # ═══════════════════════════════════════════════════════════════════════════
    #  02  RAINFALL
    # ═══════════════════════════════════════════════════════════════════════════
    section_header("02", "RAINFALL", "#2471a3")
    gap(0.06)
    ax.text(0.65, Y[0],
            "Rainfall fell at all five stations from 1990 to 2016, clearest at Gilgit",
            ha="left", va="top", fontsize=15, fontweight="bold",
            color="#2471a3", style="italic")
    Y[0] -= 0.32
    gap(0.06)

    reason(1, "Weakening Western Disturbances",
           "GB gets most of its winter rain and snow from storm systems called Western Disturbances "
           "that blow in from the Mediterranean Sea. Climate change is shifting the jet stream "
           "northward, so fewer of these storms reach GB each year, reducing vital winter moisture.",
           "#2471a3")
    gap(0.06)
    reason(2, "Indian Monsoon Shifting",
           "The summer monsoon from the Arabian Sea is arriving later and leaving earlier each year "
           "as ocean temperatures rise. GB catches only the tail end of this monsoon, so the already "
           "small share it receives is getting smaller and more unpredictable decade by decade.",
           "#2471a3")
    gap(0.06)
    reason(3, "Faster Evaporation",
           "Warmer temperatures pull moisture out of soil more quickly after rain. Even when the same "
           "amount of rain falls, the ground dries out sooner. Crops and pastures that once stayed "
           "damp for weeks after a rain event now run dry within days.",
           "#2471a3")
    gap(0.22)

    # ═══════════════════════════════════════════════════════════════════════════
    #  03  SNOWFALL
    # ═══════════════════════════════════════════════════════════════════════════
    section_header("03", "SNOWFALL", "#6c3483")
    gap(0.06)
    ax.text(0.65, Y[0],
            "Snowfall fell 12 to 18 percent below 2,500 metres between the 1990s and 2010-16",
            ha="left", va="top", fontsize=15, fontweight="bold",
            color="#6c3483", style="italic")
    Y[0] -= 0.32
    gap(0.06)

    reason(1, "Less Snow, Not More Rain",
           "Rain totals did not rise to make up for the lost snow. The snow decline tracks the "
           "overall drop in precipitation rather than a clean switch from snow to rain. Farmers "
           "who rely on snowmelt for spring irrigation get less water either way.",
           "#6c3483")
    gap(0.06)
    reason(2, "Earlier Spring Melt",
           "Warmer springs melt snow earlier, shifting river flow away from the summer growing "
           "season when farmers need it most. This dataset does not measure river flow, so it "
           "cannot say how large that shift has been in GB.",
           "#6c3483")
    gap(0.06)
    reason(3, "Karakoram Anomaly Fading",
           "GB was famous for a unique pattern where its glaciers were growing while glaciers "
           "elsewhere in Asia shrank. Strong westerly winds were delivering extra winter snowfall. "
           "Research suggests this protective effect may be weakening. This dataset alone "
           "cannot confirm it, since it has no glacier measurements.",
           "#6c3483")
    gap(0.22)

    # ═══════════════════════════════════════════════════════════════════════════
    #  04  WIND
    # ═══════════════════════════════════════════════════════════════════════════
    section_header("04", "WIND", "#1e8449")
    gap(0.06)
    ax.text(0.65, Y[0],
            "Wind was flat from 1990 to 2016; the changes after 2017 are the ERA5 break, not climate",
            ha="left", va="top", fontsize=15, fontweight="bold",
            color="#1e8449", style="italic")
    Y[0] -= 0.32
    gap(0.06)

    reason(1, "Jet Stream Moving North",
           "The atmospheric river that steers weather systems across Asia is drifting northward "
           "as the Arctic warms faster than the tropics. This pushes moisture-carrying storms "
           "away from GB, reducing the steady winter winds that historically delivered reliable "
           "precipitation to the valleys and glaciers.",
           "#1e8449")
    gap(0.06)
    reason(2, "Stronger Valley Heating",
           "Hotter ground in summer creates more powerful upward air columns inside GB valleys. "
           "This produces stronger afternoon gusts that dry out crops and pastures faster, adding "
           "to the damage already caused by reduced rainfall and faster soil evaporation.",
           "#1e8449")
    gap(0.28)

    # ═══════════════════════════════════════════════════════════════════════════
    #  CONCLUSION
    # ═══════════════════════════════════════════════════════════════════════════
    banner("CONCLUSION", height=0.48, fontsize=19, bg="#1a252f")
    gap(0.14)

    CONC = [
        ("#fef9e7", "The Real Warming is Modest but Real",
         "+0.08°C per decade over 35 years, about +0.3°C in "
         "total. The fix also removes some real change, so the "
         "true figure is likely higher. Small in number, but it "
         "matters for an ecosystem built on snow and ice."),
        ("#eaf4fb", "The Bigger Risk is Water Timing",
         "The clearer signal is in water, not temperature. "
         "Snowfall in the valleys fell 12 to 18 percent from "
         "the 1990s to 2010-16, and rainfall fell too, so less "
         "water is stored as snow for the growing season."),
        ("#fdf2f8", "Why the Data Had to Be Fixed",
         "An ERA5 update between 2016 and 2017 created a fake "
         "jump making GB look like it warmed 17 times faster. "
         "The 2.35°C per decade result was a data error, not a "
         "climate signal. Fixing it was essential for accuracy."),
    ]

    conc_w = 23.6 / 3
    max_h  = 0
    for i, (bg, ctitle, cbody) in enumerate(CONC):
        left = 0.2 + i * conc_w
        h    = conclusion_box(ctitle, cbody, bg, left, conc_w)
        max_h = max(max_h, h)
    Y[0] -= max_h + 0.14

    # ── FOOTER ────────────────────────────────────────────────────────────────
    rect = mpatches.FancyBboxPatch(
        (0.2, Y[0] - 0.28), 23.6, 0.28,
        boxstyle="square,pad=0", fc="#2c3e50", ec="none", zorder=1
    )
    ax.add_patch(rect)
    ax.text(12, Y[0] - 0.14,
            "Data: Open-Meteo Historical API  |  ERA5 ECMWF  |  "
            "Stations: Gilgit, Skardu, Hunza, Chilas, Khunjerab  |  1990 to 2024  |  Bias corrected",
            ha="center", va="center", fontsize=11.5,
            color="#7f8c8d", zorder=2)

    # Crop the canvas to the content so the poster has no empty tail
    bottom = Y[0] - 0.6
    ax.set_ylim(bottom, 34)
    fig.set_size_inches(24, 34 - bottom)

    # Final save
    print(f"Saving → {OUT}")
    fig.savefig(OUT, dpi=130, bbox_inches="tight", facecolor="white")
    print("Done.")
    plt.close()

draw_report()
