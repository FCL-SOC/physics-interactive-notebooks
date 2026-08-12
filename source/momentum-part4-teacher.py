import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", layout_file="layouts/momentum-part4-teacher.slides.json")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import altair as alt

    return alt, mo


@app.cell(hide_code=True)
def _(alt):
    def bar_group(labels, values, colors, ylim, ylabel, title):
        # Plain Vega-Lite spec dict, not chained Altair calls — see
        # momentum-part1 for why (chained calls are much slower to rebuild
        # on every slider move). One bar chart with N labelled bars.
        _pts = [{"label": _l, "value": _v} for _l, _v in zip(labels, values)]
        return {
            "data": {"values": _pts},
            "layer": [
                {
                    "mark": {"type": "bar", "stroke": "black", "strokeWidth": 0.6},
                    "encoding": {
                        "x": {"field": "label", "type": "nominal", "title": None, "sort": None},
                        "y": {"field": "value", "type": "quantitative", "title": ylabel,
                              "scale": {"domain": [-ylim, ylim]}},
                        "color": {"field": "label", "type": "nominal",
                                  "scale": {"domain": labels, "range": colors}, "legend": None},
                    },
                },
                {
                    "data": {"values": [{"y": 0}]},
                    "mark": {"type": "rule", "color": "black", "strokeWidth": 0.8},
                    "encoding": {"y": {"field": "y", "type": "quantitative"}},
                },
            ],
            "width": 260,
            "height": 260,
            "title": title,
        }

    return (bar_group,)


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
    left) and a collision type. The bar charts show the velocities and momenta
    before and after.

    **Predict first:** compare the two "total momentum" bars (before and after).
    What do you expect to see?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    m1_slider = mo.ui.slider(start=1, stop=2000, step=10, value=1000, label="$m_1$ (kg)", debounce=True)
    u1_slider = mo.ui.slider(start=-20, stop=20, step=0.5, value=10, label="$u_1$ (m/s)", debounce=True)
    m2_slider = mo.ui.slider(start=1, stop=2000, step=10, value=1000, label="$m_2$ (kg)", debounce=True)
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
        _v_common = _p_before / (_m1 + _m2)
        _v1, _v2 = _v_common, _v_common
    else:
        _v1 = ((_m1 - _m2) / (_m1 + _m2)) * _u1 + (2 * _m2 / (_m1 + _m2)) * _u2
        _v2 = (2 * _m1 / (_m1 + _m2)) * _u1 + ((_m2 - _m1) / (_m1 + _m2)) * _u2

    _p_after = _m1 * _v1 + _m2 * _v2

    mo.md(
        f"""
        **Before:** $p = m_1u_1 + m_2u_2 = ({_m1})({_u1}) + ({_m2})({_u2}) = {_p_before:,.1f}$ kg m/s

        **After:** $v_1 = {_v1:,.2f}$ m/s, $v_2 = {_v2:,.2f}$ m/s
        &nbsp;&nbsp;→&nbsp;&nbsp; $p = {_p_after:,.1f}$ kg m/s

        Momentum is conserved.
        """
    )
    return


