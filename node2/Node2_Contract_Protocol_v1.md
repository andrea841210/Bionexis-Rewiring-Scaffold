Bionexis Node-2 Contract Protocol v1 (Acting)
Module: Bionexis Node-2

Status: Acting Baseline (Not Finalized)

Source: Derived from KRAS-LUAD Reproducibility Run

Compatibility: Pan-Cancer / Agnostic

Purpose
The purpose of this protocol is to define the formal conversion of Node-1 evidence residue into a structured Node-2 reasoning packet. It serves as the authoritative interface controlling how an execution LLM (Claude) processes evidence, ensuring that reasoning remains strictly bound to Node-1 signals without narrative drift or external inference.

Contract Role
This protocol acts as the MAS-core driver, functioning as an execution contract that constrains Claude’s reasoning during the Node-2 phase. The contract explicitly prevents:

Introduction of external biological evidence.

Strategic or clinical narrative expansion.

Cross-tumor extrapolation.
Node-2 remains an evidence-bound hypothesis convergence layer.

Run Context Schema
Defines the operational boundaries based on parameters from node2_master.py:

Tumor Context: Specific malignancy environment (e.g., LUAD, CRC).

Driver Context: Primary oncogenic driver (e.g., KRAS-mut).

Variant Scope: Mutation specificity (e.g., G12C or pan-variant).

Exclusion Note: Explicit logic boundaries preventing extrapolation beyond the defined context.

Node-1 Evidence Schema
Defines units received from the Evidence Engine (MAS-G):

Input Unit Type: Signal grouping structure (Axis, Family, Module, or Cluster).

Input Members: Biological entities populating each unit (e.g., MEK, ERK, EGFR).

Signal Attributes: Qualitative descriptors (Direction, Tier, Weight) representing residue-level evidence only.

Node-2 Reasoning Frame
Defines the structural logic for processing inputs:

Reasoning Mode: Method of comparison (e.g., axis-parallel, family-contrast).

Grouping Logic: Rule for clustering or contrasting input signals.

Context Definition: Assignment logic for:

Context A: Primary dependency.

Context B: Compensatory / resistant structure.

Context C: Divergent or unresolved residue.
Reasoning may synthesize architecture-level hypotheses but must not introduce mechanistic inference.

Reasoning Register
Defines the permitted reasoning depth during execution:

Mode-R (Residue Recording): Claude records signal structure without hypothesis synthesis.

Mode-A (Architecture Hypothesis): Claude synthesizes architecture-level hypotheses from residue patterns.
Both registers remain strictly bound to Node-1 evidence.

Output Boundary
Output must remain an evidence-bound reasoning artifact. Prohibited items include:

Clinical recommendations or translational pathway proposals.

ROI or market framing.

Introduction of external evidence or cross-tumor generalization.
Node-2 stops at hypothesis architecture, not intervention design.

Expected Output
The produced Node-2 reasoning artifact contains:

Axis-wise reasoning blocks and signal clustering patterns.

Asymmetry observations and anomaly preservation.

Architecture-level hypothesis structure.
This artifact becomes the logical residue passed to Node-3.

Structural Tags
Supports the registry defined in node2_tags.py:

NOB (Narrative Ontology Binding): Tags NOB-01 through NOB-06 representing mechanistic identity and anomaly awareness.

NFB (Narrative Frame Binding): Tags NFB-01 through NFB-06.
In this phase, NFB tags remain structural placeholders only and are not activated.

Protocol Status
Current State: Acting Baseline.

Lock Status: Not yet locked into the Node-2 major task card.

Version Control: v1.0 (Derived from KRAS-LUAD reproducibility run).
