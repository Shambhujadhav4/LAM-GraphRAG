# Comprehensive Comparative Analysis & Research Matrices Report (Phase 4)
## Systematic Review: "Spatial Evidence Traceability in Multimodal Document RAG"

**Authors:** Amol Kanherkar, Vaishnavi Ghode, Shambhuraje Jadhav, Aarti Kalyane, Hema Jadhav  
**Affiliation:** Department of Artificial Intelligence & Data Science, VPKBIET Baramati, SPPU, Pune, India  
**Date:** November 20, 2026  
**Status:** **Phase 4 Final Comparative Analysis Completed**  

---

## 1. Executive Synthesis

This report provides the finalized comparative research matrices synthesized across the 50 included literature sources. It bridges the research gaps identified in existing literature surveys (Table I), analyzes the technological paradigms of the 23 core empirical systems (Table II), and exposes the evaluation void across multimodal document benchmarks (Table III).

---

## 2. Table I: Survey Coverage Matrix (Evidence Lifecycle Stages)

The 25 double-coded cells evaluate how existing literature surveys address the **Five-Stage Evidence Lifecycle Framework**:
- $\mathcal{S}_1$: Original Evidence Layer (2D tables, layouts, charts)
- $\mathcal{S}_2$: Perception & Extraction Layer (OCR, bounding boxes, table segmentation)
- $\mathcal{S}_3$: Coordinate Indexing & Structural Representation (graphs, trees, vector-coordinate bindings)
- $\mathcal{S}_4$: Cross-Page & Multi-Hop Retrieval (matrix reachability, sub-intent walking)
- $\mathcal{S}_5$: Claim-Level Attribution & Verification (atomic claims, visual grounding, arbitration)

### Inter-Rater Reliability:
- **Raw Agreement:** 22 / 25 cells = **88.00%**
- **Cohen's $\kappa$:** **0.8005 $\approx 0.80$** (Substantial inter-rater concordance)

| Survey Reference | Venue & Year | $\mathcal{S}_1$ | $\mathcal{S}_2$ | $\mathcal{S}_3$ | $\mathcal{S}_4$ | $\mathcal{S}_5$ | Identified Research Gap |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gao et al. [15]** | ACL 2026 | $\circ$ | $\bullet$ | $\times$ | $\bullet$ | $\circ$ | Focuses on context scaling and MLLM page retrieval (ColPali); lacks coordinate indexing and fine-grained claim attribution. |
| **Peng et al. [35]** | ACM TOIS 2026 | $\times$ | $\times$ | $\times$ | $\bullet$ | $\circ$ | Exhaustive survey of textual GraphRAG; completely ignores physical 2D document geometry, tables, and PDF layouts. |
| **Zhang [36]** | IJCNLP-AACL 2025 | $\circ$ | $\bullet$ | $\times$ | $\times$ | $\times$ | Evaluates MLLM visual document parsing for single-page VQA; lacks multi-page cross-document retrieval and verification. |
| **Li et al. [37]** | arXiv 2025 | $\times$ | $\times$ | $\times$ | $\circ$ | $\times$ | Focuses on long-document textual retrieval efficiency; omits 2D spatial layouts, tables, and visual charts. |
| **Ni et al. [38]** | ACM CSUR 2026 | $\times$ | $\times$ | $\times$ | $\circ$ | $\bullet$ | Comprehensive survey on trustworthy RAG and textual hallucination; does not address spatial document geometry. |
| **This Review (2026)** | **IEEE Review** | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ | **First systematic review unifying spatial layout preservation, graph multi-hop reachability, and coordinate claim attribution.** |

*Symbols: $\bullet$ Comprehensive coverage; $\circ$ Partial discussion; $\times$ Out of scope.*

---

## 3. Table II: Comparative Analysis of Core Empirical Systems (n = 23)

The 23 core empirical systems and layout extractors are audited across their technological foundations:

