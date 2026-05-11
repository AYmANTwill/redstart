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
    from scipy.integrate import solve_ivp

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, solve_ivp


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    g = 1.0   # gravité en m/s²
    M = 1.0   # masse du booster en kg
    l = 2.0   # longueur du booster
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 📝 Réponse

    Le réacteur est situé à la base du booster. Considérons les repères :

    - L'**axe du booster** fait un angle $\theta$ avec la verticale (sens trigonométrique positif).
    - La **force du réacteur** fait un angle $\phi$ avec l'axe du booster (sens trigonométrique positif).

    Ainsi, l'angle total entre la force $\vec{f}$ et la **verticale** (axe $y$) est $\theta + \phi$.

    En projetant la force $\vec{f}$ (de norme $f \geq 0$) sur les axes cartésiens, on obtient :

    $$
    \begin{aligned}
    f_x &= -f \sin(\theta + \phi) \\
    f_y &= +f \cos(\theta + \phi)
    \end{aligned}
    $$

    **Vérifications de cohérence :**

    - Si $\theta = 0$ et $\phi = 0$ : la force est verticale vers le haut. On a bien $f_x = 0$ et $f_y = +f$
    - Si $\theta = 0$ et $\phi = +\pi/2$ : la force pointe vers la gauche. On a bien $f_x = -f$ et $f_y = 0$
    - Si $\theta = +\pi/2$ (booster couché à gauche) et $\phi = 0$ : la force pointe vers la gauche. On a bien $f_x = -f$ et $f_y = 0$
    """)
    return


@app.cell
def _(np):
    def reactor_force(f, theta, phi):
        """
        Composantes cartésiennes de la force du réacteur.

        Paramètres
        ----------
        f : Amplitude de la force du réacteur (f >= 0).

        theta : Angle du booster par rapport à la verticale (rad, trigo positif).

        phi : Angle de la force par rapport à l'axe du booster (rad, trigo positif).

        Retours
        -------
        (fx, fy) : tuple de float
            Composantes cartésiennes de la force.
        """
        fx = -f * np.sin(theta + phi)
        fy = +f * np.cos(theta + phi)
        return fx, fy

    return


@app.cell
def _():
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
    mo.md(r"""
    ### 📝 Réponse

    D'après la **deuxième loi de Newton** appliquée au centre de masse du booster, on a :

    $$
    M \, \ddot{\vec{r}} = \sum \vec{F}_{\text{ext}}
    $$

    où $\vec{r}$ est la position du centre de masse, et les forces extérieures sont :

    - la **gravité** : $\vec{F}_g = (0, -Mg)^T$
    - la **poussée du réacteur** : $\vec{F}_r = \big(-f \sin(\theta + \phi),\ f \cos(\theta + \phi)\big)^T$

    (On néglige la friction de l'air comme indiqué dans l'énoncé.)

    **Écriture scalaire :**

    $$
    \begin{aligned}
    \ddot{x} &= -\dfrac{f}{M} \sin(\theta + \phi) \\
    \ddot{y} &= +\dfrac{f}{M} \cos(\theta + \phi) - g
    \end{aligned}
    $$

    ce qui permet d'écrire le système sous forme matricielle :

    $$
    \boxed{\;\begin{pmatrix} \ddot{x} \\ \ddot{y} \end{pmatrix} = \dfrac{f}{M}\, \begin{pmatrix} -\sin(\theta+\phi) \\ \cos(\theta+\phi) \end{pmatrix} + \begin{pmatrix} 0 \\ -g \end{pmatrix}\;}
    $$
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
    Le booster est modélisé par une tige rigide, de longueur $\ell$, de masse $M$ et de section négligeable. Le moment d'inertie par rapport à son centre d'inertie est donné par :

    $$
    J=\frac{M \ell^2}{12}
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l**2 / 12
    return


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
    ### 📝 Réponse

    D'après le **théorème du moment cinétique** appliqué au centre de masse du booster (corps rigide en rotation 2D) :

    $$
    J \, \ddot{\theta} = \tau
    $$

    où $\tau$ est le couple résultant des forces extérieures par rapport au centre de masse.

    **Calcul du couple.**

    - La **gravité** s'applique au centre de masse : son bras de levier est nul, donc elle ne crée **aucun couple**.
    - La **poussée du réacteur** s'applique au point $P$ situé à la **base** du booster, soit à une distance $\ell/2$ du centre de masse, dans la direction $-\vec{e}_{\text{booster}}$.

    Le vecteur position du point d'application (depuis le centre de masse) est :

    $$
    \vec{r}_P = -\dfrac{\ell}{2} \begin{pmatrix} -\sin\theta \\ \cos\theta \end{pmatrix} = \dfrac{\ell}{2} \begin{pmatrix} \sin\theta \\ -\cos\theta \end{pmatrix}
    $$

    Le vecteur force du réacteur est :

    $$
    \vec{F}_r = f \begin{pmatrix} -\sin(\theta + \phi) \\ \cos(\theta + \phi) \end{pmatrix}
    $$

    Le couple (composante $z$ du produit vectoriel) vaut :

    $$
    \tau = \vec{r}_P \wedge \vec{F}_r = r_{P,x}\, F_{r,y} - r_{P,y}\, F_{r,x}
    $$

    $$
    \tau = \dfrac{\ell}{2} \sin\theta \cdot f \cos(\theta+\phi) - \left(-\dfrac{\ell}{2}\cos\theta\right) \cdot \left(-f \sin(\theta+\phi)\right)
    $$

    $$
    \tau = \dfrac{f\ell}{2}\,\big[\sin\theta \cos(\theta+\phi) - \cos\theta \sin(\theta+\phi)\big]
    $$

    En utilisant l'identité $\sin(a-b) = \sin a \cos b - \cos a \sin b$ avec $a = \theta$ et $b = \theta + \phi$ :

    $$
    \tau = \dfrac{f\ell}{2}\,\sin(-\phi) = -\dfrac{f\ell}{2}\,\sin\phi
    $$

    **EDO du tilt :**

    $$
    \boxed{\; J\,\ddot{\theta} = -\dfrac{f\ell}{2}\,\sin\phi \;}
    $$

    soit, en remplaçant $J = M\ell^2/12$ :

    $$
    \boxed{\; \ddot{\theta} = -\dfrac{6 f}{M\ell}\,\sin\phi \;}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
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
    ### 📝 Réponse

    L'état de la dynamique du booster est modélisée par le 6-uplet $s=(x,v_x,y,v_y,\theta,\omega)$, on travaille donc dans un espace d'état à $n=6$ dimensions. On obtient alors l'équation d'évolution suivante :

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


