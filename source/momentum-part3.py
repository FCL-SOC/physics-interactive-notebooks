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
    from marimo_learn import NumericEntryWidget, PredictThenCheckWidget, OrderingWidget

    return (
        NumericEntryWidget,
        OrderingWidget,
        PredictThenCheckWidget,
        alt,
        mo,
        np,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Momentum & Impulse, Part 3: Impulse in collisions

    *VCE Physics Unit 2, AOS1, Energy and motion*

    This is **Part 3 of 4**. It follows on from Part 2 (Change in momentum). In
    this part you will learn:

    - How impulse applies to a single object in a collision, $F\Delta t = m\Delta v$
    - Why extending the collision time **reduces the force**
    - How this explains airbags, crumple zones and catching a ball softly

    *This part should take about 20 minutes.*

    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Impulse on one object

    When one object is involved in a collision, the impulse it receives equals
    its change in momentum:

    $$F\,\Delta t = m\,\Delta v$$

    We can rearrange this to find the force:

    $$F = \dfrac{m\,\Delta v}{\Delta t}$$

    Look carefully: the mass $m$ and the change in velocity $\Delta v$ are fixed
    by the situation (the object still has to speed up or stop by the same
    amount). The only thing we can change is $\Delta t$, the collision time.

    Because $\Delta t$ is on the bottom of the fraction, making it **larger**
    makes the force **smaller**:

    $$F \propto \dfrac{1}{\Delta t}$$

    > **Key idea:** stretch out the collision time and you cut down the force.
    > That is exactly what airbags, crumple zones, bending your knees when you
    > land, and moving your hands back as you catch a ball all do.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Worked example

    **A 60 kg crash-test dummy travelling at 20 m/s is brought to rest.**

    **Without an airbag** (stopping time $\Delta t = 0.1$ s):

    $F = \dfrac{m\,\Delta v}{\Delta t} = \dfrac{60 \times 20}{0.1} = 12\,000
    \text{ N}$

    **With an airbag** (stopping time stretched to $\Delta t = 0.5$ s):

    $F = \dfrac{60 \times 20}{0.5} = 2\,400 \text{ N}$

    The impulse ($m\Delta v = 1200$ kg m/s) is the **same** both times. Only the
    force changed, because the time changed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A common mistake (non-example)

    > *"The airbag reduces the impulse on the person, so they have a smaller
    > change in velocity."*

    This is **wrong**. The dummy still goes from 20 m/s to rest either way, so
    the change in velocity $\Delta v$, and the impulse $m\Delta v$, are exactly
    the same. What the airbag changes is $\Delta t$: spreading the same impulse
    over a longer time gives a **smaller average force**, not a smaller impulse.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explore it: collision time and force

    A person of fixed mass is stopping in a car crash (fixed $\Delta v$). Drag
    the **collision-time** slider and watch the force change.

    - **Left:** the grey rectangle is the crash with no airbag; the green one is
      your collision. Both have the **same area**, the impulse $m\Delta v$, so
      a wider rectangle has to be shorter.
    - **Right:** force against collision time, for this impulse.

    **Predict first:** if you make the collision take twice as long, roughly what
    happens to the force?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    dummy_mass = mo.ui.slider(start=30, stop=120, step=1, value=60, label="mass (kg)", debounce=True)
    dummy_dv = mo.ui.slider(start=1, stop=30, step=1, value=20, label="$\\Delta v$ (m/s)", debounce=True)
    collision_time = mo.ui.slider(
        start=0.02, stop=1.0, step=0.02, value=0.5, label="collision time, $\\Delta t$ (s)", debounce=True
    )
    mo.hstack([dummy_mass, dummy_dv, collision_time], justify="start", gap=2)
    return collision_time, dummy_dv, dummy_mass


@app.cell(hide_code=True)
def _(collision_time, dummy_dv, dummy_mass, mo):
    _F = dummy_mass.value * dummy_dv.value / collision_time.value
    mo.md(
        f"$F = \\dfrac{{m\\Delta v}}{{\\Delta t}} = \\dfrac{{{dummy_mass.value} \\times "
        f"{dummy_dv.value}}}{{{collision_time.value}}} = {_F:,.0f}$ N"
    )
    return


@app.cell(hide_code=True)
def _(alt, collision_time, dummy_dv, dummy_mass, mo, np):
    _impulse = dummy_mass.value * dummy_dv.value
    _t = collision_time.value
    _F = _impulse / _t
    _t_ref = 0.1  # the "no airbag" stopping time from the worked example
    _F_ref = _impulse / _t_ref
    _q = {"type": "quantitative"}

    # Left: same impulse as two force-time rectangles of equal area.
    # Plain Vega-Lite dicts, not chained Altair calls (see momentum-part1).
    _rects = [
        {"case": f"no airbag (Δt = {_t_ref} s)", "t": _t_ref, "F": _F_ref},
        {"case": f"your collision (Δt = {_t:.2f} s)", "t": _t, "F": _F},
    ]
    _color = {"field": "case", "type": "nominal", "sort": None,
              "scale": {"range": ["#969696", "#2ca02c"]},
              "legend": {"orient": "top", "title": None}}
    _ft = {
        "data": {"values": _rects},
        "layer": [
            {"mark": {"type": "rect", "fillOpacity": 0.3, "strokeWidth": 2},
             "transform": [{"calculate": "0", "as": "zero"}],
             "encoding": {
                 "x": {"field": "zero", **_q, "title": "time, t (s)", "scale": {"domain": [0, 1.0]}},
                 "x2": {"field": "t"},
                 "y": {"field": "zero", **_q, "title": "force, F (N)",
                       "scale": {"domain": [0, max(_F, _F_ref) * 1.1]}},
                 "y2": {"field": "F"},
                 "color": _color, "stroke": _color}},
        ],
        "width": 300, "height": 280,
        "title": f"Same area (impulse = {_impulse:,} kg m/s)",
    }

    # Right: F against Δt for this impulse, with the current point marked.
    _t_range = np.linspace(0.02, 1.0, 200)
    _curve = [{"x": float(_x), "y": float(_impulse / _x)} for _x in _t_range]
    _x_enc = {"field": "x", **_q, "title": "collision time, Δt (s)", "scale": {"domain": [0, 1.0]}}
    _y_enc = {"field": "y", **_q, "title": "force, F (N)",
              "scale": {"domain": [0, _impulse / 0.02 * 1.05]}}
    _curve_chart = {
        "layer": [
            {"data": {"values": _curve},
             "mark": {"type": "line", "color": "#2ca02c", "strokeWidth": 2, "clip": True},
             "encoding": {"x": _x_enc, "y": _y_enc}},
            {"data": {"values": [{"x": _t, "y": _F}]},
             "mark": {"type": "point", "color": "#2ca02c", "size": 80, "filled": True},
             "encoding": {"x": _x_enc, "y": _y_enc}},
        ],
        "width": 300, "height": 280,
        "title": "F = mΔv / Δt",
    }
    fig3 = alt.Chart.from_dict({"hconcat": [_ft, _curve_chart]}, validate=False)
    mo.center(fig3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Checkpoint

    **1. Explain why increasing the collision time decreases the force an object
    feels, even though the impulse stays the same.**
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
                The impulse $m\\Delta v$ is fixed by the mass and the change in
                velocity. Since $F = m\\Delta v / \\Delta t$, the same impulse
                spread over a **longer** time $\\Delta t$ gives a **smaller**
                average force. The force and the time are inversely related.
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
            question="A 0.15 kg cricket ball travelling at 25 m/s is caught and brought to rest in 0.2 s. Calculate the average force on the ball, in N.",
            correct_answer=0.15 * 25 / 0.2,
            tolerance=1,
            explanation="F = mΔv/Δt = (0.15 × 25) / 0.2 = 18.75 N",
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
            question=(
                "Q1. A golf club strikes a stationary 0.046 kg golf ball. "
                "The contact time is 0.00050 s and the ball leaves at "
                "65.0 m/s. Calculate the average force on the ball, in N."
            ),
            correct_answer=0.046 * 65.0 / 0.00050,
            tolerance=100,
            explanation=(
                "mΔv = 0.046 × 65.0 = 2.99 kg m s⁻¹. "
                "F = mΔv/Δt = 2.99 / 0.00050 = 5980 N"
            ),
        )
    )
    q2_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Order it: solving an impulse problem

    Same idea, as a general method — put these steps in the right order.
    """)
    return


@app.cell(hide_code=True)
def _(OrderingWidget, mo):
    order_check = mo.ui.anywidget(
        OrderingWidget(
            question="Arrange these steps for solving an impulse/force problem in order:",
            items=[
                "Identify the known mass, change in velocity, and collision time",
                "Choose F = mΔv/Δt (or J = FΔt if solving for impulse instead)",
                "Substitute the known values",
                "Solve for the unknown quantity",
                "Check the answer's sign/magnitude makes physical sense",
            ],
            shuffle=True,
        )
    )
    order_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q2. A raw egg dropped onto a pile of corrugated cardboard survives, but an
    identical egg dropped from the same height onto a hard floor breaks. Explain
    why, using $F\Delta t = m\Delta v$.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q3_explain = mo.ui.text_area(
        placeholder="Type your explanation here...", label="Your explanation:", full_width=True
    )
    q3_explain
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                The cardboard crumples, increasing the time $\\Delta t$ over
                which the egg's momentum changes to zero. The impulse
                $m\\Delta v$ is the same either way, so a longer $\\Delta t$
                means a smaller average force ($F = m\\Delta v / \\Delta t$), and
                the egg survives. The hard floor doesn't give, so $\\Delta t$ is
                tiny and the force is much larger, breaking the egg.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    ## Predict, then check

    Try the sliders further up the page first if you like, then predict.
    """)
    return


