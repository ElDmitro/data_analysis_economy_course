def split_phone(phone):
    phone = phone.strip()
    phone = phone.translate(str.maketrans('', '', '-()+'))
    if len(phone) < 10:
        return '495', phone[-7:]
    return phone[1:4], phone[-7:]


source_code, source_core = split_phone(input())
for i in range(3):
    tgt_code, tgt_core = split_phone(input())
    if tgt_code == source_code and tgt_core == source_core:
        print('YES')
    else:
        print('NO')