@app.cell
def _(M, g, l, np, solve_ivp):
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s
        return np.array([
            vx,
            -(f/M) * np.sin(theta + phi),
            vy,
            (f/M) * np.cos(theta + phi) - g,
            omega,
            -(6*f*np.sin(phi)) / (M*l)
        ])

    def redstart_solve(t_span, y0, f_phi):
        def dynamics(t, s):
            f, phi = f_phi(t, s)
            return F(s, f, phi)
    
        result = solve_ivp(dynamics, t_span, y0, method='RK45', dense_output=True, rtol=1e-8, atol=1e-8)
        return result.sol

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
    ### 📝 Answer

    En chute libre avec $f = 0$, le mouvement vertical est décrit par :

    $$
    y(t) = y_0 + v_y(0)\,t - \frac{1}{2}g\,t^2 = 10 - \frac{1}{2}t^2
    $$

    En posant $y(t_f) = \ell = 2 \text{ m}$ :

    $$
    10 - \frac{1}{2}(t_f)^2 = 2 \implies (t_f)^2 = 16 \implies t_f = 4 \,\text{ s}
    $$
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def free_fall_example():
            t_span = [0.0, 5.0]
            y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]

            def f_phi(t, y):
                return np.array([0.0, 0.0])  # no thrust

            sol = redstart_solve(t_span, y0, f_phi)

            t = np.linspace(t_span[0], t_span[1], 1000)
            y_t = sol(t)[2]  # index 2 = y position

            t_f = 4

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(t, y_t, label=r"$y(t)$ (hauteur en mètres)", color="royalblue", lw=2)
            ax.axhline(l, color="grey", ls="--", label=rf"$y = \ell = {l}$ m")
            ax.axvline(t_f, color="tomato", ls=":", lw=1.5,
                       label=rf"$t_f = 4$ s")
            ax.scatter([t_f], [l], color="tomato", zorder=5)
            ax.set_title("Chute libre — Hauteur du Centre de Masse")
            ax.set_xlabel("temps $t$ (s)")
            ax.set_ylabel("hauteur $y$ (m)")
            ax.grid(True, alpha=0.3)
            ax.legend()
            fig.tight_layout()
            return fig

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
    mo.md(r"""
    ### 📝 Réponse

    Avec $\phi = 0$ et donc $\theta = 0$ (aucune force d'inclinaison), la dynamique verticale se réduit à :

    $$
    \ddot{y} = \frac{f(t)}{M} - g
    $$

    On veut amener le système de l’état initial $(y_0,\dot y_0) = (10,-2)$ vers l’état final $(y_f,\dot y_f) = (1,0)$ à $t=5$.

    ---

    ## Stratégie — planification de trajectoire polynomiale

    On choisit une trajectoire de référence $y_r(t)$ sous forme d’un polynôme cubique satisfaisant les quatre conditions aux limites :

    $$
    y_r(t)=a_0+a_1 t+a_2 t^2+a_3 t^3
    $$

    ### Conditions aux limites

    - $y_r(0)=10 \Rightarrow a_0=10$
    - $\dot y_r(0)=-2 \Rightarrow a_1=-2$
    - $y_r(5)=1 \Rightarrow 10-10+25a_2+125a_3=1$
    - $\dot y_r(5)=0 \Rightarrow -2+10a_2+75a_3=0$

    On obtient donc le système linéaire :

    $$
    25a_2+125a_3=-9,
    \qquad
    10a_2+75a_3=2
    $$

    La résolution donne :

    $$
    a_2=-\frac{47}{50},
    \qquad
    a_3=\frac{18}{250}=\frac{9}{125}
    $$

    ---

    ## Trajectoire obtenue

    La trajectoire de référence est alors :

    $$
    y_r(t)=10-2t-\frac{47}{50}t^2+\frac{9}{125}t^3
    $$

    Sa dérivée seconde vaut :

    $$
    \ddot y_r(t)=2a_2+6a_3 t
    $$

    ---

    ## Force de commande nécessaire

    La force à appliquer est donc :

    $$
    f(t)=M\bigl(\ddot y_r(t)+g\bigr)
    $$

    c’est-à-dire :

    $$
    f(t)=M\left(2a_2+6a_3 t+g\right)
    $$

    ou encore, en remplaçant $a_2$ et $a_3$ :

    $$
    f(t)
    =
    M\left(
    -\frac{47}{25}
    +\frac{54}{125}t
    +g
    \right)
    $$
    """)
    return


