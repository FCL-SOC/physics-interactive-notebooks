# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "altair",
#     "marimo-learn==0.14.0",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", layout_file="layouts/momentum-part2-teacher.slides.json")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import altair as alt
    from marimo_learn import (
        NumericEntryWidget,
        PredictThenCheckWidget,
        MatchingWidget,
        ConceptMapWidget,
    )

    return (
        ConceptMapWidget,
        MatchingWidget,
        NumericEntryWidget,
        PredictThenCheckWidget,
        alt,
        mo,
    )


@app.function(hide_code=True)
def area_chart(
    x, y, color, xlim, ylim, xlabel, ylabel, title, label, label_xy,
    width=480, height=320,
):
    # Shared "area under a force-time line" chart builder: a plain
    # Vega-Lite spec dict (not chained Altair calls, which are much
    # slower to rebuild on every slider move — see momentum-part1 for
    # the measured comparison). x/y are the two endpoints of the top
    # edge of the shaded region; label_xy places the bold impulse
    # value text (replaces matplotlib's separate legend, simpler to
    # read at a glance).
    _pts = [{"x": float(_x), "y": float(_y)} for _x, _y in zip(x, y)]
    _x_enc = {"field": "x", "type": "quantitative", "title": xlabel,
               "scale": {"domain": list(xlim)}}
    _y_enc = {"field": "y", "type": "quantitative", "title": ylabel,
               "scale": {"domain": list(ylim)}}
    _layers = [
        {"data": {"values": _pts},
         "mark": {"type": "area", "color": color, "opacity": 0.4},
         "encoding": {"x": _x_enc, "y": _y_enc}},
        {"data": {"values": _pts},
         "mark": {"type": "line", "color": color, "strokeWidth": 2},
         "encoding": {"x": _x_enc, "y": _y_enc}},
        # Dashed guide line from the top-right corner down to the x-axis.
        {"data": {"values": [{"x": x[-1], "y": 0}, {"x": x[-1], "y": y[-1]}]},
         "mark": {"type": "line", "color": color, "strokeWidth": 1, "strokeDash": [4, 4]},
         "encoding": {"x": {"field": "x", "type": "quantitative"}, "y": {"field": "y", "type": "quantitative"}}},
        {"data": {"values": [{"y": 0}]},
         "mark": {"type": "rule", "color": "black", "strokeWidth": 0.8},
         "encoding": {"y": {"field": "y", "type": "quantitative"}}},
        {"data": {"values": [{"x": 0}]},
         "mark": {"type": "rule", "color": "black", "strokeWidth": 0.8},
         "encoding": {"x": {"field": "x", "type": "quantitative"}}},
        {"data": {"values": [{"x": label_xy[0], "y": label_xy[1]}]},
         "mark": {"type": "text", "fontWeight": "bold", "fontSize": 11, "lineBreak": "\n"},
         "encoding": {
            "x": {"field": "x", "type": "quantitative"},
            "y": {"field": "y", "type": "quantitative"},
            "text": {"value": label},
         }},
    ]
    return {
        "data": {"values": _pts},
        "layer": _layers,
        "width": width,
        "height": height,
        "title": title,
    }


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Momentum & Impulse, Part 2: Change in momentum

    *VCE Physics Unit 2, AOS1, Energy and motion*

    This is **Part 2 of 4**. It follows on from Part 1 (Momentum). In this part
    you will learn:

    - How a net force changes an object's momentum
    - The idea of **impulse**, $\Delta p = F_{net}\Delta t$
    - How to read impulse as the **area** under a force–time graph

    *This part should take about 20 minutes.*

    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A force changes momentum

    In Part 1 you calculated momentum, $p = mv$. Now: what makes momentum
    change? A **net force** acting for some **time**.

    $$\Delta p = F_{net}\,\Delta t$$

    The symbol $\Delta$ (delta) means "the change in". So $\Delta p$ is the
    change in momentum, and $\Delta t$ is the time interval the force acts over.

    We call $F_{net}\Delta t$ the **impulse**. Impulse and change in momentum are
    the same thing.

    ### Where does this come from?

    Start with Newton's second law:

    $$F_{net} = ma$$

    Multiply both sides by $\Delta t$:

    $$F_{net}\,\Delta t = ma\,\Delta t$$

    Acceleration times time is a change in velocity ($a\,\Delta t = \Delta v$),
    so:

    $$F_{net}\,\Delta t = m\,\Delta v = \Delta p$$

    > **On a force–time graph, the impulse is the area under the graph.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Worked example

    **A net force of 40 N acts on a trolley for 0.5 s. Find the change in
    momentum.**

    **Step 1** — Write down what you know.

    $F_{net} = 40 \text{ N}, \quad \Delta t = 0.5 \text{ s}$

    **Step 2** — Write the formula.

    $\Delta p = F_{net}\,\Delta t$

    **Step 3** — Substitute and solve.

    $\Delta p = 40 \times 0.5 = 20 \text{ kg m s}^{-1}$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A common mistake (non-example)

    > *"A 40 N force pushes a trolley east while 15 N of friction acts west, for
    > 0.5 s. So $\Delta p = 40 \times 0.5 = 20$ kg m s⁻¹."*

    This is **wrong**. It only uses one force. The formula needs the **net**
    force, the total of all forces:

    $F_{net} = 40 - 15 = 25 \text{ N}$

    $\Delta p = 25 \times 0.5 = 12.5 \text{ kg m s}^{-1}$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explore it: the force–time graph

    Adjust the net force and the time interval. The shaded area is the impulse,
    $\Delta p$.

    **Predict first:** if you double the time the force acts for, what happens to
    the change in momentum?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    force_slider = mo.ui.slider(
        start=-100, stop=100, step=1, value=40, label="net force, $F_{net}$ (N)", debounce=True
    )
    time_slider = mo.ui.slider(
        start=0.1, stop=5, step=0.1, value=0.5, label="time interval, $\\Delta t$ (s)", debounce=True
    )
    mo.hstack([force_slider, time_slider], justify="start", gap=2)
    return force_slider, time_slider


