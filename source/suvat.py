import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


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
def _(a_slider1, np, plt, t_slider1, u_slider1):
    _t_range = np.linspace(0, 10, 200)
    _v_range = u_slider1.value + a_slider1.value * _t_range

    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.plot(_t_range, _v_range, color="tab:blue")
    ax1.axhline(0, color="black", linewidth=0.8)
    ax1.scatter(
        [t_slider1.value],
        [u_slider1.value + a_slider1.value * t_slider1.value],
        color="tab:red",
        zorder=5,
    )
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-50, 80)
    ax1.set_xlabel("time, t (s)")
    ax1.set_ylabel("velocity, v (m/s)")
    ax1.set_title("v-t graph, gradient = acceleration")
    fig1
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
    u_slider1 = mo.ui.slider(start=-20, stop=30, step=1, value=0, label="initial velocity, $u$ (m/s)")
    a_slider1 = mo.ui.slider(start=-10, stop=10, step=0.5, value=2, label="acceleration, $a$ (m/s²)")
    t_slider1 = mo.ui.slider(start=0, stop=10, step=0.5, value=5, label="time, $t$ (s)")
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
    mo.md(r"""
    2. **A rocket sled starts from rest and accelerates at 15 m/s² for 4 s. Calculate its final velocity.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q1_answer = mo.ui.number(start=0, stop=200, step=0.1, label="Your answer (m/s):")
    q1_answer
    return (q1_answer,)


@app.cell(hide_code=True)
def _(mo, q1_answer):
    _correct = 0 + 15 * 4
    if q1_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q1_answer.value - _correct) < 0.5:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, use $v = u + at$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $v = u + at$

                $u = 0$, $a = 15$, $t = 4$

                $v = 0 + 15 \\times 4 = 60$ m/s
                """
            )
        }
    )
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
def _(a_slider2, np, plt, t_slider2, u_slider2):
    _t_range = np.linspace(0, 10, 200)
    _v_range = u_slider2.value + a_slider2.value * _t_range
    _t_fill = np.linspace(0, t_slider2.value, 100)
    _v_fill = u_slider2.value + a_slider2.value * _t_fill

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.plot(_t_range, _v_range, color="tab:blue")
    ax2.fill_between(_t_fill, _v_fill, color="tab:blue", alpha=0.3, label="area = $s$")
    ax2.axhline(0, color="black", linewidth=0.8)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(-20, 60)
    ax2.set_xlabel("time, t (s)")
    ax2.set_ylabel("velocity, v (m/s)")
    ax2.set_title("Area under a v-t graph = displacement")
    ax2.legend()
    fig2
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
    u_slider2 = mo.ui.slider(start=0, stop=20, step=1, value=5, label="initial velocity, $u$ (m/s)")
    a_slider2 = mo.ui.slider(start=-5, stop=5, step=0.5, value=2, label="acceleration, $a$ (m/s²)")
    t_slider2 = mo.ui.slider(start=0, stop=10, step=0.5, value=3, label="time, $t$ (s)")
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
    mo.md(r"""
    2. **A skateboarder starts at 2 m/s and accelerates at 1.5 m/s² for 4 s. Calculate the distance travelled.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q2_answer = mo.ui.number(start=0, stop=200, step=0.1, label="Your answer (m):")
    q2_answer
    return (q2_answer,)


@app.cell(hide_code=True)
def _(mo, q2_answer):
    _correct = 2 * 4 + 0.5 * 1.5 * 4 ** 2
    if q2_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q2_answer.value - _correct) < 0.5:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, remember to square $t$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $s = ut + \\frac{1}{2}at^2$

                $u = 2$, $a = 1.5$, $t = 4$

                $s = (2)(4) + \\frac{1}{2}(1.5)(4)^2 = 8 + 12 = 20$ m
                """
            )
        }
    )
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
def _(a_slider3, np, plt, s_slider3, u_slider3):
    _s_range = np.linspace(0, 100, 200)
    _v2_range = u_slider3.value ** 2 + 2 * a_slider3.value * _s_range

    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ax3.plot(_s_range, _v2_range, color="tab:purple")
    ax3.axhline(0, color="black", linewidth=0.8)
    _v2_point = u_slider3.value ** 2 + 2 * a_slider3.value * s_slider3.value
    ax3.scatter([s_slider3.value], [_v2_point], color="tab:red", zorder=5)
    ax3.set_xlim(0, 100)
    ax3.set_ylim(-200, 1200)
    ax3.set_xlabel("displacement, s (m)")
    ax3.set_ylabel("velocity squared, $v^2$ (m$^2$/s$^2$)")
    ax3.set_title("$v^2$ vs $s$, gradient = $2a$")
    fig3
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
    u_slider3 = mo.ui.slider(start=0, stop=30, step=1, value=10, label="initial velocity, $u$ (m/s)")
    a_slider3 = mo.ui.slider(start=-10, stop=10, step=0.5, value=3, label="acceleration, $a$ (m/s²)")
    s_slider3 = mo.ui.slider(start=0, stop=100, step=1, value=40, label="displacement, $s$ (m)")
    mo.hstack([u_slider3, a_slider3, s_slider3], justify="start", gap=2)
    return a_slider3, s_slider3, u_slider3


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Checkpoint 3

    1. **Which variable does this equation let you avoid using?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Compare your answer": mo.md(
                """
                Time, $t$. This equation is derived by combining
                $v = u + at$ and $s = ut + \\frac{1}{2}at^2$ to eliminate $t$,
                so it's useful whenever time is unknown.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    2. **A train decelerates from 30 m/s at 2 m/s² over 100 m. Calculate its speed after travelling that distance.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q3_answer = mo.ui.number(start=0, stop=50, step=0.01, label="Your answer (m/s):")
    q3_answer
    return (q3_answer,)


@app.cell(hide_code=True)
def _(mo, q3_answer):
    _correct = (30 ** 2 + 2 * (-2) * 100) ** 0.5
    if q3_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q3_answer.value - _correct) < 0.1:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, remember the train is decelerating so $a$ is negative.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $v^2 = u^2 + 2as$

                $u = 30$, $a = -2$, $s = 100$

                $v^2 = (30)^2 + 2(-2)(100) = 900 - 400 = 500$

                $v = \\sqrt{500} = 22.36$ m/s
                """
            )
        }
    )
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
def _(mo, plt, t_slider4, u_slider4, v_slider4):
    _t = t_slider4.value
    _u = u_slider4.value
    _v = v_slider4.value
    _avg = (_u + _v) / 2

    fig4, (ax4a, ax4b) = plt.subplots(1, 2, figsize=(9, 3.5))

    ax4a.plot([0, _t], [_u, _v], color="tab:blue")
    ax4a.fill_between([0, _t], [_u, _v], color="tab:blue", alpha=0.3)
    ax4a.axhline(0, color="black", linewidth=0.8)
    ax4a.set_title("Actual v-t graph")
    ax4a.set_xlabel("time, t (s)")
    ax4a.set_ylabel("velocity (m/s)")

    ax4b.plot([0, _t], [_avg, _avg], color="tab:orange")
    ax4b.fill_between([0, _t], [_avg, _avg], color="tab:orange", alpha=0.3)
    ax4b.axhline(0, color="black", linewidth=0.8)
    ax4b.set_title("Equivalent average-velocity rectangle")
    ax4b.set_xlabel("time, t (s)")
    ax4b.set_ylabel("velocity (m/s)")

    _ylim = max(abs(_u), abs(_v), abs(_avg), 1) * 1.3
    ax4a.set_ylim(-_ylim, _ylim)
    ax4b.set_ylim(-_ylim, _ylim)
    fig4.tight_layout()
    fig4
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
    u_slider4 = mo.ui.slider(start=-20, stop=20, step=1, value=4, label="initial velocity, $u$ (m/s)")
    v_slider4 = mo.ui.slider(start=-20, stop=20, step=1, value=16, label="final velocity, $v$ (m/s)")
    t_slider4 = mo.ui.slider(start=0.5, stop=10, step=0.5, value=6, label="time, $t$ (s)")
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
    mo.md(r"""
    2. **A skier increases speed from 6 m/s to 14 m/s over 8 s. Calculate the distance travelled.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q4_answer = mo.ui.number(start=0, stop=300, step=0.1, label="Your answer (m):")
    q4_answer
    return (q4_answer,)


@app.cell(hide_code=True)
def _(mo, q4_answer):
    _correct = 0.5 * (6 + 14) * 8
    if q4_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q4_answer.value - _correct) < 0.5:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, use $s = \\frac{1}{2}(u+v)t$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $s = \\frac{1}{2}(u+v)t$

                $u = 6$, $v = 14$, $t = 8$

                $s = \\frac{1}{2}(6+14)(8) = \\frac{1}{2}(20)(8) = 80$ m
                """
            )
        }
    )
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
def _(a_slider5, np, plt, t_slider5, v_slider5):
    _t_end = t_slider5.value
    _u = v_slider5.value - a_slider5.value * _t_end
    _t_range = np.linspace(0, _t_end, 200)
    _v_range = _u + a_slider5.value * _t_range

    fig5, ax5 = plt.subplots(figsize=(6, 4))
    ax5.plot(_t_range, _v_range, color="tab:green")
    ax5.fill_between(_t_range, _v_range, color="tab:green", alpha=0.3, label="area = $s$")
    ax5.axhline(0, color="black", linewidth=0.8)
    ax5.scatter([_t_end], [v_slider5.value], color="tab:red", zorder=5)
    ax5.set_xlim(0, 10)
    ax5.set_ylim(-20, 60)
    ax5.set_xlabel("time, t (s)")
    ax5.set_ylabel("velocity, v (m/s)")
    ax5.set_title("v-t graph, ending at the chosen final velocity")
    ax5.legend()
    fig5
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
    v_slider5 = mo.ui.slider(start=0, stop=40, step=1, value=25, label="final velocity, $v$ (m/s)")
    a_slider5 = mo.ui.slider(start=-10, stop=10, step=0.5, value=-4, label="acceleration, $a$ (m/s²)")
    t_slider5 = mo.ui.slider(start=0.5, stop=10, step=0.5, value=3, label="time, $t$ (s)")
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
    mo.md(r"""
    2. **A skier's velocity is 18 m/s at the bottom of a slope, after decelerating at 1 m/s² for 6 s along a flat run-out. Calculate the distance travelled during that interval.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q5_answer = mo.ui.number(start=0, stop=300, step=0.1, label="Your answer (m):")
    q5_answer
    return (q5_answer,)


@app.cell(hide_code=True)
def _(mo, q5_answer):
    _correct = 18 * 6 - 0.5 * 1 * 6 ** 2
    if q5_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q5_answer.value - _correct) < 0.5:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, use $s = vt - \\frac{1}{2}at^2$ with $v = 18$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $s = vt - \\frac{1}{2}at^2$

                $v = 18$, $a = 1$, $t = 6$

                $s = (18)(6) - \\frac{1}{2}(1)(6)^2 = 108 - 18 = 90$ m
                """
            )
        }
    )
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
def _(mo):
    mo.md(r"""
    **Q1 ($v = u + at$).** A sprinter accelerates from rest at 4.5 m/s² for 2.2 s. Calculate her velocity at the end of this time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q6_answer = mo.ui.number(start=0, stop=50, step=0.01, label="Your answer (m/s):")
    q6_answer
    return (q6_answer,)


@app.cell(hide_code=True)
def _(mo, q6_answer):
    _correct = 0 + 4.5 * 2.2
    if q6_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q6_answer.value - _correct) < 0.1:
        _fb = mo.md(f"**Correct.** $v = u + at = 0 + 4.5 \\times 2.2 = {_correct:.2f}$ m/s.")
    else:
        _fb = mo.md(f"Not quite. (Correct answer: {_correct:.2f} m/s)")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q2 ($s = ut + \frac{1}{2}at^2$).** A shopping trolley rolling at 1.2 m/s accelerates down a ramp at 0.8 m/s² for 3 s. Calculate the distance it travels.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q7_answer = mo.ui.number(start=0, stop=50, step=0.01, label="Your answer (m):")
    q7_answer
    return (q7_answer,)


@app.cell(hide_code=True)
def _(mo, q7_answer):
    _correct = 1.2 * 3 + 0.5 * 0.8 * 3 ** 2
    if q7_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q7_answer.value - _correct) < 0.1:
        _fb = mo.md(
            f"**Correct.** $s = ut + \\frac{{1}}{{2}}at^2 = (1.2)(3) + \\frac{{1}}{{2}}(0.8)(3)^2 = {_correct:.2f}$ m."
        )
    else:
        _fb = mo.md(f"Not quite. (Correct answer: {_correct:.2f} m)")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q3 ($v^2 = u^2 + 2as$).** A plane must reach 70 m/s to take off. If it accelerates from rest at 2.5 m/s², calculate the minimum runway length required.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q8_answer = mo.ui.number(start=0, stop=5000, step=1, label="Your answer (m):")
    q8_answer
    return (q8_answer,)


@app.cell(hide_code=True)
def _(mo, q8_answer):
    _correct = (70 ** 2 - 0 ** 2) / (2 * 2.5)
    if q8_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q8_answer.value - _correct) < 5:
        _fb = mo.md(
            f"**Correct.** $v^2 = u^2 + 2as \\Rightarrow s = \\dfrac{{v^2 - u^2}}{{2a}} = "
            f"\\dfrac{{70^2 - 0^2}}{{2(2.5)}} = {_correct:,.0f}$ m."
        )
    else:
        _fb = mo.md(f"Not quite. (Correct answer: {_correct:,.0f} m)")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q4 ($s = \frac{1}{2}(u+v)t$).** A lift accelerates uniformly from 0 m/s to 3 m/s over 2.5 s. Calculate the distance it travels while accelerating.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q9_answer = mo.ui.number(start=0, stop=50, step=0.01, label="Your answer (m):")
    q9_answer
    return (q9_answer,)


@app.cell(hide_code=True)
def _(mo, q9_answer):
    _correct = 0.5 * (0 + 3) * 2.5
    if q9_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q9_answer.value - _correct) < 0.1:
        _fb = mo.md(
            f"**Correct.** $s = \\frac{{1}}{{2}}(u+v)t = \\frac{{1}}{{2}}(0+3)(2.5) = {_correct:.2f}$ m."
        )
    else:
        _fb = mo.md(f"Not quite. (Correct answer: {_correct:.2f} m)")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q5 ($s = vt - \frac{1}{2}at^2$).** A car's velocity is 12 m/s as it reaches a stop sign, having decelerated at 3 m/s² for 4 s beforehand. Calculate the distance travelled during that 4 s.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q10_answer = mo.ui.number(start=0, stop=200, step=0.01, label="Your answer (m):")
    q10_answer
    return (q10_answer,)


@app.cell(hide_code=True)
def _(mo, q10_answer):
    _correct = 12 * 4 - 0.5 * (-3) * 4 ** 2
    if q10_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q10_answer.value - _correct) < 0.5:
        _fb = mo.md(
            f"**Correct.** $s = vt - \\frac{{1}}{{2}}at^2 = (12)(4) - \\frac{{1}}{{2}}(-3)(4)^2 = {_correct:.2f}$ m."
        )
    else:
        _fb = mo.md(f"Not quite. (Correct answer: {_correct:.2f} m)")
    _fb
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
