# Agent Coding Guidelines

This repository contains demos for various AI agent frameworks (AutoGen, LangChain, smolagents, phidata, Swarm, RAG implementations).

## Project Structure

```
ai-demo/
├── autogen-demo/          # AutoGen agent examples
├── langchain-demo/        # LangChain examples
│   └── tongyi-qwen-demo/  # Tongyi Qwen specific demos
├── openai-demo/           # OpenAI API demos
├── phidata-demo/          # Phi agent framework examples
├── rag-demo/              # RAG implementation examples
├── smolagents-demo/       # HuggingFace smolagents examples
├── swarm-demo/            # OpenAI Swarm examples
├── requirements.txt       # Python dependencies
└── test.ipynb             # Jupyter notebook for testing
```

## Commands

### Dependencies
```bash
pip install -r requirements.txt
```

### Running Demos
```bash
python autogen-demo/hello-autogen.py
python langchain-demo/hello-langchain.py
python smolagents-demo/hello-smolagents.py
```

### Testing
This project does not have a formal test suite. Test scripts interactively:
- Run demo scripts directly: `python <script-path>`
- Use Jupyter notebooks: `jupyter notebook test.ipynb`

### Running a Single Test (if pytest is added)
```bash
pytest tests/test_specific_feature.py -v
pytest tests/test_specific_feature.py::test_function_name -v
```

## Code Style Guidelines

### Python Version
- Target Python 3.10+ (uses type hints, structural pattern matching)

### Formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 120 characters
- Use blank lines to separate logical sections within functions
- Remove trailing whitespace

### Imports
- Group imports in order: standard library, third-party, local
- Use alphabetical ordering within groups
- Prefer absolute imports over relative imports
- Example:
```python
import asyncio
from typing import Optional

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
```

### Type Annotations
- Use type hints for function parameters and return values
- Use `Optional[X]` instead of `X | None` for compatibility
- Example:
```python
from typing import Optional

def get_weather(location: str, celsius: Optional[bool] = True) -> str:
    ...
```

### Naming Conventions
- Variables and functions: `snake_case` (e.g., `get_weather`, `total_amount`)
- Classes: `PascalCase` (e.g., `AssistantAgent`, `CodeAgent`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `API_TIMEOUT`)
- Private members: prefix with `_` (e.g., `_private_method`)

### Docstrings
- Use triple-quoted strings for module and function docstrings
- Document parameters, return values, and exceptions when non-trivial
- Chinese comments are acceptable for Chinese-speaking team context
- Example:
```python
def get_weather(location: str, celsius: Optional[bool] = True) -> str:
    """
    获取指定位置的实时天气信息

    Args:
        location: 位置名称(城市名)
        celsius: 是否使用摄氏度(默认True)

    Returns:
        格式化后的天气信息字符串
    """
```

### Error Handling
- Use specific exception types when possible
- Wrap external API calls in try-except blocks
- Return error messages as strings rather than raising exceptions for recoverable errors
- Example:
```python
try:
    response = requests.get(url)
    data = response.json()
except Exception as e:
    return f"获取天气信息时发生错误: {str(e)}"
```

### Environment Variables
- Load from `.env` file using `python-dotenv`
- Never hardcode API keys or secrets in source code
- Use `os.getenv()` or `dotenv.load_dotenv()`
- Example:
```python
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

### Async Code
- Use `async def` for asynchronous functions
- Use `asyncio.run()` or `asyncio.run_until_complete()` to execute
- Example:
```python
async def main() -> None:
    agent = AssistantAgent("assistant", model_client)
    result = await agent.run(task="Say 'Hello World!'")
    print(result)

asyncio.run(main())
```

### LLM/AI Agent Patterns
- Use framework-specific agent patterns (AutoGen, smolagents, etc.)
- Initialize agents with model and tools at construction time
- Keep prompts clear and specific
- Example:
```python
agent = CodeAgent(
    tools=[sql_engine],
    model=LiteLLMModel(model_id="gpt-4o-mini"),
)
```

### API Client Initialization
- Use environment variables for API keys
- Support configurable base URLs for API-compatible models
- Example:
```python
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
```

## Security Best Practices

1. **Never commit secrets**: Add `.env` to `.gitignore`
2. **Validate inputs**: Check user inputs before using in prompts or queries
3. **Sanitize outputs**: Be cautious with LLM-generated code or SQL
4. **Rate limiting**: Implement backoff for API calls
5. **Error messages**: Don't expose internal details in user-facing errors

## Git Conventions

- Branch naming: `feature/description` or `fix/description`
- Commit messages: Use clear, concise descriptions
- No commit of `.env` files or API keys
