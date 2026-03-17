# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python AI/LLM demo repository showcasing integration with various AI frameworks and Chinese language models. The project contains standalone demos organized by technology:

- **agent-demo/** - Custom agent implementation with tool-calling loop pattern (ReAct-style)
- **autogen-demo/** - Microsoft AutoGen framework for multi-agent conversations
- **langchain-demo/** - LangChain framework integrations with Tongyi Qwen models
- **openai-demo/** - OpenAI SDK usage with DeepSeek API compatibility
- **phidata-demo/** - PhiData agent framework with RAG and web search tools
- **rag-demo/** - Retrieval-Augmented Generation implementation from scratch
- **smolagents-demo/** - Hugging Face's lightweight agent framework examples
- **swarm-demo/** - OpenAI's lightweight multi-agent orchestration framework

## Running Scripts

Each demo is a standalone Python script. Run them directly:

```bash
python agent-demo/get-weather/run_agent.py
python autogen-demo/hello-autogen.py
python langchain-demo/tongyi-qwen-demo/tongyi-langchain-demo.py
python openai-demo/deepseek-openai-demo.py
python phidata-demo/hello-phidata.py
python rag-demo/rag-from-scratch.py
python smolagents-demo/hello-smolagents.py
python swarm-demo/deepseek-swarm-demo.py
```

## Configuration

API keys are managed via `.env` file in the project root. The project uses `python-dotenv` to load environment variables.

Required environment variables:
- `OPENAI_API_KEY` - For OpenAI GPT models (AutoGen, DeepSeek compatibility)
- `DASHSCOPE_API_KEY` - For Alibaba Tongyi Qwen models (embeddings, LLM)
- `DEEPSEEK_API_KEY` - For DeepSeek API (OpenAI-compatible endpoint)
- `SERPAPI_KEY` - For web search in smolagents demos

Install dependencies from requirements.txt:
```bash
pip install -r requirements.txt
```

## Architecture Notes

### Agent Framework Patterns
Most demos demonstrate the ReAct (Reasoning + Acting) pattern for tool calling:
1. **Thought** - LLM reasoning about what to do next
2. **Action** - Calling a tool/function with parameters
3. **Observation** - Receiving tool output
4. **Repeat** - Until task is complete

The `agent-demo/get-weather/` shows a pure Python implementation of this loop without any agent framework.

### SmolAgents Integration
- Uses `CodeAgent` class for tool calling via Python code execution
- Supports multiple LLM providers through LiteLLM wrapper: Ollama (mistral-nemo), OpenAI, Claude
- Custom tools are defined as Python functions with `@tool` decorator
- Reference: https://huggingface.co/blog/smolagents

### AutoGen Framework
- Uses async/await pattern for agent execution
- `OpenAIChatCompletionClient` can connect to OpenAI-compatible APIs (DeepSeek, Qwen, etc.)
- Agents are stateless - rely on Chat Completions API

### PhiData Agents
- Supports DeepSeek models via `DeepSeekChat` model class
- Built-in tools for web search and RAG
- Markdown-formatted responses
- Note: Some models don't support `developer` role, only `system`, `user`, `assistant`, `tool`

### RAG Pipeline
- ChromaDB for vector storage with DashScope embeddings (text-embedding-v3)
- WebBaseLoader with BeautifulSoup for HTML parsing
- LangChain Hub for prompt templates (e.g., `rlm/rag-prompt`)
- Tongyi LLM for generation

### LangChain + Tongyi
- Tongyi models from Alibaba's DashScope service
- Supports both LLM (`Tongyi`) and embeddings (`DashScopeEmbeddings`)
- Chinese language optimized

### Swarm (OpenAI)
- Educational framework for multi-agent orchestration
- Focuses on "handoffs" - agents can transfer conversations to other agents
- Lightweight, runs client-side with no state management between calls
- Not production-ready, experimental/educational only
- Works with OpenAI-compatible APIs via custom base_url

### OpenAI-Compatible APIs
Many Chinese LLM providers (DeepSeek, Tongyi Qwen) offer OpenAI-compatible endpoints:
- DeepSeek: `https://api.deepseek.com/v1`
- Tongyi Qwen: `https://dashscope.aliyuncs.com/compatible-mode/v1`
- Simply set `base_url` parameter when initializing OpenAI client

## Important: USER_AGENT Requirement
When using `WebBaseLoader`, `USER_AGENT` environment variable must be set BEFORE import (see rag-demo/rag-from-scratch.py:12-13)

## Code Style

- Chinese comments are used for AI-related functionality explanations
- Each demo script is self-contained with inline imports
- Environment loading follows pattern: `dotenv.load_dotenv()` at script start
