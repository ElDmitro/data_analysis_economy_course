nwitness = int(input())

witness_hypos = []
for i in range(nwitness):
    witness_hypos.append(set(input()))

ncar_number = int(input())
best_cands = []
cands_score = 0
for i in range(ncar_number):
    number = input()
    score = sum(hypo.intersection(set(number)) == hypo for hypo in witness_hypos)
    if score < cands_score:
        continue
    elif score == cands_score:
        best_cands.append(number)
    else:
        cands_score = score
        best_cands = [number]

print(*best_cands, sep='\n')
