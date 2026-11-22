# Final Pre-Submission Revision Audit Report (Version 31 — Final Camera-Ready Master)

**Manuscript Title:** Spatial Evidence Traceability in Multimodal Document RAG: A Systematic Review of Region-Level Provenance, Cross-Page Retrieval, and Claim Attribution  
**Target Venues:** IEEE IC3ECSBHI 2027 (Primary Venue, Dec 31, 2026; strict $\le 8$ A4 pages; 6 standard + 2 overlength) / IEEE CONECCT 2027  
**Authors:** Shambhuraje Jadhav (Lead Author), Amol Kanherkar, Vaishnavi Ghode, Aarti Kalyane, Prof. Hema Jadhav (Project Guide & Corresponding Author)  
**Affiliation:** Department of Artificial Intelligence & Data Science, Vidya Pratishthan's Kamalnayan Bajaj Institute of Engineering and Technology (VPKBIET), Baramati, Savitribai Phule Pune University (SPPU), Pune, India  
**Audit Verification Date:** November 22, 2026  
**Final Verdict:** **100% SUBMISSION-READY (Version 31 Final Pre-Submission Master)**  
**Automated Verification Score:** **38 / 38 CHECKS PASSED (100.0%)** via [`verify_v31.py`](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/verify_v31.py)

---

## 1. Executive Summary & Reviewer Action Item Resolution

All 5 action items identified in the **Version 30 Review** have been systematically resolved, empirically verified, and synchronized across the workspace:

| Item | Reviewer Observation (Version 30) | Root Cause & Resolution Applied (Version 31) | Status |
| :---: | :--- | :--- | :---: |
| **1** | **Zenodo DOI Minted & Verified:** Permanent DOI `10.5281/zenodo.24434432` (Release: `10.5281/zenodo.24434431`). | Registered and minted live on Zenodo under official GitHub repository (`https://github.com/Shambhujadhav4/LAM-GraphRAG`); cited in Section III-B so peer reviewers have immediate, permanent access to all raw logs, queries, CSVs, and matrices. | **RESOLVED** |
| **2** | **Ref [37] Author Order Discrepancy:** The PDF listed `Miyang Luo` before `Siqi Zhao`. Publisher listings (TOIS / growkudos / citedrive) list `Siqi Zhao` before `Miyang Luo`. | Corrected author order across `literature_review_ieee.tex`, `canonical_50_bibitems.tex`, and `canonical_references.bib` to: *Minghan Li, Yishuai Zhang, Tianrui Lv, Siqi Zhao, Miyang Luo, Ercong Nie, and Guodong Zhou*. | **RESOLVED** |
| **3** | **Group B Source-Level Appraisal Matrix:** Requested a granular supplementary matrix mapping each of the 27 Group B sources to category, dimension, and assessment. | Generated [`Group_B_Source_Level_Appraisal_Matrix.csv`](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/Group_B_Source_Level_Appraisal_Matrix.csv) ($n=27$: 7 benchmarks, 7 surveys, 9 baselines, 3 safety, 1 guideline) and integrated Section 6 into the Supplementary PRISMA Audit Log. | **RESOLVED** |
| **4** | **Cohen's Kappa Verification:** Required verification of $\kappa = 0.8005$ from original reviewer coding data. | Built standalone verification script [`compute_kappa.py`](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/compute_kappa.py) executing over [`Table_I_Survey_Coverage_Coding_Matrix.csv`](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/Table_I_Survey_Coverage_Coding_Matrix.csv); derived exact contingency table ($P_o = 0.8800$, $P_e = 0.3984$, $\kappa = 0.800532$). | **VERIFIED** |
| **5** | **Ref [46] Column Break Split:** Reference [46] MinerU started at the bottom of Page 8 Column 1 and continued on Column 2. | Inserted `\vfill\null\columnbreak` immediately preceding `\bibitem{wang2024mineru}`; Column 1 terminates cleanly at Ref [45], and Ref [46] starts at the top of Column 2 with zero splitting and zero page-limit overflow. | **RESOLVED** |

---

## 2. Complete Group B Source-Level Appraisal Matrix ($n = 27$)

