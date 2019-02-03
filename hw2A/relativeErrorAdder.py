def relative_error_adder(M1, M2, E1, E2):
    exact1_large = M1 / (1 - E1)
    exact1_small = M1 / (E1 + 1)
    exact2_large = M2 / (1 - E2)
    exact2_small = M2 / (E2 + 1)

    result_small_small = abs(M1 + M2 - exact1_small - exact2_small) / (exact1_small + exact2_small)
    result_large_large = abs(M1 + M2 - exact1_large - exact2_large) / (exact1_large + exact2_large)

    if result_small_small > result_large_large:
        print(result_small_small, "smaller win")
        print(result_large_large)
        return result_small_small
    else:
        print(result_small_small)
        print(result_large_large, "larger win")
        return result_large_large


print(relative_error_adder(293.5, 295.7, 0.08, 0.06))
