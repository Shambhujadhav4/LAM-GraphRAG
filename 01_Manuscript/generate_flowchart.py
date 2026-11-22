import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

# High-DPI canvas matching 3600 x 2640 publication dimensions
fig_w, fig_h = 12.0, 8.8
fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('white')

font_family = 'Segoe UI'

# --- 1. HEADER ---
ax.text(50, 96.2, "LAM-GraphRAG: System Architecture & Evidence Lifecycle Workflow",
        fontsize=20.0, fontweight='bold', ha='center', va='center',
        color='#0F172A', fontname=font_family)

ax.text(50, 93.0, "Layout-Aware Parsing, Hierarchical Pseudo-Graph Indexing, Multi-Metric Arbitration & Claim Attribution",
        fontsize=11.0, fontweight='normal', ha='center', va='center',
        color='#64748B', fontname=font_family)

# Horizontal divider
ax.plot([5.0, 95.0], [90.5, 90.5], color='#CBD5E1', lw=1.2)

# --- 2. CARD SPECIFICATIONS ---
# Cards layout: 3 rows x 3 columns
w, h = 26.0, 18.0
x_cols = [4.5, 37.0, 69.5]
y_rows = [68.0, 39.0, 10.0]

cards = {
    # Row 1
    'ingestion': {
        'x': x_cols[0], 'y': y_rows[0],
        'border': '#1D4ED8', 'bg': '#EFF6FF', 'badge_bg': '#1D4ED8',
        'badge': 'INPUT INGESTION',
        'title': 'Enterprise Inputs\n(PDFs, Tables & Charts)',
        'title_size': 12.0
    },
    'stage0': {
        'x': x_cols[1], 'y': y_rows[0],
        'border': '#D97706', 'bg': '#FFFBEB', 'badge_bg': '#B45309',
        'badge': 'STAGE 0: PERIMETER',
        'title': 'Stage 0:\nPerimeter Security &\nQuery Sanitization',
        'title_size': 12.0
    },
    'quarantine': {
        'x': x_cols[2], 'y': y_rows[0],
        'border': '#DC2626', 'bg': '#FEF2F2', 'badge_bg': '#B91C1C',
        'badge': 'FLAG FOR REVIEW',
        'title': 'Adversarial Review\n& Quarantine',
        'title_size': 12.0
    },
    # Row 2
    'stage1': {
        'x': x_cols[0], 'y': y_rows[1],
        'border': '#7C3AED', 'bg': '#F5F3FF', 'badge_bg': '#6D28D9',
        'badge': 'MODULE 1: LAYOUT PARSER',
        'title': 'Module 1:\nLayout-Aware Parsing\n(Text, 2D Grids, VLMs)',
        'title_size': 11.5
    },
    'stage2': {
        'x': x_cols[1], 'y': y_rows[1],
        'border': '#0284C7', 'bg': '#F0F9FF', 'badge_bg': '#0369A1',
        'badge': 'MODULE 2: PSEUDO-GRAPH',
        'title': 'Module 2:\nMultimodal Pseudo-Graph\nIndexing (Topic-Route-Fact)',
        'title_size': 11.5
    },
    'stage3': {
        'x': x_cols[2], 'y': y_rows[1],
        'border': '#DB2777', 'bg': '#FDF2F8', 'badge_bg': '#BE185D',
        'badge': 'MODULE 3: APs & MATRIX WALK',
        'title': 'Module 3:\nAnswer Point Decomposition\n& Matrix Propagation',
        'title_size': 11.5
    },
    # Row 3 (Traversal flows right-to-left: Module 4 -> Module 5 -> Release)
    'stage4': {
        'x': x_cols[2], 'y': y_rows[2],
        'border': '#EA580C', 'bg': '#FFF7ED', 'badge_bg': '#C2410C',
        'badge': 'MODULE 4: ARBITRATION',
        'title': 'Module 4:\nUncertainty & Multi-Metric\nEvidence Arbitration',
        'title_size': 11.5
    },
    'stage5': {
        'x': x_cols[1], 'y': y_rows[2],
        'border': '#0D9488', 'bg': '#F0FDFA', 'badge_bg': '#0F766E',
        'badge': 'MODULE 5: VERIFICATION',
        'title': 'Module 5:\nClaim Attribution, Proof\nSubgraphs & Guarded Release',
        'title_size': 11.5
    },
    'release': {
        'x': x_cols[0], 'y': y_rows[2],
        'border': '#16A34A', 'bg': '#F0FDF4', 'badge_bg': '#15803D',
        'badge': 'AUDITED RELEASE',
        'title': 'Grounded Answer &\nSpatial Bounding Boxes\n[x0, y0, x1, y1, p]',
        'title_size': 11.5
    }
}

# --- 3. DRAW CARDS ---
for key, c in cards.items():
    # Outer box
    box = FancyBboxPatch((c['x'], c['y']), w, h,
                         boxstyle="round,pad=0,rounding_size=2.0",
                         ec=c['border'], fc=c['bg'], lw=2.2, zorder=2)
    ax.add_patch(box)
    
    # Header badge pill
    bw, bh = w * 0.85, 2.5
    bx = c['x'] + (w - bw) / 2
    by = c['y'] + h - bh - 1.2
    badge_patch = FancyBboxPatch((bx, by), bw, bh,
                                 boxstyle="round,pad=0,rounding_size=1.2",
                                 ec=c['badge_bg'], fc=c['badge_bg'], lw=1.0, zorder=3)
    ax.add_patch(badge_patch)
    
    # Badge text
    ax.text(bx + bw / 2, by + bh / 2, c['badge'],
            fontsize=7.8, fontweight='bold', color='white',
            ha='center', va='center', fontname=font_family, zorder=4)
    
    # Card main title text
    text_y = c['y'] + (h - bh - 1.2) / 2
    ax.text(c['x'] + w / 2, text_y, c['title'],
            fontsize=c['title_size'], fontweight='bold', color=c['border'],
            ha='center', va='center', fontname=font_family, linespacing=1.30, zorder=4)

