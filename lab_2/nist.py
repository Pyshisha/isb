import math

from scipy.special import gammainc

from constants import PI


def bit_frequency_test(sequence) :

    sum_sequence = 0.0

    for bit in sequence:
        if bit =="1":
            sum_sequence+=1

    sum_sequence /= math.sqrt(len(sequence))
    p_value = math.erfc(sum_sequence / math.sqrt(2))

    return p_value

def test_for_identical_consecutive_bits(sequence):

    share_of_units = 0.0

    for bit in sequence:
        if bit == "1":
            share_of_units += 1

    share_of_units /=len(sequence)

    if abs(share_of_units-0.5) >= 2/math.sqrt(len(sequence)):
        return 0.0

    number_of_sign_alternations = 0.0
    for i in range(len(sequence)-1):
        if sequence[i]==sequence[i+1]:
            number_of_sign_alternations+=1

    p_value=(math.erfc((abs(number_of_sign_alternations-2*len(sequence)*share_of_units*(1- share_of_units)))/(2*math.sqrt(2*len(sequence))*share_of_units*(1- share_of_units))))

    return p_value

def test_for_the_longest_sequence_of_ones(sequence):
    v=[0, 0, 0, 0]

    block_size = 8

    for i in range(0, len(sequence), block_size):
        block = sequence[i:i + block_size]
        max_len = 0
        current_len = 0

        for bit in block:
            if bit == '1':
                current_len += 1
                if current_len > max_len:
                    max_len = current_len
            else:
                current_len = 0

        if max_len <= 1:
            v[0]+=1
        if max_len == 2:
            v[1]+=1
        if max_len == 3:
            v[2]+=1
        if max_len >= 4:
            v[3]+=1

        hi_square = 0.0

        for i in range(4):
            hi_square += ((v[i]-16*PI[i])**2)/16*PI[i]

        p_value = gammainc(1.5, hi_square / 2)

        return p_value

def tests(sequence):

    p_value = bit_frequency_test(sequence)
    conclusion = "Passed" if p_value >= 0.01 else "Failed"

    p_value = test_for_identical_consecutive_bits(sequence)
    conclusion = "Passed" if p_value >= 0.01 else "Failed"

    p_value = test_for_the_longest_sequence_of_ones(sequence)
    conclusion = "Passed" if p_value >= 0.01 else "Failed"