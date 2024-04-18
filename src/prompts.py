def create_apology_letter_prompt(blame: str, hoxy: str) -> str:
    system_prompt = open("prompts/system.txt", "r").read()
    one_shot_blame = open("prompts/one_shot_blame.txt", "r").read()
    one_shot_answer = open("prompts/one_shot_answer.txt", "r").read()

    return f"""{system_prompt}

-----

**불만 내용**:
{one_shot_blame}

**사과문**:
{one_shot_answer}

-----

**불만 내용**:
{blame}

**나의 기분**:
{hoxy}

**사과문**:
"""


def create_cot_prompt(apology_letter: str) -> str:
    cot_prompt = open("prompts/chain_of_though.txt", "r").read()

    return f"""{cot_prompt}

**사과문**:
{apology_letter}

**평가**:
"""
