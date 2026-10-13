# Structural Decipherment of Aegean Scripts via Dual-Operator Mechanics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23107988.svg)](https://doi.org/10.5281/zenodo.23107988)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Preprint--Open%20Access-success)](https://doi.org/10.5281/zenodo.23107988)

**Author:** Benjamin Edward Gray  
**Correspondence:** `graybenjamin217@gmail.com`  
**Published:** October 2026 (Zenodo Version v3)

---

## Abstract

This repository hosts the computational models, matrix formalisms, and analytical scripts accompanying the paper *"Structural Decipherment of Aegean Scripts via Dual-Operator Mechanics: A Unified Framework for Phonology, Syntax, and Metrology in Cretan Hieroglyphic, Linear A, and the Phaistos Disc"*. 

The framework establishes a mathematically rigorous linguistic and metrological engine for the undeciphered Aegean script continuum by mapping character co-occurrence probabilities onto a complex Hilbert space $\mathcal{H}$. It proves that Cretan Hieroglyphic, Linear A, and the Phaistos Disc share an identical agglutinative grammar characterized by open-syllable (CV) phonology, invariant nominal stems locked into a super-attracting unity horizon ($x^* = 1$), and detachable inflectional affixes isolated at a hyperbolic repeller boundary ($x^* = 1/2$).

---

## Core Mathematical Framework

### 1. The Transition Operator & Attractor Dynamics
The dynamic transition operator $\hat{\Omega}_G$ governs morphological boundaries via continuous functional calculus:
$$\hat{\Omega}_G(\hat{A}) = \hat{A}^{-(\mathbf{I} - \hat{A}^{-1})}$$
* **Identity Attractor ($x^* = 1$):** Stable fixed point ($\vert{}f'(1)\vert{} = 0$) representing invariant lexical roots and divine titles across contexts.
* **Phase-Gate Repeller ($x^* = 1/2$):** Hyperbolic repeller ($\vert{}f'(1/2)\vert{} \approx 2.386 > 1$) with a commutator boundary multiplier $\lambda_0^2 = (2\ln 2 + 1)^2 \approx 5.6946$, cleanly isolating detachable prefixes and suffixes.

### 2. The Prime-Indexed Dual-Dilation Operator ($\hat{D}_k$)
Operating over the continuous-discrete state space $L^2(\mathbb{R}^4) \otimes \mathbb{C}^{16}$, the operator utilizes prime channels $p_k \in \{2, 3, 5, 7, 11, \dots\}$ to quantize continuous acoustic variables into discrete topological states, serving as a strict capacity limit for the script's syllabic grid and metrological accounting framework.

---

## Repository Structure

```text
├── README.md                          # Repository documentation
├── Minoan_Syntax_Draft_3.pdf            # Full peer-review ready preprint (Zenodo v3)
└── scripts/
    └── epigraphic_analyzer.py         # Hilbert space bigram & entropy calculation engine
```

---

```text
@misc{gray2026aegean,
  author       = {Gray, Benjamin Edward},
  title        = {Structural Decipherment of Aegean Scripts via Dual-Operator Mechanics: A Unified Framework for Phonology, Syntax, and Metrology in Cretan Hieroglyphic, Linear A, and the Phaistos Disc},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v3},
  doi          = {10.5281/zenodo.23107988},
  url          = {[https://doi.org/10.5281/zenodo.23107988](https://doi.org/10.5281/zenodo.23107988)}
```

---
