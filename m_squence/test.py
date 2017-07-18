#!/usr/bin/env python3
from .m_squence import Register
from .prn_out import prn_out


if __name__ == "__main__":
    prn = int(input("Input PRN number: "))
    out = prn_out[prn]
    # print(out)

    # Generator
    gen_1 = Register(10, [3, 10], 10)
    gen_2 = Register(10, [2, 3, 6, 8, 9, 10], out)
    CA = []
    for i in range(1023):
        g_1 = gen_1.shift()[0]
        g_2 = gen_2.shift()[0] ^ gen_2.shift()[1]
        CA.append(g_1 ^ g_2)

    CA_str = ''
    for item in CA:
        CA_str = CA_str + str(item)
    print(CA_str)