@app.cell(hide_code=True)
def _(force_slider, mo, time_slider):
    _dp = force_slider.value * time_slider.value
    mo.md(
        f"$\\Delta p = F_{{net}}\\Delta t = {force_slider.value} \\times "
        f"{time_slider.value} = {_dp:,.2f}\\ \\text{{kg m s}}^{{-1}}$"
    )
    return


@app.cell(hide_code=True)
def _(alt, force_slider, mo, time_slider):
    _F = force_slider.value
    _t = time_slider.value
    _area = _F * _t

    fig2 = alt.Chart.from_dict(
        area_chart(
            [0, _t], [_F, _F], "#ff7f0e",
            xlim=(0, 5.2), ylim=(-110, 110),
            xlabel="time, t (s)", ylabel="net force, F (N)",
            title="Constant force: impulse = area of the rectangle",
            label=f"area = {_F} × {_t:.1f}\n= {_area:,.1f} kg m/s",
            label_xy=(_t / 2, _F / 2),
        ),
        validate=False,
    )
    mo.center(fig2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Checkpoint

    **1. Using the graph, explain what happens to the impulse when you increase
    the net force. What about when you increase the time?**
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
                Impulse is the area of the rectangle, $F_{net}\\times\\Delta t$.
                Increasing either the height (force) or the width (time) makes
                the area bigger, so the change in momentum increases. Doubling
                either one doubles the impulse.
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
            question="A net force of 15 N acts on an object for 3 seconds. Calculate the change in momentum, in kg m/s.",
            correct_answer=15 * 3,
            tolerance=0.5,
            explanation="Δp = F_net × Δt = 15 × 3 = 45 kg m s⁻¹",
        )
    )
    q1_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    ## Impulse as the area under a force–time graph

    So far the force was **constant**, giving a rectangle. In real situations the
    force often **changes** during the time it acts, for example a foot pushing
    off the ground, or a bat hitting a ball.

    As long as the graph is made of **straight lines**, the rule is the same:

    > **The impulse is still the area under the force–time graph.**

    You already know how to find these areas:

    - **Rectangle** (constant force): $\text{area} = F \times \Delta t$
    - **Triangle** (force ramps from 0): $\text{area} = \tfrac{1}{2} \times \Delta t \times F$
    - **Trapezium** (force changes from $F_1$ to $F_2$): $\text{area} = \tfrac{1}{2}(F_1 + F_2)\,\Delta t$

    Below, the force changes **linearly** from a starting value to an ending
    value. Drag the sliders and watch the shaded area, that area is the impulse.

    **Predict first:** if the force ramps from 0 N up to 60 N over 4 s, what is
    the impulse?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    f_start_slider = mo.ui.slider(
        start=0, stop=100, step=5, value=0, label="start force, $F_1$ (N)", debounce=True
    )
    f_end_slider = mo.ui.slider(
        start=0, stop=100, step=5, value=60, label="end force, $F_2$ (N)", debounce=True
    )
    dt_slider = mo.ui.slider(
        start=0.5, stop=5, step=0.5, value=4, label="time interval, $\\Delta t$ (s)", debounce=True
    )
    mo.hstack([f_start_slider, f_end_slider, dt_slider], justify="start", gap=2)
    return dt_slider, f_end_slider, f_start_slider


