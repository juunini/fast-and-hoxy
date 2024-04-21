import argparse
from langchain_core.language_models.chat_models import BaseChatModel

from src.models import azure_openai, google_vertexai
from src.run import run


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


def chatgpt():
    answer(azure_openai())


def gemini():
    answer(google_vertexai())


def answer(model: BaseChatModel):
    [blame, hoxy] = parse_arguments()

    ai_answer = run(model, blame, hoxy)

    print("\033[0;32m최종 답변\033[0m:")
    print(ai_answer)
