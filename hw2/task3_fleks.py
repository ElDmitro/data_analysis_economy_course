import math
import sys
from collections import defaultdict


class BankStorage:
    def __init__(self, logstream):
        self._storage = defaultdict(int)
        self._logstream = logstream
        self._cmd_line_map = {
            'DEPOSIT': self._add_deposit,
            'INCOME': self._income_entrance,
            'WITHDRAW': self._withdraw,
            'BALANCE': self._dump_balance,
            'TRANSFER': self._transfer,
        }

    def _mocked_cmd(self, *args):
        pass

    def _add_deposit(self, name, value):
        value = int(value)
        self._storage[name] += value

    def _income_entrance(self, bonus):
        bonus = int(bonus) / 100
        for name, value in self._storage.items():
            if value < 0:
                continue
            self._storage[name] += math.floor(value * bonus)

    def _withdraw(self, name, value):
        value = int(value)
        self._storage[name] -= value

    def _dump_balance(self, name):
        if name not in self._storage:
            self._logstream.write('ERROR\n')
            return
        self._logstream.write(str(self._storage[name]) + '\n')

    def _transfer(self, name_left, name_right, value):
        value = int(value)
        self._storage[name_left] -= value
        self._storage[name_right] += value

    def run_cmd(self, cmd, *args):
        cmd = self._cmd_line_map.get(cmd, self._mocked_cmd)
        cmd(*args)


storage = BankStorage(sys.stdout)
with open('input.txt') as input_stream:
    for line in input_stream:
        line = line.split()
        storage.run_cmd(line[0], *line[1:])
