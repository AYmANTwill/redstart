import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4], 
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )    
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),                
                )
            )
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Réponse

    Un état d'équilibre est un état pour lequel $\dot{s} = F(s, f, \phi) = 0$.
    Ceci nous amène à résourdre le système d'équations suivant:

    $$
        \dot{s} = F(s, f, \phi) =
        \begin{pmatrix}
        \dot{x} \\ \dot{v}_x \\ \dot{y} \\ \dot{v}_y \\ \dot{\theta} \\ \dot{\omega}
        \end{pmatrix}
        =
        \begin{pmatrix}
        v_x \\
        -\dfrac{f}{M}\sin(\theta + \phi) \\
        v_y \\
        \dfrac{f}{M}\cos(\theta + \phi) - g \\
        \omega \\
        -\dfrac{6f\, \sin\phi}{M \ell}
        \end{pmatrix}
        =
        \begin{pmatrix}
        \ 0 \\ 0 \\ 0\\ 0 \\ 0 \\ 0 \end{pmatrix}
        $$


    1. **Vitesses :** Les lignes 1, 3 et 5 nous donnent immédiatement $v_x = 0$, $v_y = 0$, et $\omega = 0$. Le booster est immobile.
    2. **Angle de poussée ($\phi$) :** La ligne 6 nous indique que $-\dfrac{6f\, \sin\phi}{M \ell} = 0$. Comme la force $f > 0$ il faut donc que $\sin\phi = 0$. Compte tenu de la contrainte $|\phi| < \pi/2$, l'unique solution est :
       $\phi = 0$
    3. **Inclinaison du booster ($\theta$) :** En remplaçant $\phi = 0$ dans la 2ème équation, on obtient $-\dfrac{f}{M}\sin(\theta) = 0$. Cela implique que $\sin\theta = 0$. Avec la contrainte $|\theta| < \pi/2$, la seule solution possible est :
       $\theta = 0$
    4. **Force de poussée ($f$) :** En insérant $\theta = 0$ et $\phi = 0$ dans la 4ème équation, on obtient $\dfrac{f}{M}\cos(0) - g = 0$, ce qui donne directement la poussée nécessaire pour compenser exactement la gravité :
       $f = Mg$
    5. **Positions ($x$ et $y$) :** Les variables de position $x$ et $y$ n'apparaissent pas du tout dans le système d'équations des dérivées. Par conséquent, elles n'influent pas sur l'équilibre et peuvent prendre n'importe quelles valeurs constantes (notons-les $x_e$ et $y_e$) (le booster peut rester en équilibre dans l'air sans forcément toucher le sol).

    **Conclusion :**

    Les valeurs correspondantes des entrées à l'équilibre sont :
    $$
    f_e = Mg, \quad \phi_e = 0
    $$
    (Pour ne pas tourner, la poussée du moteur doit être parfaitement alignée avec le centre de gravité du booster et la poussée du réacteur doit compenser exactement le poids du booster pour qu'il maintienne une altitude constante)

    Et les états d'équilibre possibles s'écrivent sous la forme du vecteur suivant :
    $$
    s_e =
    \begin{pmatrix}
    x_e \\ 0 \\ y_e \\ 0 \\ 0 \\ 0
    \end{pmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Réponse

    La linéarisation d'un système non-linéaire autour d'un équilibre repose sur une approximation au **premier ordre** (développement de Taylor). En reprenant l'état d'équilibre calculé précédemment $(x_e, 0, y_e, 0, 0, 0)$ avec les entrées $f_e = Mg$ et $\phi_e = 0$, nous pouvons exprimer les variables du système en fonction de leurs écarts :

    **États :**
    $$
    \begin{aligned}
    x &= x_e + \Delta x \implies \dot{x} = \Delta \dot{x} \\
    v_x &= 0 + \Delta v_x \implies \dot{v}_x = \Delta \dot{v}_x \\
    y &= y_e + \Delta y \implies \dot{y} = \Delta \dot{y} \\
    v_y &= 0 + \Delta v_y \implies \dot{v}_y = \Delta \dot{v}_y \\
    \theta &= 0 + \Delta \theta \implies \dot{\theta} = \Delta \dot{\theta} \\
    \omega &= 0 + \Delta \omega \implies \dot{\omega} = \Delta \dot{\omega}
    \end{aligned}
    $$

    **Entrées :**
    $$
    \begin{aligned}
    f &= Mg + \Delta f \\
    \phi &= 0 + \Delta \phi
    \end{aligned}
    $$


    **Linéarisation des équations différentielles :**

    Reprenons chaque équation du champ de vecteurs $F(s, f, \phi)$ et appliquons l'approximation au premier ordre :

    * **Axe horizontal (Position et vitesse) :**
        $$\Delta \dot{x} = \Delta v_x$$

        Pour la vitesse $v_x$ :
        $$\Delta \dot{v}_x = -\frac{Mg + \Delta f}{M} \sin(\Delta \theta + \Delta \phi)$$

        Avec l'approximation des petits angles, $\sin(\Delta \theta + \Delta \phi) \approx \Delta \theta + \Delta \phi$. En développant et en négligeant le terme du second ordre ($\Delta f \cdot \Delta \theta$ et $\Delta f \cdot \Delta \phi$), on obtient :
        $$\Delta \dot{v}_x = -g \Delta \theta - g \Delta \phi$$

    * **Axe vertical (Position et vitesse) :**
        $$\Delta \dot{y} = \Delta v_y$$

        Pour la vitesse $v_y$ :
        $$\Delta \dot{v}_y = \frac{Mg + \Delta f}{M} \cos(\Delta \theta + \Delta \phi) - g$$

        Avec l'approximation $\cos(\Delta \theta + \Delta \phi) \approx 1$, l'équation devient :
        $$\Delta \dot{v}_y \approx \frac{Mg + \Delta f}{M} - g = g + \frac{\Delta f}{M} - g = \frac{1}{M} \Delta f$$

    * **Rotation (Angle et vitesse angulaire) :**
        $$\Delta \dot{\theta} = \Delta \omega$$

        Pour l'accélération angulaire $\omega$ :
        $$\Delta \dot{\omega} = -\frac{(Mg + \Delta f) \ell}{2J} \sin(\Delta \phi)$$

        En utilisant $\sin(\Delta \phi) \approx \Delta \phi$ et en négligeant le terme du second ordre, on a :
        $$\Delta \dot{\omega} = -\frac{Mg\ell}{2J} \Delta \phi$$

    **Modèle linéarisé final :**

    En remplaçant le moment d'inertie par son expression $J = \frac{1}{12}M\ell^2$, on obtient le système suivant :

    $$
    \Delta \dot{s} =
    \begin{pmatrix}
    \Delta \dot{x} \\ \Delta \dot{v}_x \\ \Delta \dot{y} \\ \Delta \dot{v}_y \\ \Delta \dot{\theta} \\ \Delta \dot{\omega}
    \end{pmatrix}
    =
    \begin{pmatrix}
    \Delta v_x \\
    -g \Delta \theta - g \Delta \phi \\
    \Delta v_y \\
    \dfrac{1}{M} \Delta f \\
    \Delta \omega \\
    -\dfrac{6g}{\ell} \Delta \phi
    \end{pmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Réponse

    On utilise le vecteur d'état $\Delta s$ et le vecteur d'entrée $\Delta u$ définis par les écarts par rapport à l'équilibre. Le système linéaire mis sous forme standard $\Delta \dot{s} = A \Delta s + B \Delta u$ s'écrit alors :

    $$
    \Delta \dot{s} =
    \begin{pmatrix}
    \Delta \dot{x} \\ \Delta \dot{v}_x \\ \Delta \dot{y} \\ \Delta \dot{v}_y \\ \Delta \dot{\theta} \\ \Delta \dot{\omega}
    \end{pmatrix}
    =
    \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix}
    \begin{pmatrix}
    \Delta x \\ \Delta v_x \\ \Delta y \\ \Delta v_y \\ \Delta \theta \\ \Delta \omega
    \end{pmatrix}
    +
    \begin{pmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \dfrac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\dfrac{6g}{\ell}
    \end{pmatrix}
    \begin{pmatrix}
    \Delta f \\ \Delta \phi
    \end{pmatrix}
    $$

    Où les matrices de la forme standard sont :

    $$
    A =
    \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix},
    \quad
    B =
    \begin{pmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \dfrac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\dfrac{6g}{\ell}
    \end{pmatrix}
    $$
    """)
    return


@app.cell
def _(J, M, g, l, np):
    def A_et_B(J, M, g, l, np):
        A = np.array([
            [0,1,0,0,0,0],
            [0,0,0,0,-g,0],
            [0,0,0,1,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,1],
            [0,0,0,0,0,0],
        ])

        B = np.array([
            [0,0],
            [0,-g],
            [0,0],
            [1/M,0],
            [0,0],
            [0,-M * g * l / (2 * J)],
        ])

        print("A =")
        print(A)
        print()
        print("B =")
        print(B)
        return A, B

    A_et_B(J, M, g, l, np)
    return (A_et_B,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Réponse

    On observe que $A$ est une matrice strictement triangulaire supérieure, ses valeurs propres se lisent sur sa diagonale principale.

    Le spectre de la matrice $A$ est :
    $$
    \sigma(A) = \{0, 0, 0, 0, 0, 0\}
    $$

    Toutes les valeurs propres ont une partie réelle égale à $0$. La condition d'avoir une partie réelle strictement négative pour avoir un système linéaire temps-invariant asymptotiquement stable autour de son point d'équilibre n'est donc pas respectée.

    **Conclusion :**

    Cela fait sens d'un point de vue physique ; un booster en vol stationnaire n'a aucune tendance naturelle à revenir à sa position verticale s'il subit une perturbation dûe au vent par exemple; il va commencer à dériver ou à basculer indéfiniment si aucune action de contrôle ($\Delta \phi$) n'est activement appliquée pour le corriger.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Réponse
    Un système LTI de dimension $n$ est contrôlable si et seulement si sa matrice de commandabilité $\mathcal{C}$ est de rang plein, c'est-à-dire $\text{rang}(\mathcal{C}) = n$.

    Pour étudier donc la contrôlabilité de notre système linéarisé (d'ordre $n=6$) on calcule la matrice de commandabilité de Kalman $\mathcal{C}$, définie par :
    $$
    \mathcal{C} = \begin{bmatrix} B & AB & A^2B & A^3B & A^4B & A^5B \end{bmatrix}
    $$

    **1. Calcul des produits matriciels successifs :**

    En utilisant nos matrices $A$ et $B$ d'origine :
    $$
    A = \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix},
    \quad
    B = \begin{pmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    1/M & 0 \\
    0 & 0 \\
    0 & -6g/\ell
    \end{pmatrix}
    $$

    On calcule pas à pas les blocs de la matrice de Kalman :

    Le bloc $AB$ :
    $$
    AB = A \times B = \begin{pmatrix}
    0 & -g \\
    0 & 0 \\
    1/M & 0 \\
    0 & 0 \\
    0 & -6g/\ell \\
    0 & 0
    \end{pmatrix}
    $$

    Le bloc $A^2B$ :
    $$
    A^2B = A \times (AB) = \begin{pmatrix}
    0 & 0 \\
    0 & 6g^2/\ell \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0
    \end{pmatrix}
    $$

    Le bloc $A^3B$ :
    $$
    A^3B = A \times (A^2B) = \begin{pmatrix}
    0 & 6g^2/\ell \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0 \\
    0 & 0
    \end{pmatrix}
    $$

    *(Les blocs $A^4B$ et $A^5B$ sont des matrices nulles).*

    **2. Assemblage de la matrice de Kalman :**

    En concaténant ces matrices côte à côte, on obtient la matrice $\mathcal{C}$ de dimension $6 \times 12$ :

    $$
    \mathcal{C} = \begin{pmatrix}
    0 & 0 & 0 & -g & 0 & 0 & 0 & 6g^2/\ell & \dots \\
    0 & -g & 0 & 0 & 0 & 6g^2/\ell & 0 & 0 & \dots \\
    0 & 0 & 1/M & 0 & 0 & 0 & 0 & 0 & \dots \\
    1/M & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \dots \\
    0 & 0 & 0 & -6g/\ell & 0 & 0 & 0 & 0 & \dots \\
    0 & -6g/\ell & 0 & 0 & 0 & 0 & 0 & 0 & \dots
    \end{pmatrix}
    $$

    **3. Démonstration du rang plein ($n=6$) :**

    Pour prouver que le système est contrôlable, il faut démontrer que $\text{rang}(\mathcal{C}) = 6$. Pour ce faire, extrayons 6 colonnes linéairement indépendantes pour former une sous-matrice carrée $6 \times 6$.

    En choisissant (de gauche à droite) la 8ème, la 6ème, la 3ème, la 1ère, la 4ème et la 2ème colonne, nous obtenons la sous-matrice $M_c$ suivante :

    $$
    M_c = \begin{pmatrix}
    6g^2/\ell & 0 & 0 & 0 & -g & 0 \\
    0 & 6g^2/\ell & 0 & 0 & 0 & -g \\
    0 & 0 & 1/M & 0 & 0 & 0 \\
    0 & 0 & 0 & 1/M & 0 & 0 \\
    0 & 0 & 0 & 0 & -6g/\ell & 0 \\
    0 & 0 & 0 & 0 & 0 & -6g/\ell
    \end{pmatrix}
    $$

    Cette matrice $M_c$ est **triangulaire supérieure**. Son déterminant est donc simplement le produit des éléments de sa diagonale principale :

    $$
    \det(M_c) = \left(\frac{6g^2}{\ell}\right)^2 \times \left(\frac{1}{M}\right)^2 \times \left(-\frac{6g}{\ell}\right)^2
    $$

    Puisque les grandeurs physiques ($M$, $g$, $\ell$) sont strictement positives, ce déterminant est **non nul**. Les 6 colonnes choisies sont linéairement indépendantes, ce qui garantit que $\text{rang}(\mathcal{C}) = 6$.

    **Conclusion :** Le modèle linéarisé complet est totalement contrôlable.

    On peut aussi vérifier ceci par le code Python suivant :
    """)
    return


@app.cell
def _(A_et_B, J, M, g, l, np):
    def testcontrol(A, B, np):
        def controllability_matrix(A, B):
            n = A.shape[0]
            cols = [B]
            for _ in range(1, n):
                cols.append(A @ cols[-1])
            return np.hstack(cols)

        C_mat = controllability_matrix(A, B)
        rank_C = np.linalg.matrix_rank(C_mat)
        print(f"Rang de la matrice de commandabilité: {rank_C} (state dimension n = {A.shape[0]})")
        print("Le système est contrôable:", rank_C == A.shape[0])
        return C_mat, controllability_matrix, rank_C
    A, B = A_et_B(J, M, g, l, np)    
    testcontrol(A, B, np)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Conclusion** :

    Le système est bel et bien contrôlable
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Réponse

    Pour réduire le système aux seules dynamiques latérales, on ignore l'axe vertical ($y$ et $\dot{y}$) et on fixe la force $f = Mg$, ceci implique que la variation de force est nulle ($\Delta f = 0$).

    Le nouveau vecteur d'état latéral $\Delta s_{lat}$ et la nouvelle entrée $\Delta u_{lat}$ sont :
    $$
    \Delta s_{lat} =
    \begin{pmatrix}
    \Delta x \\ \Delta v_x \\ \Delta \theta \\ \Delta \omega
    \end{pmatrix},
    \quad
    \Delta u_{lat} = \Delta \phi
    $$

    **1. Matrices du système réduit :**

    En extrayant les lignes et colonnes correspondantes de notre modèle complet (et en annulant les termes en $\Delta f$), nous obtenons le système réduit $\Delta \dot{s}_{lat} = A_{lat} \Delta s_{lat} + B_{lat} \Delta u_{lat}$ avec :

    $$
    A_{lat} =
    \begin{pmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{pmatrix},
    \quad
    B_{lat} =
    \begin{pmatrix}
    0 \\
    -g \\
    0 \\
    -\dfrac{6g}{\ell}
    \end{pmatrix}
    $$

    **2. Contrôlabilité du nouveau système :**

    Pour vérifier si ce système réduit (d'ordre $n=4$) est contrôlable, nous devons construire sa matrice de commandabilité de Kalman :
    $$
    \mathcal{C}_{lat} = \begin{bmatrix} B_{lat} & A_{lat}B_{lat} & A_{lat}^2B_{lat} & A_{lat}^3B_{lat} \end{bmatrix}
    $$

    Calculons successivement chaque colonne de cette matrice :

    * **1ère colonne ($B_{lat}$) :**
    $$
    B_{lat} = \begin{pmatrix} 0 \\ -g \\ 0 \\ -\dfrac{6g}{\ell} \end{pmatrix}
    $$

    * **2ème colonne ($A_{lat}B_{lat}$) :**
    $$
    A_{lat}B_{lat} =
    \begin{pmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{pmatrix}
    \begin{pmatrix} 0 \\ -g \\ 0 \\ -\dfrac{6g}{\ell} \end{pmatrix}
    = \begin{pmatrix} -g \\ 0 \\ -\dfrac{6g}{\ell} \\ 0 \end{pmatrix}
    $$

    * **3ème colonne ($A_{lat}^2B_{lat}$) :**
    $$
    A_{lat}^2B_{lat} = A_{lat} \times (A_{lat}B_{lat}) =
    \begin{pmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{pmatrix}
    \begin{pmatrix} -g \\ 0 \\ -\dfrac{6g}{\ell} \\ 0 \end{pmatrix}
    = \begin{pmatrix} 0 \\ \dfrac{6g^2}{\ell} \\ 0 \\ 0 \end{pmatrix}
    $$

    * **4ème colonne ($A_{lat}^3B_{lat}$) :**
    $$
    A_{lat}^3B_{lat} = A_{lat} \times (A_{lat}^2B_{lat}) =
    \begin{pmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{pmatrix}
    \begin{pmatrix} 0 \\ \dfrac{6g^2}{\ell} \\ 0 \\ 0 \end{pmatrix}
    = \begin{pmatrix} \dfrac{6g^2}{\ell} \\ 0 \\ 0 \\ 0 \end{pmatrix}
    $$

    En assemblant ces 4 colonnes, on obtient la matrice de Kalman $\mathcal{C}_{lat}$ :

    $$
    \mathcal{C}_{lat} =
    \begin{pmatrix}
    0 & -g & 0 & \dfrac{6g^2}{\ell} \\
    -g & 0 & \dfrac{6g^2}{\ell} & 0 \\
    0 & -\dfrac{6g}{\ell} & 0 & 0 \\
    -\dfrac{6g}{\ell} & 0 & 0 & 0
    \end{pmatrix}
    $$

    **Conclusion sur la contrôlabilité :**

    La matrice $\mathcal{C}_{lat}$ est une matrice anti-triangulaire. Le produit des éléments de son anti-diagonale est :
    $$
    \left(-\dfrac{6g}{\ell}\right) \times \left(-\dfrac{6g}{\ell}\right) \times \left(\dfrac{6g^2}{\ell}\right) \times \left(\dfrac{6g^2}{\ell}\right)
    $$
    Puisque les grandeurs $g$ et $\ell$ sont strictement positives, ce produit est non nul, ce qui implique que le déterminant de la matrice est non nul.

    La matrice est donc de **rang plein (rang = 4)**. Le système latéral réduit est **contrôlable**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Réponse
    """)
    return


@app.cell
def _(g, np, plt, scipy):
    def plot_linearized_free_fall():
        A_lat = np.array([
            [0, 1,  0, 0],
            [0, 0, -g, 0],
            [0, 0,  0, 1],
            [0, 0,  0, 0]
        ])
    
        y0 = np.array([0.0, 0.0, np.pi/4, 0.0])
    
        def fun(t, state):
            return A_lat @ state
        
        t_span = [0.0, 25.0] # Simulation sur 5 secondes
        result = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        
        t = np.linspace(t_span[0], t_span[1], 500)
        states = result.sol(t)
        x_t = states[0]      
        theta_t = states[2]  
    
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
        ax1.plot(t, x_t, color='blue')
        ax1.set_title("Position latérale x(t)")
        ax1.set_xlabel("Temps (s)")
        ax1.set_ylabel("x (m)")
        ax1.grid(True)
    
        ax2.plot(t, theta_t, color='red')
        ax2.set_title("Angle d'inclinaison θ(t)")
        ax2.set_xlabel("Temps (s)")
        ax2.set_ylabel("θ (rad)")
        ax2.grid(True)
    
        return fig

    plot_linearized_free_fall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Analyse physique des résultats

    **Ce que l'on observe sur les graphes :**
    * L'angle d'inclinaison $\theta(t)$ **reste parfaitement constant** à sa valeur initiale de $\pi/4$ (environ 0.78 rad) tout au long de la simulation.
    * La position latérale $x(t)$ décrit une **courbe parabolique** (le booster dérive de plus en plus vite vers la gauche, dans les valeurs négatives).

    **Comment l'expliquer physiquement ?**

    1. **L'angle constant ($\theta$) :** Le booster est soumis à deux forces : la gravité et la poussée du réacteur. La gravité s'applique au centre de masse (elle ne crée donc pas de rotation). La poussée du réacteur ($f = Mg$) est parfaitement alignée avec l'axe du booster puisque l'angle $\phi$  est nul. Sa ligne d'action passe donc par le centre de masse. Puisqu'aucune force ne crée de bras de levier, le moment des forces (couple) est nul. Le booster ne subit aucune accélération angulaire ($\Delta \dot{\omega} = 0$) et conserve indéfiniment son inclinaison initiale de 45°.

    2. **La dérive parabolique ($x$) :** Le booster est incliné à 45°, mais la norme de sa poussée reste fixée à $f = Mg$. Si l'on regarde l'équation de notre dynamique latérale linéarisée, l'accélération horizontale vaut $\Delta \dot{v}_x = -g \Delta \theta - g \Delta \phi$.
    Puisque $\Delta \phi = 0$ et $\Delta \theta = \pi/4$ (constante positive), l'accélération horizontale devient une constante strictement négative. L'intégration d'une accélération constante donne une vitesse linéaire et une position suivant une trajectoire quadratique (parabole). Le réacteur pousse constamment le booster "sur le côté".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
