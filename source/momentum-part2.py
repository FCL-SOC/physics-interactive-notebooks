import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import altair as alt

    return alt, mo


@app.cell(hide_code=True)
def _(alt):
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

    return (area_chart,)


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
def _(alt, area_chart, force_slider, mo, time_slider):
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
    mo.md(r"""
    **2. A net force of 15 N acts on an object for 3 seconds. Calculate the
    change in momentum.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q1_answer = mo.ui.number(start=0, stop=200, step=0.1, label="Your answer (kg m/s):")
    q1_answer
    return (q1_answer,)


@app.cell(hide_code=True)
def _(mo, q1_answer):
    _correct = 15 * 3
    if q1_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q1_answer.value - _correct) < 0.5:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, $\\Delta p = F_{net}\\Delta t = 15 \\times 3$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $\\Delta p = F_{net}\\,\\Delta t$

                $F_{net} = 15, \\quad \\Delta t = 3$

                $\\Delta p = 15 \\times 3 = 45 \\text{ kg m s}^{-1}$
                """
            )
        }
    )
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
def _(alt, area_chart, dt_slider, f_end_slider, f_start_slider, mo):
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
    mo.md(r"""
    **Read the area.** A net force ramps up **linearly from 0 N to 50 N over
    3.0 s**. The area under this graph is a triangle. Calculate the impulse.

    *Hint: area of a triangle $= \tfrac{1}{2} \times \text{base} \times \text{height}$.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q_area_answer = mo.ui.number(start=0, stop=500, step=0.1, label="Your answer (kg m/s):")
    q_area_answer
    return (q_area_answer,)


@app.cell(hide_code=True)
def _(mo, q_area_answer):
    _correct = 0.5 * 3.0 * 50
    if q_area_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q_area_answer.value - _correct) < 0.5:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Not quite, the area of the triangle is $\\tfrac{1}{2} \\times 3.0 \\times 50$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                The graph is a triangle with base $\\Delta t = 3.0$ s and height
                $F = 50$ N.

                $\\Delta p = \\text{area} = \\tfrac{1}{2} \\times \\text{base}
                \\times \\text{height} = \\tfrac{1}{2} \\times 3.0 \\times 50
                = 75 \\text{ kg m s}^{-1}$
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick practice

    **Q1. A net force of 8.0 N acts on a box for 2.5 s. Calculate the impulse.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q2_answer = mo.ui.number(start=0, stop=200, step=0.1, label="Your answer (kg m/s):")
    q2_answer
    return (q2_answer,)


@app.cell(hide_code=True)
def _(mo, q2_answer):
    _correct = 8.0 * 2.5
    if q2_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q2_answer.value - _correct) < 0.2:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, $\\Delta p = 8.0 \\times 2.5$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q2. A 30 N force pushes a crate east while 12 N of friction acts west. The
    forces act for 4.0 s. Calculate the change in momentum.**

    *Hint: find the net force first.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q3_answer = mo.ui.number(start=0, stop=300, step=0.1, label="Your answer (kg m/s):")
    q3_answer
    return (q3_answer,)


@app.cell(hide_code=True)
def _(mo, q3_answer):
    _correct = (30 - 12) * 4.0
    if q3_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q3_answer.value - _correct) < 0.5:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Not quite, the net force is $30 - 12 = 18$ N.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $F_{net} = 30 - 12 = 18 \\text{ N}$

                $\\Delta p = F_{net}\\,\\Delta t = 18 \\times 4.0 = 72
                \\text{ kg m s}^{-1}$
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------

    ## Predict, observe, explain

    For each task: **predict** first (before touching anything), then **observe**
    using the sliders further up the page, then **explain** what you saw. Scroll
    back up to the graphs to test each prediction.

    ### Task 1 — doubling the time

    Using the **changing-force** graph, set $F_1 = 20$ N, $F_2 = 60$ N and
    $\Delta t = 2$ s. Now you are going to double the time to $\Delta t = 4$ s.

    **Predict:** what will happen to the impulse (the shaded area)?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    poe1_predict = mo.ui.radio(
        options=[
            "It stays the same",
            "It doubles",
            "It halves",
            "It goes up, but not exactly double",
        ],
        label="My prediction:",
    )
    poe1_predict
    return (poe1_predict,)


@app.cell(hide_code=True)
def _(mo):
    poe1_explain = mo.ui.text_area(
        placeholder="Now move the slider to Δt = 4 s. What happened, and why?",
        label="Observe, then explain:",
        full_width=True,
    )
    poe1_explain
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Reveal answer": mo.md(
                """
                **It doubles.** The impulse is the area
                $\\tfrac{1}{2}(F_1 + F_2)\\,\\Delta t$. The forces are unchanged,
                so the *height* of the shape is the same, but doubling
                $\\Delta t$ doubles the *width*, and therefore doubles the area.
                At $\\Delta t = 2$ s the impulse is
                $\\tfrac{1}{2}(20 + 60)(2) = 80$ kg m/s; at $\\Delta t = 4$ s it
                is $\\tfrac{1}{2}(20 + 60)(4) = 160$ kg m/s.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 2 — same area, different shape

    Compare two ways of delivering an impulse over the **same** 3.0 s:

    - **A:** a *constant* force of 40 N (a rectangle), and
    - **B:** a force ramping *linearly from 0 N up to 80 N* (a triangle).

    **Predict:** which delivers the larger impulse, A, B, or are they equal?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    poe2_predict = mo.ui.radio(
        options=[
            "A (the constant 40 N force)",
            "B (the ramp up to 80 N)",
            "They are equal",
        ],
        label="My prediction:",
    )
    poe2_predict
    return (poe2_predict,)


@app.cell(hide_code=True)
def _(mo):
    poe2_explain = mo.ui.text_area(
        placeholder="Use the two graphs to find each area, then explain what you found.",
        label="Observe, then explain:",
        full_width=True,
    )
    poe2_explain
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Reveal answer": mo.md(
                """
                **They are equal.** Both areas work out to 120 kg m/s:

                - A (rectangle): $\\text{area} = 40 \\times 3.0 = 120$ kg m/s
                - B (triangle): $\\text{area} = \\tfrac{1}{2} \\times 3.0
                  \\times 80 = 120$ kg m/s

                A bigger *peak* force does not automatically mean a bigger
                impulse, what matters is the **area** under the graph. Because
                B only reaches 80 N at the very end, it spends most of the time
                below 40 N, and the two areas end up the same.
                """
            )
        }
    )
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
