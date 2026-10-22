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
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import altair as alt
    from marimo_learn import (
        NumericEntryWidget,
        PredictThenCheckWidget,
        OrderingWidget,
        ConceptMapWidget,
    )

    return (
        ConceptMapWidget,
        NumericEntryWidget,
        OrderingWidget,
        PredictThenCheckWidget,
        alt,
        mo,
    )


@app.function(hide_code=True)
def before_after_bars(rows, items, colors, domain, ylabel, title, width=230):
    # Plain Vega-Lite spec dict, not chained Altair calls — see
    # momentum-part1 for why (chained calls are much slower to rebuild
    # on every slider move). Before and After sit side by side on ONE
    # shared y axis, with a bar per item inside each, so the eye can
    # compare totals directly. rows: [{"stage", "item", "value"}].
    _color = {"field": "item", "type": "nominal",
              "scale": {"domain": items, "range": colors},
              "legend": {"orient": "top", "title": None}}
    return {
        "data": {"values": rows},
        "layer": [
            {
                "mark": {"type": "bar", "stroke": "black", "strokeWidth": 0.6},
                "encoding": {
                    "x": {"field": "stage", "type": "nominal", "title": None,
                          "sort": ["Before", "After"], "axis": {"labelAngle": 0}},
                    "xOffset": {"field": "item", "sort": items},
                    "y": {"field": "value", "type": "quantitative", "title": ylabel,
                          "scale": {"domain": list(domain)}},
                    "color": _color,
                },
            },
            {
                "data": {"values": [{"y": 0}]},
                "mark": {"type": "rule", "color": "black", "strokeWidth": 0.8},
                "encoding": {"y": {"field": "y", "type": "quantitative"}},
            },
        ],
        "width": width,
        "height": 260,
        "title": title,
    }


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Momentum & Impulse, Part 4: Conservation of momentum

    *VCE Physics Unit 2, AOS1, Energy and motion*

    This is **Part 4 of 4**, the final part. It follows on from Part 3 (Impulse
    in collisions). In this part you will learn:

    - What an **isolated system** is
    - Why total momentum is conserved in a collision
    - How to use $m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2$

    *This part should take about 20 minutes.*

    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Total momentum is conserved

    In an **isolated system** (one with no external net force), the **total**
    momentum before a collision equals the total momentum after. We say momentum
    is **conserved**:

    $$m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2$$

    - $u$ = velocity **before** the collision (initial)
    - $v$ = velocity **after** the collision (final)
    - the subscripts $1$ and $2$ label the two objects

    This works for **every** type of collision, whether the objects bounce apart
    (elastic) or stick together (inelastic).

    Remember velocity has direction, so watch the **signs**: take one direction
    as positive and the opposite as negative.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Worked example

    **A 1000 kg car moving at 10 m/s rear-ends a stationary 1000 kg car, and the
    two lock together. Find their common velocity afterwards.**

    **Step 1** — Total momentum before.

    $p_{before} = m_1u_1 + m_2u_2 = 1000 \times 10 + 1000 \times 0 = 10\,000
    \text{ kg m s}^{-1}$

    **Step 2** — Momentum is conserved, so the total after is the same.

    $p_{after} = 10\,000 \text{ kg m s}^{-1}$

    **Step 3** — The cars lock together, so they share one velocity $v$.

    $10\,000 = m_1 v + m_2 v = (1000 + 1000)\,v = 2000\,v$

    **Step 4** — Solve.

    $v = \dfrac{10\,000}{2000} = 5 \text{ m/s}$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A common mistake (non-example)

    > *"Momentum is conserved, so each car keeps the same momentum it started
    > with."*

    This is **wrong**. Conservation applies to the **total** momentum of the
    system, not to each object on its own. Individual objects' momenta change all
    the time during a collision. It is only the sum, $p_1 + p_2$ before $= p_1' +
    p_2'$ after, that stays constant, and only because no external net force acts.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explore it: the collision simulator

    Choose each object's mass and initial velocity (positive = right, negative =
    left) and a collision type. The bar charts show the velocities, momenta
    and total kinetic energy before and after, on shared axes.

    **Predict first:** compare the two "total momentum" bars (before and after).
    What do you expect to see?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    m1_slider = mo.ui.slider(start=10, stop=2000, step=10, value=1000, label="$m_1$ (kg)", debounce=True)
    u1_slider = mo.ui.slider(start=-20, stop=20, step=0.5, value=10, label="$u_1$ (m/s)", debounce=True)
    m2_slider = mo.ui.slider(start=10, stop=2000, step=10, value=1000, label="$m_2$ (kg)", debounce=True)
    u2_slider = mo.ui.slider(start=-20, stop=20, step=0.5, value=0, label="$u_2$ (m/s)", debounce=True)
    collision_type = mo.ui.radio(
        options=["Perfectly inelastic (stick together)", "Elastic (bounce apart)"],
        value="Perfectly inelastic (stick together)",
        label="Collision type",
    )
    mo.vstack(
        [
            mo.hstack([m1_slider, u1_slider], justify="start", gap=2),
            mo.hstack([m2_slider, u2_slider], justify="start", gap=2),
            collision_type,
        ]
    )
    return collision_type, m1_slider, m2_slider, u1_slider, u2_slider


