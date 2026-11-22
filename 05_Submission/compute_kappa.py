import csv

with open('Presentation/Table_I_Survey_Coverage_Coding_Matrix.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

cats = ['Full', 'Partial', 'Out']
m = {r: {c: 0 for c in cats} for r in cats}
for row in rows:
    m[row['RevA']][row['RevB']] += 1

total = len(rows)
agreements = sum(m[c][c] for c in cats)

print('RevA \\ RevB   Full  Partial  Out  Total')
for r in cats:
    tot = sum(m[r][c] for c in cats)
    print('%-12s %4d %8d %4d  %5d' % (r, m[r]['Full'], m[r]['Partial'], m[r]['Out'], tot))

col_totals = {c: sum(m[r][c] for r in cats) for c in cats}
print('%-12s %4d %8d %4d  %5d' % ('Total', col_totals['Full'], col_totals['Partial'], col_totals['Out'], total))

po = agreements / total
pe = sum((sum(m[c][x] for x in cats) / total) * (col_totals[c] / total) for c in cats)
kappa = (po - pe) / (1 - pe)

print('\nObserved Agreement Po = %d/%d = %.4f (%.2f%%)' % (agreements, total, po, po*100))
print('Expected Agreement Pe = %.6f' % pe)
print('Cohen Kappa = %.6f (rounded: %.4f)' % (kappa, kappa))
