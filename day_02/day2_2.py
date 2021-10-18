import math
from typing import List
from day2_input import intcode


TARGET = 19690720

def compute_output(input_code: List[int], noun: int, verb: int):
    code = input_code.copy()
    code[1] = noun
    code[2] = verb
    n_instructions = math.ceil(len(code) / 4)

    for i in range(n_instructions):
        base_i = i*4
        product = 0
        if code[base_i] == 99:
            break
        if code[base_i] == 1:
            product = code[code[base_i + 1]] + code[code[base_i + 2]]
        elif code[base_i] == 2:
            product = code[code[base_i + 1]] * code[code[base_i + 2]]
        code[code[base_i + 3]] = product

    return intcode[0]

target_noun = 0
target_verb = 0

for i_noun in range(99):
    for i_verb in range(99):
        output = compute_output(intcode, i_noun, i_verb)
        if output == TARGET:
            target_noun, target_verb = i_noun, i_verb
            break

print(100 * target_noun + target_verb)
