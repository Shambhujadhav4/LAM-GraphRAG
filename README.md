# LAM-GraphRAG IEEE Review: Modular Research & Manuscript System

[![DOI](https://zenodo.org/badge/1467228249.svg)](https://doi.org/10.5281/zenodo.24434431)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Shambhujadhav4/LAM-GraphRAG)

**Title:** Spatial Evidence Traceability in Multimodal Document RAG: A Systematic Review of Region-Level Provenance, Cross-Page Retrieval, and Claim Attribution  
**Lead Author:** Shambhuraje Jadhav (`shambhuraje.jadhav.aids.2023@vpkbiet.org`)  
**Co-Authors:**  
- Amol Kanherkar (`amol.kanherkar.aids.2023@vpkbiet.org`)  
- Vaishnavi Ghode (`vaishnavi.ghode.aids.2023@vpkbiet.org`)  
- Aarti Kalyane (`aarti.kalyane.aids.2023@vpkbiet.org`)  
- Prof. Hema Jadhav (Project Guide & Corresponding Author, `hema.jadhav@vpkbiet.org`)  
**Institution:** Department of Artificial Intelligence & Data Science, Vidya Pratishthan's Kamalnayan Bajaj Institute of Engineering and Technology (VPKBIET), Baramati, SPPU, Pune, India  
**Archived Zenodo DOI:** [`10.5281/zenodo.24434432`](https://doi.org/10.5281/zenodo.24434432) (Release Snapshot: [`10.5281/zenodo.24434431`](https://doi.org/10.5281/zenodo.24434431))  
**Official Public Repository:** `https://github.com/Shambhujadhav4/LAM-GraphRAG`  
**Target Venue:** IEEE IC3ECSBHI 2027 (Dec 31, 2026; 6+2 pages) / IEEE CONECCT 2027  
**Status:** **Submission-Ready (Version 31 Verified Master)**

---

## 1. Two-Workstream Architecture

To prevent repeatedly redesigning and compiling the PDF whenever experimental datasets or search logs are updated, this project was decoupled into two independent workstreams:

```
┌────────────────────────────────────────┐       ┌────────────────────────────────────────┐
│     WORKSTREAM A: IEEE MANUSCRIPT      │       │     WORKSTREAM B: RESEARCH DATA        │
│  (Structure, Formatting, Stable Tech)  │       │   (Literature, Matrices, PRISMA)       │
├────────────────────────────────────────┤       ├────────────────────────────────────────┤
│ • IEEE double-column LaTeX template    │       │ • Verify 50 canonical references       │
│ • Title, Authors, Affiliations         │       │ • Classify core vs supporting papers   │
│ • Section I: Introduction & Problem    │       │ • Genuine database search & screening  │
│ • Section II: Background & Lifecycle   │       │ • Benchmark metrics & quality appraisal│
│ • Section III: Review Methodology      │       │ • Inter-rater reliability (κ) calc     │
│ • Section IV: Spatial Extraction (RQ1) │       │ • Finalize comparative matrices        │
│ • Section V: Graph Reasoning (RQ2,RQ3) │       │                                        │
│ • Section VI: Benchmark Audit (RQ4)    │       │                                        │
│ • Section VII: Challenges & LAM-Graph  │       │                                        │
│ • Section VIII: Conclusion             │       │                                        │
└───────────────────┬────────────────────┘       └───────────────────┬────────────────────┘
                    │                                                │
                    └───────────────────────┬────────────────────────┘
                                            ▼
                        ┌────────────────────────────────────────┐
                        │       FINAL SYNTHESIZED PACKAGE        │
                        │   (100% Concordance, Bijective Cites)   │
                        └────────────────────────────────────────┘
```

---

## 2. Directory Structure

```
LAM-GraphRAG-IEEE-Review/
│
├── 01_Manuscript/
│   ├── literature_review_ieee.tex              # Master IEEE conference manuscript (473 lines, 4,698 words)
│   ├── canonical_50_bibitems.tex               # Verified IEEE \bibitem definitions (50 entries)
│   ├── canonical_references.bib                # Standard BibTeX file for all 50 references
│   ├── rag_pipeline_flowchart.png              # High-DPI LAM-GraphRAG architecture diagram
│   ├── figures/                                # Graphic figures subdirectory
│   ├── IEEE_Manuscript_Submission_Package.zip  # Turnkey Overleaf upload package
│   └── IEEE_Manuscript_Template_v1.zip         # Template release bundle
│
├── 02_Literature/
│   ├── Verified_References.csv                 # 50 verified publications with full metadata
│   ├── Survey_Comparison.csv                   # 25-cell Table I survey comparison matrix (κ = 0.80)
│   ├── LITERATURE_VERIFICATION_REPORT.md       # Comprehensive publisher registry verification report
│   └── Core_Papers/                            # Technical profiles of 23 core empirical systems
│
├── 03_Research_Data/
│   ├── Evidence_Extraction.csv                 # Detailed 42-column extraction matrix (50 studies)
│   ├── Quality_Appraisal.csv                   # Stratified MQA scores (Q1–Q6)
│   ├── Screening_Decisions.csv                 # 86 full-text eligibility decisions (κ = 0.90)
│   ├── Table_II_Core_Systems_Matrix.csv        # 23 core primary empirical systems taxonomy
│   ├── Table_III_Benchmark_Audit_Matrix.csv    # 9 benchmarks audited across decoupled dimensions
│   ├── COMPARATIVE_ANALYSIS_REPORT.md          # Comprehensive comparative synthesis of Tables I, II, III
│   └── Search_Exports/                         # Harvested records (540 raw, 532 unique)
│
├── 04_PRISMA/
│   ├── Search_Log.md                           # Systematic search queries, stream yields, and protocol
│   └── Screening_Log.csv                       # Title & abstract screening decisions (532 records, κ = 0.81)
│
└── 05_Submission/
    └── Submission_Checklist.md                 # Submission portal copy-paste fields & IEEE AI disclosure
```

---

## 3. Implementation Roadmap Status

| Phase | Main Task | Status | Output Deliverable |
| :--- | :--- | :---: | :--- |
| **Phase 1** | **IEEE Template & Stable Manuscript Sections** | **COMPLETED** | `01_Manuscript/literature_review_ieee.tex` (Template v1.0) |
| **Phase 2** | **Verify Existing 50 Sources & Classify** | **COMPLETED** | `02_Literature/Verified_References.csv` & Verification Report |
| **Phase 3** | **Genuine Literature Search & Screening** | **COMPLETED** | `03_Research_Data/Search_Exports/` & `04_PRISMA/` |
| **Phase 4** | **Comparative Analysis & Benchmark Validation**| **COMPLETED** | `Table II` (23 Systems) & `Table III` (9 Benchmarks) Matrices |
| **Phase 5** | **Merge Validated Evidence into Manuscript** | **COMPLETED** | Merged `literature_review_ieee.tex` with 100% Numeric Concordance |
| **Phase 6** | **Final Formatting & Submission Checks** | **COMPLETED** | `IEEE_Manuscript_Submission_Package.zip` & Turnkey Portal Kit |

---

## 4. Key PRISMA Quantitative Yields (Concordance Verification)

- **Identification:** 540 candidate records harvested across 4 targeted streams (Crossref & arXiv APIs).
- **Deduplication:** 532 unique records (8 duplicates removed via title/DOI hash).
- **Title/Abstract Screening:** 532 screened $\to$ 446 excluded across Scope 1–4 $\to$ 86 passed (Agreement: 94.55%, $\kappa = 0.81$).
- **Full-Text Eligibility:** 86 assessed $\to$ 36 excluded across E1–E4 $\to$ 50 included (Agreement: 95.35%, $\kappa = 0.90$).
- **Evidence Synthesis:** 50 studies = 23 Core Primary Empirical Systems (Group A) + 27 Supporting Literature Sources (Group B).
- **Citation Bijection:** 50 out of 50 citations cited in `.tex` and defined in `.bib` and `canonical_50_bibitems.tex` (100% match).