@app.cell
def _(M, g, l, np, plt, redstart_solve):
    def controlled_landing():
            t_span = [0.0, 5.0]
            tf = 5.0
            y0_val = 10.0
            vy0_val = -2.0
            yf_val = l / 2       # = 1.0 (à ras du sol)
            vyf_val = 0.0

            # Résoudre pour un polynome de degré 3
            # y_r(t) = a0 + a1*t + a2*t^2 + a3*t^3
            a0 = y0_val
            a1 = vy0_val
            # 25*a2 + 125*a3 = yf - a0 - a1*tf
            # 10*a2 +  75*a3 = vyf - a1
            rhs1 = yf_val - a0 - a1 * tf          # = 1 - 10 + 10 = 1
            rhs2 = vyf_val - a1                    # = 0 + 2 = 2
            A_mat = np.array([[tf**2, tf**3], [2*tf, 3*tf**2]])
            a2, a3 = np.linalg.solve(A_mat, [rhs1, rhs2])

            def y_ref(t):
                return a0 + a1*t + a2*t**2 + a3*t**3

            def vy_ref(t):
                return a1 + 2*a2*t + 3*a3*t**2

            def ay_ref(t):
                return 2*a2 + 6*a3*t

            def f_controlled(t):
                # f de telle sorte que ay = f/M - g => f = M*(ay + g)
                force = M * (ay_ref(t) + g)
                return max(force, 0.0)  

            def f_phi(t, y):
                return np.array([f_controlled(t), 0.0])  # phi=0

            y0 = [0.0, 0.0, y0_val, vy0_val, 0.0, 0.0]
            sol = redstart_solve(t_span, y0, f_phi)

            t = np.linspace(0, 5, 1000)
            state = sol(t)
            y_sim = state[2]
            vy_sim = state[3]
            f_vals = np.array([f_controlled(ti) for ti in t])
            y_ref_vals = np.array([y_ref(ti) for ti in t])

            fig, axes = plt.subplots(1, 3, figsize=(14, 4))

            axes[0].plot(t, y_sim, label="$y(t)$ simulé", color="royalblue", lw=2)
            axes[0].plot(t, y_ref_vals, label="$y_r(t)$ de réference", color="orange",
                         ls="--", lw=1.5)
            axes[0].axhline(l / 2, color="grey", ls=":", label=r"$y = \ell/2$ (ground)")
            axes[0].set_title("Hauteur $y(t)$")
            axes[0].set_xlabel("temps $t$ (s)")
            axes[0].set_ylabel("hauteur (m)")
            axes[0].legend(fontsize=8)
            axes[0].grid(True, alpha=0.3)

            axes[1].plot(t, vy_sim, color="green", lw=2)
            axes[1].axhline(0, color="grey", ls="--")
            axes[1].set_title("Vitesse verticale $\\dot{y}$")
            axes[1].set_xlabel("temps $t$ (s)")
            axes[1].set_ylabel("vitesse $v_y(t)$ (m/s)")
            axes[1].grid(True, alpha=0.3)

            axes[2].plot(t, f_vals, color="tomato", lw=2)
            axes[2].axhline(M * g, color="grey", ls="--", label="$f = Mg$")
            axes[2].set_title("Force $f(t)$")
            axes[2].set_xlabel("temps $t$ (s)")
            axes[2].set_ylabel("force (N)")
            axes[2].legend(fontsize=8)
            axes[2].grid(True, alpha=0.3)

            fig.suptitle("Contrôle d'atterissage", fontsize=13, fontweight="bold")
            fig.tight_layout()

            final = sol(5.0)

            return fig

    controlled_landing()
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

    return (svg,)


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


