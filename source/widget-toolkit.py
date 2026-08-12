# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "altair",
#     "numpy",
#     "pandas",
#     "matplotlib",
#     "wigglystuff==0.5.25",
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
    import pandas as pd
    import altair as alt
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from wigglystuff import TangleSlider, Slider2D, Matrix, HoverZoom, TextCompare
    from marimo_learn import (
        MultipleChoiceWidget,
        NumericEntryWidget,
        PredictThenCheckWidget,
        OrderingWidget,
        MatchingWidget,
        LabelingWidget,
        ConceptMapWidget,
        FlashcardWidget,
        World,
        Color,
    )

    return (
        Color,
        ConceptMapWidget,
        FlashcardWidget,
        HoverZoom,
        LabelingWidget,
        Matrix,
        MatchingWidget,
        MultipleChoiceWidget,
        NumericEntryWidget,
        OrderingWidget,
        PredictThenCheckWidget,
        Slider2D,
        TangleSlider,
        TextCompare,
        World,
        alt,
        mo,
        np,
        pd,
        plt,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Widget toolkit — reference notebook

    This is **not a lesson** — it's a working reference of every interactive
    widget available for building physics notebooks in this repo, beyond the
    plain `mo.ui.slider` / `mo.ui.radio` / `mo.ui.number` used so far. Each
    section below is a minimal, physics-flavoured example plus a short note on
    when it's actually worth reaching for.

    They come from two packages, both pip-installable
    (`pip install wigglystuff marimo-learn`):

    - **[wigglystuff](https://koaning.github.io/wigglystuff/)** — small
      general-purpose interactive widgets (sliders, 2D pickers, image
      overlays).
    - **[marimo-learn](https://pypi.org/project/marimo-learn/)** — formative
      assessment widgets (multiple choice, matching, ordering, etc.) plus a
      turtle-graphics toy.

    All of them are used via `mo.ui.anywidget(...)`, same as any other marimo
    UI element — read `.value` (or a widget-specific attribute, noted per
    section) in a *different* cell than the one that defines it, same rule as
    every other UI element in this repo.

    **To copy a widget into a real notebook:** find its section below, copy
    the cell(s), swap the physics example for your own numbers/question, and
    delete the "why" note. The summary table at the end also says which
    existing hand-rolled pattern (e.g. the `mo.ui.number` + manual tolerance
    check used for "Quick practice" cells) each widget can replace.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Inline draggable numbers — `TangleSlider`

    A number that drags directly **inside a sentence**, instead of sitting in
    a slider block above/below the text. Best used to replace `mo.ui.slider`
    wherever a value is quoted in prose — it keeps the reading flow and the
    interactivity in the same place.

    **Why reach for this:** every existing notebook currently separates
    "here's a sentence with a number in it" from "here's a slider that
    changes that number" into two cells. TangleSlider merges them.
    """)
    return


@app.cell(hide_code=True)
def _(TangleSlider, mo):
    mass_tangle = mo.ui.anywidget(
        TangleSlider(amount=1200, min_value=200, max_value=3000, step=50, digits=0)
    )
    velocity_tangle = mo.ui.anywidget(
        TangleSlider(amount=15, min_value=0, max_value=40, step=1, digits=0)
    )
    return mass_tangle, velocity_tangle


@app.cell(hide_code=True)
def _(mass_tangle, mo, velocity_tangle):
    _p = mass_tangle.amount * velocity_tangle.amount
    mo.md(f"""
    A car of mass {mass_tangle} kg travelling at {velocity_tangle} m/s has
    momentum $p = mv = {_p:,.0f}\\ \\text{{kg m s}}^{{-1}}$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    mass_tangle = mo.ui.anywidget(
        TangleSlider(amount=1200, min_value=200, max_value=3000, step=50, digits=0)
    )
    # in a later cell:
    mo.md(f"A car of mass {mass_tangle} kg ...")   # renders as an inline draggable number
    mass_tangle.amount                              # the current numeric value
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. 2D point picker — `Slider2D`

    Drag a single point around a bounded 2D region. Reaches further than a
    pair of ordinary sliders because the drag itself is spatial — it's the
    natural fit for anything that *is* a 2D vector: resultant force, launch
    velocity (speed at an angle), displacement.

    **Why reach for this:** the planned "Forces and motion" and "Application
    of motion" (projectile motion) topics are still ⬜ in
    `NOTEBOOK-PROGRESS.md` — this is the widget to build them with, instead of
    two separate x/y sliders.
    """)
    return


@app.cell(hide_code=True)
def _(Slider2D, mo):
    force_2d = mo.ui.anywidget(
        Slider2D(width=320, height=320, x_bounds=(-20.0, 20.0), y_bounds=(-20.0, 20.0))
    )
    force_2d
    return (force_2d,)


@app.cell(hide_code=True)
def _(force_2d, mo, np):
    _fx, _fy = force_2d.x, force_2d.y
    _mag = np.hypot(_fx, _fy)
    _angle = np.degrees(np.arctan2(_fy, _fx))
    mo.callout(
        f"Resultant force: {_mag:.1f} N at {_angle:.0f}° "
        f"(components: Fx = {_fx:.1f} N, Fy = {_fy:.1f} N)"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    force_2d = mo.ui.anywidget(
        Slider2D(width=320, height=320, x_bounds=(-20.0, 20.0), y_bounds=(-20.0, 20.0))
    )
    # in a later cell:
    force_2d.x, force_2d.y   # the picked point's coordinates
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Numeric answer with built-in tolerance — `NumericEntryWidget`

    Direct replacement for the "Quick practice" pattern used throughout the
    momentum/SUVAT notebooks (`mo.ui.number` + a hand-written
    `abs(x - correct) < tol` check in a second cell). This widget bundles the
    tolerance check and the explanation into the widget itself, so a practice
    question becomes one cell instead of two.

    **Why reach for this:** cuts the boilerplate on the most common cell type
    in every notebook so far.
    """)
    return


@app.cell(hide_code=True)
def _(NumericEntryWidget, mo):
    p_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="A 0.058 kg tennis ball is served at 50 m/s. What is its momentum, in kg m/s?",
            correct_answer=0.058 * 50,
            tolerance=0.05,
            explanation="p = mv = 0.058 × 50 = 2.9 kg m s⁻¹",
        )
    )
    p_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    p_check = mo.ui.anywidget(
        NumericEntryWidget(
            question="...",
            correct_answer=2.9,
            tolerance=0.05,
            explanation="p = mv = 0.058 × 50 = 2.9 kg m s⁻¹",
        )
    )
    # in a later cell, if you want to read the result (e.g. for a running score):
    p_check.value.get("value", {}).get("ok")
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Predict, then check — `PredictThenCheckWidget`

    Matches the predict-observe-explain cells already hand-built in
    momentum-part1 (`poe_predict` radio + `poe_explain` text area + a reveal
    accordion). This widget bundles all three steps — prediction, the actual
    outcome, and an explanation per option — into one component.

    **Why reach for this:** same predict-observe-explain pattern, less
    scaffolding to write per question.
    """)
    return


@app.cell(hide_code=True)
def _(PredictThenCheckWidget, mo):
    poe_check = mo.ui.anywidget(
        PredictThenCheckWidget(
            question=(
                "Two identical trolleys collide and stick together. Trolley A "
                "(moving) hits stationary trolley B. What happens to their "
                "combined speed compared to trolley A's original speed?"
            ),
            code="# momentum before = momentum after\nm * v_A = (m + m) * v_combined",
            output="v_combined = v_A / 2",
            options=[
                "It stays the same",
                "It halves",
                "It doubles",
                "It drops to zero",
            ],
            correct_answer=1,
            explanations=[
                "Wrong: mass has doubled, so momentum conservation forces a speed change.",
                "Correct: total mass doubled, so for momentum to be conserved, speed must halve.",
                "Wrong: colliding and sticking together only ever reduces speed, never increases it.",
                "Wrong: momentum isn't destroyed in a collision — only kinetic energy is (partially) lost.",
            ],
        )
    )
    poe_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Multiple choice with instant feedback — `MultipleChoiceWidget`

    Replacement for a conceptual-check `mo.ui.radio` + manual correctness
    check. Built-in explanation shown after the student answers.
    """)
    return


