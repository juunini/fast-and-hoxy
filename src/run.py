from langchain_core.language_models.chat_models import BaseChatModel

from src.prompts import create_apology_letter_prompt, create_cot_prompt


def run(model: BaseChatModel, blame: str, hoxy: str) -> str:
    apology_letter_prompt = create_apology_letter_prompt(blame, hoxy)

    print("\033[0;32m1차 프롬프트\033[0m:")
    print(apology_letter_prompt)
    print("\n────────────────────\n")

    apology_letter = model.invoke(apology_letter_prompt).content

    print("\033[0;32m1차 결과\033[0m:")
    print(apology_letter)
    print("\n────────────────────\n")

    cot_prompt = create_cot_prompt(apology_letter)

    print("\033[0;32m2차 프롬프트\033[0m:")
    print(cot_prompt)
    print("\n────────────────────\n")

    fixed_apology_letter = model.invoke(cot_prompt).content

    return fixed_apology_letter
