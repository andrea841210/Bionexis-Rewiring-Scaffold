# ==========================================
# Bionexis Node-2: Tag Mapping Registry
# Update: Residue-Oriented Binding (v1.1)
# ==========================================

from .node2_master_v1_1 import node2_core

class BionexisTagRegistry:
    """
    將 Node-2 的推理殘跡與 Master Template v1.1 的標籤系統進行映射。
    不再生成敘事內容，僅保留結構化參數綁定。
    """
    def __init__(self, core_params):
        self.p = core_params.params
        
        # --- [Section 5] NOB: Narrative Ontology Binding ---
        # 記錄「它是什麼」：機制身分完全錨定於 Driver 與 Variant 參數 [cite: 25, 28]
        self.NOB_MAP = {
            "NOB-01": f"Pathway Identity: {self.p['driver_context']} pathway", # 
            "NOB-02": f"Mechanistic Role: Unit ({self.p['input_unit_type']}) function in {self.p['driver_context']} axis", # 
            "NOB-03": f"Mutation Class: {self.p['variant_scope']} alteration class", # 
            "NOB-04": "Functional Consequence: Axis-specific effect (Residue Only)", # 
            "NOB-05": "Evidence Boundary: Node-1 validation scope", # 
            "NOB-06": f"Anomaly Awareness: Conflict signals in {self.p['tumor_context']} context" # 
        }

        # --- [Section 6] NFB: Narrative Frame Binding ---
        # 記錄「推理結構」：僅保留戰略框架的邏輯佔位，移除報告敘事 
        self.NFB_MAP = {
            "NFB-01": f"Clinical Problem: Unmet need in {self.p['tumor_context']} (Logic Bound)", # [cite: 33]
            "NFB-02": f"Competitive Failure: {self.p['driver_context']} resistance logic", # [cite: 33]
            "NFB-03": "Mechanism-to-Outcome: Structural mapping residue", # [cite: 33]
            "NFB-04": "ROI Hypothesis: [Founder/MAS-Core Supply Only]", # [cite: 33]
            "NFB-05": f"Context Win: Tactical advantage for Context [A/B/C] in {self.p['tumor_context']}", # [cite: 33]
            "NFB-06": f"Risk Flags: Assumptions for {self.p['variant_scope']} in {self.p['tumor_context']}" # [cite: 33]
        }

# 初始化標籤註冊表
node2_tag_registry = BionexisTagRegistry(node2_core)