@app.cell(hide_code=True)
def _(MultipleChoiceWidget, mo):
    mc_check = mo.ui.anywidget(
        MultipleChoiceWidget(
            question="A ball is thrown straight up. At the very top of its flight, what is its acceleration?",
            options=["Zero", "g, downward", "g, upward", "Depends on the throw speed"],
            correct_answer=1,
            explanation=(
                "Gravity acts on the ball for the whole flight, including the instant "
                "its velocity is zero at the top — acceleration is g downward throughout."
            ),
        )
    )
    mc_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Ordering — `OrderingWidget`

    Drag items into the correct sequence. Good for problem-solving method
    (steps to solve a momentum conservation problem), a physical process
    (stages of a projectile's flight), or an investigation write-up
    (scientific method) — anything where the *order* is the thing being
    tested, not a single fact.
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
    ## 7. Matching — `MatchingWidget`

    Draw connections between two columns. Good for quantity↔unit,
    symbol↔definition, or scenario↔equation drills.
    """)
    return


@app.cell(hide_code=True)
def _(MatchingWidget, mo):
    match_check = mo.ui.anywidget(
        MatchingWidget(
            question="Match each quantity to its SI unit:",
            left=["Momentum", "Impulse", "Force", "Velocity"],
            right=["N s", "m s⁻¹", "kg m s⁻¹", "N"],
            correct_matches={0: 2, 1: 0, 2: 3, 3: 1},
        )
    )
    match_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Labeling — `LabelingWidget`

    Tag lines of text/working with the correct label from a fixed set. Good
    for annotating a worked example line-by-line (which line is "identify
    knowns", which is "substitute", which is "state the answer with
    direction") or breaking down an equation term by term.
    """)
    return


