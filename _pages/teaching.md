---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

## Lectures and seminars

### Lecture notes

- [Ordinary Differential Equations](/files/skript_ode.pdf)
- [Bochner Spaces](/files/skript_bochner.pdf)
- [Differential Equations II/B](/files/skript_dgl2b.pdf)
- [Differential Equations III](/files/skript_dgl3.pdf)

## Supervisions

<ul class="compact-list">
{% assign teachings = site.teaching | sort: "date" | reverse %}
{% for t in teachings %}
  {% if t.role == 'supervision' %}
    <li>
      <strong><a href="{{ t.url | relative_url }}">{{ t.title }}</a></strong>
      {% if t.type %} — {{ t.type }}{% endif %}
      {% if t.venue %}<br><span style="opacity:0.9">{{ t.venue }}</span>{% endif %}
      {% if t.location %}<span style="opacity:0.9"> · {{ t.location }}</span>{% endif %}
      {% if t.date %}<span style="opacity:0.8"> · {{ t.date | date: "%Y" }}</span>{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

## Assistantships

<ul class="compact-list">
{% for t in teachings %}
  {% if t.role == 'assistance' %}
    <li>
      <strong><a href="{{ t.url | relative_url }}">{{ t.title }}</a></strong>
      {% if t.type %} — {{ t.type }}{% endif %}
      {% if t.venue %}<br><span style="opacity:0.9">{{ t.venue }}</span>{% endif %}
      {% if t.location %}<span style="opacity:0.9"> · {{ t.location }}</span>{% endif %}
      {% if t.date %}<span style="opacity:0.8"> · {{ t.date | date: "%Y" }}</span>{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

## Theses

### Supervised theses (as first or co-supervisor)

**Master’s theses**

- Rebecca Bär (2023). *Kurzzeitexistenz von Lösungen autonomer Differenzialgleichungen am Beispiel des Räuber-Beute-Modells.* University of Freiburg (co-supervisor with Dr. Susanne Knies).
- Lena Maria Kunze (2025). *A Constructive Approach to Stationary Thermo-rheological Viscous Fluid Dynamics.* TU Berlin (first supervisor).
- Kerem Dogan (2025). *Convergence analysis for a finite element approximation for the steady model for thermo-rheological fluids.* TU Berlin (first supervisor).
- Niclas Mamerow (2026). *A Crouzeix–Raviart approximation of the obstacle problem.* TU Berlin (first supervisor).

**Bachelor’s theses**

- Paul Maier (2023). *Zur Finite-Differenzen-Methode für die Transportgleichung.* TU Berlin (first supervisor).
- Stephan Frank Arndt (2023). *Finite-Differenzen-Methode für die Wellengleichung.* TU Berlin (first supervisor).
- Yannick Julian Ciomer (2024). *Finite-Differenzen-Methode mit Anwendungen auf die Wärmeleitungsgleichung.* TU Berlin (first supervisor).
- Lennart Korte (2024). *Semidiskretisierung abstrakter Gradientenflüsse.* TU Berlin (first supervisor).
- Linus Jonas (2024). *A posteriori Fehleridentitäten auf Grundlage konvexer Dualität.* TU Berlin (first supervisor).
- Majeb Hobbi (2025). *Schwache Lösbarkeit der p(x)-Laplace-Gleichung mit Dirichlet-Randbedingung.* TU Berlin (first supervisor).
- Vigan Memeti (2025). *Der Hauptsatz über pseudo-monotone Perturbationen maximal monotoner Operatoren.* TU Berlin (first supervisor).
- Lan Jing (2026). *Approximation von Sattelpunktsproblemen.* TU Berlin (first supervisor).

### Currently supervised theses (as first supervisor)

**Master’s theses**

- Joram Xylander Gmeiner. *Modelling and analysis for an optimal insulation problem with convective heat transfer.* TU Berlin.
- Valentin Emil Menno Bonjer. *Direct numerical approximation of pulsatile flows of smart fluids.* TU Berlin.
- Sophia Engelbrecht. *Modelling active microswimmers with stochastic orientation: multiplicative noise on the sphere and derivation of the Fokker–Planck equation.* TU Berlin (co-supervisor with Sebastian Heidenreich, PTB).