# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "altair",
#     "numpy",
#     "marimo-learn==0.14.0",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import altair as alt
    from marimo_learn import (
        NumericEntryWidget,
        PredictThenCheckWidget,
        LabelingWidget,
        MatchingWidget,
        ConceptMapWidget,
    )

    return (
        ConceptMapWidget,
        LabelingWidget,
        MatchingWidget,
        NumericEntryWidget,
        PredictThenCheckWidget,
        alt,
        mo,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Momentum & Impulse, Part 1: Momentum

    *VCE Physics Unit 2, AOS1, Energy and motion*

    This is **Part 1 of 4**. In this part you will learn:

    - What momentum is
    - How to calculate it with $p = mv$
    - Why momentum has a direction

    *This part should take about 20 minutes.*

    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What is momentum?

    **Momentum** measures how hard it is to stop a moving object. A fast, heavy
    object is hard to stop, so it has a large momentum.

    Momentum is the mass of an object multiplied by its velocity:

    $$p = mv$$

    - $p$ = momentum, in kilogram metres per second ($\text{kg m s}^{-1}$)
    - $m$ = mass, in kilograms (kg)
    - $v$ = velocity, in metres per second ($\text{m s}^{-1}$)

    The unit of momentum comes straight from multiplying the units of mass and
    velocity:

    $$[\text{kg m s}^{-1}] = [\text{kg}] \times [\text{m s}^{-1}]$$

    Because velocity has a **direction**, momentum has a direction too. It always
    points the same way the object is moving. We show direction with a **sign**:
    for example, we might take east (or right) as positive and west (or left) as
    negative.

    > **Key idea:** a heavy, slow object can have the *same* momentum as a light,
    > fast object.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Worked example

    **A 1200 kg car travels east at 15 m/s. Calculate the car's momentum.**

    **Step 1** — Write down what you know.

    $m = 1200 \text{ kg}, \quad v = +15 \text{ m/s (east)}$

    **Step 2** — Write the formula.

    $p = mv$

    **Step 3** — Substitute and solve.

    $p = 1200 \times 15 = 18\,000 \text{ kg m s}^{-1}$

    **Step 4** — State the answer *with its direction*.

    $p = 18\,000 \text{ kg m s}^{-1} \text{ east}$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A common mistake

    > *"A 20 kg trolley moving at 3 m/s has more momentum than a 4 kg trolley
    > moving at 15 m/s, because 20 is bigger than 4."*

    This is **wrong**. It compares mass alone, not momentum. You must multiply
    mass by velocity:

    - Trolley A: $p = 20 \times 3 = 60 \text{ kg m s}^{-1}$
    - Trolley B: $p = 4 \times 15 = 60 \text{ kg m s}^{-1}$

    They have the **same** momentum. A heavy slow object and a light fast object
    can match.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explore it: the momentum graph

    Below are two balls. Drag the sliders to change each ball's mass and
    velocity, and watch how the momentum bar changes.

    **Before you touch the sliders, predict:** if you double a ball's velocity,
    what happens to its momentum?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mass_slider1 = mo.ui.slider(
        start=1, stop=30, step=1, value=20, label="Ball 1 mass, $m$ (kg)",
        debounce=True,
    )
    velocity_slider1 = mo.ui.slider(
        start=-20, stop=20, step=1, value=-5, label="Ball 1 velocity, $v$ (m/s)",
        debounce=True,
    )
    mass_slider2 = mo.ui.slider(
        start=1, stop=20, step=1, value=10, label="Ball 2 mass, $m$ (kg)",
        debounce=True,
    )
    velocity_slider2 = mo.ui.slider(
        start=-38, stop=38, step=1, value=10, label="Ball 2 velocity, $v$ (m/s)",
        debounce=True,
    )

    mo.hstack(
        [
            mo.vstack([mass_slider1, velocity_slider1], justify="start"),
            mo.vstack([mass_slider2, velocity_slider2], justify="start"),
        ]
    )
    return mass_slider1, mass_slider2, velocity_slider1, velocity_slider2


@app.cell(hide_code=True)
def _(mass_slider1, mass_slider2, mo, velocity_slider1, velocity_slider2):
    _p1 = mass_slider1.value * velocity_slider1.value
    _p2 = mass_slider2.value * velocity_slider2.value
    mo.md(
        f"""
        $p_1 = {mass_slider1.value} \\times {velocity_slider1.value} =
        {_p1:,.1f}\\ \\text{{kg m s}}^{{-1}}$
        Direction: **{'positive (e.g. east)' if _p1 > 0 else ('negative (e.g. west)' if _p1 < 0 else 'stationary, zero momentum')}**

        $p_2 = {mass_slider2.value} \\times {velocity_slider2.value} =
        {_p2:,.1f}\\ \\text{{kg m s}}^{{-1}}$
        Direction: **{'positive (e.g. east)' if _p2 > 0 else ('negative (e.g. west)' if _p2 < 0 else 'stationary, zero momentum')}**
        """
    )
    return


@app.cell(hide_code=True)
def _(alt, mass_slider1, mass_slider2, velocity_slider1, velocity_slider2):
    _m1 = mass_slider1.value
    _v1 = velocity_slider1.value
    _p1 = _m1 * _v1

    _m2 = mass_slider2.value
    _v2 = velocity_slider2.value
    _p2 = _m2 * _v2

    # Ball 1 uses graded shades of red, Ball 2 graded shades of blue.
    # Within each ball the shade darkens from mass -> velocity -> momentum.
    _reds = ["#fcae91", "#fb6a4a", "#cb181d"]
    _blues = ["#bdd7e7", "#6baed6", "#2171b5"]

    def _panel(label, value, color, ylim, unit, title=None, title_color=None):
        # Built as a plain Vega-Lite spec dict rather than chained Altair
        # calls: each .mark_x()/.encode()/.properties() call deep-copies
        # the whole chart internally, which made this cell's rebuild (18
        # such objects) take ~500ms per slider move. A dict + from_dict(
        # validate=False) skips that entirely — same output, ~50x faster.
        _spec = {
            "data": {"values": [{"label": label, "value": value}]},
            "layer": [
                {
                    "mark": {"type": "bar", "color": color, "stroke": "black", "strokeWidth": 0.6},
                    "encoding": {
                        "x": {"field": "label", "type": "nominal", "title": None,
                              "axis": {"labels": False, "ticks": False}},
                        "y": {"field": "value", "type": "quantitative",
                              "title": f"{label} ({unit})",
                              "scale": {"domain": [-ylim, ylim]}},
                    },
                },
                {
                    "data": {"values": [{"y": 0}]},
                    "mark": {"type": "rule", "color": "black", "strokeWidth": 0.8},
                    "encoding": {"y": {"field": "y", "type": "quantitative"}},
                },
                {
                    # Value label on the bar so meaning does not rely on colour alone.
                    "mark": {"type": "text", "align": "center",
                             "baseline": "bottom" if value >= 0 else "top",
                             "dy": -6 if value >= 0 else 6,
                             "fontWeight": "bold", "fontSize": 11},
                    "encoding": {
                        "x": {"field": "label", "type": "nominal", "axis": None},
                        "y": {"field": "value", "type": "quantitative"},
                        "text": {"field": "value", "type": "quantitative", "format": ",.0f"},
                    },
                },
            ],
            "width": 110,
            "height": 180,
        }
        if title:
            _spec["title"] = {"text": title, "color": title_color, "fontSize": 13, "fontWeight": "bold"}
        return _spec

    # Row 1: Ball 1, row 2: Ball 2 — matches the original panel-grid layout.
    _row1 = {
        "hconcat": [
            _panel("Mass", _m1, _reds[0], 33, "kg"),
            _panel("Velocity", _v1, _reds[1], 40, "m/s", title="Ball 1", title_color="#cb181d"),
            _panel("Momentum", _p1, _reds[2], 800, "kg m/s"),
        ]
    }
    _row2 = {
        "hconcat": [
            _panel("Mass", _m2, _blues[0], 33, "kg"),
            _panel("Velocity", _v2, _blues[1], 40, "m/s", title="Ball 2", title_color="#2171b5"),
            _panel("Momentum", _p2, _blues[2], 800, "kg m/s"),
        ]
    }

    fig1 = alt.Chart.from_dict(
        {"vconcat": [_row1, _row2], "config": {"view": {"strokeWidth": 0}}},
        validate=False,
    )
    fig1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Checkpoint

    Use the sliders above to help you answer these.

    **1. What does an object need in order to have a *negative* momentum?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    check1_explain = mo.ui.text_area(
        placeholder="Type your answer here...", label="Your answer:", full_width=True
    )
    check1_explain
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Reveal answer": mo.md(
                """
                A **negative velocity** (moving in the direction you have chosen
                as negative). Mass is always positive, so only the velocity can
                make the momentum negative.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **2.**
    """)
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q1_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="A 0.058 kg tennis ball is served at 50 m/s. Calculate its momentum, in kg m/s.",
            correct_answer=0.058 * 50,
            tolerance=0.05,
            explanation="p = mv = 0.058 × 50 = 2.9 kg m s⁻¹",
        )
    )
    q1_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quick practice
    """)
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q2_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="Q1. Calculate the momentum of a 5.20 kg cat running north at 4.50 m/s, in kg m/s.",
            correct_answer=5.20 * 4.50,
            tolerance=0.1,
            explanation="p = mv = 5.20 × 4.50 = 23.4 kg m s⁻¹",
        )
    )
    q2_check
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q3_check = mo.ui.anywidget(
        NumericEntryWidget(
            question=(
                "Q2. A 9 kg bowling ball moves at +12 m/s. A 5 kg bowling "
                "ball has the same momentum. What is the velocity of the "
                "5 kg ball, in m/s?"
            ),
            correct_answer=9 * 12 / 5,
            tolerance=0.05,
            explanation=(
                "Momentum of the 9 kg ball: p = 9 × 12 = 108 kg m s⁻¹. "
                "The 5 kg ball has the same momentum, so 108 = 5 × v, "
                "giving v = 108 ÷ 5 = 21.6 m/s."
            ),
        )
    )
    q3_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    ## Additional activity: predict, then check

    Try the sliders above first if you like, then predict without them.
    """)
    return