@app.cell
def _(svg):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        W = x_max - x_min   # largeur de la scène en unités monde
        H = y_max - y_min   # hauteur de la scène en unités monde
        vb = f"{x_min} {-y_max} {W} {H}"

        # Arrière-plan : ciel (au-dessus du sol y=0) et sol (en-dessous de y=0)
        ciel = svg.rect(x=x_min, y=0, width=W, height=y_max,
                        fill="#87CEEB")()           # bleu ciel
        sol = svg.rect(x=x_min, y=y_min, width=W, height=(-y_min),
                       fill="#8B6914")()            # brun terreux

        # Zone d'atterrissage : 2 m de large, centrée sur (0, 0), posée sur la surface du sol
        pad_l = 2.0
        pad_h = 0.05  # fine bande
        pad = svg.rect(x=-pad_l/2, y=-pad_h, width=pad_l, height=pad_h,
                       fill="#22c55e")()           # vert vif

        # Assemblage des éléments de la scène (système de coordonnées retourné via transform sur <g>)
        elements_scene = [ciel, sol, pad] + list(objects)
        groupe_scene = svg.g(transform="scale(1,-1)")(*elements_scene)

        image = svg.svg(viewBox=vb, width="300", height=str(int(300 * H / W)), xmlns="http://www.w3.org/2000/svg")(groupe_scene)
        return str(image)

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Monde vide
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Monde avec un carré noir sur la zone d'atterrissage
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Monde avec un carré rouge en haut à gauche et un carré bleu en haut à droite
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


