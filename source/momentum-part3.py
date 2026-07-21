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

    **Predict first:** if you make the collision take twice as long, roughly what
    happens to the force?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    dummy_mass = mo.ui.slider(start=30, stop=120, step=1, value=60, label="mass (kg)")
    dummy_dv = mo.ui.slider(start=1, stop=30, step=1, value=20, label="$\\Delta v$ (m/s)")
    collision_time = mo.ui.slider(
        start=0.02, stop=1.0, step=0.02, value=0.1, label="collision time, $\\Delta t$ (s)"
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
def _(collision_time, dummy_dv, dummy_mass, np, plt):
    _t_range = np.linspace(0.02, 1.0, 200)
    _F_range = dummy_mass.value * dummy_dv.value / _t_range

    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ax3.plot(_t_range, _F_range, color="tab:green")
    ax3.set_xlabel("collision time, $\\Delta t$ (s)")
    ax3.set_ylim(0, 175000)
    ax3.set_ylabel("force experienced, F (N)")
    ax3.set_title("Longer collision time → smaller force, for fixed $m\\Delta v$")
    ax3.scatter(
        [collision_time.value],
        [dummy_mass.value * dummy_dv.value / collision_time.value],
        color="tab:red",
        zorder=5,
    )
    fig3
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
    mo.md(r"""
    **2. A 0.15 kg cricket ball travelling at 25 m/s is caught and brought to
    rest in 0.2 s. Calculate the average force on the ball.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q1_answer = mo.ui.number(start=0, stop=100, step=0.1, label="Your answer (N):")
    q1_answer
    return (q1_answer,)


@app.cell(hide_code=True)
def _(mo, q1_answer):
    _correct = 0.15 * 25 / 0.2
    if q1_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q1_answer.value - _correct) < 1:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, $F = \\dfrac{m\\Delta v}{\\Delta t} = \\dfrac{0.15 \\times 25}{0.2}$.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $F = \\dfrac{m\\,\\Delta v}{\\Delta t}$

                $m = 0.15, \\quad \\Delta v = 25, \\quad \\Delta t = 0.2$

                $F = \\dfrac{0.15 \\times 25}{0.2} = 18.75 \\text{ N}$
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick practice

    **Q1. A golf club strikes a stationary 0.046 kg golf ball. The contact time
    is 0.00050 s and the ball leaves at 65.0 m/s. Calculate the average force on
    the ball.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q2_answer = mo.ui.number(start=0, stop=20000, step=1, label="Your answer (N):")
    q2_answer
    return (q2_answer,)


@app.cell(hide_code=True)
def _(mo, q2_answer):
    _correct = 0.046 * 65.0 / 0.00050
    if q2_answer.value is None:
        _fb = mo.md("*Enter a value above.*")
    elif abs(q2_answer.value - _correct) < 100:
        _fb = mo.md("**Correct.**")
    else:
        _fb = mo.md("Try again, find $m\\Delta v = 0.046 \\times 65$, then divide by 0.00050.")
    _fb
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
                $m\\Delta v = 0.046 \\times 65.0 = 2.99 \\text{ kg m s}^{-1}$

                $F = \\dfrac{m\\Delta v}{\\Delta t} = \\dfrac{2.99}{0.00050}
                = 5980 \\text{ N}$
                """
            )
        }
    )
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

    ## Additional activity: predict, observe, explain

    **Predict** first (before touching anything), then **observe** using the
    mass, $\Delta v$ and collision-time sliders further up the page, then
    **explain** what you saw.

    Leave the mass and $\Delta v$ as they are. Set the **collision time to
    $\Delta t = 0.2$ s** and note the force. Now you are going to **double the
    collision time to $\Delta t = 0.4$ s**.

    **Predict:** what will happen to the force experienced?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    poe_predict = mo.ui.radio(
        options=[
            "It stays the same",
            "It doubles",
            "It halves",
            "It goes down, but not exactly half",
        ],
        label="My prediction:",
    )
    poe_predict
    return


@app.cell(hide_code=True)
def _(mo):
    poe_explain = mo.ui.text_area(
        placeholder="Now drag the collision-time slider from 0.2 s to 0.4 s. What happened to the force, and why?",
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
                **It halves.** The force is $F = m\\Delta v / \\Delta t$. The
                mass and $\\Delta v$ are unchanged, so the impulse on top stays
                the same. Doubling the time on the bottom halves the force, force
                and collision time are *inversely proportional*. This is exactly
                why a longer, softer collision (airbag, crumple zone, bent knees)
                protects you: same impulse, spread over more time, means less
                force.
                """
            )
        }
    )
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
