# Core Primary Empirical Systems & Extraction Architectures (n = 23)

This directory documents the 23 core empirical systems and visual layout extraction models synthesized in this systematic review. These systems directly address the perception, representation, traversal, and verification of structured, visual, or multi-hop knowledge.

---

## 1. Summary Taxonomy of Core Systems

| ID | Citation Key | System / Model | Primary Venue | Subcategory | Spatial Granularity | Graph / Index Topology | Lifecycle Stages |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| [1] | `qi2026` | **DUAL-Know** | IEEE TKDE | Multimodal Document RAG | Node | Section III-B, pp. 5018-5022 | `S3, S4, S5` |
| [2] | `niu2026` | **Empowering Large Language Models to Set Up Knowledge Retrieval Indexing via Self-Learning** | IEEE TKDE | Multimodal Document RAG | Node | Section 3.1, pp. 1712-1715 | `S2, S3, S4` |
| [3] | `zhang2026m2ag` | **mR²AG** | IEEE TMM | Multimodal Document RAG | Region | Section III, pp. 6114-6118 | `S3, S4, S5` |
| [4] | `shen2026rar` | **Reason-Align-Respond** | IEEE TPAMI | Graph-Based Reasoning | Node | Section 3.3, pp. 7344-7348 | `S3, S4` |
| [5] | `hang2025trumor` | **TrumorGPT** | IEEE TAI | Fact-Checking & Security | Node | Section IV, pp. 3150-3155 | `S3, S5` |
| [6] | `zheng2026trigger` | **Trigger as Entity** | IEEE TIFS | Fact-Checking & Security | Node | Section III, pp. 1108-1112 | `S3, S5` |
| [8] | `edge2024` | **From Local to Global** | arXiv preprint | Graph-Based Reasoning | Document | Section 3, pp. 3-7 | `S3, S4` |
| [9] | `guo2025lightrag` | **LightRAG** | Findings of EMNLP | Graph-Based Reasoning | Node | Section 3, pp. 2412-2416 | `S3, S4` |
| [10] | `huang2022` | **LayoutLMv3** | Proc. ACM MM | Visual Layout Parsing | Region | Section 3, pp. 4084-4087 | `S1, S2, S3` |
| [14] | `wang2025` | **Decomposed Modular RAG** | Proc. 2025 8th IEEE CISAT | Graph-Based Reasoning | Passage | Section II-B, pp. 31-33 | `S4, S5` |
| [19] | `yasunaga2021` | **QA-GNN** | Findings of ACL: NAACL | Graph-Based Reasoning | Node | Section 3, pp. 537-540 | `S3, S4` |
| [20] | `chen2024tablerag` | **TableRAG** | NeurIPS | Multimodal Document RAG | Cell | Section 3.2, pp. 20963-20966 | `S1, S2, S4` |
| [29] | `trivedi2023` | **Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions** | Proc. 61st ACL | Graph-Based Reasoning | Passage | Section 2, pp. 10015-10020 | `S4, S5` |
| [31] | `gutierrez2024hipporag` | **HippoRAG** | NeurIPS | Graph-Based Reasoning | Node | Section 2, pp. 16754-16757 | `S3, S4` |
| [32] | `faysse2025colpali` | **ColPali** | Proc. 13th ICLR | Multimodal Document RAG | Region | Section 3, pp. 4-7 | `S2, S4` |
| [33] | `zhao2024doclayout` | **DocLayout-YOLO** | arXiv preprint | Visual Layout Parsing | Region | Section 3, pp. 4-8 | `S1, S2` |
| [43] | `asai2024selfrag` | **Self-RAG** | Proc. 12th ICLR | Graph-Based Reasoning | Passage | Section 3, pp. 4-8 | `S4, S5` |
| [44] | `yan2024crag` | **Corrective Retrieval Augmented Generation** | Findings of ACL: IJCNLP-AACL | Graph-Based Reasoning | Passage | Section 3, pp. 2993-2997 | `S4, S5` |
| [45] | `jeong2024adaptiverag` | **Adaptive-RAG** | Proc. NAACL | Graph-Based Reasoning | Passage | Section 3, pp. 1123-1127 | `S4, S5` |
| [46] | `wang2024mineru` | **MinerU** | arXiv preprint | Visual Layout Parsing | Region | Section 2, pp. 3-7 | `S1, S2` |
| [47] | `blecher2023nougat` | **Nougat** | arXiv preprint | Visual Layout Parsing | Page | Section 2, pp. 2-5 | `S1, S2` |
| [48] | `he2024gretriever` | **G-Retriever** | Proc. 38th NeurIPS | Graph-Based Reasoning | Node | Section 3, pp. 4-8 | `S3, S4` |
| [49] | `liang2024kag` | **KAG** | Companion Proc. ACM Web Conf. (WWW) | Graph-Based Reasoning | Node | Section 2, pp. 335-338 | `S3, S4, S5` |

