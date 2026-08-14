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
    from marimo_learn import NumericEntryWidget, MatchingWidget, ConceptMapWidget

    return ConceptMapWidget, MatchingWidget, NumericEntryWidget, alt, mo, np


@app.function(hide_code=True)
def line_chart(
    x, y, color, xlim, ylim, xlabel, ylabel, title,
    fill=False, fill_label=None, fill_x=None, fill_y=None,
    scatter=None, scatter_color="#d62728",
    width=480, height=320,
):
    # Shared single-panel line-chart builder for all SUVAT graphs: a
    # plain Vega-Lite spec dict (not chained Altair calls, which are
    # much slower to rebuild on every slider move — see momentum-part1
    # for the measured comparison). Edit colours/labels/domains as
    # plain dict values below; each chart cell just calls this with
    # its own x/y data and options. fill_x/fill_y let the shaded area
    # cover a different (usually shorter) range than the line itself;
    # they default to the line's own x/y when not given.
    _pts = [{"x": float(_x), "y": float(_y)} for _x, _y in zip(x, y)]
    _x_enc = {"field": "x", "type": "quantitative", "title": xlabel,
               "scale": {"domain": list(xlim)}, "axis": {"grid": False}}
    _y_enc = {"field": "y", "type": "quantitative", "title": ylabel,
               "scale": {"domain": list(ylim)}, "axis": {"grid": False}}
    _layers = []
    if fill:
        _fill_x = x if fill_x is None else fill_x
        _fill_y = y if fill_y is None else fill_y
        _fill_pts = [{"x": float(_x), "y": float(_y)} for _x, _y in zip(_fill_x, _fill_y)]
        _layers.append({
            "data": {"values": _fill_pts},
            "mark": {"type": "area", "color": color, "opacity": 0.3},
            "encoding": {"x": _x_enc, "y": _y_enc},
        })
    _layers.append({
        "mark": {"type": "line", "color": color, "strokeWidth": 2},
        "encoding": {"x": _x_enc, "y": _y_enc},
    })
    _layers.append({
        "data": {"values": [{"y": 0}]},
        "mark": {"type": "rule", "color": "black", "strokeWidth": 0.8},
        "encoding": {"y": {"field": "y", "type": "quantitative"}},
    })
    if fill and fill_label:
        _mid = _fill_pts[len(_fill_pts) // 2]
        _layers.append({
            "data": {"values": [{"x": _mid["x"], "y": _mid["y"] / 2}]},
            "mark": {"type": "text", "fontWeight": "bold", "fontSize": 11},
            "encoding": {
                "x": {"field": "x", "type": "quantitative"},
                "y": {"field": "y", "type": "quantitative"},
                "text": {"value": fill_label},
            },
        })
    if scatter:
        _layers.append({
            "data": {"values": [{"x": scatter[0], "y": scatter[1]}]},
            "mark": {"type": "point", "color": scatter_color, "size": 70, "filled": True},
            "encoding": {
                "x": {"field": "x", "type": "quantitative"},
                "y": {"field": "y", "type": "quantitative"},
            },
        })
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
    ## Unit 2, AOS1, The SUVAT Equations

    *VCE Physics Unit 2, Area of Study 1, Motion*

    This notebook covers the five equations of motion for constant (uniform) acceleration in a straight line:

    - $v = u + at$
    - $s = ut + \frac{1}{2}at^2$
    - $v^2 = u^2 + 2as$
    - $s = \frac{1}{2}(u+v)t$
    - $s = vt - \frac{1}{2}at^2$

    where:

    - $s$ = displacement (m)
    - $u$ = initial velocity (m/s)
    - $v$ = final velocity (m/s)
    - $a$ = acceleration (m/s$^2$)
    - $t$ = time (s)

    **Every one of these equations only works when the acceleration is constant.** If the acceleration is changing (e.g. air resistance increasing with speed), none of them apply directly.

    *This workbook should take about 60-70 minutes to complete*

    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. $v = u + at$

    This equation tells you the final velocity of an object after accelerating at a constant rate $a$ for a time $t$, starting from an initial velocity $u$.

    It comes directly from the definition of acceleration, $a = \dfrac{v - u}{t}$, rearranged to make $v$ the subject.

    ### Example
    **A cyclist starts from rest and accelerates at 2 m/s² for 5 s. Find the cyclist's final velocity.**

    * *Identify known values:*

        $u = 0$, $a = 2$, $t = 5$

    * *Substitute into $v = u + at$:*

        $\rightarrow v = 0 + 2 \times 5$

        $\rightarrow v = 10$ m/s

    ### Common Errors

    "A car travelling at 20 m/s brakes, slowing down with a deceleration of 4 m/s² for 3 s. So $v = 20 + 4 \times 3 = 32$ m/s."

    This is wrong, a deceleration is a negative acceleration in the direction of travel. The correct substitution is $a = -4$, giving $v = 20 + (-4)(3) = 8$ m/s. Always assign a sign to $a$ based on whether the object speeds up or slows down relative to its direction of motion.

    ### View the Graph Below
    Adjust the initial velocity and acceleration below and see how the final velocity changes over time. The gradient of the line is the acceleration.
    """)
    return


@app.cell(hide_code=True)
def _(a_slider1, alt, mo, np, t_slider1, u_slider1):
    _t_range = np.linspace(0, 10, 200)
    _v_range = u_slider1.value + a_slider1.value * _t_range

    fig1 = alt.Chart.from_dict(
        line_chart(
            _t_range, _v_range, "#1f77b4",
            xlim=(0, 10), ylim=(-50, 80),
            xlabel="time, t (s)", ylabel="velocity, v (m/s)",
            title="v-t graph, gradient = acceleration",
            scatter=(t_slider1.value, u_slider1.value + a_slider1.value * t_slider1.value),
        ),
        validate=False,
    )
    mo.center(fig1)
    return


@app.cell(hide_code=True)
def _(a_slider1, mo, t_slider1, u_slider1):
    _v = u_slider1.value + a_slider1.value * t_slider1.value
    mo.md(
        f"$v = u + at = {u_slider1.value} + ({a_slider1.value})({t_slider1.value}) = {_v:,.1f}$ m/s"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    u_slider1 = mo.ui.slider(start=-20, stop=30, step=1, value=0, label="initial velocity, $u$ (m/s)", debounce=True)
    a_slider1 = mo.ui.slider(start=-10, stop=10, step=0.5, value=2, label="acceleration, $a$ (m/s²)", debounce=True)
    t_slider1 = mo.ui.slider(start=0, stop=10, step=0.5, value=5, label="time, $t$ (s)", debounce=True)
    mo.hstack([u_slider1, a_slider1, t_slider1], justify="start", gap=2)
    return a_slider1, t_slider1, u_slider1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Checkpoint 1

    1. **What does the gradient of a v-t graph represent?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                The gradient of a v-t graph is the rate of change of velocity with
                respect to time, which is the acceleration.
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
            question="A rocket sled starts from rest and accelerates at 15 m/s² for 4 s. Calculate its final velocity, in m/s.",
            correct_answer=0 + 15 * 4,
            tolerance=0.5,
            explanation="v = u + at = 0 + 15 × 4 = 60 m/s",
        )
    )
    q1_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ----------
    ## 2. $s = ut + \frac{1}{2}at^2$

    On a v-t graph, the displacement is the **area under the graph**. This equation gives that area directly for constant acceleration: the $ut$ term is the rectangle formed by the initial velocity, and the $\frac{1}{2}at^2$ term is the extra triangular area added by the acceleration.

    ### Example
    **A ball is launched along a ramp with an initial velocity of 5 m/s and accelerates at 2 m/s² for 3 s. Find the distance it travels.**

    * *Identify known values:*

        $u = 5$, $a = 2$, $t = 3$

    * *Substitute into $s = ut + \frac{1}{2}at^2$:*

        $\rightarrow s = (5)(3) + \frac{1}{2}(2)(3)^2$

        $\rightarrow s = 15 + 9$

        $\rightarrow s = 24$ m

    ### Common Errors

    "$s = ut + \frac{1}{2}at = (5)(3) + \frac{1}{2}(2)(3) = 15 + 3 = 18$ m."

    This is wrong, the time term in the second part of the equation is **squared** ($t^2$), not $t$. Forgetting to square $t$ under-counts the contribution of acceleration, which grows quadratically, not linearly, with time.

    ### View the Graph Below
    Adjust the initial velocity, acceleration, and time below. The shaded area under the v-t graph is the displacement, $s$.
    """)
    return