| ID | Study Reference | Venue | Input Modality | Extraction Method | Graph / Topology | Provenance Unit | Lifecycle Stages | Key Technical Limitation |
| :-: | :--- | :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| [1] | Qi et al. (2026) | IEEE TKDE | Text + Knowledge Graph | Entity Description Extraction | DGHMA Hetero-Graph | Reasoning Traversal Path | `S3, S4, S5` | Assumes pre-existing curated knowledge graph; ignores 2D spatial layouts, tables, and visual chart bitmaps. |
| [2] | Niu et al. (2026) | IEEE TKDE | Text Documents | Topic-Route-Fact Induction | In-Memory Pseudo-Graph Tree | Fact Information Item (FII) | `S2, S3, S4` | Text-only focus; lacks visual layout coordinate anchoring and uncertainty-aware path arbitration. |
| [3] | Zhang et al. (2026) | IEEE TMM | Text + Image | Dynamic Relevance Routing | Relevance Reflection Graph | Multimodal Span | `S3, S4, S5` | Scoped to single-turn knowledge VQA; lacks cross-page document hierarchy and tabular relational tracking. |
| [4] | Shen et al. (2026) | IEEE TPAMI | Text + KG | Symbolic Constraint Alignment | Knowledge Graph | Symbolic Reasoning Path | `S3, S4` | Requires structured KG triples; lacks direct ingestion of raw multi-page PDF bounding boxes. |
| [5] | Hang et al. (2025) | IEEE TAI | Text + Claims | Fact-Checking Subgraph Mining | Veracity Subgraph | Veracity Subgraph Path | `S3, S5` | Evaluates textual claims on social news; does not model complex enterprise tabular matrices or charts. |
| [6] | Zheng et al. (2026) | IEEE TIFS | Text + Graph | Backdoor Trigger Detection | Entity-Relationship Graph | Trigger Entity Span | `S3, S5` | Focuses on adversarial security attacks on graph RAG; does not address visual layout preservation. |
| [8] | Edge et al. (2024) | arXiv | Text Documents | LLM Triple Prompting | Leiden Community KG | Passage Cluster | `S3, S4` | Computationally expensive LLM extraction; discards physical 2D PDF layout bounding boxes. |
| [9] | Guo et al. (2025) | Findings of EMNLP | Text Documents | Dual-Level Entity/Theme Extraction | Entity + Theme Graph | Graph Node | `S3, S4` | Text-focused scope; does not model 2D tabular cell dependencies or visual infographics. |
| [10] | Huang et al. (2022) | ACM MM | Text + Layout + Image | Unified Multimodal Masking | None (Linear Tokens) | 2D Bounding Box | `S1, S2, S3` | Token-level document pre-training; lacks graph-based multi-hop retrieval and claim verification. |
| [14] | Wang et al. (2025) | Proc. 8th IEEE CISAT | Text Documents | Sub-Intent Tree Decomposition | Decomposed Modular Hierarchy | Passage Sub-chunk | `S4, S5` | Evaluated on unimodal text SLMs; lacks multimodal coordinate anchoring and chart comprehension. |
| [19] | Yasunaga et al. (2021) | Findings of NAACL | Text + ConceptNet | GNN Joint Message Passing | Joint LM-KG Graph | KG Concept Node | `S3, S4` | Requires static external commonsense KG; cannot extract dynamic layout graphs from raw documents. |
| [20] | Chen et al. (2024) | NeurIPS | Large Spreadsheets | Schema & Cell Retrieval | Cell-Path Routing | Table Cell Coordinate | `S1, S2, S4` | Evaluates serialized tabular spreadsheets; lacks physical multi-page PDF layout and visual charts. |
| [29] | Trivedi et al. (2023) | Proc. 61st ACL | Text Documents | Interleaved Chain-of-Thought | Iterative Prompt Chain | Passage Sentence | `S4, S5` | Iterative prompt hops risk stochastic path divergence; lacks algebraic graph reachability bounds. |
| [31] | Gutierrez et al. (2024) | NeurIPS | Text Documents | OpenIE Triple Extraction | Associative Memory Graph | Entity Node | `S3, S4` | Personalized PageRank over text entities; lacks 2D document layout preservation and visual grounding. |
| [32] | Faysse et al. (2025) | Proc. 13th ICLR | Visual PDF Pages | PaliGemma Multi-Vector Embeddings | None (Late Interaction Patches) | Page Level | `S2, S4` | High memory footprint for patch vectors; lacks symbolic multi-hop graph reasoning and cell coordinates. |
| [33] | Zhao et al. (2024) | arXiv | Document Bitmaps | YOLOv10 + GL-CRM | None (Bounding Box Blocks) | 2D Bounding Box | `S1, S2` | Perception and segmentation only; lacks downstream graph indexing and multi-hop retrieval. |
| [43] | Asai et al. (2024) | Proc. 12th ICLR | Text Documents | Reflection Token Modeling | Beam Search Reflection Tree | Passage Sub-span | `S4, S5` | Requires specialized LLM instruction tuning; lacks spatial bounding box coordinate tracking. |
| [44] | Yan et al. (2026) | Findings of IJCNLP-AACL | Text Documents | Retrieval Evaluator & Refinement | Static Refinement Chain | Passage Slice | `S4, S5` | Textual refinement only; does not handle visual layout, table headers, or cross-page spatial graphs. |
| [45] | Jeong et al. (2024) | Proc. NAACL | Text Documents | Complexity-Aware Query Classifier | Multi-Step Routing Tree | Passage Chunk | `S4, S5` | Query classifier routes text queries; does not model multimodal layout complexity or table schemas. |
| [46] | Wang et al. (2024) | arXiv | Multi-Page PDF Bitmaps | Hybrid Layout & Formula Extraction | Markdown Document Hierarchy | Block / Region | `S1, S2` | Outputs serialized markdown text; strips raw physical bounding box coordinates during serialization. |
| [47] | Blecher et al. (2023) | arXiv | Document Bitmaps | Vision-to-Markdown Transformer | None (Linear Text) | None (Linear Text) | `S1, S2` | Autoregressive generation discards spatial coordinate geometry, preventing fine-grained visual attribution. |
| [48] | He et al. (2024) | Proc. 38th NeurIPS | Textual Graphs | Prize-Collecting Steiner Tree | Targeted Subgraph | Subgraph Node / Edge | `S3, S4` | Assumes input is already an explicit graph; lacks direct visual document layout parsing. |
| [49] | Liang et al. (2025) | Companion Proc. ACM WWW | Text + Professional Domain KG | Mutual-Indexing (Chunk & KG) | Domain Knowledge Graph | Logical KG Path | `S3, S4, S5` | Optimized for symbolic enterprise KGs; does not ingest physical 2D layout bounding boxes from PDFs. |