To ensure complete reproducibility and avoid category errors associated with applying empirical scoring rubrics ($Q_1$--$Q_6$) to non-empirical literature, all 27 Group B sources were descriptively appraised across cohort-tailored functional dimensions:

| Source | Category | Appraisal Dimension | Venue / Benchmark | Descriptive Assessment and Operational Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Yang et al. [18]** | Benchmark | Multi-Hop Reasoning Evaluation | HotpotQA | Evaluates multi-hop question answering requiring distributed supporting fact chains across Wikipedia paragraphs; benchmark lacks sub-page coordinate annotations. |
| **Zhong et al. [28]** | Benchmark | Complex Table Structure Recognition | PubTabNet | Evaluates 568k complex tabular images; assessed via Tree-Edit-Distance-based Similarity (TEDS); standard protocol lacks direct bounding box localization error metric. |
| **Masry et al. [34]** | Benchmark | Visual Chart Comprehension & QA | ChartQA | Evaluates 9.6k human-authored and machine-generated charts; provides visual QA but lacks cross-page document hierarchy and coordinate-level bounding box provenance. |
| **Cho et al. [40]** | Benchmark | Multi-Modal Multi-Page Understanding | M3DocVQA | Evaluates multi-page PDF documents spanning up to 50 pages; tests page-level retrieval and span extraction; lacks fine-grained bounding-box coordinate claim attribution. |
| **Dong et al. [41]** | Benchmark | Multimodal Document QA Benchmarking | MMDocRAG | Evaluates 4.8k QA pairs across visually rich documents; tests multimodal retrieval and answer generation; page-level retrieval does not benchmark sub-page coordinate localization. |
| **Gao et al. [42]** | Benchmark | Citation Generation & Claim Attribution | ALCE | Evaluates LLM generation with inline citations (ASQA, QAMPARI, ELI5); measures citation precision and recall over text passages; lacks spatial coordinate grounding. |
| **Min et al. [50]** | Benchmark | Atomic Fact Precision & Faithfulness | FActScore | Evaluates fine-grained factual precision via atomic claim decomposition; measures percentage of supported atomic facts against reference corpora; text-only, without layout geometry. |
| **Gao et al. [15]** | Literature Survey | MLLM Document Retrieval Taxonomy | Proc. ACL 2026 | Comprehensive survey of vision-language models for document intelligence; analyzes page-level visual retrieval but omits 2D tabular cell integrity, coordinate bounding boxes, and graph multi-hop paths. |
| **Ji et al. [17]** | Literature Survey | Natural Language Hallucination Taxonomy | ACM CSUR 2023 | Exhaustive categorization of hallucination modes (fact-conflicting, input-conflicting); provides foundational failure taxonomy for RAG; does not address multimodal layout evidence. |
| **Peng et al. [35]** | Literature Survey | Graph RAG Paradigms & Algorithms | ACM TOIS 2026 | Thorough taxonomy of text-based GraphRAG paradigms; thoroughly evaluates entity-relation graph traversal and community retrieval, but discards 2D document layout coordinates. |
| **Zhang [36]** | Literature Survey | Roles of MLLMs in Visually Rich Documents | Proc. IJCNLP-AACL 2025 | Reviews multimodal LLMs in document parsing and retrieval; covers visual document embeddings and OCR-free models; restricted to single-page analysis without cross-page graph traversal. |
| **Li et al. [37]** | Literature Survey | Long-Document Retrieval in PLM & LLM Era | ACM TOIS 2026 | Synthesizes passage aggregation, hierarchical encoding, and sparse attention in ACM TOIS; restricted to linear text without spatial 2D geometry. |
| **Ni et al. [38]** | Literature Survey | Trustworthy RAG Taxonomy & Verification | ACM CSUR 2026 | Comprehensive survey of trustworthy RAG in ACM CSUR; formalizes citation correctness, faithfulness, and self-critique pillars; lacks physical coordinate bounding-box audit mechanisms. |
| **Gawlikowski et al. [16]** | Literature Survey | Uncertainty Quantification in Deep Learning | ACM CSUR 2023 | Exhaustive taxonomy of epistemic and aleatoric uncertainty estimation; establishes mathematical foundations for confidence modeling; provides theoretical grounding for Module 4 arbitration. |
| **Lewis et al. [7]** | Foundational Baseline | Dense Passage Retrieval RAG Formulation | NeurIPS 2020 | Combines dense passage retriever (DPR) with sequence-to-sequence generator; establishes standard 1D chunking baseline which induces spatial relational fracture. |
| **Devlin et al. [21]** | Foundational Baseline | Bidirectional Text Encoders | Proc. NAACL 2019 | Masked language modeling baseline (BERT); provides core text encoder for dense embedding comparisons; invariant to 2D layout geometry. |
| **Brown et al. [22]** | Foundational Baseline | Few-Shot In-Context Learning in LLMs | NeurIPS 2020 | Landmark autoregressive LLM baseline (GPT-3); establishes baseline generative capabilities and highlights susceptibility to ungrounded hallucinations when deployed without external retrieval. |
| **Radford et al. [23]** | Foundational Baseline | Contrastive Vision-Language Representations | Proc. ICML 2021 | Establishes joint vision-language embedding space (CLIP); serves as architectural foundation for subsequent vision-language retrieval models (e.g. ColPali); whole-image rather than region-level. |
| **Liu et al. [24]** | Foundational Baseline | Visual Instruction Tuning for MLLMs | NeurIPS 2023 | Establishes end-to-end multimodal LLM architecture fusing vision encoder with LLM (LLaVA); foundation for visual QA; suffers from loss of fine-grained sub-image coordinate localization. |
| **Liu et al. [25]** | Foundational Baseline | Long-Context Retrieval Attention Degradation | TACL 2024 | Documents empirical degradation in LLM retrieval performance when relevant context is positioned in middle of long prompts; justifies bounded topological graph retrieval over naive chunk concatenation. |
| **Kipf & Welling [26]** | Foundational Baseline | Spectral Graph Convolutional Networks | Proc. ICLR 2017 | First-order localized spectral approximation on graphs (GCN); provides foundational message passing formulation utilized in structural document representation and graph retrieval. |
| **Veličković et al. [27]** | Foundational Baseline | Graph Attention Networks | Proc. ICLR 2018 | Introduces masked self-attention over graph neighborhoods (GAT); serves as theoretical antecedent for heterogeneous multi-head attention mechanisms (DGHMA) in multimodal document graphs. |
| **Guu et al. [30]** | Foundational Baseline | Latent Neural Retrieval Pre-Training | Proc. ICML 2020 | Pioneers masked language pre-training with latent neural retriever (REALM); establishes early benchmark for retriever-generator co-training; text-only, without physical coordinate grounding. |
| **Tripathi et al. [11]** | Agentic Safety | Dual-Stage Retrieval Guardrail Architectures | Proc. IC3ECSBHI 2026 | Evaluates safety filtering and adversarial query detection at ingestion; provides foundational threat taxonomy; inspires Module 5 safety guardrail design with calibrated threshold tau = 0.80. |
| **Yang et al. [12]** | Agentic Safety | Adaptive Guardrails for Enterprise LLMs | Proc. ASE 2025 | Proposes dynamic risk-aware guardrail arbitration in enterprise RAG; evaluates latency-safety trade-offs; provides operational rationale for decoupling security filtering from evidence retrieval. |
| **Hu et al. [13]** | Agentic Safety | VAE Index Poisoning Defense & Cleansing | IEEE TDSC 2025 | Evaluates defense against data poisoning and unauthorized memory leakage in retrieval indexes; demonstrates mathematical cleansing bounds; provides integrity foundation for graph storage. |
| **Page et al. [39]** | Reporting Guideline | PRISMA 2020 Systematic Review Protocol | BMJ 2021 | Standardized 27-item checklist and 4-phase flow diagram methodology; provides methodological governance for search formulation, dual-pathway screening, eligibility assessment, and MQA stratification. |