@app.cell(hide_code=True)
def _(a_slider2, alt, mo, np, t_slider2, u_slider2):
    _t_range = np.linspace(0, 10, 200)
    _v_range = u_slider2.value + a_slider2.value * _t_range
    _t_fill = np.linspace(0, t_slider2.value, 100)
    _v_fill = u_slider2.value + a_slider2.value * _t_fill

    fig2 = alt.Chart.from_dict(
        line_chart(
            _t_range, _v_range, "#1f77b4",
            xlim=(0, 10), ylim=(-20, 60),
            xlabel="time, t (s)", ylabel="velocity, v (m/s)",
            title="Area under a v-t graph = displacement",
            fill=True, fill_label="area = s", fill_x=_t_fill, fill_y=_v_fill,
        ),
        validate=False,
    )
    mo.center(fig2)
    return


@app.cell(hide_code=True)
def _(a_slider2, mo, t_slider2, u_slider2):
    _s = u_slider2.value * t_slider2.value + 0.5 * a_slider2.value * t_slider2.value ** 2
    mo.md(
        f"$s = ut + \\frac{{1}}{{2}}at^2 = ({u_slider2.value})({t_slider2.value}) + "
        f"\\frac{{1}}{{2}}({a_slider2.value})({t_slider2.value})^2 = {_s:,.1f}$ m"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    u_slider2 = mo.ui.slider(start=0, stop=20, step=1, value=5, label="initial velocity, $u$ (m/s)", debounce=True)
    a_slider2 = mo.ui.slider(start=-5, stop=5, step=0.5, value=2, label="acceleration, $a$ (m/s²)", debounce=True)
    t_slider2 = mo.ui.slider(start=0, stop=10, step=0.5, value=3, label="time, $t$ (s)", debounce=True)
    mo.hstack([u_slider2, a_slider2, t_slider2], justify="start", gap=2)
    return a_slider2, t_slider2, u_slider2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Checkpoint 2

    1. **What does the area under a v-t graph represent?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                The area under a v-t graph represents the displacement of the
                object over that time interval.
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
    q2_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="A skateboarder starts at 2 m/s and accelerates at 1.5 m/s² for 4 s. Calculate the distance travelled, in m.",
            correct_answer=2 * 4 + 0.5 * 1.5 * 4**2,
            tolerance=0.5,
            explanation="s = ut + ½at² = (2)(4) + ½(1.5)(4)² = 8 + 12 = 20 m",
        )
    )
    q2_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ----------
    ## 3. $v^2 = u^2 + 2as$

    This equation is useful whenever **time is not known or not needed**. It comes from combining the first two SUVAT equations to eliminate $t$.

    ### Example
    **A car accelerates from 10 m/s at 3 m/s² over a distance of 40 m. Find its final velocity.**

    * *Identify known values:*

        $u = 10$, $a = 3$, $s = 40$

    * *Substitute into $v^2 = u^2 + 2as$:*

        $\rightarrow v^2 = (10)^2 + 2(3)(40)$

        $\rightarrow v^2 = 100 + 240 = 340$

        $\rightarrow v = \sqrt{340} = 18.4$ m/s

    ### Common Errors

    "A train decelerating from 20 m/s at 5 m/s² travels 50 m, so $v^2 = 400 - 500 = -100$ m/s."

    This is wrong on two counts. First, you cannot leave the answer as $v^2$, take the square root to get $v$. Second, and more importantly, a negative result under the square root means the situation described is impossible, the train would have already stopped before reaching 50 m. Always check that your answer makes physical sense before (and after) taking the square root.

    ### View the Graph Below
    Adjust the initial velocity, acceleration, and distance below to see how $v^2$ changes with $s$. This relationship is a straight line, with gradient $2a$ and $v^2$-intercept $u^2$.
    """)
    return


@app.cell(hide_code=True)
def _(a_slider3, alt, mo, np, s_slider3, u_slider3):
    _s_range = np.linspace(0, 100, 200)
    _v2_range = u_slider3.value ** 2 + 2 * a_slider3.value * _s_range
    _v2_point = u_slider3.value ** 2 + 2 * a_slider3.value * s_slider3.value

    fig3 = alt.Chart.from_dict(
        line_chart(
            _s_range, _v2_range, "#9467bd",
            xlim=(0, 100), ylim=(-200, 1200),
            xlabel="displacement, s (m)", ylabel="velocity squared, v² (m²/s²)",
            title="v² vs s, gradient = 2a",
            scatter=(s_slider3.value, _v2_point),
        ),
        validate=False,
    )
    mo.center(fig3)
    return


@app.cell(hide_code=True)
def _(a_slider3, mo, s_slider3, u_slider3):
    _v2 = u_slider3.value ** 2 + 2 * a_slider3.value * s_slider3.value
    if _v2 < 0:
        _msg = "This is impossible, the object would have already stopped before reaching this distance."
    else:
        _msg = f"$v = \\sqrt{{{_v2:,.1f}}} = {_v2 ** 0.5:,.2f}$ m/s"
    mo.md(
        f"$v^2 = u^2 + 2as = ({u_slider3.value})^2 + 2({a_slider3.value})({s_slider3.value}) = {_v2:,.1f}$\n\n{_msg}"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    u_slider3 = mo.ui.slider(start=0, stop=30, step=1, value=10, label="initial velocity, $u$ (m/s)", debounce=True)
    a_slider3 = mo.ui.slider(start=-10, stop=10, step=0.5, value=3, label="acceleration, $a$ (m/s²)", debounce=True)
    s_slider3 = mo.ui.slider(start=0, stop=100, step=1, value=40, label="displacement, $s$ (m)", debounce=True)
    mo.hstack([u_slider3, a_slider3, s_slider3], justify="start", gap=2)
    return a_slider3, s_slider3, u_slider3


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Checkpoint 3

    1. **Match each equation to the variable it lets you avoid using.**
    """)
    return


