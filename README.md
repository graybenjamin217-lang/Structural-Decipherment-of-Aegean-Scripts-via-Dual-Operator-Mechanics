# Structural Decipherment of Aegean Scripts via Dual-Operator Mechanics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23107988.svg)](https://doi.org/10.5281/zenodo.23107988)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Preprint-Open Access](https://img.shields.io/badge/Status-Preprint--Open%20Access-green.svg)](https://doi.org/10.5281/zenodo.23107988)

**Author:** Benjamin Edward Gray  
**Correspondence:** graybenjamin217@gmail.com  
**Current Preprint:** Zenodo (Version v4, November 2026)  

---

## Abstract

This repository hosts the mathematical documentation, matrix formalisms, and data specifications accompanying the paper *"Structural Decipherment of Aegean Scripts via Dual-Operator Mechanics: A Unified Framework for Phonology, Syntax, and Metrology in Cretan Hieroglyphic, Linear A, and the Phaistos Disc"*.

The framework establishes a parameter-free mathematical and metrological engine for the undeciphered Aegean script continuum by mapping sequential sign transition amplitudes onto a finite-dimensional complex Hilbert space $\mathcal{H} = \mathcal{H}_{\text{syll}} \oplus \mathcal{H}_{\text{metro}}$. It demonstrates that Cretan Hieroglyphic, Linear A, and the Phaistos Disc share an invariant agglutinative grammar governed by the fixed-point attractor dynamics of the Universal Feedback Operator $\hat{\Omega}_G$ and the discrete capacity constraints of the prime-indexed dual-dilation operator $\hat{D}_k$.

---

## Core Mathematical Framework

### 1. The Transition Feedback Operator ($\hat{\Omega}_G$) & Basin Partition Theorem
Sequential symbol co-occurrences are encoded into a regularized transition operator $\hat{A}_0 \in \mathcal{B}(\mathcal{H})$ bounded below by the invariant spectral floor $\varepsilon_0 = 1/16 = 0.0625$. The non-linear feedback operator is defined via continuous functional calculus:

$$\hat{\Omega}_G(\hat{A}) = \hat{A}^{-(\mathbf{I} - \hat{A}^{-1})}$$

The scalar transition map $f(x) = x^{-(1 - 1/x)}$ partitions conditional transition probabilities $x \in (0, 1]$ into two deterministic morphological regimes:

* **Super-Attracting Root Horizon ($x^* = 1$):**  
  Evaluating the first derivative yields $\vert{}f'(1)\vert{} = 0$. For any interior bigram with $P(\sigma_j \mid \sigma_i) > 1/2$, iterated application of $\hat{\Omega}_G$ converges quadratically to $x^* = 1$, locking invariant nominal stems and divine titles (e.g., `-SA-SA-RA-ME`, `PA-I-TO`, `KU-RO`).
* **Hyperbolic Phase-Gate Repeller ($x^* = 1/2$):**  
  Evaluating the Jacobian at $x^* = 1/2$ yields $\vert{}f'(1/2)\vert{} = 1 + 2\ln 2 \approx 2.3863 > 1$, with commutator boundary multiplier:
  $$\lambda_0^2 = (1 + 2\ln 2)^2 \approx 5.6944$$
  The repeller acts as an exact dynamical separatrix. Bigrams exhibiting morphological branching ($P(\sigma_j \mid \sigma_i) \le 1/2$, corresponding to Shannon entropy $H \ge 1\text{ bit}$) undergo off-axis phase ejection toward the spectral floor $\varepsilon_0$, automatically isolating bound prefixes (`JA-`, `I-`, `A-`) and inflectional suffixes (`-TE`, `-TI`, `-ME`).

### 2. The Prime-Indexed Dual-Dilation Operator ($\hat{D}_k$)
The operator $\hat{D}_k$ acts across the discrete epigraphic space $\mathcal{H}_{\text{syll}} \oplus \mathcal{H}_{\text{metro}} \cong (\mathbb{C}^{16} \otimes \mathbb{C}^5) \oplus \ell^2(\mathbb{Z}_p)$ using prime-indexed channels $p_k \in \{2, 3, 5\}$:

* **Phonemic CV Quantization:** Binds the open-syllable (CV) inventory to 16 consonantal onset channels and 5 cardinal vowel channels, establishing the strict core syllabic capacity limit:
  $$\dim(\mathcal{H}_{\text{CV}}) = 16 \times 5 = 80 \text{ core syllabograms}$$
* **Metrological Accounting Engine:** Generates the Linear A fractional series (Klasmatograms) from prime-reciprocal eigenvalues $\lambda_{p_k, m} = p_k^{-m}$, yielding the exact dyadic fraction series ($J = 1/2, E = 1/4, F = 1/8, K = 1/16$) and sub-unit sexagesimal divisions under global additive closure (`KU-RO` total) and orthogonal deficit (`KI-RO`) constraints.

---

## Repository Structure

```text
├── README.md                      # Core mathematical documentation & invariants
├── Minoan_Syntax_Draft_4.pdf      # Full preprint (Zenodo v4)
├── scripts/
│   └── epigraphic_tokenizer.py   # Text-matrix encoder and empirical transition builder
└── data/
    ├── linear_a_votive.txt        # GORILA libation and votive inscriptions
    └── phaistos_fields.txt        # Stamped sign token sequences (Duhoux corpus)