@app.cell(hide_code=True)
def _(PredictThenCheckWidget, mo):
    poe_check = mo.ui.anywidget(
        PredictThenCheckWidget(
            question=(
                "Ball 1 starts at mass = 10 kg, velocity = 4 m/s "
                "(momentum = 40 kg·m/s). If you double the velocity to "
                "8 m/s, leaving the mass unchanged, what happens to the "
                "momentum?"
            ),
            code="p = m × v\n10 kg × 4 m/s = 40 kg·m/s\n10 kg × 8 m/s = ?",
            output="10 kg × 8 m/s = 80 kg·m/s",
            options=[
                "It stays the same",
                "It doubles",
                "It halves",
                "It goes up by 10",
            ],
            correct_answer=1,
            explanations=[
                "Wrong: momentum depends on velocity as well as mass, so changing v does change p.",
                "Correct: momentum is directly proportional to velocity (p = mv), so doubling v doubles p — from 40 to 80 kg·m/s.",
                "Wrong: halving would happen if velocity were halved, not doubled.",
                "Wrong: momentum scales multiplicatively with velocity (×2), not by a fixed addition.",
            ],
        )
    )
    poe_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Match it: quantity and unit
    """)
    return


@app.cell(hide_code=True)
def _(MatchingWidget, mo):
    unit_match = mo.ui.anywidget(
        MatchingWidget(
            question="Match each quantity to its SI unit:",
            left=["Momentum, p", "Mass, m", "Velocity, v"],
            right=["kg m s⁻¹", "kg", "m s⁻¹"],
            correct_matches={0: 0, 1: 1, 2: 2},
        )
    )
    unit_match
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Label it: the worked example, step by step

    Here's the same 1200 kg car example from earlier — this time, label
    which step each line belongs to.
    """)
    return


