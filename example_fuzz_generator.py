from typing import Final, TypeAlias, Iterable

T_ALPHABET: TypeAlias = str
T_WORD: TypeAlias = str

T_INDEX_OF_CHARACTER: TypeAlias = int

DEFAULT_ALPHABET: Final[T_ALPHABET] = '123'


def generate_2(word_length: int, quantity: int, alphabet: T_ALPHABET) -> Iterable[T_WORD]:
    min_index_of_character_in_alphabet: Final[T_INDEX_OF_CHARACTER] = 0
    max_index_of_character_in_alphabet: Final[T_INDEX_OF_CHARACTER] = len(alphabet) - 1

    word_as_list_of_indexes: list[T_INDEX_OF_CHARACTER] = [min_index_of_character_in_alphabet] * word_length

    current_position: int = len(word_as_list_of_indexes) - 1
    previous_position: int = current_position

    last_position: int = word_length - 1

    count = 0
    while count < quantity:

        if current_position == previous_position == last_position:
            if word_as_list_of_indexes[current_position] <= max_index_of_character_in_alphabet:
                yield ''.join([alphabet[index] for index in word_as_list_of_indexes])
                word_as_list_of_indexes[current_position] += 1
            else:
                word_as_list_of_indexes[current_position] = min_index_of_character_in_alphabet
                previous_position = current_position
                current_position -= 1
                # [0, 0, 0]


        elif current_position < previous_position:
            word_as_list_of_indexes[current_position] -= 1

            raise NotImplementedError(
                f'Not implemented. {word_as_list_of_indexes=}, {current_position=}, {previous_position=}'
            )


# def generate(word_length: int, quantity: int, alphabet: T_ALPHABET) -> list[T_WORD]:
#     index = 0
#     words_list = []
#     while len(words_list) != quantity:
#         for _ in range(word_length):
#             count = 0
#             if count != word_length:
#                 for letter in alphabet:
#                     word = ''
#                     word += letter + alphabet[count]
#                     words_list.append(word)
#             word = word + letter
#             # word = letter + some_string[count]
#             count += 1
#     return words_list


# 1. Последовательно добавление определенных символов до нужной длинны
# 2. Добавление слова в список
# 3. Переход к следующему символу последовательно, запоминая какие символы были использованны
# 111 -> берет первый символ и сумирует по длинне строки
# 112 -> берет первый символ и сумирует на 1 раз меньше + новый символ
# 113 -> берет первый символ и сумирует на 1 раз меньше + новый символ
# так как символ [0] использовался
# 121 ->
# 122
def main():
    alphabet = DEFAULT_ALPHABET

    # my_list = list(range(10))
    #
    # position__previous = 6
    # position__current = 7
    # my_list[position__current]

    # print()

    # print(generate(word_length=3, quantity=5, alphabet=alphabet))

    for word in generate_2(word_length=3, quantity=5, alphabet=alphabet):
        print(word)


if __name__ == '__main__':
    main()