@app.cell(hide_code=True)
def _(LabelingWidget, mo):
    label_check = mo.ui.anywidget(
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
    label_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 9. Concept map — `ConceptMapWidget`

    Draw labelled connections between concepts. Fits the existing "Unit
    Review — concept map" pattern already used at the end of the Unit 2 AOS1
    slide deck — this is an interactive version of that same idea, good as an
    end-of-topic synthesis activity rather than a per-question drill.
    """)
    return


@app.cell(hide_code=True)
def _(ConceptMapWidget, mo):
    concept_check = mo.ui.anywidget(
        ConceptMapWidget(
            question="Map the relationships between these quantities:",
            concepts=["Force", "Mass", "Acceleration", "Momentum", "Impulse"],
            terms=["causes", "changes", "equals rate of change of", "equals change in"],
            correct_edges=[
                {"from": "Force", "to": "Acceleration", "label": "causes"},
                {"from": "Mass", "to": "Acceleration", "label": "changes"},
                {"from": "Force", "to": "Momentum", "label": "equals rate of change of"},
                {"from": "Impulse", "to": "Momentum", "label": "equals change in"},
            ],
        )
    )
    concept_check
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 10. Flashcards — `FlashcardWidget`

    Self-rated recall deck (got it / almost / no). Not a per-topic tool — best
    as a dedicated revision notebook covering formulas/definitions across a
    whole AOS ahead of a SAC or exam.
    """)
    return


@app.cell(hide_code=True)
def _(FlashcardWidget, mo):
    flashcards = mo.ui.anywidget(
        FlashcardWidget(
            question="Momentum & impulse — formula recall:",
            cards=[
                {"front": "Momentum formula?", "back": "p = mv"},
                {"front": "Impulse formula?", "back": "J = FΔt = Δp"},
                {"front": "Units of momentum?", "back": "kg m s⁻¹ (equivalent to N s)"},
                {
                    "front": "Why do airbags reduce injury?",
                    "back": "They extend the collision time Δt, which reduces the force F for the same impulse (FΔt = Δp is fixed).",
                },
            ],
            shuffle=True,
        )
    )
    flashcards
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 11. Magnifier over an image or chart — `HoverZoom`

    An overlay that magnifies whatever is under the cursor. Only worth it for
    **static images or matplotlib figures** with dense detail (many labelled
    points, a busy diagram) — Altair charts already have native tooltips/zoom,
    so don't bother wrapping an Altair chart in this.
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    _rng = np.random.default_rng(7)
    _n = 40
    _x = _rng.uniform(0, 10, _n)
    _y = _rng.uniform(0, 10, _n)
    _labels = [f"P{i}" for i in range(_n)]

    _fig, _ax = plt.subplots(figsize=(6, 5), dpi=150)
    _ax.scatter(_x, _y, s=14, alpha=0.6)
    for _xi, _yi, _lab in zip(_x, _y, _labels):
        _ax.annotate(_lab, (_xi, _yi), fontsize=4, alpha=0.7, ha="center", va="bottom")
    _ax.set_title(f"{_n} labelled points — hover to zoom and read labels")
    _fig.tight_layout()
    hoverzoom_fig = _fig
    return (hoverzoom_fig,)


