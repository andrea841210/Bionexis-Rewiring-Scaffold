# Node-2 Contract — KRAS-LUAD Run-2

## 0. Contract Role

This artifact is a contract assembly layer.

It is not:
- a final scientific report
- a strategic summary
- a clinical recommendation
- a translational proposal

Its function is to bind:
- Node-1 evidence residue
- master schema
- structural tag registry

into a bounded Node-2 execution packet for Claude.

---

## A. Run Context

- Tumor Context: LUAD  
- Driver Context: KRAS-mut  
- Variant Scope: KRAS-mut vs WT comparison  
- Input Unit Type: axis  
- Run ID: Run-2  
- Contract Mode: residue-oriented / Claude-ready  

### Exclusion Note

- do not run Node-2 reasoning
- do not add biological interpretation beyond Node-1 evidence
- do not expand to Node-3
- do not convert residue into narrative claims
- preserve ambiguity where present

### Run Grammar (from master schema)

- If MEK in KRAS-mut within LUAD  
- If ERK in KRAS-mut within LUAD  
- If EGFR in KRAS-mut within LUAD  
- If FGFR in KRAS-mut within LUAD  
- If pan-HER in KRAS-mut within LUAD  

Reasoning mode:
- axis-parallel residue binding

Axis set:

- MEK  
- ERK  
- EGFR  
- FGFR  
- pan-HER  

---

# B. Node-1 Input Schema

Node-1 residue is accepted under the following locked schema.

### Source Mode
recording-only

### Scope
directional IC50 behavior only

### Comparison Basis
KRAS-mut vs WT median IC50 shift per probe

### Direction Codes

- **S** = sensitive shift  
- **R** = resistant shift  
- **M** = mixed signal across probes  
- **0** = not evaluable  

### Tier Codes

- **Tier 1** — clear directionality with strong consistency and larger median shift  
- **Tier 2** — directionality present with moderate signal  
- **Tier 3** — mixed / weak evidence  
- **Tier 0** — not evaluable  

### Accepted Fields per Axis

- axis
- direction code
- tier
- IC50 observation
- anomaly note
- evaluable probe count
- median delta residue

No mechanism inference.  
No causal claims.  
No axis expansion.

---

# C. Node-1 Evidence Residue

## LUAD Entry Grid

| Axis | Direction | Tier |
|-----|------|------|
| MEK | S | Tier 1 |
| ERK | S | Tier 2 |
| EGFR | R | Tier 1 |
| FGFR | M | Tier 3 |
| pan-HER | R | Tier 1 |

---

## Axis Residue Table

### 1. MEK

- Direction: **S**
- Tier: **1**
- Observation: 4/4 probes show lower IC50 in KRAS-mut vs WT
- Median delta: **-0.71**
- Probes: **n = 4**
- Anomaly: none (neg=4, pos=0)

---

### 2. ERK

- Direction: **S**
- Tier: **2**
- Observation: 2/2 probes show lower IC50 in KRAS-mut vs WT
- Median delta: **-0.20**
- Probes: **n = 2**
- Anomaly: none (neg=2, pos=0)

---

### 3. EGFR

- Direction: **R**
- Tier: **1**
- Observation: 4/4 probes show higher IC50 in KRAS-mut vs WT
- Median delta: **0.51**
- Probes: **n = 4**
- Anomaly: none (neg=0, pos=4)

---

### 4. FGFR

- Direction: **M**
- Tier: **3**
- Observation: probe deltas mixed
- Median delta: **0.08**
- Probes: **n = 5**
- Anomaly: mixed signals (neg=2, pos=3)

---

### 5. pan-HER

- Direction: **R**
- Tier: **1**
- Observation: 2/2 probes show higher IC50 in KRAS-mut vs WT
- Median delta: **1.14**
- Probes: **n = 2**
- Anomaly: none (neg=0, pos=2)

---

## Node-1 Residue Summary

Tier-1 axes  
- MEK (S)  
- EGFR (R)  
- pan-HER (R)

Tier-2 axis  
- ERK (S)

Tier-3 axis  
- FGFR (M)

Conflict-bearing axis  
- FGFR

---

# D. Node-2 Reasoning Frame

This section defines **the reasoning frame only**.

No reasoning execution occurs in this contract.

### Frame Type

- residue-oriented
- axis-parallel
- LUAD-bound
- Node-1 residue anchored

### Frame Input

Claude receives the following axis entries:

- MEK → Tier 1 (S)
- ERK → Tier 2 (S)
- EGFR → Tier 1 (R)
- FGFR → Tier 3 (M)
- pan-HER → Tier 1 (R)

### Frame Priority

Primary anchors  
- Tier-1 axes

Secondary anchor  
- Tier-2 axis

Conflict axis  
- Tier-3 axis

### Frame Behavior

Claude may:

- reason within axis boundaries
- compare residue patterns
- preserve anomaly signals

Claude may **not**:

- overwrite Node-1 direction codes
- collapse mixed signals
- introduce clinical claims
- extrapolate beyond LUAD
- convert IC50 signals into causal claims

---

# E. Output Boundary

Allowed output class:

- Node-2 reasoning artifact

Disallowed output class:

- clinical recommendation
- translational expansion
- market / ROI conclusion
- founder narrative
- cross-tumor generalization

Boundary rules:

- preserve recording-only residue origin
- preserve LUAD context
- preserve KRAS-mut vs WT comparison
- preserve anomaly signals
- do not introduce new external evidence

---

# F. Expected Output

Claude should return a Node-2 reasoning artifact that is:

- LUAD-bounded
- axis-structured
- residue-anchored
- ambiguity-preserving
- non-clinical
- non-translational

Minimum structure expected:

- axis-wise reasoning blocks
- explicit tier handling
- explicit FGFR ambiguity preservation
- no claim inflation

---

# G. Structural Tags

## NOB — Narrative Ontology Binding

- **NOB-01** Pathway Identity: KRAS-mut pathway  
- **NOB-02** Mechanistic Role: axis unit in KRAS network  
- **NOB-03** Mutation Class: KRAS-mut vs WT comparison  
- **NOB-04** Functional Consequence: axis effect (residue only)  
- **NOB-05** Evidence Boundary: Node-1 validation scope  
- **NOB-06** Anomaly Awareness: LUAD signal conflicts  

---

## NFB — Narrative Frame Binding

- **NFB-01** Clinical Problem: unmet need in LUAD  
- **NFB-02** Competitive Failure: KRAS resistance logic  
- **NFB-03** Mechanism-to-Outcome mapping  
- **NFB-04** ROI Hypothesis *(Founder supply only)*  
- **NFB-05** Context Win *(LUAD tactical framing)*  
- **NFB-06** Risk Flags *(KRAS-mut comparison assumptions)*  

---

# Contract Closure

This contract binds:

- Node-1 LUAD residue
- Node-2 master schema v1.1
- Node-2 tag registry

Status:

- Claude-ready
- reasoning not executed
- ambiguity preserved
- LUAD Run-2 bound
