## 📃 Flock (Flexible Low-code Orchestrating Collaborative-agent Kits)

<p align="center">
  <a href="./docs/README_cn.md">简体中文</a> |
  <a href="./README.md">English</a> |
  <a href="./docs/README_ja.md">日本語</a> |
  <a href="#how-to-get-started">Getting Started</a>
</p>

> [!NOTE]

> ### 🎉 What's New 2024/12/18
>
> - **If-Else Node**: Added If-Else node to support conditional logic in workflows! The node supports various condition types including Contains, Not contains, Start with, End with, Is, Is not, Is empty, and Is not empty. Multiple conditions can be combined using AND/OR operators for complex conditional logic, allowing you to create sophisticated branching workflows based on your data.

> ### 🎉 What's New 2024/12/7
>
> - **Code Execution Node**: Added Python code execution capabilities to workflows! This node allows you to write and execute Python scripts directly within your workflow, supporting variable references and dynamic data transformations. Perfect for arithmetic operations, data processing, text manipulation, and custom logic that goes beyond preset node functionalities.

> ### 🎉 What's New 2024/11/12
>
> - **Intent Recognition Node**: New Intent Recognition node that can automatically identify user input intent based on preset categories, supporting multi-classification routing!
>   <img src="assets/intent.png" alt="intent recognition" width="500" />
>
> - **CrewAI Node Support**: Now you can leverage CrewAI's powerful multi-agent capabilities in your workflows! Create sophisticated agent teams and orchestrate complex collaborative tasks with ease.
>   <img src="assets/crewai.jpg" alt="crewai" width="500"  />

### Flock is a workflow-based low-code platform for rapidly building chatbots, RAG applications, and coordinating multi-agent teams. Built on LangChain and LangGraph, it provides a flexible, low-code orchestrating solution for collaborative agents, supporting chatbots, RAG applications, agents, and multi-agent systems, with the capability for offline operation.

<video src="https://private-user-images.githubusercontent.com/49232224/386539219-5dc96133-72f3-4cc3-9f50-096c38bde715.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE2NjMzNDQsIm5iZiI6MTczMTY2MzA0NCwicGF0aCI6Ii80OTIzMjIyNC8zODY1MzkyMTktNWRjOTYxMzMtNzJmMy00Y2MzLTlmNTAtMDk2YzM4YmRlNzE1Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE1VDA5MzA0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVhOWY1NTc1Mjk5YWU1MjZmNmQyNmY3Mzk0YjY2MGYyMzlmZWQ2MTVkMjExODEwNmY3YmMxYTVmNGRhNzMxZWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.69R3pTktxrl8C6tdduABLiRhkhwdfeVO3vlGGTGK4to" data-canonical-src="https://private-user-images.githubusercontent.com/49232224/386539219-5dc96133-72f3-4cc3-9f50-096c38bde715.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE2NjMzNDQsIm5iZiI6MTczMTY2MzA0NCwicGF0aCI6Ii80OTIzMjIyNC8zODY1MzkyMTktNWRjOTYxMzMtNzJmMy00Y2MzLTlmNTAtMDk2YzM4YmRlNzE1Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE1VDA5MzA0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVhOWY1NTc1Mjk5YWU1MjZmNmQyNmY3Mzk0YjY2MGYyMzlmZWQ2MTVkMjExODEwNmY3YmMxYTVmNGRhNzMxZWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.69R3pTktxrl8C6tdduABLiRhkhwdfeVO3vlGGTGK4to" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px">
 </video>

### 🤖️ Overview

 <img src="assets/Overview.png" alt="overview"  />

### Work Flow

 <img src="assets/workflow.png" alt="overview"  />

### Node Types and Functions

Flock's workflow system consists of various node types, each serving a specific purpose:

1. Input Node: Processes initial input and converts it into a format the workflow can handle.
2. LLM Node: Utilizes large language models for text generation and processing.
3. Retrieval Node: Fetches relevant information from knowledge bases.
4. Tool Node: Executes specific tasks or operations, extending workflow functionality.
5. Retrieval Tool Node: Combines retrieval capabilities with tool functionality.
6. Intent Recognition Node: Automatically identifies user input intent based on preset categories and routes to different processing flows.
7. Answer Node: Generates final answers or outputs, integrating results from previous nodes.
8. Subgraph Node: Encapsulates a complete sub-workflow, allowing for modular design.
9. Start and End Nodes: Mark the beginning and end of the workflow.

Future planned nodes include:

- Conditional Branch Node (If-Else)
- File Upload Node
- Code Execution Node
- Parameter Extraction Node

These nodes can be combined to create powerful and flexible workflows suitable for various complex business needs and application scenarios.

### Image Tools use