@app.cell(hide_code=True)
def _(HoverZoom, hoverzoom_fig, mo):
    mo.ui.anywidget(HoverZoom(hoverzoom_fig, zoom_factor=4.0, width=460))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 12. Editable matrix — `Matrix`

    An editable matrix widget wired to a linked plot. This is genuinely more
    a linear-algebra/data-science tool than a VCE Physics 1–4 one — included
    here for completeness, but there's no current topic it clearly fits.
    Might become useful later for a 2D coordinate-transform demo. Low
    priority — skip unless a specific topic calls for it.
    """)
    return


@app.cell(hide_code=True)
def _(Matrix, mo, np):
    demo_matrix = mo.ui.anywidget(Matrix(np.array([[1.0, 0.0], [0.0, 1.0]]), step=0.1))
    demo_matrix
    return (demo_matrix,)


@app.cell(hide_code=True)
def _(alt, demo_matrix, mo, np, pd):
    _pts = np.array([[1, 0], [0, 1], [1, 1], [-1, -1]])
    _tfm = _pts @ np.array(demo_matrix.matrix)
    _df = pd.DataFrame({"x": _tfm[:, 0], "y": _tfm[:, 1]})
    _spec = {
        "data": {"values": _df.to_dict("records")},
        "mark": {"type": "point", "size": 100, "filled": True},
        "encoding": {
            "x": {"field": "x", "type": "quantitative", "scale": {"domain": [-3, 3]}},
            "y": {"field": "y", "type": "quantitative", "scale": {"domain": [-3, 3]}},
        },
        "width": 240,
        "height": 240,
    }
    mo.center(alt.Chart.from_dict(_spec, validate=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 13. Text comparison — `TextCompare`

    Side-by-side text diff, highlighting shared passages. No clear physics
    *content* fit for Units 1–4 — the only plausible use is comparing a
    student's investigation write-up against a model answer, which isn't
    really "interactive notebook" territory. Included for completeness only.
    """)
    return


@app.cell(hide_code=True)
def _(TextCompare, mo):
    text_compare_demo = mo.ui.anywidget(
        TextCompare(
            text_a="Momentum is conserved in an isolated system during a collision.",
            text_b="In an isolated system, total momentum is conserved during any collision.",
            min_match_words=3,
        )
    )
    text_compare_demo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 14. Turtle graphics — `World` / `Color`

    A tiny turtle-graphics engine — write a coroutine that steps a turtle
    forward/turns it, and it draws as it goes. Could visualise a
    vector-addition path (walk each vector head-to-tail) or a projectile
    trajectory being traced out step by step. A bigger custom-build lift than
    the other widgets here for a novelty payoff — stretch idea, not a
    priority, but a nice one if a topic ever calls for an animated path.
    """)
    return


@app.cell(hide_code=True)
def _(Color, World, mo):
    _world = World()

    async def _vector_walk(world, turtle):
        # Head-to-tail vector addition: 8 m east, then 6 m north.
        turtle.set_color(Color.BLUE)
        await turtle.forward(80)  # 8 m east, scaled
        turtle.set_color(Color.RED)
        turtle.left(90)
        await turtle.forward(60)  # 6 m north, scaled

    _world.set_coroutine(_vector_walk)
    mo.ui.anywidget(_world)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Summary — what to reach for

    | Widget | Package | Replaces / fits | Priority |
    |---|---|---|---|
    | `TangleSlider` | wigglystuff | `mo.ui.slider` for any value quoted in prose | High — retrofit freely |
    | `Slider2D` | wigglystuff | a pair of x/y sliders for anything that's really one 2D vector | High — use for Forces and motion, projectile motion |
    | `NumericEntryWidget` | marimo-learn | hand-rolled `mo.ui.number` + tolerance check ("Quick practice" cells) | High — direct swap |
    | `PredictThenCheckWidget` | marimo-learn | hand-rolled predict/explain/reveal cells (momentum-part1 POE pattern) | High — direct swap |
    | `MultipleChoiceWidget` | marimo-learn | `mo.ui.radio` conceptual checks | High — direct swap |
    | `OrderingWidget` | marimo-learn | new: sequencing method/process questions | Medium — new topics |
    | `MatchingWidget` | marimo-learn | new: quantity↔unit / symbol↔definition drills | Medium — new topics |
    | `LabelingWidget` | marimo-learn | new: annotate a worked example or graph line-by-line | Medium — new topics |
    | `ConceptMapWidget` | marimo-learn | interactive version of the existing "Unit Review — concept map" slide | Medium — end-of-topic review |
    | `FlashcardWidget` | marimo-learn | new: dedicated revision notebook, formula/definition recall | Medium — revision notebook only |
    | `HoverZoom` | wigglystuff | magnifying a dense **matplotlib/image** diagram (not Altair — it already has tooltips) | Situational |
    | `Matrix` | wigglystuff | no current physics fit | Low |
    | `TextCompare` | wigglystuff | no current physics fit | Low |
    | `World` / `Color` (turtle) | marimo-learn | animated vector-addition or trajectory path | Stretch |

    **Dependencies to add** wherever any of these are used:
    `pip install wigglystuff marimo-learn` (installs `anywidget` as a
    transitive dependency of both).
    """)
    return


if __name__ == "__main__":
    app.run()
