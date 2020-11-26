import math
from collections import defaultdict


def add_deposit(storage, name, value):
    value = int(value)
    storage[name] += value


def income_entrance(storage, bonus):
    bonus = int(bonus) / 100
    for name, value in storage.items():
        if value < 0:
            continue
        storage[name] += math.floor(value * bonus)


def withdraw(storage, name, value):
    value = int(value)
    storage[name] -= value


def dump_balance(storage, name):
    if name not in storage:
        print('ERROR')
        return
    print(storage[name])


def transfer(storage, name_left, name_right, value):
    value = int(value)
    storage[name_left] -= value
    storage[name_right] += value


CMD_LINE_MAP = {
    'DEPOSIT': add_deposit,
    'INCOME': income_entrance,
    'WITHDRAW': withdraw,
    'BALANCE': dump_balance,
    'TRANSFER': transfer,
}


def mocked_cmd(storage, *args):
    pass


def parse_cmd(line):
    args = line.split()
    return CMD_LINE_MAP.get(args[0], mocked_cmd), args[1:]


storage = defaultdict(int)
with open('input.txt') as input_stream:
    for line in input_stream:
        cmd, args = parse_cmd(line)
        cmd(storage, *args)
