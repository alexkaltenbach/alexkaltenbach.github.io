---
layout: archive
title: "Research"
description: "Research by Alex Kaltenbach: convex duality, error control, smart fluids, parametric PDEs and scientific computing."
permalink: /research/
author_profile: true
---
My research focuses on the numerical analysis of nonlinear PDEs and nonsmooth variational problems. I combine nonlinear functional analysis, convex duality, and structure-preserving discretisation to develop reliable approximations, computable error estimates, and efficient nonlinear solvers.

## Main research areas

### Duality-based numerical methods

I use continuous and discrete convex duality to derive primal-dual error identities for *a priori* and *a posteriori* analysis, adaptive refinement, and error control for iterative solvers. My work includes explicit flux reconstructions and solvers based on semi-implicit gradient flows and prox-based semismooth Newton methods. Applications include obstacle and Signorini problems, TV minimisation, and digital twins for structural health monitoring. Current directions include subgradient flows, higher-order discretisations, PDE-constrained optimisation, and learning-enhanced iterative solvers.

### Analysis and numerics of non-Newtonian and smart fluids

I develop existence theory for nonlinear flow models and establish convergence and error estimates for finite element and discontinuous Galerkin approximations. My work includes variable-exponent and micropolar fluids, evolution equations in time-dependent energy spaces, and generalised pseudomonotonicity methods. Current research addresses fully coupled smart-fluid systems, particularly chemically reacting fluids and models of synovial lubrication.

<figure class="research-figure">
  <a href="{{ '/images/research/smart-fluids-convergence.png' | relative_url }}" aria-label="Open the smart-fluid comparison figure at full resolution">
    <img src="{{ '/images/research/smart-fluids-convergence.png' | relative_url }}" alt="Velocity profiles on the left and discretization errors under refinement on the right for a variable-exponent flow model." width="3915" height="1589" loading="lazy" decoding="async">
  </a>
  <figcaption>Finite element approximation of a variable-exponent flow model: velocity profiles (left) and errors under refinement (right). From the numerical experiments for pulsatile smart-fluid flows; <a href="https://github.com/alexkaltenbach/pulsatile-smart-fluids-code/tree/main/pLaplaceMixed">code and experiment details</a>.</figcaption>
</figure>

## Further research directions

### Optimal thermal insulation

I study the optimal distribution of a prescribed amount of insulating material around heat-conducting bodies, accounting for their geometry and convective heat exchange with the surroundings. My work combines variational analysis with finite element approximation and iterative optimisation methods.

### Neural approximation of parametric PDEs

I study neural approximations of parameter-to-solution maps and their mathematical error analysis. Building on best-approximation results and *a priori* estimates for the Deep Ritz method, current work combines variational energies with physics-informed residuals for parametric *p*-Stokes systems, including parameter-dependent material laws, forcing, and geometries.

### Quantum-hydrodynamic generative modelling

I develop PDE-based generative methods using Schrödinger dynamics and their Madelung formulation. PDE-constrained optimisation determines an initial phase so that the resulting deterministic dynamics transport a reference distribution towards a prescribed target. Current research addresses scalable phase identification, structure-preserving discretisations, and error control.

From 2027, I will serve as scientific co-lead of two [funded research projects](/third-party-funding/) on learning-enhanced iterative methods (DFG–NSFC) and duality-based error control for digital twins (MATH+).



## Selected publications

<ul class="pub-list">
{% assign selected_keys = '2024-02-09-paper,2024-07-15-paper,2025-07-30-paper,2022-07-05-paper' | split: ',' %}
{% for key in selected_keys %}
  {% assign selected_pub = site.publications | where: 'key', key | first %}
  {% if selected_pub %}{% include publication-item.html pub=selected_pub %}{% endif %}
{% endfor %}
</ul>

[All publications]({{ '/publications/' | relative_url }})

## Code & materials

- **[Pulsatile smart-fluid flows](https://github.com/alexkaltenbach/pulsatile-smart-fluids-code).** FEniCS/DOLFIN implementations, experiment runners and figures for variable-exponent flow models.
- **[p-Stokes equations with slip boundary conditions](https://github.com/alexkaltenbach/pstokes-slip-pressure-code).** Reproducibility package for the pressure-error experiments, including implementation notes and environment specifications.
- **[Quantum-hydrodynamic generative modelling](https://github.com/alexkaltenbach/qh-gem-matlab).** MATLAB implementations, reference data and scripts for reproducing the paper figures.

Lecture notes are available under [Teaching]({{ '/teaching/#lecture-notes' | relative_url }}); the four sessions of the Freiburg lecture series are linked under [Talks]({{ '/talks/#lecture-series-materials' | relative_url }}).
