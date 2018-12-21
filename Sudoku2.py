rows = '123456789'
cols = 'ABCDEFGHI'
cells = [c + r for r in rows for c in cols]
rows3 = ['123','456','789']
cols3 = ['ABC','DEF','GHI']
sqrs3 =  [(c,r) for r in rows3 for c in cols3]
sqrs = [a+b for r,c in sqrs3 for a in r for b in c]
