import random
import concurrent.futures
from settings import CHARACTERS
from init_logging import init_logging


def generator_word(length: int = 10, conditions: str = CHARACTERS):
    some_word = ''
    for _ in range(length):
        some_word.append(random.choice(conditions))
    return "".join(some_word)


def generator_sync(quantity: int) -> list[str]:
    list_with_word = []
    for _ in range(quantity):
        list_with_word.append(generator_word())
    return list_with_word


def calculate_process(quantity) -> str:
    with concurrent.futures.ProcessPoolExecutor() as worker:
        results = worker.map(
            generator_word,
            quantity,
        )
        worker.submit(generator_word, args=(quantity[0],))
    return results


def main():
    start = 10
    quantity = list(range(start, start + 1000))
    print(calculate_process(quantity=quantity))
    # print()


if __name__ == "__main__":
    init_logging()
    main()