@app.cell(hide_code=True)
def _(dt_slider, f_end_slider, f_start_slider, mo):
    _f1 = f_start_slider.value
    _f2 = f_end_slider.value
    _dt = dt_slider.value
    _area = 0.5 * (_f1 + _f2) * _dt
    _shape = "rectangle" if _f1 == _f2 else ("triangle" if _f1 == 0 or _f2 == 0 else "trapezium")
    mo.md(
        f"""
        Shape under the graph: **{_shape}**

        $\\Delta p = \\tfrac{{1}}{{2}}(F_1 + F_2)\\,\\Delta t
        = \\tfrac{{1}}{{2}}({_f1} + {_f2}) \\times {_dt}
        = {_area:,.1f}\\ \\text{{kg m s}}^{{-1}}$
        """
    )
    return


@app.cell(hide_code=True)
def _(alt, dt_slider, f_end_slider, f_start_slider, mo):
    _f1 = f_start_slider.value
    _f2 = f_end_slider.value
    _dt = dt_slider.value
    _area = 0.5 * (_f1 + _f2) * _dt

    fig_area = alt.Chart.from_dict(
        area_chart(
            [0, _dt], [_f1, _f2], "#9467bd",
            xlim=(0, 5.2), ylim=(0, 110),
            xlabel="time, t (s)", ylabel="net force, F (N)",
            title="Changing force: impulse = area under the straight line",
            label=f"impulse = {_area:,.1f} kg m/s",
            label_xy=(_dt / 2, max(_f1 + _f2, 10) / 4),
        ),
        validate=False,
    )
    mo.center(fig_area)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Read the area.**
    """)
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q_area_check = mo.ui.anywidget(
        NumericEntryWidget(
            question=(
                "A net force ramps up linearly from 0 N to 50 N over 3.0 s. "
                "The area under this graph is a triangle. Calculate the "
                "impulse, in kg m/s. (Hint: area of a triangle = ½ × base × "
                "height.)"
            ),
            correct_answer=0.5 * 3.0 * 50,
            tolerance=0.5,
            explanation=(
                "The graph is a triangle with base Δt = 3.0 s and height "
                "F = 50 N. Δp = area = ½ × base × height = ½ × 3.0 × 50 "
                "= 75 kg m s⁻¹"
            ),
        )
    )
    q_area_check
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
            question="Q1. A net force of 8.0 N acts on a box for 2.5 s. Calculate the impulse, in kg m/s.",
            correct_answer=8.0 * 2.5,
            tolerance=0.2,
            explanation="Δp = F_net × Δt = 8.0 × 2.5 = 20 kg m s⁻¹",
        )
    )
    q2_check
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q3_check = mo.ui.anywidget(
        NumericEntryWidget(
            question=(
                "Q2. A 30 N force pushes a crate east while 12 N of friction "
                "acts west. The forces act for 4.0 s. Calculate the change "
                "in momentum, in kg m/s. (Hint: find the net force first.)"
            ),
            correct_answer=(30 - 12) * 4.0,
            tolerance=0.5,
            explanation=(
                "F_net = 30 − 12 = 18 N. Δp = F_net × Δt = 18 × 4.0 "
                "= 72 kg m s⁻¹"
            ),
        )
    )
    q3_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    ## Match it: quantity and unit
    """)
    return