@app.cell
def _(M, g, l, np, svg):
    def booster(x, y, theta, f, phi):
        # Dimensions du corps du booster
        body_w = 0.15        # largeur du rectangle
        body_h = l       # hauteur totale 

        # Longueur de la flamme : proportionnelle à f ; l/2 quand f == M*g
        flame_length = (l / 2) * (f / (M * g)) if f > 0 else 0.0
        flame_w = 0.10

        # Corps du booster (centré à l'origine locale)
        body = svg.rect(
            x=-body_w / 2,
            y=-l/2,
            width=body_w,
            height=body_h,
            fill="#94a3b8",
            stroke="#475569",
            stroke_width="0.01",
            rx="0.04",
        )()

        # Cône de nez (petit triangle au sommet)
        nose_h = 0.15
        nose = svg.polygon(
            points=f"{-body_w/2},{l/2} {body_w/2},{l/2} 0,{l/2 + nose_h}",
            fill="#000000",
        )()
    
        if flame_length > 0:
            flame_rect = svg.rect(
                x=-flame_w / 2,
                y=-l/2,               # part de la base
                width=flame_w,
                height=flame_length,  # s'étend vers le bas (y négatif)
                fill="#f97316",
                opacity="0.85",
            )()
            # Rotation de la flamme de phi autour du point de base (0, -l/2)
            # phi > 0 tourne dans le sens CCW (trigo positif)
            flame_group = svg.g(transform=f"rotate({np.degrees(phi+np.pi)}, 0, {-l/2})")(flame_rect)
        else:
            flame_group = svg.g()()

        # Assemblage des parties dans le repère local, puis application position + inclinaison
        booster_group = svg.g(
            transform=f"translate({x},{y}) rotate({np.degrees(-theta)}, 0, 0)"
        )(flame_group, body, nose)

        return str(booster_group)

    return (booster,)


@app.cell
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
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 4),
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


@app.cell
def _(M, g, l, np):
    def booster_anim(x_fn, y_fn, theta_fn, f_fn, phi_fn, T, n_frames=60):
        times = np.linspace(0, T, n_frames + 1)
        dur = f"{T}s"
        key_times = ";".join(f"{t/T:.4f}" for t in times)

        # Échantillonnage de tous les paramètres à chaque keyframe
        xs     = [x_fn(t)     for t in times]
        ys     = [y_fn(t)     for t in times]
        thetas = [theta_fn(t) for t in times]
        fs     = [f_fn(t)     for t in times]
        phis   = [phi_fn(t)   for t in times]

        # Dimensions
        body_w = 0.15
        body_h = l        # hauteur totale 
        nose_h = 0.15

        # Valeurs de translation et rotation pour chaque keyframe
        translate_vals = ";".join(f"{x},{y}" for x, y in zip(xs, ys))
        # Rotation : -theta degrés (car l'axe y est retourné en SVG)
        rotate_vals = ";".join(f"{np.degrees(-th)},0,0" for th in thetas)

        # Longueur de flamme et rotation phi à chaque keyframe
        flame_lengths  = [(l / 2) * (fv / (M * g)) if fv > 0 else 0.0 for fv in fs]
        flame_len_vals = ";".join(f"{fl:.4f}" for fl in flame_lengths)
        # Rotation de la flamme autour de la base (0, -l/2)
        flame_phi_vals = ";".join(
            f"{np.degrees(pv + np.pi):.4f},0,{-l/2}"
            for pv in phis
        )

        svg_str = f"""
    <g>
      <!-- Translation de l'ensemble du booster -->
      <animateTransform attributeName="transform" type="translate"
        values="{translate_vals}" keyTimes="{key_times}"
        dur="{dur}" repeatCount="indefinite" calcMode="linear"/>
      <g>
        <!-- Rotation du booster autour de son centre de masse -->
        <animateTransform attributeName="transform" type="rotate"
          values="{rotate_vals}" keyTimes="{key_times}"
          dur="{dur}" repeatCount="indefinite" calcMode="linear"/>

        <!-- Flamme (sous la base en y local = -l/2) -->
        <g>
          <animateTransform attributeName="transform" type="rotate"
            values="{flame_phi_vals}" keyTimes="{key_times}"
            dur="{dur}" repeatCount="indefinite" calcMode="linear"/>
          <rect x="{-0.10/2}" y="{-l/2}" width="0.10" height="0" fill="#f97316" opacity="0.85">
            <animate attributeName="height"
              values="{flame_len_vals}" keyTimes="{key_times}"
              dur="{dur}" repeatCount="indefinite" calcMode="linear"/>
          </rect>
        </g>

        <!-- Corps du booster -->
        <rect x="{-body_w/2}" y="{-l/2}" width="{body_w}" height="{body_h}"
              fill="#94a3b8" stroke="#475569" stroke-width="0.01" rx="0.04"/>

        <!-- Cône de nez -->
        <polygon points="{-body_w/2},{l/2} {body_w/2},{l/2} 0,{l/2+nose_h}" fill="#ef4444"/>
      </g>
    </g>
    """
        return svg_str

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np, world):
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


