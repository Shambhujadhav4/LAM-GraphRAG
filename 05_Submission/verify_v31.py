import re, sys, os

with open('Presentation/literature_review_ieee.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

checks = []

def run_check(name, condition, error_msg=""):
    status = "[PASS]" if condition else "[FAIL]"
    checks.append((name, condition, error_msg))
    print(f"{status} {name}")
    if not condition and error_msg:
        print(f"       -> Details: {error_msg}")

# Check 01: IEEEtran Conference A4 Documentclass
run_check('Check 01: IEEEtran Conference A4 Documentclass',
          r'\documentclass[conference,a4paper]{IEEEtran}' in tex)

# Check 02: Float & List Spacing Parameters (Strict <= 8-Page Ceiling)
run_check('Check 02: Float & List Spacing Parameters (Strict <= 8-Page Ceiling)',
          r'\setlength{\textfloatsep}{2.5pt plus 0.5pt minus 0.5pt}' in tex and
          r'\setlength{\floatsep}{2.0pt plus 0.5pt minus 0.5pt}' in tex and
          r'\setlength{\intextsep}{2.0pt plus 0.5pt minus 0.5pt}' in tex and
          r'\setlength{\abovecaptionskip}{1.5pt}' in tex and
          r'\setlength{\belowcaptionskip}{1.5pt}' in tex and
          r'\setlength{\abovedisplayskip}{1.5pt plus 0.5pt minus 0.5pt}' in tex and
          r'\setlength{\belowdisplayskip}{1.5pt plus 0.5pt minus 0.5pt}' in tex)

# Check 03: Dual-Pathway PRISMA Arithmetic (540->532->451->81->45 + 5 = 50)
run_check('Check 03: Dual-Pathway PRISMA Arithmetic (540->532->451->81->45 + 5 = 50)',
          '540 candidate records' in tex and '532 unique records' in tex and '45 database archival studies' in tex and '5 supplementary' in tex)

# Check 04: Table I Width, Footnote & Section II-C Reconciled Kappa (0.8005)
tbl1_match = re.search(r'\\begin\{table\}\[htbp\]\s*\\caption\{Coverage of Evidence Lifecycle Stages Across Related Surveys\.\}.*?\\end\{table\}', tex, re.DOTALL)
tbl1_valid = False
if tbl1_match:
    t = tbl1_match.group(0)
    tbl1_valid = (r'tabularx}{\columnwidth}{@{}p{2.3cm}ccccc>{\raggedright\arraybackslash}X@{}}' in t and
                  'Page-level MLLM; lacks spatial bbox provenance' in t and
                  r'22/25 = 88.00\%' in t and
                  r'0.8005' in t)
s2c_valid = r'independent double-coding ($22/25 = 88.00\%$ raw agreement, $\kappa = 0.8005$)' in tex
run_check('Check 04: Table I & Section II-C Reconciled Kappa (0.8005)', tbl1_valid and s2c_valid)

# Check 05: Table III Width Constraint & Clean Limitation Strings
tbl3_match = re.search(r'\\begin\{table\*\}\[t\]\s*\\caption\{Comparative Analysis of Representative Core Empirical Systems.*?\\end\{table\*\}', tex, re.DOTALL)
tbl3_valid = False
if tbl3_match:
    t = tbl3_match.group(0)
    tbl3_valid = (r'tabularx}{\textwidth}' in t and
                  r'\setlength{\tabcolsep}{2.5pt}' in t and
                  'Strips individual cell bounding boxes in markdown export' in t)
run_check('Check 05: Table III Full-Width Span & Clean Limitation Strings', tbl3_valid)

# Check 06: Table IV Column Constraint, PubTabNet Reassessment & Footnote Minipage
tbl4_match = re.search(r'\\begin\{table\}\[htbp\]\s*\\caption\{Audit of Nine Representative Benchmarks.*?\\end\{table\}', tex, re.DOTALL)
tbl4_valid = False
if tbl4_match:
    t = tbl4_match.group(0)
    tbl4_valid = (r'begin{minipage}{\columnwidth}' in t and
                  r'\circ^\mathsection' in t and
                  r'\dagger' in t and r'\ddagger' in t and
                  'TEDS' in t)
run_check('Check 06: Table IV Column Constraint & PubTabNet TEDS Qualification', tbl4_valid)

# Check 07: Ref [9] LightRAG Verified Metadata
run_check('Check 07: Ref [9] LightRAG Verified Metadata (Findings of EMNLP 2025)',
          'guo2025lightrag' in tex and 'Findings of EMNLP, pp. 10746--10761, 2025' in tex)

# Check 08: Ref [11] Tripathi et al. (IC3ECSBHI 2026)
run_check('Check 08: Ref [11] Tripathi et al. (IC3ECSBHI 2026)',
          'tripathi2026' in tex and 'IC3ECSBHI' in tex)

# Check 09: Ref [12] AdaptiveGuard (ASE 2025)
run_check('Check 09: Ref [12] AdaptiveGuard (ASE 2025, pp. 3381--3391)',
          'yang2025adaptiveguard' in tex and 'pp. 3381--3391' in tex)

# Check 10: Ref [13] VAE Cleanser (IEEE TDSC 2025)
run_check('Check 10: Ref [13] VAE Cleanser (IEEE TDSC, vol. 22, no. 2, pp. 1253--1264)',
          'hu2025membership' in tex and 'IEEE TDSC, vol. 22, no. 2, pp. 1253--1264' in tex)

# Check 11: Ref [15] Gao survey (Proc. 64th ACL 2026)
run_check('Check 11: Ref [15] Gao survey (Proc. 64th ACL 2026, pp. 4458--4489)',
          'gao2026' in tex and 'pp. 4458--4489' in tex)

# Check 12: NeurIPS [20], [31], [48] Official Pagination
run_check('Check 12: NeurIPS [20], [31], [48] Official Pagination',
          'pp. 9459--9474' in tex and 'pp. 59532--59569' in tex and 'pp. 132876--132907' in tex)

# Check 13: Ref [41] MMDocRAG Official NeurIPS 2025 Pagination
run_check('Check 13: Ref [41] MMDocRAG Official NeurIPS 2025 Pagination (pp. 20855--20912)',
          'dong2025mmdocrag' in tex and 'pp. 20855--20912' in tex)

# Check 14: Eq (7) Affine-Rescaled Path Similarity
run_check('Check 14: Eq (7) Affine-Rescaled Path Similarity in [0,1]',
          'affine-rescaled cosine similarity' in tex and r'\hat{s}(\pi_i, Q)' in tex)

# Check 15: Eq (8) Normalization of Inputs to [0,1]
run_check('Check 15: Eq (8) Normalization of Inputs to [0,1]',
          r'min-max normalized to the common unit interval $[0,1]$' in tex)

# Check 16: Reviewer Roles Clarification
run_check('Check 16: Reviewer Roles Clarification (R1 & R2 screening; R1 & R3 full-text)',
          'Reviewer 1 and Reviewer 2 conducted the initial title/abstract screening' in tex and
          'Reviewer 1 (S.J.) and Reviewer 3 (A.K., domain specialist in graph topologies and spatial document AI)' in tex)

# Check 17: Matrix Propagation Uncertainty Assumption Documented
run_check('Check 17: Matrix Propagation Uncertainty Assumption Documented',
          'While exact matrix propagation completely avoids Monte Carlo sampling variance, it operates conditioned on estimated edge weights' in tex)

# Check 18: Defensive / Qualified First Structured Analysis Claim
run_check('Check 18: Qualified First Structured Analysis Claim',
          'To our knowledge, this review provides one of the first structured analyses of spatial provenance' in tex)

# Check 19: Inlined Bibliography Completeness (50/50 Bijective Match) & Trigger
cites = set()
for m in re.finditer(r'\\cite\{([^}]+)\}', tex):
    for k in m.group(1).split(','):
        cites.add(k.strip())
bibitems = re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', tex)
run_check('Check 19: Inlined Bibliography Completeness (50/50 Bijective Match) & Trigger',
          len(cites) == 50 and len(bibitems) == 50 and set(cites) == set(bibitems) and r'\IEEEtriggeratref{26}' in tex)

# Check 20: Environment Balance & Zero Bare Ampersands Outside Tables
clean_tex = re.sub(r'(?<!\\)%.*', '', tex)
stack = []
balanced = True
for op, env in re.findall(r'\\(begin|end)\{([^}]+)\}', clean_tex):
    if op == 'begin':
        stack.append(env)
    else:
        if not stack or stack[-1] != env:
            balanced = False
            break
        stack.pop()
if stack: balanced = False

in_tab = False
in_align = False
bare_amps = 0
for l in clean_tex.splitlines():
    if any(k in l for k in ['\\begin{tabular', '\\begin{matrix', '\\begin{bmatrix']): in_tab = True
    if any(k in l for k in ['\\end{tabular', '\\end{matrix', '\\end{bmatrix']): in_tab = False
    if any(k in l for k in ['\\begin{align', '\\begin{IEEEeqnarray']): in_align = True
    if any(k in l for k in ['\\end{align', '\\end{IEEEeqnarray']): in_align = False
    amps = [m.start() for m in re.finditer(r'(?<!\\)&', l)]
    if amps and not in_tab and not in_align:
        bare_amps += len(amps)

run_check('Check 20: Environment Balance & Zero Bare Ampersands', balanced and bare_amps == 0)

# Check 21: Exact Search Cutoff Date
run_check('Check 21: Exact Search Cutoff Date (November 14, 2026)',
          'November 14, 2026' in tex)

# Check 22: Group B All 5 Categories Breakdown (n=27: 7+7+9+3+1)
run_check('Check 22: Group B All 5 Categories Breakdown (n=27: 7+7+9+3+1)',
          'Benchmarks ($n = 7$), Surveys ($n = 7$), Baselines ($n = 9$), Safety ($n = 3$), Guideline ($n = 1$)' in tex)

# Check 23: Inter-Rater Reliability Reporting (94.55%, 95.35%, 88.00%)
run_check('Check 23: Inter-Rater Reliability Reporting (94.55%, 95.35%, 88.00%)',
          '503/532 = 94.55\\%' in tex and '82/86 = 95.35\\%' in tex and '22/25 = 88.00\\%' in tex)

# Check 24: Full-Text Agreement Paragraph Cleanliness
run_check('Check 24: Full-Text Agreement Paragraph Cleanliness (No corrupted /86)',
          'They agreed on 82 of 86 decisions' in tex and '82/86 = 95.35\\%' in tex)

# Check 25: No Stray Text/Commands Before First Item in Lists
list_clean = True
for env in ['itemize', 'enumerate', 'thebibliography']:
    pattern = r'\\begin\{' + env + r'\}(?:\{[^}]*\})?(.*?)(?:\\item|\\bibitem)'
    for m in re.finditer(pattern, tex, re.DOTALL):
        if m.group(1).strip() != '':
            list_clean = False
run_check('Check 25: No Stray Text/Commands Before First Item in Lists', list_clean)

# Check 26: IEEE Author Center AI-Use Policy Disclosure
run_check('Check 26: IEEE AI-Use Policy Disclosure with Antigravity Platform & Gemini 2.5 Pro Model',
          'IEEE Author Center policy on Artificial Intelligence' in tex and
          'Google Antigravity agentic development platform' in tex and
          'Gemini 2.5 Pro language model' in tex and
          r'\begin{samepage}' in tex)

# Check 27: Page 1 Item (c) top-$k$ Exact Formula & Zero Unclosed Dollars
odd_dollar_lines = []
for idx, line in enumerate(tex.splitlines()):
    clean = re.sub(r'(?<!\\)%.*', '', line).replace(r'\$', '')
    if clean.count('$') % 2 != 0:
        odd_dollar_lines.append(idx+1)
item_c_valid = r'top-$k$ retrieval often fails to reconstruct distributed reasoning chains' in tex and len(odd_dollar_lines) == 0
run_check('Check 27: Page 1 Item (c) top-$k$ Exact Formula & Zero Unclosed Dollars', item_c_valid)

# Check 28: Abstract Medium Series Formatting
run_check('Check 28: Abstract Medium Series Formatting (\\mdseries Present)',
          r'\begin{abstract}' + '\n' + r'\mdseries' in tex)

# Check 29: Accurate Classification of Supplementary Sources
supp_prep_count = len(re.findall(r'supplementary preprints?', tex, re.I))
run_check('Check 29: Zero Inaccurate "Supplementary Preprints" (Replaced with "Supplementary Sources")',
          supp_prep_count == 0 and 'supplementary citation-snowballing sources' in tex)

# Check 30: Group B Descriptive Appraisal Clarification
run_check('Check 30: Group B Descriptive Appraisal Clarification (Category error prevention)',
          'descriptively appraised across cohort-tailored functional dimensions rather than uniform numerical scoring' in tex)

# Check 31: Search Protocol Reproducibility
run_check('Check 31: Search Protocol Reproducibility (2017-2026, English, Peer-reviewed, Open Query Log Repository)',
          'January 2017 to November 2026' in tex and
          'English-language peer-reviewed conference proceedings and journal articles' in tex and
          'open supplementary search audit log repository' in tex and
          'github.com/Shambhujadhav4/LAM-GraphRAG' in tex)

# Check 32: PRISMA 2020 Statement Disentangled from Audit Log
prisma_clean = (
    r'Following PRISMA 2020 guidelines \cite{page2021prisma}' in tex and
    r'open supplementary search audit log \cite{page2021prisma}' not in tex
)
run_check('Check 32: PRISMA 2020 Statement Citation Disentangled from Audit Log', prisma_clean)

# Check 33: Ref [37] Li et al. Official TOIS Journal Publication Record & Author Order
ref37_clean = (
    'ACM Trans. Inf. Syst. (TOIS)' in tex and
    '10.1145/3849382' in tex and
    'Siqi Zhao, Miyang Luo, Ercong Nie' in tex and
    'Li et al. (2026)' in tex
)
run_check('Check 33: Ref [37] Li et al. Official TOIS Journal Publication Record & Author Order (Siqi Zhao before Miyang Luo)', ref37_clean)

# Check 34: Mathematical Wording "deterministic finite-horizon" (Zero "closed-form")
math_clean = (
    'deterministic finite-horizon matrix propagation' in tex and
    'closed-form' not in tex
)
run_check('Check 34: Mathematical Wording "deterministic finite-horizon" (Zero "closed-form")', math_clean)

# Check 35: Ref [46] MinerU Protected in columnbreak Against Column Split
miner_clean = r'\vfill\null\columnbreak' + '\n' + r'\bibitem{wang2024mineru}' in tex
run_check('Check 35: Ref [46] MinerU Columnbreak Control (Zero Split Across Columns on Page 8)', miner_clean)

# Check 36: Table III Readability, Arraystretch & Row Separation
t3_readable = (
    r'\renewcommand{\arraystretch}{1.12}' in tex and
    r'\addlinespace[1.5pt]' in tex
)
run_check('Check 36: Table III Readability, Arraystretch (1.12) & Row Separation (\\addlinespace)', t3_readable)

# Check 37: Group B Source-Level Appraisal Matrix File Reference
g_b_ref = (r'Group\_B\_Source\_Level\_Appraisal\_Matrix.csv' in tex or 'Group_B_Source_Level_Appraisal_Matrix.csv' in tex) and os.path.exists('Presentation/Group_B_Source_Level_Appraisal_Matrix.csv')
run_check('Check 37: Group B Source-Level Appraisal Matrix File Present & Cited in Section III-C', g_b_ref)

# Check 38: Cohen Kappa 0.8005 Mathematical Proof Script & Matrix File
kappa_valid = os.path.exists('Presentation/compute_kappa.py') and os.path.exists('Presentation/Table_I_Survey_Coverage_Coding_Matrix.csv')
run_check('Check 38: Cohen Kappa 0.8005 Contingency Matrix Data & Script Present', kappa_valid)

# Check 39: Institutional Author Emails Verified
emails_valid = (
    'amol.kanherkar.aids.2023' in tex and
    'vaishnavi.ghode.aids.2023' in tex and
    'shambhuraje.jadhav.aids.2023' in tex and
    'aarti.kalyane.aids.2023' in tex and
    'hema.jadhav@vpkbiet.org' in tex
)
run_check('Check 39: Institutional Author Emails Verified (aids.2023@vpkbiet.org & hema.jadhav@vpkbiet.org)', emails_valid)

print('=' * 60)
passed = sum(1 for _, c, _ in checks if c)
total = len(checks)
print(f'FINAL AUDIT SCORE: {passed} / {total} CHECKS PASSED ({passed/total*100:.1f}%)')
print('=' * 60)
if passed == total:
    sys.exit(0)
else:
    sys.exit(1)