![image](https://github.com/user-attachments/assets/4097b087-0309-4aab-8be9-a06fdc9d4964)

### Knowledge Retrieval

![image](https://github.com/user-attachments/assets/836fac80-ab49-4f6b-973c-25ba173149eb)

### Human in the loop (human approval or let the LLM rethink or ask human for help)

<p>
  <img src="https://github.com/user-attachments/assets/ec53f7de-10cb-4001-897a-2695da9cf6bf" alt="image" style="width: 49%; display: inline-block;">
  <img src="https://github.com/user-attachments/assets/1c7d383d-e6bf-42b8-94ec-9f0c37be19b8" alt="image" style="width: 49%; display: inline-block;">
</p>

Inspired by the [StreetLamb](https://github.com/StreetLamb) project and its [tribe](https://github.com/StreetLamb/tribe) project , Flock adopts much of the approach and code.
Building on this foundation, it introduces some new features and directions of its own.

Some of the layout in this project references [Lobe-chat](https://github.com/lobehub/lobe-chat), [Dify](https://github.com/langgenius/dify), and [fastgpt](https://github.com/labring/FastGPT).
They are all excellent open-source projects, thanks🙇‍.

### 👨‍💻 Development

Project tech stack: LangChain + LangGraph + React + Next.js + Chakra UI + PostgreSQL

> [!NOTE]
>
> ### 🤖 Model System
>
> Flock supports various model providers and makes it easy to add new ones. Check out our [Models Guide](./docs/Add_New_Model_Providers_Guide.md) to learn about supported models and how to add support for new providers.

> ### 🛠️ Tools System
>
> Flock comes with various built-in tools and supports easy integration of custom tools. Check out our [Tools Guide](./docs/Add_New_Tools_Guide.md) to learn about available tools and how to add your own.

### 💡RoadMap

1 APP

- [x] ChatBot
- [x] SimpleRAG
- [x] Hierarchical Agent
- [x] Sequential Agent
- [x] Work-Flow
- [x] Intent Recognition Node - Automatically identify user input intent and route to different processing flows
- [x] CrewAI Integration
- [ ] More muti-agent ---On Progress

2 Model

- [x] OpenAI
- [x] ZhipuAI
- [x] Siliconflow
- [x] Ollama
- [x] Qwen
- [ ] Xinference

3 Ohters

- [x] Tools Calling
- [x] I18n
- [ ] Langchain Templates

### 🏘️Highlights

- Persistent conversations: Save and maintain chat histories, allowing you to continue conversations.
- Observability: Monitor and track your agents’ performance and outputs in real-time using LangSmith to ensure they operate efficiently.
- Tool Calling: Enable your agents to utilize external tools and APIs.
- Retrieval Augmented Generation: Enable your agents to reason with your internal knowledge base.
- Human-In-The-Loop: Enable human approval before tool calling.
- Open Source Models: Use open-source LLM models such as llama, Qwen and Glm.
- Multi-Tenancy: Manage and support multiple users and teams.

### How to get started

#### 1. Preparation

##### 1.1 Clone the Code

git clone https://github.com/Onelevenvy/flock.git

##### 1.2 Copy Environment Configuration File

```bash
cp .env.example .env
```

##### 1.3 Generate Secret Keys

Some environment variables in the .env file have a default value of changethis.
You have to change them with a secret key, to generate secret keys you can run the following command:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copy the content and use that as password / secret key. And run that again to generate another secure key.

##### 1.3 Insatll postgres，qdrant,redis

```bash
cd docker
docker compose  --env-file ../.env up -d
```

#### 2.Run Backend

##### 2.1 Installation of the basic environment

Server startup requires Python 3.10.x. It is recommended to use pyenv for quick installation of the Python environment.

To install additional Python versions, use pyenv install.

```bash
pyenv install 3.10
```

To switch to the "3.10" Python environment, use the following command:

```bash
pyenv global 3.10
```

Follow these steps :
Navigate to the "backen" directory:

```bash
cd backend
```

activate the environment.

```bash
poetry env use 3.10
poetry install
```

##### 2.2 initiral data

```bash
# Let the DB start
python /app/app/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /app/app/initial_data.py
```

##### 2.3 run unicorn

```bash
 uvicorn app.main:app --reload --log-level debug
```

##### 2.4 run celery (Not necessary, unless you want to use the rag function)

```bash
poetry run celery -A app.core.celery_app.celery_app worker --loglevel=debug
poetry run celery -A app.core.celery_app.celery_app worker -l info -P solo
```

#### 3.Run Frontend

##### 3.1 Enter the web directory and install the dependencies

```bash
cd web
pnpm install
```

##### 3.2 Start the web service

```bash
cd web
pnpm dev

# or pnpm build then pnpm start
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Onelevenvy/flock&type=Date)](https://star-history.com/#Onelevenvy/flock&Date)
