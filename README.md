# CHATGPT-SEARCH simple package for quick search

The CHATGPT-SEARCH is a simple integration of openAI-chatGPT-3.0 to feed your query answers in your terminal. 

Work in Progress! :)

## Installation
### From Pypi
```
pip install chatgpt-search
```

### Source code
```sh
pipenv --python 3.9.13
pipenv shell
pipenv install
```

## Usage

### As a Command Line Interface

#### Setup

Required to authenticate. In this step you have to provide a path to the file containing the session key. A simple txt file with the key only is enough.
```sh
chatgpt setup
```

*Tip: Use a file named .session_key in chatgpt-api top directory. It will be ignored by git - see .gitignore.*

The key will be saved to
```python
Path.home() / ".chatgpt_api" / "key.txt"
```

Session messages are logged to
```python
Path.home() / ".chatgpt_api" / "logs"
```

#### Start chatting

```sh
chatgpt start
![]http://www.giphy.com/gifs/eAoIiKFEGg1wzXxanx
```


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This is a personal project, not affiliated in any way with OpenAI. If you have any objections, contact @abhijeetkr93.

