from typing import List, Tuple, Union
from functools import reduce

with open('input.txt') as file:
    transmission = file.read()

sequence = ''.join(map(lambda h: bin(int(h, 16))[2:].zfill(4), list(transmission)))


class Literal:
    def __init__(self, version: int, content_bits: str):
        self.version = version
        self.value = int(content_bits, 2)

    def sum_version(self):
        return self.version

    def apply(self):
        return self.value


class Operator:
    def __init__(self, version: int, type_id: int, subpackets):
        self.version = version
        self.type_id = type_id
        self.subpackets: List[Union[Literal, Operator]] = subpackets

    def sum_version(self) -> int:
        return self.version + sum([p.sum_version() for p in self.subpackets])

    def apply(self) -> int:
        return {
            0: sum,
            1: lambda x: reduce(int.__mul__, x),
            2: min,
            3: max,
            5: lambda x: int(x[0] > x[1]),
            6: lambda x: int(x[0] < x[1]),
            7: lambda x: int(x[0] == x[1])
        }[self.type_id]([p.apply() for p in self.subpackets])


def parse_packet(sequence) -> Tuple[str, Union[Literal, Operator]]:
    version = int(sequence[:3], 2)
    type_id = int(sequence[3:6], 2)
    sequence = sequence[6:]
    if type_id == 4:  # Literal
        content = ''
        while sequence[0] == '1':
            content += sequence[1:5]
            sequence = sequence[5:]
        content += sequence[1:5]
        return sequence[5:], Literal(version, content)
    else:  # Operator
        subpackets: List[Union[Literal, Operator]] = []
        if sequence[0] == '0':
            subseq_length = int(sequence[1:16], 2)
            subpackets_sequence = sequence[16:16 + subseq_length]
            while subpackets_sequence:
                subpackets_sequence, p = parse_packet(subpackets_sequence)
                subpackets.append(p)
            sequence = sequence[16 + subseq_length:]
        else:
            operator_nr_packets = int(sequence[1:12], 2)
            sequence = sequence[12:]
            for _ in range(operator_nr_packets):
                sequence, p = parse_packet(sequence)
                subpackets.append(p)
        return sequence, Operator(version, type_id, subpackets)


_, packet = parse_packet(sequence)

# part 1
print(packet.sum_version())

# part 2
print(packet.apply())
