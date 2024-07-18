import enum


class OAuth2SSOProvider(str, enum.Enum):
    google = "google"
    github = "github"
    authentik = "authentik"


class ChatRole(str, enum.Enum):
    system = "system"
    user = "user"
    assistant = "assistant"


class FilterType(str, enum.Enum):
    llm = "llm"
    python = "python"


class APIProvider(str, enum.Enum):
    openai = "openai"
    together = "together"
    llama3 = "llama3"


class CompetitionPhase(str, enum.Enum):
    preparation = "preparation"
    defense = "defense"
    reconnaissance = "reconnaissance"
    evaluation = "evaluation"
    finished = "finished"