---

## 4. Table III: Decoupled Multimodal Document Benchmark Audit

Existing benchmarks conflate textual question answering with spatial evidence localization. To resolve this, we decouple benchmark evaluation across four explicit operational dimensions:
1. **Txt-R (Text Retrieval):** Measures whether relevant text passages are retrieved (Recall@K, MRR).
2. **Doc-G (Page-Level Grounding):** Measures whether the system isolates the correct physical document page in multi-page corpora (Page Recall@K, Page NDCG).
3. **Coord-L (Region/Cell Coordinate Localization):** Measures whether the system accurately pinpoints 2D bounding boxes or tabular cell coordinates ($[x_1, y_1, x_2, y_2]$, CIR, Bounding Box IoU).
4. **Clm-A (Claim Attribution):** Measures whether generated claims are supported by cited evidence regions (Citation Precision, Citation Recall, FActScore).

| Benchmark | Venue | Modalities | Primary Target | Txt-R | Doc-G | Coord-L | Clm-A | Formal Evaluation Metrics | Identified Evaluation Gap |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **HotpotQA** | EMNLP | Pure Text | 2-Hop Fact Chains | • | × | × | ○ | EM, F1, Supporting Fact Recall | Pure text passages; completely lacks 2D document layout, tables, or visual bounding boxes. |
| **ChartQA** | ACL Findings | Chart Images | Visual / Numerical QA | × | × | × | × | Relaxed Accuracy (RA) | Evaluates end-to-end question answering over single chart images; does not evaluate passage retrieval, page grounding, or bounding-box localization. |
| **ALCE** | EMNLP | Text Documents | Citation Support | • | × | × | • | Citation Precision, Citation Recall, Disagreement | Evaluates citation attribution over unformatted text chunks; lacks visual layout grounding or coordinate bounding boxes. |
| **TableRAG** | NeurIPS | Spreadsheets | Million-Token Tables | • | ○ | ○ | × | Table Cell Recall@K, Answer Accuracy | Operates on logical spreadsheet cell addressing rather than physical 2D PDF layout bounding boxes; does not evaluate claim attribution. |
| **ViDoRe** | ICLR | Visual Pages | Visual Page Retrieval | × | • | × | × | Page NDCG@5, Page Recall@5 | Evaluates page-level image retrieval; does not evaluate sub-page coordinate localization or generated claim attribution. |
| **M3DocVQA** | ICCVW | Multi-Page PDFs | Multi-Page DocVQA | ○ | ○ | × | × | ANLS, Evidence Page Accuracy | Evaluates document QA and page-level evidence retrieval; does not formalize coordinate bounding box IoU or claim verification. |
| **MMDocRAG** | NeurIPS | PDF Pages | End-to-End MM-RAG | ○ | • | × | × | Page Hit@K, VQA Accuracy | Focuses on coarse whole-page retrieval without evaluating fine-grained coordinate bounding boxes or claim attribution. |
| **PubTabNet** | ECCV | Scientific Tables | Table Recognition | × | × | • | × | TEDS (Tree-Edit-Distance), Cell IoU | Benchmark for table structure recognition and OCR bounding boxes; lacks information retrieval and multi-hop question answering. |
| **FActScore** | EMNLP | Text Documents | Atomic Fact Precision | × | × | × | ○ | Atomic Fact Accuracy (%) | Evaluates factual accuracy of generated text against Wikipedia; lacks multimodal grounding and document layout coordinates. |

---

## 5. Critical Finding: The Benchmark Evaluation Void

Crucially, our audit in Table III proves that **among all evaluated multimodal document benchmarks, zero benchmarks jointly evaluate region/cell coordinate localization (Coord-L) and claim-level attribution (Clm-A) simultaneously**:
- Benchmarks evaluating factual attribution (ALCE [42] for citations, FActScore [50] for atomic fact precision) operate strictly over linear text passages without visual layout coordinates ($	ext{Coord-L} = 	imes$).
- Benchmarks focusing on multi-page visual retrieval (ViDoRe [32], MMDocRAG [41], M3DocVQA [40]) evaluate whole-page retrieval ($	ext{Doc-G} = ullet$) but fail to evaluate bounding-box coordinates ($	ext{Coord-L} = 	imes$) or atomic claim support ($	ext{Clm-A} = 	imes$).
- Benchmarks providing fine-grained cell coordinates (TableRAG [20]) operate on serialized spreadsheet cells rather than 2D visual PDF layouts and lack claim-level attribution.
- Benchmarks evaluating physical bounding box IoU (PubTabNet [28]) evaluate perception and OCR in isolation without end-to-end information retrieval or question answering.

This empirical void validates the core thesis of our systematic review and directly motivates the **LAM-GraphRAG** architectural blueprint.
