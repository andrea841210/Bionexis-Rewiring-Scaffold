# ==========================================
# Bionexis Node-2: Tag Mapping Registry
# NOB (Ontology) & NFB (Frame) Implementation
# ==========================================

from .node2_master_v1_1 import node2_core

class BionexisTagRegistry:
    def __init__(self, core_params):
        self.p = core_params.params
        
        # --- [Section 5] NOB: Narrative Ontology Binding ---
        # 定義「它是什麼」：機制身分錨定於 Driver Context
        self.NOB_MAP = {
            "NOB-01": "Pathway Identity: (Driver Context) pathway",
            "NOB-02": f"Mechanistic Role: Function of {self.p['driver_context']} axis",
            "NOB-03": f"Mutation Class: {self.p['variant_scope']} alteration",
            "NOB-04": "Functional Consequence: Axis-specific effect",
            "NOB-05": "Evidence Boundary: Pre-clinical validation scope",
            "NOB-06": f"Anomaly Awareness: Conflicting signals in {self.p['tumor_context']}"
        }

        # --- [Section 6] NFB: Narrative Frame Binding ---
        # 定義「為什麼重要」：戰略價值錨定於 Tumor + Driver Context
        self.NFB_MAP = {
            "NFB-01": f"Clinical Problem: Unmet need in {self.p['tumor_context']} driven by {self.p['driver_context']}",
            "NFB-02": f"Competitive Failure: Why existing approaches fail against {self.p['driver_context']}",
            "NFB-03": "Mechanism-to-Outcome: Clinical outcome mapping",
            "NFB-04": "ROI Hypothesis: Strategic value argument",
            "NFB-05": f"Context Win: Tactical advantage within {self.p['tumor_context']}",
            "NFB-06": "Risk Flags: Strategic assumptions requiring validation"
        }

# 此檔案目前為架構存檔，當參數從 None 轉變為具體數值時，這些標籤將自動填滿。
