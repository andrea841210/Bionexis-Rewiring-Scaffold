# Node-2 Contract Assembly
# Bionexis / KRAS–LUAD Run 2
# Bound from master schema + Node-1 input + run-specific interpretation

---

## 0. Contract Role

This artifact is a contract assembly layer.

It is not:
- a final scientific report
- a strategic summary
- a clinical recommendation
- a translational proposal

Its function is to bind:
- master schema
- Node-1 evidence
- run-specific interpretation
into a bounded Node-2 execution packet for Claude.

---

## A. Run Context

- Tumor Context: LUAD
- Driver Context: KRAS-mut
- Variant Scope: KRAS-mut vs WT comparison
- Exclusion Note:
  - no clinical recommendation
  - no ROI / market framing
  - no Node-3 translational expansion
  - no cross-tumor extrapolation unless explicitly marked as contrast only

Run grammar rendered from master schema:

- If MAPK-family contrast in KRAS-mut within LUAD
- If RTK-family contrast in KRAS-mut within LUAD
- If divergent branch signal in KRAS-mut within LUAD

---

## B. Node-1 Input Schema

### Input Unit Type
family-contrast reasoning built from axis-level Node-1 evidence

### Input Members

#### MAPK Family
- MEK
- ERK

#### RTK Family
- EGFR
- pan-HER

#### Divergent Branch
- FGFR

### Signal Attributes
Each input unit is derived from Node-1 evidence using:
- direction code: S / R / M
- tier level: 1 / 2 / 3
- directionality consistency
- distribution residue
- anomaly / mixed-signal residue where applicable

### LUAD Node-1 Pattern Summary
- MEK: Sensitive, Tier 1
- ERK: Sensitive, Tier 2
- EGFR: Resistant, Tier 1
- pan-HER: Resistant, Tier 1
- FGFR: Mixed, Tier 3

### Bound Family-Level Compression
- MAPK family: sensitivity-weighted dominant branch
- RTK family: resistance-weighted contrasting branch
- FGFR: divergent / non-stable residue branch

---

## C. Node-1 Evidence Residue

### Trend Summary
Within LUAD:
- MAPK-side probes show a sensitivity trend in KRAS-mut context
- RTK-side probes show a resistance trend in KRAS-mut context
- FGFR-side probes do not form a stable directional branch

### Residue Compression
This run should be interpreted as:
- a relatively clean contrast between MAPK-family sensitivity and RTK-family resistance
- with FGFR retained only as a divergent residue, not as a primary anchor

### Anomaly / Conflict Note
- ERK is weaker than MEK and should not be over-promoted beyond Tier-2 support
- FGFR remains mixed and should not be forced into a dominant or compensatory role
- Claude must preserve this asymmetry and not flatten all branches into equal-confidence mechanisms

### Source Note
All reasoning must remain bound to Node-1 direction / tier / distribution residue only.
No new evidence source may be introduced inside this contract.

---

## D. Node-2 Reasoning Frame

### Reasoning Mode
family-contrast

### Grouping Logic
- Family A: MAPK family
  - MEK
  - ERK
- Family B: RTK family
  - EGFR
  - pan-HER
- Residual Branch:
  - FGFR

### Context Definition
This run uses LUAD-specific rewiring comparison logic.

Interpretive framing:
- Context A = MAPK active-state candidate
- Context B = RTK compensatory architecture candidate
- Context C = divergent / residual branch logic

Important:
These are interpretive context labels derived from Node-1 topology.
They are not asserted mechanisms or experimental results.

### Core Comparison Question
Claude should reason only within this contrast:

How should LUAD KRAS-mut Node-1 topology be structurally interpreted when:
- MAPK-family signal trends toward sensitivity
- RTK-family signal trends toward resistance
- FGFR remains mixed / weak / non-stable

---

## E. Output Boundary for Claude

Claude must:
- generate only Node-2 hypothesis structure
- remain within rewiring logic
- remain at architecture level, not final mechanistic conclusion
- avoid clinical recommendation
- avoid drug selection advice
- avoid market / ROI framing
- avoid Node-3 translational language
- avoid outcome assertion
- avoid writing as if the mechanism is already proven

Claude must not:
- introduce new pathways outside the bound family frame unless explicitly marked as speculative edge residue
- convert Node-1 directionality directly into biological fact
- flatten mixed residue into a stable branch
- escalate this artifact into proposal / strategy / treatment narrative

---

## F. Expected Output Type

Claude is allowed to return:

1. Structural hypotheses
   - family-level rewiring models
   - branch-priority contrasts
   - dominant-vs-compensatory logic

2. Rewiring contrasts
   - MAPK-family dominant-state candidate
   - RTK-family compensatory / insulated-state candidate
   - FGFR residual / unstable branch candidate

3. Candidate proxy directions
   - directionally testable contrasts
   - logic-level divergence
   - branch-shift possibilities
   - architecture-level conditional comparisons

4. Experimental suggestion layer
   - allowed only if still within Node-2 boundary
   - must remain as drylab / hypothesis-supporting suggestion
   - must not become Node-3 actionable pathway design

Claude is not allowed to return:
- final therapeutic claims
- translational prioritization
- product strategy
- market positioning
- clinical sequencing claims

---

## G. Optional Structural Tag Frame
### NOB-Oriented Binding
- NOB-01 Pathway Identity:
  - KRAS-related signaling contrast within LUAD
- NOB-02 Mechanistic Role:
  - family-level branch function under LUAD KRAS-mut context
- NOB-03 Mutation / Alteration Class:
  - KRAS-mut alteration class
- NOB-04 Functional Consequence:
  - axis-specific residue only
- NOB-05 Evidence Boundary:
  - Node-1 validation scope only
- NOB-06 Anomaly Awareness:
  - ERK weaker support than MEK; FGFR mixed residue

### NFB-Oriented Binding
- NFB should remain inert / minimally interpreted in this run
- do not expand into strategic or clinical narrative
- use only as structural placeholders if required by template

---

## H. Final Instruction to Claude

Read this contract as a bounded execution packet.

You are not generating a polished report.
You are not inventing the task.
You are not extending to Node-3.

You are asked only to:
- interpret LUAD Node-1 family-level topology
- generate bounded Node-2 rewiring hypotheses
- preserve asymmetry between strong, moderate, and mixed branches
- keep all output within architecture-level reasoning