@app.cell(hide_code=True)
def _(collision_type, m1_slider, m2_slider, mo, u1_slider, u2_slider):
    _m1, _m2 = m1_slider.value, m2_slider.value
    _u1, _u2 = u1_slider.value, u2_slider.value
    _p_before = _m1 * _u1 + _m2 * _u2

    if collision_type.value.startswith("Perfectly"):
        v1_after = v2_after = _p_before / (_m1 + _m2)
    else:
        v1_after = ((_m1 - _m2) / (_m1 + _m2)) * _u1 + (2 * _m2 / (_m1 + _m2)) * _u2
        v2_after = (2 * _m1 / (_m1 + _m2)) * _u1 + ((_m2 - _m1) / (_m1 + _m2)) * _u2

    _p_after = _m1 * v1_after + _m2 * v2_after

    mo.md(
        f"""
        **Before:** $p = m_1u_1 + m_2u_2 = ({_m1})({_u1}) + ({_m2})({_u2}) = {_p_before:,.1f}$ kg m/s

        **After:** $v_1 = {v1_after:,.2f}$ m/s, $v_2 = {v2_after:,.2f}$ m/s
        &nbsp;&nbsp;→&nbsp;&nbsp; $p = {_p_after:,.1f}$ kg m/s

        Momentum is conserved.
        """
    )
    return v1_after, v2_after


@app.cell(hide_code=True)
def _(alt, m1_slider, m2_slider, mo, u1_slider, u2_slider, v1_after, v2_after):
    _m1, _m2 = m1_slider.value, m2_slider.value
    _u1, _u2 = u1_slider.value, u2_slider.value
    _v1, _v2 = v1_after, v2_after

    _vel = [
        {"stage": "Before", "item": "object 1", "value": _u1},
        {"stage": "Before", "item": "object 2", "value": _u2},
        {"stage": "After", "item": "object 1", "value": _v1},
        {"stage": "After", "item": "object 2", "value": _v2},
    ]
    _mom = []
    for _stage, _a, _b in [("Before", _m1 * _u1, _m2 * _u2), ("After", _m1 * _v1, _m2 * _v2)]:
        _mom += [
            {"stage": _stage, "item": "object 1", "value": _a},
            {"stage": _stage, "item": "object 2", "value": _b},
            {"stage": _stage, "item": "total", "value": _a + _b},
        ]
    _ke = [
        {"stage": "Before", "item": "total", "value": 0.5 * _m1 * _u1**2 + 0.5 * _m2 * _u2**2},
        {"stage": "After", "item": "total", "value": 0.5 * _m1 * _v1**2 + 0.5 * _m2 * _v2**2},
    ]

    # Axes sized to fit: elastic collisions reach ~40 m/s and 80 000 kg m/s
    # at the slider extremes.
    _ylim_v = max(22, *(abs(_r["value"]) for _r in _vel)) * 1.05
    _ylim_p = max(42000, *(abs(_r["value"]) for _r in _mom)) * 1.05
    _ylim_k = max(1000, *(_r["value"] for _r in _ke)) * 1.1

    _objects = ["object 1", "object 2"]
    _blue_red = ["#2171b5", "#cb181d"]
    fig4 = alt.Chart.from_dict(
        {
            "hconcat": [
                before_after_bars(_vel, _objects, _blue_red, (-_ylim_v, _ylim_v),
                                  "Velocity (m/s)", "Velocity"),
                before_after_bars(_mom, _objects + ["total"], _blue_red + ["#525252"],
                                  (-_ylim_p, _ylim_p), "Momentum (kg·m/s)", "Momentum"),
                before_after_bars(_ke, ["total"], ["#ff7f0e"], (0, _ylim_k),
                                  "Kinetic energy (J)", "Total kinetic energy", width=140),
            ],
            # Each panel has its own colour and bar-offset mapping (2, 3 and 1
            # categories); shared scales mis-colour and mis-order the bars.
            "resolve": {"scale": {"color": "independent", "xOffset": "independent"}},
        },
        validate=False,
    )
    mo.center(fig4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Checkpoint

    **1. Looking at the "total momentum" bars, what stays the same before and
    after the collision? What changes?**
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
                The **total** momentum bar is the same height before and after,
                momentum is conserved. The **individual** objects' momenta (and
                their velocities) change, but their sum does not.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **2.** Use the simulator (set $m_1 = 900$, $u_1 = 8$, $m_2 = 1500$, $u_2 = 0$, perfectly inelastic) to check your answer.
    """)
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q1_check = mo.ui.anywidget(
        NumericEntryWidget(
            question=(
                "A 900 kg car travelling at 8 m/s hits a stationary 1500 kg "
                "truck and they lock together. Calculate their common "
                "velocity afterwards, in m/s."
            ),
            correct_answer=(900 * 8 + 1500 * 0) / (900 + 1500),
            tolerance=0.05,
            explanation=(
                "p_before = 900 × 8 + 1500 × 0 = 7200 kg m s⁻¹. They lock "
                "together, so 7200 = (900 + 1500)v = 2400v, giving "
                "v = 7200 / 2400 = 3 m/s."
            ),
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
                "Q1. A 750 kg car travelling at 15.0 m/s rear-ends a "
                "stationary 900 kg car and the two lock together. Calculate "
                "their common velocity just after the collision, in m/s."
            ),
            correct_answer=750 * 15.0 / (750 + 900),
            tolerance=0.05,
            explanation=(
                "p_before = 750 × 15.0 = 11 250 kg m s⁻¹. "
                "11 250 = (750 + 900)v = 1650v, giving v = 11 250 / 1650 "
                "= 6.82 m/s."
            ),
        )
    )
    q2_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q2. Two ice skaters stand at rest, facing each other, then push off. Skater
    A (50.0 kg) moves right at 3.00 m/s.**

    *Hint: the total momentum before they push off is zero.*
    """)
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q3_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="Calculate the speed of skater B (70.0 kg), in m/s.",
            correct_answer=50.0 * 3.00 / 70.0,
            tolerance=0.05,
            explanation=(
                "Total momentum stays zero, so 50.0 × 3.00 = 70.0 × v_B, "
                "giving v_B = 150 / 70.0 = 2.14 m/s."
            ),
        )
    )
    q3_check
    return


