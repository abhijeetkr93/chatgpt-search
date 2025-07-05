# chatgpt-search Pypi package for quick CLI search

[chatgpt-search](https://pypi.org/project/chatgpt-search/) pypi is a simple integration of openAI chatGPT-3.0 models like (text-davinci-003, code-davinci-002, text-curie-001, text-babbage-001, text-ada-001 etc.) with python 
to feed your queries answers in terminal.

> Tips: *update ```models.toml``` for tuning models based on your need and use-cases.* 

## Installation
### From Pypi
```
$ pip install chatgpt-search
```
![installpackage](https://media.giphy.com/media/hWJGpCAAclpyqyPoeN/giphy.gif)

### Source code
```sh
$ pipenv --python 3.9.13
$ pipenv shell
$ git clone https://github.com/abhijeetkr93/chatgpt-search.git
```

#### Setup
set env 'CHATGPT_KEY' for api queries. get free api key by signing up here `https://beta.openai.com/signup`

```sh
$ export CHATGPT_KEY='XXXXXXXXXXXXX'
$ python -m search
Ask Anything (type exit to close):
```
source code: *$ python src/search/__main__.py*

#### Start Playing
![writestory](https://media.giphy.com/media/e09ykfVdv4IDybFhpQ/giphy.gif)
![bucket-sort](https://media.giphy.com/media/yZtKPeVHgkYzKt5WgO/giphy.gif)
![explain-code](https://media.giphy.com/media/yHBfRBn0IGH6zvuOZd/giphy.gif)
![query](https://media.giphy.com/media/NmpD5uzyLOZxPQq3Qq/giphy.gif)
## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This is a personal project, not affiliated in any way with OpenAI. If you have any objections, contact @abhijeetkr93.

