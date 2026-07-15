import argparse
import sys
from .generator import PasswordGenerator
from .constants import WORD_LIST

COLORS = {
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "reset": "\033[0m",
}


def color_text(text: str, color: str) -> str:
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"


def main():
    parser = argparse.ArgumentParser(
        description="Безопасный генератор паролей с дополнительными функциями."
    )
    parser.add_argument(
        "-l", "--length", type=int, default=16,
        help="Длина пароля (по умолчанию 16)"
    )
    parser.add_argument(
        "--no-lower", action="store_true",
        help="Исключить строчные буквы"
    )
    parser.add_argument(
        "--no-upper", action="store_true",
        help="Исключить прописные буквы"
    )
    parser.add_argument(
        "--no-digits", action="store_true",
        help="Исключить цифры"
    )
    parser.add_argument(
        "--no-special", action="store_true",
        help="Исключить специальные символы"
    )
    parser.add_argument(
        "--no-ambiguous", action="store_true",
        help="Исключить неоднозначные символы (l, I, 1, 0, O и т.п.)"
    )
    parser.add_argument(
        "-p", "--phrase", action="store_true",
        help="Сгенерировать пароль-фразу из слов вместо обычного"
    )
    parser.add_argument(
        "-w", "--words", type=int, default=4,
        help="Количество слов в фразе (только с --phrase)"
    )
    parser.add_argument(
        "-s", "--separator", type=str, default="-",
        help="Разделитель для фразы (по умолчанию '-')"
    )
    parser.add_argument(
        "--no-phrase-digits", action="store_true",
        help="Не добавлять цифры в фразу"
    )
    parser.add_argument(
        "--phrase-digits-count", type=int, default=2,
        help="Количество цифр в конце фразы"
    )
    parser.add_argument(
        "--no-capitalize", action="store_true",
        help="Не делать первую букву каждого слова заглавной (в фразе)"
    )
    parser.add_argument(
        "-e", "--entropy", action="store_true",
        help="Показать энтропию и оценку стойкости сгенерированного пароля"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=1,
        help="Количество паролей для генерации (по умолчанию 1)"
    )

    args = parser.parse_args()

    gen = PasswordGenerator(
        length=args.length,
        use_lower=not args.no_lower,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_special=not args.no_special,
        ambiguous=not args.no_ambiguous,
    )

    try:
        if args.phrase:
            #Генерация фраз
            for i in range(args.count):
                password = gen.generate_phrase(
                    words=args.words,
                    separator=args.separator,
                    add_digits=not args.no_phrase_digits,
                    digit_count=args.phrase_digits_count,
                    capitalize=not args.no_capitalize,
                )
                print_password(password, gen, args.entropy)
        else:
            #Генерация обычных паролей
            for i in range(args.count):
                password = gen.generate()
                print_password(password, gen, args.entropy)
    except ValueError as e:
        print(color_text(f"Ошибка: {e}", "red"), file=sys.stderr)
        sys.exit(1)


def print_password(password: str, gen: PasswordGenerator, show_entropy: bool):
    print(color_text(password, "green"))
    if show_entropy:
        ent = gen.entropy(password)
        label = gen.strength_label(ent)
        print(
            f"  {color_text('Энтропия:', 'yellow')} {ent:.1f} бит  "
            f"({color_text(label, 'yellow')})"
        )


if __name__ == "__main__":
    main()