@app.cell(hide_code=True)
def _(LabelingWidget, mo):
    worked_example_label = mo.ui.anywidget(
        LabelingWidget(
            question="Label each line of this worked momentum problem:",
            labels=["Identify knowns", "Apply formula", "Substitute values", "State answer"],
            text_lines=[
                "m = 1200 kg, v = 15 m/s east",
                "p = mv",
                "p = 1200 × 15",
                "p = 18 000 kg m/s east",
            ],
            correct_labels={0: [0], 1: [1], 2: [2], 3: [3]},
        )
    )
    worked_example_label
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concept map: getting from one quantity to another

    $p = mv$ isn't just one formula — it's three, depending on which
    quantity you're solving for. Map how to get from one to another.
    """)
    return


@app.cell(hide_code=True)
def _(ConceptMapWidget, mo):
    momentum_concept_map = mo.ui.anywidget(
        ConceptMapWidget(
            question="Map how to convert between these quantities:",
            concepts=["Momentum (p)", "Mass (m)", "Velocity (v)"],
            terms=["× v →", "× m →", "÷ v →", "÷ m →"],
            correct_edges=[
                {"from": "Mass (m)", "to": "Momentum (p)", "label": "× v →"},
                {"from": "Velocity (v)", "to": "Momentum (p)", "label": "× m →"},
                {"from": "Momentum (p)", "to": "Mass (m)", "label": "÷ v →"},
                {"from": "Momentum (p)", "to": "Velocity (v)", "label": "÷ m →"},
            ],
        )
    )
    momentum_concept_map
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    **Next:** Part 2 looks at what happens to momentum when a force acts, the
    idea of **impulse**, $\Delta p = F_{net}\Delta t$.

    ------

    Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
    — free to use, adapt, and share for non-commercial purposes, with attribution.
    Developed with the assistance of Claude (Anthropic), referenced against the
    [VCE Physics Study Design](https://www.vcaa.vic.edu.au/curriculum/vce/vce-study-designs/physics) (VCAA).
    """)
    return


if __name__ == "__main__":
    app.run()