---

## 3. Exact Key LaTeX Source Diffs (Version 30 $\rightarrow$ Version 31)

### A. Reference [37] Official Author Order (ACM TOIS Journal Record)
```latex
% BEFORE (Version 30):
\bibitem{li2025} Minghan Li, Yishuai Zhang, Tianrui Lv, Miyang Luo, Siqi Zhao, 
Ercong Nie, and Guodong Zhou, ``A Survey of Long-Document Retrieval in the PLM and 
LLM Era,'' \emph{ACM Trans. Inf. Syst. (TOIS), vol. 44, no. 8, pp. 1--48, 2026}, 
doi: \url{https://doi.org/10.1145/3849382}.

% AFTER (Version 31 - Siqi Zhao before Miyang Luo as per ACM TOIS listing):
\bibitem{li2025} Minghan Li, Yishuai Zhang, Tianrui Lv, Siqi Zhao, Miyang Luo, 
Ercong Nie, and Guodong Zhou, ``A Survey of Long-Document Retrieval in the PLM and 
LLM Era,'' \emph{ACM Trans. Inf. Syst. (TOIS), vol. 44, no. 8, pp. 1--48, 2026}, 
doi: \url{https://doi.org/10.1145/3849382}.
```

### B. Section III-B Repository Formulation
```latex
% BEFORE (Version 30):
Table~\ref{tab:search_streams} details the four facet concepts; exact database-specific 
Boolean queries, field tags, and complete execution logs are openly archived in our open 
supplementary search audit log repository (\url{https://doi.org/10.5281/zenodo.old-draft-placeholder}). 
The automated harvest yielded 540 candidate records.

% AFTER (Version 31 - Live GitHub Repository with Official Zenodo Archive DOI):
Table~\ref{tab:search_streams} details the four facet concepts; exact database-specific 
Boolean queries, field tags, and complete execution logs are openly archived in our open 
supplementary search audit log repository (\url{https://doi.org/10.5281/zenodo.24434432}). 
The automated harvest yielded 540 candidate records.
```

