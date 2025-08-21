def slice_test(input: list[str]) -> list[str]:
    return input[slice(0, 1)]


print(slice_test(["0", "7", "4", "2"]))
