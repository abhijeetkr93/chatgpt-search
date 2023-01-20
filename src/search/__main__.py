# __main__.py

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from viewer import ChatGPTService, ConfigService

key = os.getenv("CHATGPT_KEY")
chatgpt_service = ChatGPTService(key)


def main():
    """Handle search query with ChatGPT"""

    # @todo: beautify using inquiry
    while True:
        question = input("Ask Anything (type exit to close): ")
        try:
            if question == "exit":
                break
            else:
                if not chatgpt_service.service_ok:
                    break
                model_type = ConfigService.get_model_type(query=question)
                chatgpt_service.conf_service = ConfigService(model_type)
                response = chatgpt_service.search_query(question)
                print(response)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
