# ==========================================
# Bionexis Node-2: Binding Card Structure
# Update: Reasoning Residue (Non-Narrative)
# ==========================================

class Node2BindingCard:
    def __init__(self):
        # 1. Run Identity [cite: 6, 11]
        self.run_identity = {
            "run_id": None,
            "tumor_context": None,
            "driver_context": None,
            "variant_scope": None,
            "exclusion_note": None
        }

        # 2. Node-1 Input Schema [cite: 18, 42]
        # 支援 axis / family / module / cluster 等多種輸入單元
        self.input_schema = {
            "unit_type": None,
            "members": [],
            "signal_attributes": None  # Direction / Tier / Weight / etc.
        }

        # 3. Node-1 Evidence Residue [cite: 20, 21]
        self.evidence_residue = {
            "trend_summary_ref": None,
            "anomaly_ref": None,
            "evidence_source": None
        }

        # 4. Node-2 Reasoning Frame [cite: 38, 39]
        # 定義推理邏輯結構，而非固定矩陣
        self.reasoning_frame = {
            "mode": None,              # axis-parallel / family-contrast / etc.
            "grouping_logic": None,
            "context_definition": None  # A/B/C or custom
        }

        # 5. Node-2 Execution Residue [cite: 40, 42]
        self.execution_residue = {
            "template_version": "v1.1",
            "execution_scope": None,
            "completion_status": "Logic Bound",
            "analyst_notes": None
        }

# 初始化綁定卡結構
node2_residue = Node2BindingCard()