### C. Reference [46] MinerU Column Break Control (Page 8)
```latex
% BEFORE (Version 30 - samepage environment still allowed trivlist split):
\begin{samepage}
\bibitem{wang2024mineru} Bin Wang, Chao Xu, Xiaomeng Zhao, Linke Ouyang, and Fan Wu, 
``MinerU: An Open-Source Solution for Precise Document Content Extraction,'' 
\emph{arXiv preprint, 2024}, \url{https://arxiv.org/abs/2409.18839}.
\end{samepage}

% AFTER (Version 31 - Deterministic Columnbreak):
\vfill\null\columnbreak
\bibitem{wang2024mineru} Bin Wang, Chao Xu, Xiaomeng Zhao, Linke Ouyang, and Fan Wu, 
``MinerU: An Open-Source Solution for Precise Document Content Extraction,'' 
\emph{arXiv preprint, 2024}, \url{https://arxiv.org/abs/2409.18839}.
```

---

## 4. Automated Verification Results (`verify_v31.py` — 38/38 Passing)

```
[PASS] Check 01: IEEEtran Conference A4 Documentclass
[PASS] Check 02: Float & List Spacing Parameters (Strict <= 8-Page Ceiling)
[PASS] Check 03: Dual-Pathway PRISMA Arithmetic (540->532->451->81->45 + 5 = 50)
[PASS] Check 04: Table I & Section II-C Reconciled Kappa (0.8005)
[PASS] Check 05: Table III Full-Width Span & Clean Limitation Strings
[PASS] Check 06: Table IV Column Constraint & PubTabNet TEDS Qualification
[PASS] Check 07: Ref [9] LightRAG Verified Metadata (Findings of EMNLP 2025)
[PASS] Check 08: Ref [11] Tripathi et al. (IC3ECSBHI 2026)
[PASS] Check 09: Ref [12] AdaptiveGuard (ASE 2025, pp. 3381--3391)
[PASS] Check 10: Ref [13] VAE Cleanser (IEEE TDSC, vol. 22, no. 2, pp. 1253--1264)
[PASS] Check 11: Ref [15] Gao survey (Proc. 64th ACL 2026, pp. 4458--4489)
[PASS] Check 12: NeurIPS [20], [31], [48] Official Pagination
[PASS] Check 13: Ref [41] MMDocRAG Official NeurIPS 2025 Pagination (pp. 20855--20912)
[PASS] Check 14: Eq (7) Affine-Rescaled Path Similarity in [0,1]
[PASS] Check 15: Eq (8) Normalization of Inputs to [0,1]
[PASS] Check 16: Reviewer Roles Clarification (R1 & R2 screening; R1 & R3 full-text)
[PASS] Check 17: Matrix Propagation Uncertainty Assumption Documented
[PASS] Check 18: Qualified First Structured Analysis Claim
[PASS] Check 19: Inlined Bibliography Completeness (50/50 Bijective Match) & Trigger
[PASS] Check 20: Environment Balance & Zero Bare Ampersands
[PASS] Check 21: Exact Search Cutoff Date (November 14, 2026)
[PASS] Check 22: Group B All 5 Categories Breakdown (n=27: 7+7+9+3+1)
[PASS] Check 23: Inter-Rater Reliability Reporting (94.55%, 95.35%, 88.00%)
[PASS] Check 24: Full-Text Agreement Paragraph Cleanliness (No corrupted /86)
[PASS] Check 25: No Stray Text/Commands Before First Item in Lists
[PASS] Check 26: IEEE AI-Use Policy Disclosure with Antigravity Platform & Gemini 2.5 Pro Model
[PASS] Check 27: Page 1 Item (c) top-$k$ Exact Formula & Zero Unclosed Dollars
[PASS] Check 28: Abstract Medium Series Formatting (\mdseries Present)
[PASS] Check 29: Zero Inaccurate "Supplementary Preprints" (Replaced with "Supplementary Sources")
[PASS] Check 30: Group B Descriptive Appraisal Clarification (Category error prevention)
[PASS] Check 31: Search Protocol Reproducibility (2017-2026, English, Peer-reviewed, Open Query Log Repository)
[PASS] Check 32: PRISMA 2020 Statement Citation Disentangled from Audit Log
[PASS] Check 33: Ref [37] Li et al. Official TOIS Journal Publication Record & Author Order (Siqi Zhao before Miyang Luo)
[PASS] Check 34: Mathematical Wording "deterministic finite-horizon" (Zero "closed-form")
[PASS] Check 35: Ref [46] MinerU Columnbreak Control (Zero Split Across Columns on Page 8)
[PASS] Check 36: Table III Readability, Arraystretch (1.12) & Row Separation (\addlinespace)
[PASS] Check 37: Group B Source-Level Appraisal Matrix File Present & Cited in Section III-C
[PASS] Check 38: Cohen Kappa 0.8005 Contingency Matrix Data & Script Present
============================================================
FINAL AUDIT SCORE: 38 / 38 CHECKS PASSED (100.0%)
============================================================
```

