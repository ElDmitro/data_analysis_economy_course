from collections import OrderedDict


FIRST_PARTY_DENOMINATOR = 450


votes = OrderedDict()
total_votes = 0
with open('input.txt') as input_stream:
    for line in input_stream:
        party, party_votes = line.rsplit(maxsplit=1)
        votes[party] = int(party_votes)
        total_votes += int(party_votes)

first_party_partial = total_votes / FIRST_PARTY_DENOMINATOR
tickets = OrderedDict()
ratios = OrderedDict()
total_tickets = 0
for key, value in votes.items():
    tickets[key] = value // first_party_partial
    ratios[key] = (value / first_party_partial) % 1
    total_tickets += value // first_party_partial

tickets_left = FIRST_PARTY_DENOMINATOR - total_tickets
for key, value in sorted(ratios.items(), key=lambda party: -party[1]):
    if tickets_left <= 0:
        break
    tickets[key] += 1
    tickets_left -= 1

for key, value in tickets.items():
    print(key, int(value))