@app.cell(hide_code=True)
def _(alt, bar_group, collision_type, m1_slider, m2_slider, mo, u1_slider, u2_slider):
    _m1, _m2 = m1_slider.value, m2_slider.value
    _u1, _u2 = u1_slider.value, u2_slider.value
    _p_before = _m1 * _u1 + _m2 * _u2

    if collision_type.value.startswith("Perfectly"):
        _v_common = _p_before / (_m1 + _m2)
        _v1, _v2 = _v_common, _v_common
    else:
        _v1 = ((_m1 - _m2) / (_m1 + _m2)) * _u1 + (2 * _m2 / (_m1 + _m2)) * _u2
        _v2 = (2 * _m1 / (_m1 + _m2)) * _u1 + ((_m2 - _m1) / (_m1 + _m2)) * _u2

    _p1_before = _m1 * _u1
    _p2_before = _m2 * _u2
    _pt_before = _p1_before + _p2_before
    _p1_after = _m1 * _v1
    _p2_after = _m2 * _v2
    _pt_after = _p1_after + _p2_after

    _labels = ["object 1", "object 2"]
    _labels1 = ["object 1", "object 2", "total"]
    _colors = ["#1f77b4", "#d62728"]
    _colors1 = ["#1f77b4", "#d62728", "#ff7f0e"]
    _ylim_v = 22
    _ylim_p = 42000

    _panel_a = bar_group(_labels, [_u1, _u2], _colors, _ylim_v, "Velocity (m/s)", "Velocities Before")
    _panel_b = bar_group(_labels, [_v1, _v2], _colors, _ylim_v, "Velocity (m/s)", "Velocities After")
    _panel_c = bar_group(_labels1, [_p1_before, _p2_before, _pt_before], _colors1, _ylim_p, "Momentum (kg·m/s)", "Momentum Before")
    _panel_d = bar_group(_labels1, [_p1_after, _p2_after, _pt_after], _colors1, _ylim_p, "Momentum (kg·m/s)", "Momentum After")

    fig4 = alt.Chart.from_dict(
        {
            "vconcat": [
                {"hconcat": [_panel_a, _panel_b]},
                {"hconcat": [_panel_c, _panel_d]},
            ],
            # Without this, Vega-Lite tries to share one colour scale
            # across all 4 panels — since panel A only has 2 categories
            # (object 1/2) but panel C has 3 (+ total), the shared scale
            # silently mis-colours the "total" bar. Each panel needs its
            # own colour mapping.
            "resolve": {"scale": {"color": "independent"}},
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
    mo.md(r"""
    **2. A 900 kg car travelling at 8 m/s hits a stationary 1500 kg truck and
    they lock together. Use the simulator (set $m_1 = 900$, $u_1 = 8$, $m_2 =
    1500$, $u_2 = 0$, perfectly inelastic) to find the momentum before, then
    calculate their common velocity afterwards.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q1_answer = mo.ui.number(start=-20, stop=20, step=0.01, label="Your answer (m/s):")
    q1_answer
    return (q1_answer,)


@app.cell(hide_code=True)
def _(mo, q1_answer):
    _correct = (900 * 8 + 1500 * 0) / (900 + 1500)
    if q1_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q1_answer.value - _correct) < 0.05:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, momentum before is $900 \\times 8 = 7200$, then divide by the total mass.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $p_{before} = 900 \\times 8 + 1500 \\times 0 = 7200
                \\text{ kg m s}^{-1}$

                They lock together, so they share one velocity:

                $7200 = (900 + 1500)\\,v = 2400\\,v$

                $v = \\dfrac{7200}{2400} = 3 \\text{ m/s}$
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick practice

    **Q1. A 750 kg car travelling at 15.0 m/s rear-ends a stationary 900 kg car
    and the two lock together. Calculate their common velocity just after the
    collision.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q2_answer = mo.ui.number(start=0, stop=30, step=0.01, label="Your answer (m/s):")
    q2_answer
    return (q2_answer,)


@app.cell(hide_code=True)
def _(mo, q2_answer):
    _correct = 750 * 15.0 / (750 + 900)
    if q2_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q2_answer.value - _correct) < 0.05:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, momentum before is $750 \\times 15$, then divide by the total mass.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $p_{before} = 750 \\times 15.0 = 11\\,250 \\text{ kg m s}^{-1}$

                $11\\,250 = (750 + 900)\\,v = 1650\\,v$

                $v = \\dfrac{11\\,250}{1650} = 6.82 \\text{ m/s}$
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q2. Two ice skaters stand at rest, facing each other, then push off. Skater
    A (50.0 kg) moves right at 3.00 m/s. Calculate the speed of skater B (70.0
    kg), and explain why B must move the opposite way.**

    *Hint: the total momentum before they push off is zero.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q3_answer = mo.ui.number(start=0, stop=10, step=0.01, label="Skater B's speed (m/s):")
    q3_explain = mo.ui.text_area(
        placeholder="Explain why B moves the opposite way...", label="Explanation:", full_width=True
    )
    mo.vstack([q3_answer, q3_explain])
    return (q3_answer,)


@app.cell(hide_code=True)
def _(mo, q3_answer):
    _correct = 50.0 * 3.00 / 70.0
    if q3_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q3_answer.value - _correct) < 0.05:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, total momentum stays zero, so $50 \\times 3 = 70 \\times v_B$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                Before pushing off the total momentum is zero. It must stay zero,
                so the two momenta must cancel:

                $50.0 \\times 3.00 = 70.0 \\times v_B$

                $v_B = \\dfrac{150}{70.0} = 2.14 \\text{ m/s}$

                B must move in the **opposite** direction so that its (negative)
                momentum cancels A's (positive) momentum, keeping the total at
                zero.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    ## Additional activity: predict, observe, explain

    **Predict** first (before touching anything), then **observe** using the
    collision simulator further up the page, then **explain** what you saw.

    Set $m_1 = 1000$ kg, $u_1 = 10$ m/s, $m_2 = 1000$ kg, $u_2 = 0$. You are
    going to switch the collision type from **perfectly inelastic (stick
    together)** to **elastic (bounce apart)**.

    **Predict:** what will happen to the **total** momentum bar (before vs after)
    when you change the collision type?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    poe_predict = mo.ui.radio(
        options=[
            "The total momentum after changes",
            "The total momentum after stays the same",
            "The total momentum becomes zero",
        ],
        label="My prediction:",
    )
    poe_predict
    return


@app.cell(hide_code=True)
def _(mo):
    poe_explain = mo.ui.text_area(
        placeholder="Now switch between the two collision types. What happened to the individual bars, and to the total? Why?",
        label="Observe, then explain:",
        full_width=True,
    )
    poe_explain
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Reveal answer": mo.md(
                """
                **The total momentum after stays the same.** Changing the
                collision type changes how the momentum is *shared* between the
                two objects, the individual bars look completely different, but
                the **total** momentum bar is identical before and after in both
                cases. Momentum is conserved for any collision in an isolated
                system, whether the objects stick together or bounce apart. (What
                *does* differ between the two types is the kinetic energy, but
                that is a story for a later topic.)
                """
            )
        }
    )
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
