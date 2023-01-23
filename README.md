# chatgpt-search simple package for quick search

chatgpt-search pypi is a simple integration of openAI chatGPT-3.0 models like (text-davinci-003, code-davinci-002, text-curie-001, text-babbage-001, text-ada-001 etc.) with python 
to feed your queries answers in terminal.

> Tips: *update ```models.toml``` for tuning models based on your need and use-cases.* 

## Installation
### From Pypi
```
$ pip install chatgpt-search
```

### Source code
```sh
$ pipenv --python 3.9.13
$ pipenv shell
$ git clone https://github.com/mbroton/chatgpt-api.git
```

## Usage

### As a Command Line Interface

#### Setup
set env 'CHATGPT_KEY' for api queries. get free api key by signing up here `https://beta.openai.com/signup`

```sh
$ export CHATGPT_KEY='XXXXXXXXXXXXX'
$ python -m search
or 
$ python src/search/__main__.py
```
you get the prompt to put any queries.
```sh
Ask Anything (type exit to close):
```
type 'exit' if you want to close it. 

#### Start Searching

![tobedeleted](https://media.giphy.com/media/eAoIiKFEGg1wzXxanx/giphy.gif)


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This is a personal project, not affiliated in any way with OpenAI. If you have any objections, contact @abhijeetkr93.

