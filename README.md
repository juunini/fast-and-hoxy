# 빠르고 꼬운말

[빠르고 꼬운말 '만들어 줘'](https://velog.io/@juunini/fast-and-hoxy1)

## Install

```sh
git clone https://github.com/juunini/fast-and-hoxy.git
cd fast-and-hoxy
poetry install
```

## Config

`config.py` 파일을 수정합니다.

## Usage

### Azure OpenAI(ChatGPT)

```sh
poetry run chatgpt "요즘은 별 내용은 없고, 그냥 드립으로 도배 하는게 아티클 퀄임?
이거 좋다고 따봉 눌러주는 클라스하고는 연예인 개발자 되기 쉽고만" "꼬우면 님도 하셈ㅋㅋ"
```

### Google VertexAI(Gemini)

```sh
poetry run gemini "요즘은 별 내용은 없고, 그냥 드립으로 도배 하는게 아티클 퀄임?
이거 좋다고 따봉 눌러주는 클라스하고는 연예인 개발자 되기 쉽고만" "꼬우면 님도 하셈ㅋㅋ"
```