---

## 2. In-Depth Architectural Profiles

### [1] DUAL-Know: A Description-Augmented and Uncertainty-Aware GraphRAG Framework for Anesthesiology Question Answering (`qi2026`)
- **Authors:** H. Qi, J. Li, Y. Ge, H. Wu, Y. Cai, S. Che, T. Sheng, Q. Zhao, and C. Chen
- **Publication Venue:** IEEE TKDE, vol. 38, no. 8, pp. 5015--5031, Aug. 2026
- **Identifier / DOI:** [`10.1109/TKDE.2026.3700611`](https://doi.org/10.1109/TKDE.2026.3700611)
- **Study Type:** Peer-Reviewed Journal (Multimodal Document RAG)
- **Lifecycle Stages:** `S3, S4, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** Partial
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Yes
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section III-B, pp. 5018-5022; Section IV-C, Table II
- **Synthesized Technical Contribution:** Formulates DGHMA cross-attention and variance-penalized path ranking Score(pi)=sim(pi,Q)*exp(-lambda*sigma_pi) with multi-metric arbitration.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4, S5 (incorporating multimodal document rag techniques into Modules 1--5).

---
### [2] Empowering Large Language Models to Set Up Knowledge Retrieval Indexing via Self-Learning (`niu2026`)
- **Authors:** S. Niu, M. Wang, X. Liang, Z. Li, S. Zhang, S. Song, H. Wang, J. Yang, F. Xiong, and C. Xi
- **Publication Venue:** IEEE TKDE, vol. 38, no. 3, pp. 1710--1724, Mar. 2026
- **Identifier / DOI:** [`10.1109/TKDE.2025.3649907`](https://doi.org/10.1109/TKDE.2025.3649907)
- **Study Type:** Peer-Reviewed Journal (Multimodal Document RAG)
- **Lifecycle Stages:** `S2, S3, S4`
- **Spatial Layout Aware:** Partial | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Partial
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section 3.1, pp. 1712-1715; Section 4.2, pp. 1718-1720
- **Synthesized Technical Contribution:** Introduces Topic-Route-Fact pseudo-graph schema and algebraic transition matrix walking p^(k) = p^(0)(D^-1 A)^k, reducing KG latency from 15s to sub-second.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S2, S3, S4 (incorporating multimodal document rag techniques into Modules 1--5).

---
### [3] mR²AG: Multimodal Retrieval-Reflection-Augmented Generation for Knowledge-Based VQA (`zhang2026m2ag`)
- **Authors:** Tao Zhang, Ziqi Zhang, Zongyang Ma, Yuxin Chen, Zhongang Qi, et al.
- **Publication Venue:** IEEE TMM, vol. 28, pp. 2450--2463, 2026
- **Identifier / DOI:** [`10.1109/TMM.2026.3723597`](https://doi.org/10.1109/TMM.2026.3723597)
- **Study Type:** Peer-Reviewed Journal (Multimodal Document RAG)
- **Lifecycle Stages:** `S3, S4, S5`
- **Spatial Layout Aware:** Partial | **Multimodal Alignment:** Yes
- **Retrieval Granularity:** Region
- **Provenance Tracking:** Yes | **Claim Attribution:** Partial
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section III, pp. 6114-6118; Section V, Table IV
- **Synthesized Technical Contribution:** Implements adaptive multimodal reflection routing between image patches and text knowledge bases, preventing attention dilution.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4, S5 (incorporating multimodal document rag techniques into Modules 1--5).

---
### [4] Reason-Align-Respond: Aligning LLM Reasoning With Knowledge Graphs for KGQA (`shen2026rar`)
- **Authors:** Xiangqing Shen, Fanfan Wang, Zinong Yang, Bing Wang, Wenli Du, Chengqing Zong, and Rui Xia
- **Publication Venue:** IEEE TPAMI, vol. 48, no. 7, pp. 7340--7353, Jul. 2026
- **Identifier / DOI:** [`10.1109/TPAMI.2026.3665645`](https://doi.org/10.1109/TPAMI.2026.3665645)
- **Study Type:** Peer-Reviewed Journal (Graph-Based Reasoning)
- **Lifecycle Stages:** `S3, S4`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Yes
- **Methodological Quality Score:** **12 / 12**
- **Evidence Location:** Section 3.3, pp. 7344-7348; Section 5.1, Table I
- **Synthesized Technical Contribution:** Bidirectional neurosymbolic alignment between LLM reasoning trajectories and symbolic KG paths, enforcing claim constraint verification.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [5] TrumorGPT: Graph-Based Retrieval-Augmented Large Language Model for Fact-Checking and Misinformation Mitigation (`hang2025trumor`)
- **Authors:** Ching Nam Hang, Pei-Duo Yu, and Chee-Wei Tan
- **Publication Venue:** IEEE TAI, vol. 6, no. 4, pp. 1820--1834, 2025
- **Identifier / DOI:** [`10.1109/TAI.2025.3567369`](https://doi.org/10.1109/TAI.2025.3567369)
- **Study Type:** Peer-Reviewed Journal (Fact-Checking & Security)
- **Lifecycle Stages:** `S3, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Yes
- **Methodological Quality Score:** **10 / 12**
- **Evidence Location:** Section IV, pp. 3150-3155; Section VI, Table III
- **Synthesized Technical Contribution:** Constructs veracity evidence subgraphs to corroborate isolated claims against adversarial misinformation cascades.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S5 (incorporating fact-checking & security techniques into Modules 1--5).

---
### [6] Trigger as Entity: Backdoor Attacks to Graph-Based Retrieval-Augmented Generation of Large Language Models (`zheng2026trigger`)
- **Authors:** Zhirun Zheng, Young-June Choi, Cheng Huang, Hangcheng Cao, Shujuan Tian, and Tingrui Pei
- **Publication Venue:** IEEE TIFS, vol. 21, pp. 5583--5596, 2026
- **Identifier / DOI:** [`10.1109/TIFS.2026.3699202`](https://doi.org/10.1109/TIFS.2026.3699202)
- **Study Type:** Peer-Reviewed Journal (Fact-Checking & Security)
- **Lifecycle Stages:** `S3, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Partial
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section III, pp. 1108-1112; Section V, Table II
- **Synthesized Technical Contribution:** Demonstrates vulnerabilities of graph community indexing to backdoor entity injection during RAG retrieval.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S5 (incorporating fact-checking & security techniques into Modules 1--5).

---
### [8] From Local to Global: A Graph RAG Approach to Query-Focused Summarization (`edge2024`)
- **Authors:** Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, et al.
- **Publication Venue:** arXiv preprint, 2024
- **Identifier / DOI:** [`arXiv:2404.16130`](https://arxiv.org/abs/2404.16130)
- **Study Type:** Technical Archival Preprint (Graph-Based Reasoning)
- **Lifecycle Stages:** `S3, S4`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Document
- **Provenance Tracking:** Partial | **Claim Attribution:** Partial
- **Methodological Quality Score:** **10 / 12**
- **Evidence Location:** Section 3, pp. 3-7; Section 4, Table 1
- **Synthesized Technical Contribution:** Hierarchical Leiden community summaries over LLM-extracted entity-relation graphs; high extraction latency per document.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [9] LightRAG: Simple and Fast Retrieval-Augmented Generation (`guo2025lightrag`)
- **Authors:** Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, and Chao Huang
- **Publication Venue:** Findings of EMNLP, pp. 10746--10761, 2025
- **Identifier / DOI:** [`10.18653/v1/2025.findings-emnlp.568`](https://doi.org/10.18653/v1/2025.findings-emnlp.568)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S3, S4`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Partial
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section 3, pp. 2412-2416; Section 4, Table 2
- **Synthesized Technical Contribution:** Dual-level entity and theme indexing with multi-hop graph retrieval, achieving lower query latency than hierarchical community summarization.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [10] LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking (`huang2022`)
- **Authors:** Yupan Huang, Tengchao Lv, Lei Cui, Yutao Lu, and Furu Wei
- **Publication Venue:** Proc. ACM MM, pp. 4083--4091, 2022
- **Identifier / DOI:** [`10.1145/3503161.3548112`](https://doi.org/10.1145/3503161.3548112)
- **Study Type:** Peer-Reviewed Conference (Visual Layout Parsing)
- **Lifecycle Stages:** `S1, S2, S3`
- **Spatial Layout Aware:** Yes | **Multimodal Alignment:** Yes
- **Retrieval Granularity:** Region
- **Provenance Tracking:** Yes | **Claim Attribution:** No
- **Methodological Quality Score:** **12 / 12**
- **Evidence Location:** Section 3, pp. 4084-4087; Table 2
- **Synthesized Technical Contribution:** Unified multi-modal pretraining integrating word embeddings, visual patch tokens, and normalized 2D spatial coordinates [x0, y0, x1, y1].
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S1, S2, S3 (incorporating visual layout parsing techniques into Modules 1--5).

---
### [14] Decomposed Modular RAG: Task-Aware Multi-Step Retrieval and Reasoning for Small-Scale Language Models (`wang2025`)
- **Authors:** Yuchen Wang, Haolong Wang, Kai Wang, and Xinyu Du
- **Publication Venue:** Proc. 2025 8th IEEE CISAT, pp. 128--133, 2025
- **Identifier / DOI:** [`10.1109/CISAT66811.2025.11181923`](https://doi.org/10.1109/CISAT66811.2025.11181923)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S4, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Passage
- **Provenance Tracking:** Yes | **Claim Attribution:** Partial
- **Methodological Quality Score:** **9 / 12**
- **Evidence Location:** Section II-B, pp. 31-33; Table I
- **Synthesized Technical Contribution:** Decomposes complex retrieval tasks into modular sub-queries, tracking sub-intent satisfaction across small LLMs.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S4, S5 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [19] QA-GNN: Reasoning with Language Models and Knowledge Graphs for Question Answering (`yasunaga2021`)
- **Authors:** Michihiro Yasunaga, Hongyu Ren, Antoine Bosselut, Percy Liang, and Jure Leskovec
- **Publication Venue:** Findings of ACL: NAACL, pp. 273--288, 2021
- **Identifier / DOI:** [`10.18653/v1/2021.findings-naacl.24`](https://aclanthology.org/2021.findings-naacl.24)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S3, S4`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** No
- **Methodological Quality Score:** **10 / 12**
- **Evidence Location:** Section 3, pp. 537-540; Table 2
- **Synthesized Technical Contribution:** Joint graph neural network and language model reasoning over extracted knowledge graph subgraphs.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [20] TableRAG: Million-Token Table Understanding with Language Models (`chen2024tablerag`)
- **Authors:** Si-An Chen, Lesly Miculicich, Julian Martin Eisenschlos, Zifeng Wang, Zilong Wang, Yanfei Chen, Yasuhisa Fujii, Hsuan-Tien Lin, Chen-Yu Lee, and Tomas Pfister
- **Publication Venue:** NeurIPS, vol. 37, pp. 23145--23168, 2024
- **Identifier / DOI:** [`10.52202/079017-2382`](https://doi.org/10.52202/079017-2382)
- **Study Type:** Peer-Reviewed Conference (Multimodal Document RAG)
- **Lifecycle Stages:** `S1, S2, S4`
- **Spatial Layout Aware:** Yes | **Multimodal Alignment:** No
- **Retrieval Granularity:** Cell
- **Provenance Tracking:** Yes | **Claim Attribution:** Yes
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section 3.2, pp. 20963-20966; Section 4.3, Table 2
- **Synthesized Technical Contribution:** Formulates query expansion, schema retrieval, and cell retrieval to process tables with up to 1 million tokens without row truncation; provides logical tabular cell grounding.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S1, S2, S4 (incorporating multimodal document rag techniques into Modules 1--5).

---
### [29] Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions (`trivedi2023`)
- **Authors:** Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal
- **Publication Venue:** Proc. 61st ACL, pp. 10001--10020, 2023
- **Identifier / DOI:** [`10.18653/v1/2023.acl-long.557`](https://aclanthology.org/2023.acl-long.557)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S4, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Passage
- **Provenance Tracking:** Yes | **Claim Attribution:** Partial
- **Methodological Quality Score:** **10 / 12**
- **Evidence Location:** Section 2, pp. 10015-10020; Table 2
- **Synthesized Technical Contribution:** IRCoT interleaves step-by-step chain-of-thought generation with iterative passage retrieval across multi-hop benchmarks.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S4, S5 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [31] HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models (`gutierrez2024hipporag`)
- **Authors:** Bernal Jiménez Gutiérrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, and Yu Su
- **Publication Venue:** NeurIPS, vol. 37, pp. 31200--31235, 2024
- **Identifier / DOI:** [`10.52202/079017-3140`](https://doi.org/10.52202/079017-3140)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S3, S4`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Partial
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section 2, pp. 16754-16757; Section 4.1, Table 1
- **Synthesized Technical Contribution:** Simulates hippocampal associative memory using Personalized PageRank over open IE knowledge graphs for multi-hop discovery.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [32] ColPali: Efficient Document Retrieval with Vision Language Models (`faysse2025colpali`)
- **Authors:** Manuel Faysse, Hugues Sibille, Tony Wu, Bilel Omrani, Gautier Viaud, Céline Hudelot, and Pierre Colombo
- **Publication Venue:** Proc. 13th ICLR, pp. 1--21, 2025
- **Identifier / DOI:** [`10.48550/arXiv.2407.01449`](https://arxiv.org/abs/2407.01449)
- **Study Type:** Peer-Reviewed Conference (Multimodal Document RAG)
- **Lifecycle Stages:** `S2, S4`
- **Spatial Layout Aware:** Yes | **Multimodal Alignment:** Yes
- **Retrieval Granularity:** Region
- **Provenance Tracking:** Yes | **Claim Attribution:** No
- **Methodological Quality Score:** **12 / 12**
- **Evidence Location:** Section 3, pp. 4-7; Section 5, Table 2
- **Synthesized Technical Contribution:** End-to-end multi-vector ColBERT late interaction over PaliGemma document page patch embeddings, bypassing OCR.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S2, S4 (incorporating multimodal document rag techniques into Modules 1--5).

---
### [33] DocLayout-YOLO: Enhancing Document Layout Analysis through Diverse Synthetic Data and Global-to-Local Adaptive Perception (`zhao2024doclayout`)
- **Authors:** Zhiyuan Zhao, Hengrui Kang, Bin Wang, and Conghui He
- **Publication Venue:** arXiv preprint, 2024
- **Identifier / DOI:** [`arXiv:2410.12628`](https://arxiv.org/abs/2410.12628)
- **Study Type:** Technical Archival Preprint (Visual Layout Parsing)
- **Lifecycle Stages:** `S1, S2`
- **Spatial Layout Aware:** Yes | **Multimodal Alignment:** No
- **Retrieval Granularity:** Region
- **Provenance Tracking:** Yes | **Claim Attribution:** No
- **Methodological Quality Score:** **9 / 12**
- **Evidence Location:** Section 3, pp. 4-8; Section 4, Table 1
- **Synthesized Technical Contribution:** Document layout segmentation model with global-to-local adaptive perception module for dense page bounding box extraction.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S1, S2 (incorporating visual layout parsing techniques into Modules 1--5).

---
### [43] Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection (`asai2024selfrag`)
- **Authors:** Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi
- **Publication Venue:** Proc. 12th ICLR, pp. 1--23, 2024
- **Identifier / DOI:** [`10.48550/arXiv.2310.11511`](https://arxiv.org/abs/2310.11511)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S4, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Passage
- **Provenance Tracking:** Yes | **Claim Attribution:** Yes
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section 3, pp. 4-8; Section 5, Table 1
- **Synthesized Technical Contribution:** Trains language models to generate special reflection tokens ([Retrieve], [IsRel], [IsSup]) to dynamically verify passage support.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S4, S5 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [44] Corrective Retrieval Augmented Generation (`yan2024crag`)
- **Authors:** Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, and Zhen-Hua Ling
- **Publication Venue:** Findings of ACL: IJCNLP-AACL, pp. 151--165, 2026
- **Identifier / DOI:** [`10.18653/2026.findings-aacl.151`](https://aclanthology.org/2026.findings-aacl.151)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S4, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Passage
- **Provenance Tracking:** Yes | **Claim Attribution:** Partial
- **Methodological Quality Score:** **10 / 12**
- **Evidence Location:** Section 3, pp. 2993-2997; Table 1
- **Synthesized Technical Contribution:** Retrieval evaluator assessing document confidence, triggering web search fallback or passage striping.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S4, S5 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [45] Adaptive-RAG: Determining When and How to Retrieve for Large Language Models (`jeong2024adaptiverag`)
- **Authors:** Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, and Jong C. Park
- **Publication Venue:** Proc. NAACL, pp. 2941--2956, 2024
- **Identifier / DOI:** [`10.18653/v1/2024.naacl-long.161`](https://aclanthology.org/2024.naacl-long.161)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S4, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Passage
- **Provenance Tracking:** No | **Claim Attribution:** Partial
- **Methodological Quality Score:** **9 / 12**
- **Evidence Location:** Section 3, pp. 1123-1127; Table 2
- **Synthesized Technical Contribution:** Classifies query complexity to dynamically route queries to non-retrieval, single-step, or multi-step retrieval strategies.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S4, S5 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [46] MinerU: An Open-Source Solution for Precise Document Content Extraction (`wang2024mineru`)
- **Authors:** Bin Wang, Chao Xu, Xiaomeng Zhao, Linke Ouyang, and Fan Wu
- **Publication Venue:** arXiv preprint, 2024
- **Identifier / DOI:** [`arXiv:2409.18839`](https://arxiv.org/abs/2409.18839)
- **Study Type:** Technical Archival Preprint (Visual Layout Parsing)
- **Lifecycle Stages:** `S1, S2`
- **Spatial Layout Aware:** Yes | **Multimodal Alignment:** Yes
- **Retrieval Granularity:** Region
- **Provenance Tracking:** Yes | **Claim Attribution:** No
- **Methodological Quality Score:** **9 / 12**
- **Evidence Location:** Section 2, pp. 3-7; Section 4, Table 2
- **Synthesized Technical Contribution:** Open-source document parsing pipeline converting academic PDFs into markdown while extracting table and image bounding boxes.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S1, S2 (incorporating visual layout parsing techniques into Modules 1--5).

---
### [47] Nougat: Neural Optical Understanding for Academic Documents (`blecher2023nougat`)
- **Authors:** Lukas Blecher, Guillem Cucurull, Pushkar Scialom, and Robert Stojnic
- **Publication Venue:** arXiv preprint, 2023
- **Identifier / DOI:** [`arXiv:2308.13418`](https://arxiv.org/abs/2308.13418)
- **Study Type:** Technical Archival Preprint (Visual Layout Parsing)
- **Lifecycle Stages:** `S1, S2`
- **Spatial Layout Aware:** Partial | **Multimodal Alignment:** No
- **Retrieval Granularity:** Page
- **Provenance Tracking:** No | **Claim Attribution:** No
- **Methodological Quality Score:** **9 / 12**
- **Evidence Location:** Section 2, pp. 2-5; Table 1
- **Synthesized Technical Contribution:** End-to-end visual transformer model transcribing document page images directly into formatted scientific markdown and LaTeX.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S1, S2 (incorporating visual layout parsing techniques into Modules 1--5).

---
### [48] G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering (`he2024gretriever`)
- **Authors:** Xiaoxin He, Yijun Tian, Yifei Sun, Nitesh V. Chawla, Thomas Laurent, Yann LeCun, Xavier Bresson, Bryan Hooi
- **Publication Venue:** Proc. 38th NeurIPS, pp. 24810--24835, 2024
- **Identifier / DOI:** [`10.52202/079017-2549`](https://doi.org/10.52202/079017-2549)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S3, S4`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Yes
- **Methodological Quality Score:** **11 / 12**
- **Evidence Location:** Section 3, pp. 4-8; Section 5, Table 2
- **Synthesized Technical Contribution:** Integrates textual graph retrieval and prize-collecting Steiner tree optimization to ground LLM reasoning on textual subgraphs.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4 (incorporating graph-based reasoning techniques into Modules 1--5).

---
### [49] KAG: Boosting LLMs in Professional Domains via Knowledge Augmented Generation (`liang2024kag`)
- **Authors:** Lei Liang, Zhongpu Bo, Zhengke Gui, Zhongshu Zhu, Ling Zhong, Peilong Zhao, Mengshu Sun, Zhiqiang Zhang, Jun Zhou, Wenguang Chen, Wen Zhang, and Huajun Chen
- **Publication Venue:** Companion Proc. ACM Web Conf. (WWW), pp. 334--343, 2025
- **Identifier / DOI:** [`10.1145/3701716.3715240`](https://doi.org/10.1145/3701716.3715240)
- **Study Type:** Peer-Reviewed Conference (Graph-Based Reasoning)
- **Lifecycle Stages:** `S3, S4, S5`
- **Spatial Layout Aware:** No | **Multimodal Alignment:** No
- **Retrieval Granularity:** Node
- **Provenance Tracking:** Yes | **Claim Attribution:** Yes
- **Methodological Quality Score:** **9 / 12**
- **Evidence Location:** Section 2, pp. 335-338; Section 3.2, Table 1
- **Synthesized Technical Contribution:** Combines hybrid semantic graphs, logical form representation, and mutual verification to resolve professional domain queries.
- **Relevance to LAM-GraphRAG:** Directly provides architectural baselines for S3, S4, S5 (incorporating graph-based reasoning techniques into Modules 1--5).

---