@app.cell(hide_code=True)
def _(MatchingWidget, mo):
    impulse_unit_match = mo.ui.anywidget(
        MatchingWidget(
            question="Match each quantity to its SI unit:",
            left=["Force, F", "Impulse, J", "Momentum, p"],
            right=["N", "N·s", "kg m s⁻¹"],
            correct_matches={0: 0, 1: 1, 2: 2},
        )
    )
    impulse_unit_match
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concept map: force, time, and momentum

    $\Delta p = F_{net}\Delta t$ links four quantities together. Map how they
    relate.
    """)
    return


@app.cell(hide_code=True)
def _(ConceptMapWidget, mo):
    impulse_concept_map = mo.ui.anywidget(
        ConceptMapWidget(
            question="Map the relationships between these quantities:",
            concepts=["Net force (F)", "Time interval (Δt)", "Impulse (J)", "Change in momentum (Δp)"],
            terms=["× Δt →", "× F →", "is equal to"],
            correct_edges=[
                {"from": "Net force (F)", "to": "Impulse (J)", "label": "× Δt →"},
                {"from": "Time interval (Δt)", "to": "Impulse (J)", "label": "× F →"},
                {"from": "Impulse (J)", "to": "Change in momentum (Δp)", "label": "is equal to"},
            ],
        )
    )
    impulse_concept_map
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
    poe1_check = mo.ui.anywidget(
        PredictThenCheckWidget(
            question=(
                "Using the changing-force graph, set F₁ = 20 N, F₂ = 60 N "
                "and Δt = 2 s (impulse = 80 kg·m/s). If you double the time "
                "to Δt = 4 s, what happens to the impulse?"
            ),
            code="Δp = ½(F₁ + F₂) × Δt\n½(20 + 60) × 2 = 80 kg·m/s\n½(20 + 60) × 4 = ?",
            output="½(20 + 60) × 4 = 160 kg·m/s",
            options=[
                "It stays the same",
                "It doubles",
                "It halves",
                "It goes up, but not exactly double",
            ],
            correct_answer=1,
            explanations=[
                "Wrong: the impulse is an area, and doubling the width of that area does change it.",
                "Correct: the forces (height) are unchanged, so doubling Δt (width) doubles the area — from 80 to 160 kg·m/s.",
                "Wrong: halving would happen if Δt were halved, not doubled.",
                "Wrong: because the forces stay the same, the area scales exactly with Δt — it does double.",
            ],
        )
    )
    poe1_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Same area, different shape

    Compare two ways of delivering an impulse over the **same** 3.0 s:

    - **A:** a *constant* force of 40 N (a rectangle), and
    - **B:** a force ramping *linearly from 0 N up to 80 N* (a triangle).
    """)
    return


@app.cell(hide_code=True)
def _(PredictThenCheckWidget, mo):
    poe2_check = mo.ui.anywidget(
        PredictThenCheckWidget(
            question="Which delivers the larger impulse over 3.0 s: A (constant 40 N), B (ramp 0→80 N), or are they equal?",
            code="A (rectangle): 40 × 3.0 = ?\nB (triangle): ½ × 3.0 × 80 = ?",
            output="A: 120 kg·m/s   B: 120 kg·m/s",
            options=[
                "A (the constant 40 N force)",
                "B (the ramp up to 80 N)",
                "They are equal",
            ],
            correct_answer=2,
            explanations=[
                "Wrong: A's area (rectangle) works out to 40 × 3.0 = 120 kg·m/s, the same as B.",
                "Wrong: a bigger peak force (80 N) doesn't mean a bigger impulse — B spends most of the interval below 40 N.",
                "Correct: both areas equal 120 kg·m/s. What matters is the area under the graph, not the peak force.",
            ],
        )
    )
    poe2_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    **Next:** Part 3 uses impulse to explain why crumple zones, airbags and
    catching a ball "softly" reduce the **force** you feel, $F\Delta t = m\Delta v$.

    ------

    Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
    — free to use, adapt, and share for non-commercial purposes, with attribution.
    Developed with the assistance of Claude (Anthropic), referenced against the
    [VCE Physics Study Design](https://www.vcaa.vic.edu.au/curriculum/vce/vce-study-designs/physics) (VCAA).
    """)
    return


if __name__ == "__main__":
    app.run()
