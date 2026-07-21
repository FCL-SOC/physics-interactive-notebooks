import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, plt


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
        start=1, stop=30, step=1, value=20, label="Ball 1 mass, $m$ (kg)"
    )
    velocity_slider1 = mo.ui.slider(
        start=-20, stop=20, step=1, value=-5, label="Ball 1 velocity, $v$ (m/s)"
    )
    mass_slider2 = mo.ui.slider(
        start=1, stop=20, step=1, value=10, label="Ball 2 mass, $m$ (kg)"
    )
    velocity_slider2 = mo.ui.slider(
        start=-38, stop=38, step=1, value=10, label="Ball 2 velocity, $v$ (m/s)"
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
def _(mass_slider1, mass_slider2, plt, velocity_slider1, velocity_slider2):
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

    def _panel(ax, label, value, color, ylim, unit):
        ax.bar([label], [value], color=color, edgecolor="black", linewidth=0.6)
        ax.axhline(0, color="black", linewidth=0.8)
        ax.set_ylabel(f"{label} ({unit})")
        ax.set_ylim(-ylim, ylim)
        ax.grid(which="major", alpha=0.5, axis="y")
        ax.grid(which="minor", alpha=0.3, axis="y")
        ax.minorticks_on()
        # Value label on the bar so meaning does not rely on colour alone.
        _va = "bottom" if value >= 0 else "top"
        _off = 0.03 * ylim if value >= 0 else -0.03 * ylim
        ax.annotate(
            f"{value:,.0f}",
            xy=(0, value),
            xytext=(0, value + _off),
            ha="center",
            va=_va,
            fontweight="bold",
            fontsize=11,
        )

    fig1, ([ax1a, ax1b, ax1c], [ax1d, ax1e, ax1f]) = plt.subplots(
        2, 3, figsize=(9, 6)
    )

    # Ball 1 (top row) — shades of red
    _panel(ax1a, "Mass", _m1, _reds[0], 33, "kg")
    _panel(ax1b, "Velocity", _v1, _reds[1], 40, "m/s")
    _panel(ax1c, "Momentum", _p1, _reds[2], 800, "kg m/s")
    ax1a.set_ylabel("Mass (kg)")

    # Ball 2 (bottom row) — shades of blue
    _panel(ax1d, "Mass", _m2, _blues[0], 33, "kg")
    _panel(ax1e, "Velocity", _v2, _blues[1], 40, "m/s")
    _panel(ax1f, "Momentum", _p2, _blues[2], 800, "kg m/s")
    ax1d.set_ylabel("Mass (kg)")

    ax1b.set_title("Ball 1", fontsize=13, fontweight="bold", color="#cb181d")
    ax1e.set_title("Ball 2", fontsize=13, fontweight="bold", color="#2171b5")

    fig1.tight_layout()
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
    mo.md(r"""
    **2. A 0.058 kg tennis ball is served at 50 m/s. Calculate its momentum.**

    *Hint: use $p = mv$.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q1_answer = mo.ui.number(start=0, stop=100, step=0.01, label="Your answer (kg m/s):")
    q1_answer
    return (q1_answer,)


@app.cell(hide_code=True)
def _(mo, q1_answer):
    _correct = 0.058 * 50
    if q1_answer.value == 0:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q1_answer.value - _correct) < 0.05:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Not quite, use $p = mv$ with $m = 0.058$ and $v = 50$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $p = mv$

                $m = 0.058, \\quad v = 50$

                $p = 0.058 \\times 50 = 2.9 \\text{ kg m s}^{-1}$
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick practice

    **Q1. Calculate the momentum of a 5.20 kg cat running north at 4.50 m/s.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q2_answer = mo.ui.number(start=0, stop=100, step=0.01, label="Your answer (kg m/s):")
    q2_answer
    return (q2_answer,)


@app.cell(hide_code=True)
def _(mo, q2_answer):
    _correct = 5.20 * 4.50
    if q2_answer.value == 0:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q2_answer.value - _correct) < 0.1:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, $p = 5.20 \\times 4.50$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q2. A 9 kg bowling ball moves at +12 m/s. A 5 kg bowling ball has the
    *same* momentum. What is the velocity of the 5 kg ball?**

    *Hint: first find the momentum of the 9 kg ball, then use it to find the
    velocity of the 5 kg ball.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q3_answer = mo.ui.number(start=0, stop=50, step=0.01, label="Your answer (m/s):")
    q3_answer
    return (q3_answer,)


@app.cell(hide_code=True)
def _(mo, q3_answer):
    _correct = 9 * 12 / 5
    if q3_answer.value == 0:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q3_answer.value - _correct) < 0.05:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Not quite, find $p = 9 \\times 12$ first, then divide by 5.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                Momentum of the 9 kg ball: $p = 9 \\times 12 = 108
                \\text{ kg m s}^{-1}$.

                The 5 kg ball has the same momentum, so:

                $108 = 5 \\times v$

                $v = 108 \\div 5 = 21.6 \\text{ m/s}$
                """
            )
        }
    )
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
