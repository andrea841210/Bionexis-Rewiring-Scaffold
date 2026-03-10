# ==========================================
# Bionexis Node-2: Tag Mapping Registry
# Update: Residue-Oriented Binding (v1.1)
# ==========================================

from .node2_master_v1_1 import node2_core

class BionexisTagRegistry:
    """
    Maps Node-2 reasoning residue to the Master Template v1.1 tag system.
    Strictly preserves structured parameter binding; does not generate narrative content.
    """
    def __init__(self, core_params):
        self.p = core_params.params
        
        # --- [Section 5] NOB: Narrative Ontology Binding ---
        # Identity: Anchored strictly to Driver and Variant parameters
        self.NOB_MAP = {
            "NOB-01": f"Pathway Identity: {self.p['driver_context']} pathway",
            "NOB-02": f"Mechanistic Role: Unit ({self.p['input_unit_type']}) function in {self.p['driver_context']} axis",
            "NOB-03": f"Mutation Class: {self.p['variant_scope']} alteration class",
            "NOB-04": "Functional Consequence: Axis-specific effect (Residue Only)",
            "NOB-05": "Evidence Boundary: Node-1 validation scope",
            "NOB-06": f"Anomaly Awareness: Conflict signals in {self.p['tumor_context']} context"
        }

        # --- [Section 6] NFB: Narrative Frame Binding ---
        # Structure: Preserves strategic frame placeholders; removes report-style narrative
        self.NFB_MAP = {
            "NFB-01": f"Clinical Problem: Unmet need in {self.p['tumor_context']} (Logic Bound)",
            "NFB-02": f"Competitive Failure: {self.p['driver_context']} resistance logic",
            "NFB-03": "Mechanism-to-Outcome: Structural mapping residue",
            "NFB-04": "ROI Hypothesis: [Founder/MAS-Core Supply Only]",
            "NFB-05": f"Context Win: Tactical advantage for Context [A/B/C] in {self.p['tumor_context']}",
            "NFB-06": f"Risk Flags: Assumptions for {self.p['variant_scope']} in {self.p['tumor_context']}"
        }

# Tag Registry Initialization
node2_tag_registry = BionexisTagRegistry(node2_core)
