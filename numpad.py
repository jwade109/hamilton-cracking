#!/usr/bin/env python

import itertools

def get_possible_passwords(key_sequence):

    phone_keys = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    keys = list()
    for num in key_sequence:
        if num not in phone_keys:
            raise ValueError("{} is not a supported number".format(num))
        if phone_keys[num]:
            keys.append(phone_keys[num])

    possible_list = list(itertools.product(*keys))
    ret = list()
    for elem in possible_list:
        ret.append("".join(elem))
    return ret
