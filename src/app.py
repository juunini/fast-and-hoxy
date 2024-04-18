from src.azure_openai import run
import argparse


def parse_arguments() -> list[str]:
    parser = argparse.ArgumentParser(
        usage='poetry run <azure or google> "<blame>" "<hoxy>"'
    )
    parser.add_argument("blame", type=str, help="당신에게 온 불평을 쓰십시오")
    parser.add_argument("hoxy", type=str, help="당신의 심정을 쓰십시오")
    args = parser.parse_args()

    print("\n────────────────────\n")
    print(f"\033[0;32m- 불만 내용\033[0m: {args.blame}")
    print(f"\033[0;32m- 나의 기분\033[0m: {args.hoxy}")
    print("\n────────────────────\n")

    return [args.blame, args.hoxy]


def azure_openai():
    [blame, hoxy] = parse_arguments()

    ai_answer = run(blame, hoxy)

    print("\033[0;32m최종 답변\033[0m:")
    print(ai_answer)