@app.cell(hide_code=True)
def _(PredictThenCheckWidget, mo):
    poe_check = mo.ui.anywidget(
        PredictThenCheckWidget(
            question=(
                "A person of fixed mass and Δv is stopping in a car crash. "
                "At collision time Δt = 0.2 s the force is F. If the "
                "collision time is doubled to Δt = 0.4 s, what happens to "
                "the force?"
            ),
            code="F = mΔv / Δt\nAt Δt = 0.2 s: F\nAt Δt = 0.4 s: ?",
            output="F is halved",
            options=[
                "It stays the same",
                "It doubles",
                "It halves",
                "It goes down, but not exactly half",
            ],
            correct_answer=2,
            explanations=[
                "Wrong: F = mΔv/Δt — changing Δt on the bottom of the fraction does change F.",
                "Wrong: doubling the denominator makes F smaller, not bigger.",
                "Correct: mass and Δv (so the impulse mΔv) are unchanged; doubling Δt on the bottom exactly halves F — force and collision time are inversely proportional.",
                "Wrong: because mΔv is exactly fixed, doubling Δt gives an exact half, not an approximate change.",
            ],
        )
    )
    poe_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    **Next:** Part 4 puts two objects together and looks at **conservation of
    momentum** in collisions.

    ------

    Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
    — free to use, adapt, and share for non-commercial purposes, with attribution.
    Developed with the assistance of Claude (Anthropic), referenced against the
    [VCE Physics Study Design](https://www.vcaa.vic.edu.au/curriculum/vce/vce-study-designs/physics) (VCAA).
    """)
    return


if __name__ == "__main__":
    app.run()
