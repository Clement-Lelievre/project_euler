"""70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.

What is the expected number of distinct colours in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij)."""
from random import choice
from multiprocessing import Pool

# the fact that I need to display the correct first nine digits tells me
# that Monte Carlo is not the way to go, but I still want to try


def draw(
    nb_colors: int = 7, nb_balls_per_color: int = 10, nb_balls_out: int = 20
) -> int:
    remaining_balls = list(range(nb_balls_per_color * nb_colors))
    if nb_balls_out > nb_colors * nb_balls_per_color:
        raise ValueError("Too many balls out")
    colors_drawn = set()
    for _ in range(nb_balls_out):
        remaining_balls.remove(ball_nb := choice(remaining_balls))
        colors_drawn.add(ball_nb // 10)
    return len(colors_drawn)


def simulate(n_sim: int) -> float:
    return sum(draw() for _ in range(n_sim))


def multi_process(n_sim: int = 10_000_000, n_proc: int = 8):
    with Pool(n_proc) as p:
        all_simulation_locations = p.map(simulate, [n_sim] * n_proc)
    print(sum(all_simulation_locations) / (n_proc * n_sim))


if __name__ == "__main__":
    multi_process()
