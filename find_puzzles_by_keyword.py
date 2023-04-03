from typing import Iterable
import requests

BASE_URL = "https://projecteuler.net/problem="


def find_puzzles_by_keyword(kws: Iterable[str]) -> list[str]:
    """Retrieves the list of pages containing the keyword.

    Args:
        keyword_ (Iterable[str]): the list of keywords

    Returns:
        list[str]: _description_
    """
    if not kws:
        return []
    kws = [keyword_.strip().lower() for keyword_ in kws]
    pages = []
    for page_nb in range(
        1, 826
    ):  # to do : find the max number of pages. Hardcoded for now
        url = BASE_URL + str(page_nb)
        text = requests.get(url).text
        if any(
            keyword_ in text.lower() for keyword_ in kws
        ):  # potential improvements : use regex, use semantic proximity score
            print(page_nb)
            pages.append(page_nb)
    return pages


if __name__ == "__main__":
    find_puzzles_by_keyword(["machine learning", "data science"])