@app.cell(hide_code=True)
def _(MatchingWidget, mo):
    equation_match = mo.ui.anywidget(
        MatchingWidget(
            question="Match each SUVAT equation to the variable it omits:",
            left=["v = u + at", "s = ut + ½at²", "v² = u² + 2as", "s = ½(u+v)t", "s = vt − ½at²"],
            right=["s", "v", "t", "a", "u"],
            correct_matches={0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
        )
    )
    equation_match
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **2.**
    """)
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q3_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="A train decelerates from 30 m/s at 2 m/s² over 100 m. Calculate its speed after travelling that distance, in m/s. (Remember: the train is decelerating, so a is negative.)",
            correct_answer=(30**2 + 2 * (-2) * 100) ** 0.5,
            tolerance=0.1,
            explanation="v² = u² + 2as = (30)² + 2(−2)(100) = 900 − 400 = 500, so v = √500 = 22.36 m/s",
        )
    )
    q3_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ----------
    ## 4. $s = \frac{1}{2}(u+v)t$

    Under constant acceleration, the average velocity is simply the mean of the initial and final velocities. Multiplying this average velocity by time gives the displacement.

    ### Example
    **A cyclist increases speed from 4 m/s to 16 m/s over 6 s. Find the distance travelled.**

    * *Identify known values:*

        $u = 4$, $v = 16$, $t = 6$

    * *Substitute into $s = \frac{1}{2}(u+v)t$:*

        $\rightarrow s = \frac{1}{2}(4 + 16)(6)$

        $\rightarrow s = \frac{1}{2}(20)(6)$

        $\rightarrow s = 60$ m

    ### Common Errors

    "A ball's velocity changes from +10 m/s to -10 m/s as it bounces back over 5 s, so the average velocity is $\frac{10 + (-10)}{2} = 0$, meaning it travelled 0 m."

    This isn't necessarily wrong, but it's a common source of confusion: this equation gives **displacement**, not distance travelled. An average velocity of zero means the object ends up back where it started (net displacement of zero), even though it may have travelled a large distance in each direction. Always be clear on whether a question asks for displacement or distance.

    ### View the Graph Below
    Adjust the initial velocity, final velocity, and time below. The shaded trapezoid area equals the shaded rectangle area, both represent the same displacement, $s$.
    """)
    return


