# viewer.py
import os
import json
import openai
import pathlib

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
except Exception as err:
    print(f"error: {err}")


class ConfigService:
    """
    set configuration based on usability
    """
    def __init__(self) -> None:
        _cfg = {"chatgpt": {}}
        # print('********************')
        # print(pathlib.Path().absolute())
        # print(os.path.abspath(os.path.dirname(__file__)))
        # @todo: dynamic enough to serve different type of queries
        with open("src/search/config.toml", "rb") as conf:
            _cfg = tomllib.load(conf)
        self.MODEL = _cfg["chatgpt"].get("model")
        self.TEMP = _cfg["chatgpt"].get("temperature", 0)
        self.MAX_TOKENS = _cfg["chatgpt"].get("max_tokens", 100)
        self.TOP_P = _cfg["chatgpt"].get("top_p", 1)
        self.FREQ_PENALTY = _cfg["chatgpt"].get("frequency_penalty", 0.0)
        self.PRES_PENALTY = _cfg["chatgpt"].get("presence_penalty", 0.0)


class ChatGPTService:
    def __init__(self, key=None):
        self.key = key
        self.service_ok = False
        self._initialise_key()
        self.cnf = ConfigService()

    def _initialise_key(self):
        try:
            if self.key:
                openai.api_key = self.key
                self.service_ok = True
            else:
                print("please set openai key env var: CHATGPT_KEY")
        except Exception as err:
            print(f"invalid key: {err}")

    @staticmethod
    def create_prompt(question: str) -> str:
        """
        create prompt for search query in models
        """
        payload = {
            "query": f"{question}",
            "num_results": 2,
            "filters": {
                "date_range": {"start": "2022-01-01", "end": "2023-12-31"},
                "language": "en",
            },
            "sort_by": "relevance",
        }
        return json.dumps({"prompt": "search", "query": payload})

    def search_query(self, query: str) -> str:
        """
        execute search query to openai engine
        """

        try:
            # response = openai.Completion.create(
            #     engine="text-davinci-002",
            #     prompt=ChatGPTService.create_prompt(query),
            #     max_tokens=100
            # )
            response = openai.Completion.create(
                model=self.cnf.MODEL,
                prompt=f"/*{query}*/",
                temperature=self.cnf.TEMP,
                max_tokens=self.cnf.MAX_TOKENS,
                top_p=self.cnf.TOP_P,
                frequency_penalty=self.cnf.FREQ_PENALTY,
                presence_penalty=self.cnf.PRES_PENALTY,
            )
            print(response)
            response = response["choices"][0]["text"]
            return response
        except Exception as err:
            print(f'error: {err}')
            return "Unknown"