# --- 4. CONNECTING LINES & PILL LABELS ---
def draw_pill_label(x, y, text, border_color='#94A3B8'):
    pw = len(text) * 0.44 + 1.2
    ph = 2.1
    px = x - pw / 2
    py = y - ph / 2
    pill = FancyBboxPatch((px, py), pw, ph,
                          boxstyle="round,pad=0,rounding_size=0.8",
                          ec=border_color, fc='white', lw=1.1, zorder=6)
    ax.add_patch(pill)
    ax.text(x, y, text, fontsize=7.2, fontweight='bold',
            color='#1E293B', ha='center', va='center',
            fontname=font_family, zorder=7)

arrow_props = dict(color='#0F172A', lw=2.0, zorder=1)

# Connection 1: Ingestion -> Stage 0 (Horizontal)
ax.plot([cards['ingestion']['x'] + w, cards['stage0']['x']],
        [cards['ingestion']['y'] + h * 0.72, cards['stage0']['y'] + h * 0.72], **arrow_props)
draw_pill_label((cards['ingestion']['x'] + w + cards['stage0']['x']) / 2,
                cards['ingestion']['y'] + h * 0.72, "User Query", '#1D4ED8')

# Connection 2: Ingestion -> Module 1 (Vertical)
ax.plot([cards['ingestion']['x'] + w * 0.5, cards['stage1']['x'] + w * 0.5],
        [cards['ingestion']['y'], cards['stage1']['y'] + h], **arrow_props)
draw_pill_label(cards['ingestion']['x'] + w * 0.5,
                (cards['ingestion']['y'] + cards['stage1']['y'] + h) / 2, "Doc Stream", '#7C3AED')

# Connection 3: Stage 0 -> Quarantine (Horizontal)
ax.plot([cards['stage0']['x'] + w, cards['quarantine']['x']],
        [cards['stage0']['y'] + h * 0.72, cards['quarantine']['y'] + h * 0.72], **arrow_props)
draw_pill_label((cards['stage0']['x'] + w + cards['quarantine']['x']) / 2,
                cards['stage0']['y'] + h * 0.72, r"Flagged ($\tau > 0.80$)", '#DC2626')

# Connection 4: Stage 0 -> Module 2 (Vertical)
ax.plot([cards['stage0']['x'] + w * 0.5, cards['stage2']['x'] + w * 0.5],
        [cards['stage0']['y'], cards['stage2']['y'] + h], **arrow_props)
draw_pill_label(cards['stage0']['x'] + w * 0.5,
                (cards['stage0']['y'] + cards['stage2']['y'] + h) / 2, "Sanitized Query", '#0284C7')

# Connection 5: Module 1 -> Module 2 (Horizontal)
ax.plot([cards['stage1']['x'] + w, cards['stage2']['x']],
        [cards['stage1']['y'] + h * 0.5, cards['stage2']['y'] + h * 0.5], **arrow_props)
draw_pill_label((cards['stage1']['x'] + w + cards['stage2']['x']) / 2,
                cards['stage1']['y'] + h * 0.5, "2D Grids & FIIs", '#0284C7')

# Connection 6: Module 2 -> Module 3 (Horizontal)
ax.plot([cards['stage2']['x'] + w, cards['stage3']['x']],
        [cards['stage2']['y'] + h * 0.5, cards['stage3']['y'] + h * 0.5], **arrow_props)
draw_pill_label((cards['stage2']['x'] + w + cards['stage3']['x']) / 2,
                cards['stage2']['y'] + h * 0.5, "Pseudo-Graph", '#DB2777')

# Connection 7: Module 3 -> Module 4 (Vertical)
ax.plot([cards['stage3']['x'] + w * 0.5, cards['stage4']['x'] + w * 0.5],
        [cards['stage3']['y'], cards['stage4']['y'] + h], **arrow_props)
draw_pill_label(cards['stage3']['x'] + w * 0.5,
                (cards['stage3']['y'] + cards['stage4']['y'] + h) / 2, "Candidate Paths", '#EA580C')

# Connection 8: Module 4 -> Module 5 (Horizontal, moving left)
ax.plot([cards['stage4']['x'], cards['stage5']['x'] + w],
        [cards['stage4']['y'] + h * 0.5, cards['stage5']['y'] + h * 0.5], **arrow_props)
draw_pill_label((cards['stage4']['x'] + cards['stage5']['x'] + w) / 2,
                cards['stage4']['y'] + h * 0.5, "Arbitrated Evidence", '#0D9488')

# Connection 9: Module 5 -> Release (Horizontal, moving left)
ax.plot([cards['stage5']['x'], cards['release']['x'] + w],
        [cards['stage5']['y'] + h * 0.5, cards['release']['y'] + h * 0.5], **arrow_props)
draw_pill_label((cards['stage5']['x'] + cards['release']['x'] + w) / 2,
                cards['stage5']['y'] + h * 0.5, "Attributed Release", '#16A34A')

# --- 5. FOOTER BANNER ---
ax.text(50, 4.0, "Flag queries for review when similarity to known adversarial patterns exceeds the illustrative threshold \u03c4 = 0.80, subject to empirical calibration.",
        fontsize=8.8, fontstyle='italic', ha='center', va='center',
        color='#475569', fontname=font_family)

plt.tight_layout()
plt.savefig('rag_pipeline_flowchart.png', dpi=300, bbox_inches='tight', pad_inches=0.10)
print("Updated Version 20 flowchart generated successfully as rag_pipeline_flowchart.png")
