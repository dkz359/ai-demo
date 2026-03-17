# AI Demo

一个展示各种 AI 框架和大语言模型集成的 Python 示例项目。

## 项目简介

本项目汇集了多个主流 AI 框架的示例代码，涵盖了大语言模型(LLM)、智能体(Agent)、检索增强生成(RAG)等技术的实践应用。特别关注中文大模型（如通义千问、DeepSeek）与各种框架的集成。

## 项目结构

```
ai-demo/
├── agent-demo/          # 自定义智能体实现（ReAct 模式）
├── autogen-demo/        # Microsoft AutoGen 多智能体框架
├── langchain-demo/      # LangChain 框架集成
├── openai-demo/         # OpenAI SDK 使用示例
├── phidata-demo/        # PhiData 智能体框架
├── rag-demo/            # 检索增强生成(RAG)实现
├── smolagents-demo/     # Hugging Face SmolAgents
└── swarm-demo/          # OpenAI Swarm 多智能体编排
```

## 快速开始

### 1. 环境准备

确保已安装 Python 3.8+，然后安装依赖：

```bash
pip install -r requirements.txt
```

### 2. 配置 API 密钥

在项目根目录创建 `.env` 文件，添加所需的 API 密钥：

```env
OPENAI_API_KEY=your_openai_api_key
DASHSCOPE_API_KEY=your_dashscope_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
SERPAPI_KEY=your_serpapi_key
```

### 3. 运行示例

每个 demo 都是独立的 Python 脚本，可以直接运行：

```bash
# 智能体示例
python agent-demo/get-weather/run_agent.py

# AutoGen 示例
python autogen-demo/hello-autogen.py

# LangChain 示例
python langchain-demo/tongyi-qwen-demo/tongyi-langchain-demo.py

# OpenAI SDK 示例
python openai-demo/deepseek-openai-demo.py

# PhiData 示例
python phidata-demo/hello-phidata.py

# RAG 示例
python rag-demo/rag-from-scratch.py

# SmolAgents 示例
python smolagents-demo/hello-smolagents.py

# Swarm 示例
python swarm-demo/deepseek-swarm-demo.py
```

## 各模块说明

### agent-demo
展示了从零实现的智能体，使用 ReAct（推理+行动）模式进行工具调用和任务执行。包含天气查询和景点推荐的完整示例。

### autogen-demo
使用 Microsoft 的 AutoGen 框架创建多智能体对话系统，支持异步执行和 OpenAI 兼容 API。

### langchain-demo
LangChain 框架与通义千问模型的集成示例，展示了链式调用、提示词模板等功能。

### openai-demo
使用 OpenAI SDK 调用 DeepSeek API 的示例，展示了 OpenAI 兼容接口的使用方式。

### phidata-demo
PhiData 智能体框架的使用示例，包含 RAG 智能体和网络搜索智能体。

### rag-demo
从零实现的检索增强生成系统，使用 ChromaDB 进行向量存储，通义千问进行文本生成。

### smolagents-demo
Hugging Face 的轻量级智能体框架，支持通过 Python 代码执行来调用工具。

### swarm-demo
OpenAI 发布的轻量级多智能体编排框架，专注于智能体之间的交接(handoff)模式。

## 技术栈

- **LLM 提供商**：OpenAI、通义千问(DashScope)、DeepSeek
- **框架**：LangChain、AutoGen、PhiData、SmolAgents、Swarm
- **向量数据库**：ChromaDB
- **工具集成**：SerpAPI 搜索、DuckDuckGo、SQLAlchemy

## 学习资源

- [LangChain 文档](https://python.langchain.com/)
- [AutoGen 文档](https://microsoft.github.io/autogen/)
- [SmolAgents 博客](https://huggingface.co/blog/smolagents)
- [Swarm GitHub](https://github.com/openai/swarm)
- [通义千问文档](https://help.aliyun.com/zh/dashscope/)

## 许可证

本项目仅供学习和参考使用。

## 贡献

欢迎提交 Issue 和 Pull Request！
