import requests

BASE_URL = "https://projecteuler.net/problem="


def find_puzzles_by_keyword(keyword_: str) -> list[str]:
    """Retrieves the list of pages containing the keyword.

    Args:
        keyword_ (str): _description_

    Returns:
        list[str]: _description_
    """
    keyword_ = keyword_.strip().lower()
    pages = []
    for page_nb in range(
        1, 826
    ):  # to do : find the max number of pages. Hardcoded for now
        url = BASE_URL + str(page_nb)
        text = requests.get(url).text
        if (
            keyword_ in text.lower()
        ):  # potential improvements : use regex, use semantic proximity score
            print(page_nb)
            pages.append(page_nb)
    return pages


if __name__ == "__main__":
    find_puzzles_by_keyword("chess")