@app.cell(hide_code=True)
def _(alt, mo, t_slider4, u_slider4, v_slider4):
    _t = t_slider4.value
    _u = u_slider4.value
    _v = v_slider4.value
    _avg = (_u + _v) / 2
    _ylim = max(abs(_u), abs(_v), abs(_avg), 1) * 1.3

    _panel_a = line_chart(
        [0, _t], [_u, _v], "#1f77b4",
        xlim=(0, max(_t, 0.1)), ylim=(-_ylim, _ylim),
        xlabel="time, t (s)", ylabel="velocity (m/s)",
        title="Actual v-t graph",
        fill=True, width=280, height=280,
    )
    _panel_b = line_chart(
        [0, _t], [_avg, _avg], "#ff7f0e",
        xlim=(0, max(_t, 0.1)), ylim=(-_ylim, _ylim),
        xlabel="time, t (s)", ylabel="velocity (m/s)",
        title="Equivalent average-velocity rectangle",
        fill=True, width=280, height=280,
    )
    fig4 = alt.Chart.from_dict({"hconcat": [_panel_a, _panel_b]}, validate=False)
    mo.center(fig4)
    return


@app.cell(hide_code=True)
def _(mo, t_slider4, u_slider4, v_slider4):
    _s = 0.5 * (u_slider4.value + v_slider4.value) * t_slider4.value
    mo.md(
        f"$s = \\frac{{1}}{{2}}(u+v)t = \\frac{{1}}{{2}}({u_slider4.value} + {v_slider4.value})({t_slider4.value}) = {_s:,.1f}$ m"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    u_slider4 = mo.ui.slider(start=-20, stop=20, step=1, value=4, label="initial velocity, $u$ (m/s)", debounce=True)
    v_slider4 = mo.ui.slider(start=-20, stop=20, step=1, value=16, label="final velocity, $v$ (m/s)", debounce=True)
    t_slider4 = mo.ui.slider(start=0.5, stop=10, step=0.5, value=6, label="time, $t$ (s)", debounce=True)
    mo.hstack([u_slider4, v_slider4, t_slider4], justify="start", gap=2)
    return t_slider4, u_slider4, v_slider4


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Checkpoint 4

    1. **Why does this equation only work if the acceleration is constant?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                Average velocity only equals the simple mean of the initial and
                final velocities when velocity changes at a constant rate
                (constant acceleration). If acceleration varies, the velocity-time
                graph is curved, not a straight line, so the true average velocity
                is no longer the midpoint of $u$ and $v$.
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
    q4_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="A skier increases speed from 6 m/s to 14 m/s over 8 s. Calculate the distance travelled, in m.",
            correct_answer=0.5 * (6 + 14) * 8,
            tolerance=0.5,
            explanation="s = ½(u+v)t = ½(6+14)(8) = ½(20)(8) = 80 m",
        )
    )
    q4_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ----------
    ## 5. $s = vt - \frac{1}{2}at^2$

    This equation gives displacement in terms of the **final** velocity $v$ instead of the initial velocity $u$. It's useful when the final velocity is known but the initial velocity isn't.

    ### Example
    **A car's velocity is 25 m/s at the end of a 3 s interval, during which it decelerated at 4 m/s². Find the displacement during that interval.**

    * *Identify known values:*

        $v = 25$, $a = -4$, $t = 3$

    * *Substitute into $s = vt - \frac{1}{2}at^2$:*

        $\rightarrow s = (25)(3) - \frac{1}{2}(-4)(3)^2$

        $\rightarrow s = 75 - (-18)$

        $\rightarrow s = 93$ m

    ### Common Errors

    "Using $s = vt - \frac{1}{2}at^2$ with $v = 25$ treated as the **initial** velocity."

    This is wrong, this equation specifically uses the **final** velocity $v$, not the initial velocity $u$. It looks structurally similar to $s = ut + \frac{1}{2}at^2$, but the sign in front of the acceleration term is negative and the velocity used is the one at the **end** of the interval. Mixing up $u$ and $v$ between these two equations is one of the most common SUVAT errors.

    ### View the Graph Below
    Adjust the final velocity, acceleration, and time below. The shaded area under the graph, ending at the chosen final velocity, is the displacement, $s$.
    """)
    return


@app.cell(hide_code=True)
def _(a_slider5, alt, mo, np, t_slider5, v_slider5):
    _t_end = t_slider5.value
    _u = v_slider5.value - a_slider5.value * _t_end
    _t_range = np.linspace(0, _t_end, 200)
    _v_range = _u + a_slider5.value * _t_range

    fig5 = alt.Chart.from_dict(
        line_chart(
            _t_range, _v_range, "#2ca02c",
            xlim=(0, 10), ylim=(-20, 60),
            xlabel="time, t (s)", ylabel="velocity, v (m/s)",
            title="v-t graph, ending at the chosen final velocity",
            fill=True, fill_label="area = s",
            scatter=(_t_end, v_slider5.value),
        ),
        validate=False,
    )
    mo.center(fig5)
    return


@app.cell(hide_code=True)
def _(a_slider5, mo, t_slider5, v_slider5):
    _s = v_slider5.value * t_slider5.value - 0.5 * a_slider5.value * t_slider5.value ** 2
    mo.md(
        f"$s = vt - \\frac{{1}}{{2}}at^2 = ({v_slider5.value})({t_slider5.value}) - "
        f"\\frac{{1}}{{2}}({a_slider5.value})({t_slider5.value})^2 = {_s:,.1f}$ m"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    v_slider5 = mo.ui.slider(start=0, stop=40, step=1, value=25, label="final velocity, $v$ (m/s)", debounce=True)
    a_slider5 = mo.ui.slider(start=-10, stop=10, step=0.5, value=-4, label="acceleration, $a$ (m/s²)", debounce=True)
    t_slider5 = mo.ui.slider(start=0.5, stop=10, step=0.5, value=3, label="time, $t$ (s)", debounce=True)
    mo.hstack([v_slider5, a_slider5, t_slider5], justify="start", gap=2)
    return a_slider5, t_slider5, v_slider5


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Checkpoint 5

    1. **How does this equation differ from $s = ut + \frac{1}{2}at^2$?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                It uses the final velocity $v$ instead of the initial velocity
                $u$, and the acceleration term is subtracted rather than added.
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
    q5_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="A skier's velocity is 18 m/s at the bottom of a slope, after decelerating at 1 m/s² for 6 s along a flat run-out. Calculate the distance travelled during that interval, in m.",
            correct_answer=18 * 6 - 0.5 * 1 * 6**2,
            tolerance=0.5,
            explanation="s = vt − ½at² = (18)(6) − ½(1)(6)² = 108 − 18 = 90 m",
        )
    )
    q5_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ----------
    ## Concept map: velocity, acceleration, and displacement

    On a v-t graph, both of the "extra" quantities in the SUVAT equations
    come straight from velocity. Map how.
    """)
    return


