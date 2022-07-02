import concurrent.futures
import logging
from typing import Iterator

from settings import CHARACTERS
from init_logging import init_logging
from fuzz_generator import generate, DEFAULT_ALPHABET


def generator_word(length: int = 5, quantity: int = len(CHARACTERS) + 1, conditions: str = CHARACTERS):
    logging.info(generate(word_length=length, quantity=quantity, alphabet=conditions))
    return generate


def calculate_thread(quantity: list[int]) -> list[str]:
    with concurrent.futures.ThreadPoolExecutor() as worker:
        futures = [
            worker.submit(generator_word, number) for number in quantity
        ]
        items = concurrent.futures.as_completed(futures)
    return items


# def calculate_process(quantity: list[int]) -> list[str]:
#     with concurrent.futures.ProcessPoolExecutor() as worker:
#         results = worker.map(
#             generator_word,
#             quantity,
#         )
#         worker.submit(generator_word, args=(quantity[0],))
#     return results


def main():
    alphabet = DEFAULT_ALPHABET
    word_length = 5
    quantity = len(CHARACTERS)
    combinations = list(range(1, quantity + 1))
    # calculate_process(quantity=combinations)
    calculate_thread(quantity=combinations)
    print()


if __name__ == "__main__":
    init_logging()
    main()