@app.cell(hide_code=True)
def _(mo):
    q3_explain = mo.ui.text_area(
        placeholder="Explain why B moves the opposite way...", label="Explanation:", full_width=True
    )
    q3_explain
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                B must move in the **opposite** direction so that its
                (negative) momentum cancels A's (positive) momentum,
                keeping the total at zero.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Order it: solving a conservation-of-momentum problem
    """)
    return


@app.cell(hide_code=True)
def _(OrderingWidget, mo):
    order_check = mo.ui.anywidget(
        OrderingWidget(
            question="Arrange these steps for solving a conservation-of-momentum problem in order:",
            items=[
                "Identify the system and confirm no external horizontal forces act",
                "Write total momentum before = total momentum after",
                "Substitute known masses and velocities",
                "Solve for the unknown quantity",
                "Check the answer's sign/direction makes physical sense",
            ],
            shuffle=True,
        )
    )
    order_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    ## Predict, then check

    Try the collision simulator further up the page first if you like, then
    predict.
    """)
    return


@app.cell(hide_code=True)
def _(PredictThenCheckWidget, mo):
    poe_check = mo.ui.anywidget(
        PredictThenCheckWidget(
            question=(
                "Set m1 = 1000 kg, u1 = 10 m/s, m2 = 1000 kg, u2 = 0. If "
                "you switch the collision type from perfectly inelastic "
                "(stick together) to elastic (bounce apart), what happens "
                "to the total momentum bar (before vs after)?"
            ),
            code=(
                "Inelastic: p_after = (m1+m2) × v_common\n"
                "Elastic: p_after = m1×v1 + m2×v2\n"
                "Both cases: p_before = m1×u1 + m2×u2 = 10 000 kg·m/s"
            ),
            output="p_after = 10 000 kg·m/s in both cases",
            options=[
                "The total momentum after changes",
                "The total momentum after stays the same",
                "The total momentum becomes zero",
            ],
            correct_answer=1,
            explanations=[
                "Wrong: the collision type changes how momentum is shared between the two objects, not the total.",
                "Correct: momentum is conserved for any collision in an isolated system, whether objects stick together or bounce apart — only the individual bars differ, not the total.",
                "Wrong: the system isn't losing momentum — it's conserved, not destroyed.",
            ],
        )
    )
    poe_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concept map: the momentum & impulse series

    A capstone map linking the quantities from all four parts.
    """)
    return


@app.cell(hide_code=True)
def _(ConceptMapWidget, mo):
    series_concept_map = mo.ui.anywidget(
        ConceptMapWidget(
            question="Map the relationships between these quantities:",
            concepts=["Force (F)", "Mass (m)", "Velocity (v)", "Momentum (p)", "Impulse (J)"],
            terms=["causes a change in", "× v →", "× Δt →", "is equal to a change in"],
            correct_edges=[
                {"from": "Mass (m)", "to": "Momentum (p)", "label": "× v →"},
                {"from": "Force (F)", "to": "Momentum (p)", "label": "causes a change in"},
                {"from": "Force (F)", "to": "Impulse (J)", "label": "× Δt →"},
                {"from": "Impulse (J)", "to": "Momentum (p)", "label": "is equal to a change in"},
            ],
        )
    )
    series_concept_map
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    **Well done, that completes the four-part Momentum & Impulse series.** You
    can now calculate momentum, use impulse to find forces and changes in
    momentum, and apply conservation of momentum to collisions.

    ------

    Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
    — free to use, adapt, and share for non-commercial purposes, with attribution.
    Developed with the assistance of Claude (Anthropic), referenced against the
    [VCE Physics Study Design](https://www.vcaa.vic.edu.au/curriculum/vce/vce-study-designs/physics) (VCAA).
    """)
    return


if __name__ == "__main__":
    app.run()