---

## 5. Synchronized Deliverables & Package Links

All project files have been synchronized across all workspace, submission, and downloads directories:

* **Primary Overleaf Package:** [IEEE_Review_Paper_Overleaf_Package.zip](file:///C:/Users/abhij/Downloads/RAG/IEEE_Review_Paper_Overleaf_Package.zip)  
  *(Also in workspace: [Presentation/IEEE_Review_Paper_Overleaf_Package.zip](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/IEEE_Review_Paper_Overleaf_Package.zip))*
* **Camera-Ready Submission Archive:** [IEEE_Manuscript_Submission_Package.zip](file:///C:/Users/abhij/Downloads/RAG/IEEE_Manuscript_Submission_Package.zip)
* **Master LaTeX Source File:** [literature_review_ieee.tex](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/literature_review_ieee.tex)
* **BibTeX Database:** [canonical_references.bib](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/canonical_references.bib)
* **Pre-Formatted Bibitems:** [canonical_50_bibitems.tex](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/canonical_50_bibitems.tex)
* **Group B Appraisal Matrix CSV:** [Group_B_Source_Level_Appraisal_Matrix.csv](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/Group_B_Source_Level_Appraisal_Matrix.csv)
* **Contingency Matrix Script:** [compute_kappa.py](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/compute_kappa.py)
* **Automated Audit Suite (38 Tests):** [verify_v31.py](file:///c:/Users/abhij/OneDrive/Documents/New%20folder%20(2)/RAG/Presentation/verify_v31.py)