@app.cell
def _(M, booster_anim, g, l, np, redstart_solve, world):
    def make_anim(y0_state, f_phi_fn, t_span=(0.0, 5.0), view=[-3, 3, -2, 12]):
        sol = redstart_solve(t_span, y0_state, f_phi_fn)
    
        # Trouver quand le booster atteint le sol
        T = t_span[1] - t_span[0]
        t_eval = np.linspace(t_span[0], t_span[1], 1000)
        y_vals = sol(t_eval)[2]
    
        # Chercher le moment où y atteint l/2 
        ground_idx = np.where(y_vals <= l/2)[0]
        if len(ground_idx) > 0:
            T = t_eval[ground_idx[0]]  # s'arrêter au premier contact avec le sol
            if T == t_span[0]:  # éviter T=0
                T = t_span[1] - t_span[0]
    
        def x_fn(t):     
            if t <= T:
                return float(sol(t)[0])
            else:
                return float(sol(T)[0])
        def y_fn(t):     
            if t <= T:
                return float(sol(t)[2])
            else:
                return float(sol(T)[2])
        def theta_fn(t): 
            if t <= T:
                return float(sol(t)[4])
            else:
                return float(sol(T)[4])
        def f_fn(t):
            if t <= T:
                return float(f_phi_fn(t, sol(t))[0])
            else:
                return 0.0  # plus de poussée après l'atterrissage
        def phi_fn(t):
            if t <= T:
                return float(f_phi_fn(t, sol(t))[1])
            else:
                return 0.0

        anim = booster_anim(x_fn, y_fn, theta_fn, f_fn, phi_fn, T=t_span[1] - t_span[0])
        return world(view, anim)

    # ── Scenario 1 : Chute libre ────────────────────────────────────────────────
    def fp1(t, y) : 
        return np.array([0.0, 0.0])
    anim1 = make_anim([0.0, 0.0, 10.0, 0.0, 0.0, 0.0], fp1)

    # ── Scenario 2 : ───────────
    def fp2(t, y): 
        return np.array([M * g, 0.0])
    anim2 = make_anim([0.0, 0.0, 10.0, 0.0, 0.0, 0.0], fp2)

    # ── Scenario 3 :  ─────────────────────────────────
    def fp3(t, y): 
        return np.array([M * g, np.pi / 8])
    anim3 = make_anim([0.0, 0.0, 10.0, 0.0, 0.0, 0.0], fp3, view=[-6, 6, -2, 12])

    # ── Scenario 4 : ───────────────────────────────────────
    tf_c = 5.0
    a0_c, a1_c = 10.0, -2.0
    yf_c = l / 2
    A_c = np.array([[tf_c**2, tf_c**3], [2*tf_c, 3*tf_c**2]])
    a2_c, a3_c = np.linalg.solve(A_c, [yf_c - a0_c - a1_c*tf_c, 0.0 - a1_c])

    def f_landing(t):
        ay = 2*a2_c + 6*a3_c*t
        return float(max(M * (ay + g), 0.0))

    def fp4(t, y): return np.array([f_landing(t), 0.0])
    anim4 = make_anim([0.0, 0.0, 10.0, -2.0, 0.0, 0.0], fp4)
    return anim1, anim2, anim3, anim4


@app.cell
def _(anim1, mo):
    #Scénario1

    mo.Html(anim1).center()
    return


@app.cell
def _(anim2, mo):
    #Scénario2

    mo.Html(anim2).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Résultat logique pour le scénario 2, car $\vec{f} + \vec{P}=\vec{0}$:.
    """)
    return


@app.cell
def _(anim3, mo):
    #Scénario3

    mo.Html(anim3).center()
    return


@app.cell
def _(anim4, mo):
    #Scénario4

    mo.Html(anim4).center()
    return


if __name__ == "__main__":
    app.run()
