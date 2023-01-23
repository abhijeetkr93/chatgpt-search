from enum import Enum


class ModelTypes(Enum):
    TEXT_QA = "text-qa"
    TEXT_COMPLETION = "text-completion"
    TEXT_LONG_QA = "text-long-qa"
    TEXT_ML = "text-ml"
    CODE = "code"

    def __repr__(self) -> str:
        return f"ModelTypes.{self.name}"


CODE_KEYWORDS = [
    "javascript",
    "array",
    "data",
    "algorithm",
    "python",
    "js",
    "node",
    "py",
    "mysql",
    "postgres",
    "database",
    "tech",
    "coding",
    "error",
    "bug",
    "console",
    "terminal",
    "vue",
    "react",
    "express",
    "angular",
    "mongo",
    "gcp",
    "aws",
    "azure",
    "network",
]