@app.cell(hide_code=True)
def _(ConceptMapWidget, mo):
    suvat_concept_map = mo.ui.anywidget(
        ConceptMapWidget(
            question="Map the relationships between these quantities:",
            concepts=["Velocity (v)", "Acceleration (a)", "Displacement (s)"],
            terms=["rate of change →", "area under graph →"],
            correct_edges=[
                {"from": "Velocity (v)", "to": "Acceleration (a)", "label": "rate of change →"},
                {"from": "Velocity (v)", "to": "Displacement (s)", "label": "area under graph →"},
            ],
        )
    )
    suvat_concept_map
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ----------
    ## 6. Practice set

    A set of questions covering all five SUVAT equations. Work through them in order, numeric answers are checked automatically.
    """)
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q6_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="Q1 (v = u + at). A sprinter accelerates from rest at 4.5 m/s² for 2.2 s. Calculate her velocity at the end of this time, in m/s.",
            correct_answer=0 + 4.5 * 2.2,
            tolerance=0.1,
            explanation="v = u + at = 0 + 4.5 × 2.2 = 9.90 m/s",
        )
    )
    q6_check
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q7_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="Q2 (s = ut + ½at²). A shopping trolley rolling at 1.2 m/s accelerates down a ramp at 0.8 m/s² for 3 s. Calculate the distance it travels, in m.",
            correct_answer=1.2 * 3 + 0.5 * 0.8 * 3**2,
            tolerance=0.1,
            explanation="s = ut + ½at² = (1.2)(3) + ½(0.8)(3)² = 3.60 + 3.60 = 7.20 m",
        )
    )
    q7_check
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q8_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="Q3 (v² = u² + 2as). A plane must reach 70 m/s to take off. If it accelerates from rest at 2.5 m/s², calculate the minimum runway length required, in m.",
            correct_answer=(70**2 - 0**2) / (2 * 2.5),
            tolerance=5,
            explanation="v² = u² + 2as ⟹ s = (v² − u²)/(2a) = (70² − 0²)/(2×2.5) = 980 m",
        )
    )
    q8_check
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q9_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="Q4 (s = ½(u+v)t). A lift accelerates uniformly from 0 m/s to 3 m/s over 2.5 s. Calculate the distance it travels while accelerating, in m.",
            correct_answer=0.5 * (0 + 3) * 2.5,
            tolerance=0.1,
            explanation="s = ½(u+v)t = ½(0+3)(2.5) = 3.75 m",
        )
    )
    q9_check
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    q10_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="Q5 (s = vt − ½at²). A car's velocity is 12 m/s as it reaches a stop sign, having decelerated at 3 m/s² for 4 s beforehand. Calculate the distance travelled during that 4 s, in m.",
            correct_answer=12 * 4 - 0.5 * (-3) * 4**2,
            tolerance=0.5,
            explanation="s = vt − ½at² = (12)(4) − ½(−3)(4)² = 48 + 24 = 72 m",
        )
    )
    q10_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q6 (explain, no auto-marking).** A ball is thrown straight up. At its highest point, its velocity is momentarily zero. Explain why its acceleration is not also zero at that instant.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q11_explain = mo.ui.text_area(placeholder="Type your explanation here...", label="Your explanation:", full_width=True)
    q11_explain
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                Velocity and acceleration are independent quantities, velocity
                being momentarily zero doesn't mean it's staying zero. Gravity
                acts on the ball continuously, at a constant $9.8$ m/s²
                downward, regardless of the ball's instantaneous velocity. At the
                highest point the ball is still accelerating downward, which is
                exactly why it doesn't stay at that height, it immediately
                begins to fall.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reflection

    In your own words, explain why all five SUVAT equations only apply when the acceleration is constant.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    reflection = mo.ui.text_area(
        placeholder="Type your explanation here...", label="Your explanation:", full_width=True
    )
    reflection
    return (reflection,)


@app.cell(hide_code=True)
def _(mo, reflection):
    mo.md("*(No auto-marking for this one, show your teacher or discuss with a partner.)*") if reflection.value else mo.md("")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                Each SUVAT equation is derived assuming a constant, unchanging
                acceleration, e.g. $v = u + at$ assumes $a$ is the same value
                for the whole time interval $t$. If acceleration varies (for
                example, a car's engine force changing, or air resistance
                growing with speed), the v-t graph is no longer a straight
                line, so the simple relationships between $u$, $v$, $a$, $s$,
                and $t$ used to derive these equations no longer hold. In
                those cases, calculus (or numerical methods) is needed instead.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    *Licensed under CC BY-NC-SA 4.0, free to use, adapt, and share for
    non-commercial purposes, with attribution; no warranty or liability
    accepted. Developed with the assistance of Claude (Anthropic),
    referenced against the VCE Physics Study Design (VCAA).*
    """)
    return


if __name__ == "__main__":
    app.run()
