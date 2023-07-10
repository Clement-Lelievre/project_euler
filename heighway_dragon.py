"""https://projecteuler.net/problem=220

I computed the first few expansions:
Fa
FaRbFR
FaRbFRRLFaLbFR
FaRbFRRLFaLbFRRLFaRbFRLLFaLbFR

FaRbFRRLFaLbFRRLFaRbFRLLFaLbFRRLFaRbFRRLFaLbFRLLFaRbFRLLFaLbFR

FaRbFRRLFaLbFRRLFaRbFRLLFaLbFRRLFaRbFRRLFaLbFRLLFaRbFRLLFaLbFRRLFaRbFRRLFaLbFRRLFaRbFRLLFaLbFRLLFaRbFRRLFaLbFRLLFaRbFRLLFaLbFR

FaRbFRRLFaLbFRRLFaRbFRLLFaLbFRRLFaRbFRRLFaLbFRLLFaRbFRLLFaLbFRRLFaRbFRRLFaLbFRRLFaRbFRLLFaLbFRLLFaRbFRRLFaLbFRLLFaRbFRLLFaLbFRRLFaRbFRRLFaLbFRRLFaRbFRLLFaLbFRRLFaRbFRRLFaLbFRLLFaRbFRLLFaLbFRLLFaRbFRRLFaLbFRRLFaRbFRLLFaLbFRLLFaRbFRRLFaLbFRLLFaRbFRLLFaLbFR
"""


def compute(seq: str, loc: tuple[int], heading: str) -> tuple[tuple[int], str]:
    """Computes the location and heading after following the given sequence.

    Args:
        seq (str): _description_
        loc (tuple[int]): _description_
        heading (str): _description_

    Returns:
        tuple[tuple[int], str]: _description_
    """
    assert heading in ("U", "D", "L", "R")
    for char in seq:
        if char == "F":
            if heading == "U":
                loc = (loc[0], loc[1] + 1)
            elif heading == "D":
                loc = (loc[0], loc[1] - 1)
            elif heading == "L":
                loc = (loc[0] - 1, loc[1])
            elif heading == "R":
                loc = (loc[0] + 1, loc[1])
        elif char == "L":
            if heading == "U":
                heading = "L"
            elif heading == "D":
                heading = "R"
            elif heading == "L":
                heading = "D"
            elif heading == "R":
                heading = "U"
        elif char == "R":
            if heading == "U":
                heading = "R"
            elif heading == "D":
                heading = "L"
            elif heading == "L":
                heading = "U"
            elif heading == "R":
                heading = "D"
    return loc, heading

def move(current_loc: tuple[int], vector: tuple[int], heading: str) -> tuple[tuple[int], str]:
    """Moves the current location in the given direction.

    Args:
        current_loc (tuple[int]): _description_
        vector (tuple[int]): _description_
        heading (str): _description_

    Returns:
        tuple[tuple[int], str]: _description_
    """
    if heading == "U":
        return (current_loc[0] + vector[0], current_loc[1] + vector[1]), heading
    if heading == "D":
        return (current_loc[0] - vector[0], current_loc[1] - vector[1]), heading
    if heading == "L":
        return (current_loc[0] - vector[1], current_loc[1] + vector[0]), heading
    if heading == "R":
        return (current_loc[0] + vector[1], current_loc[1] - vector[0]), heading


def get_pos_after(n: int) -> str:
    assert n >= 3
    minus_two, minus_one = "FaRbFR", "FaRbFRRLFaLbFR"
    previous_half = "FaLbFR"
    posminus1, headingminus1 = compute(minus_one, (0, 0), "U")
    posminus2, headingminus2 = compute(minus_two, (0, 0), "U")
    previous_half, headingprevious = compute(previous_half, (0, 0), "U")
    # for _ in range(n - 2):
    #     next_seq = minus_one + 'RL' + minus_two + 'LL' + previous_half
    #     previous_half = minus_two + 'LL' + previous_half
    #     minus_two, minus_one = minus_one, next_seq
    for _ in range(n - 2):
        new_pos = 


if __name__ == "__main__":
    print(len(get_pos_after(30)))
