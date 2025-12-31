# Example Agent based off Agno Framework

This repository includes:
- A small **pre-built Agent** to use as a starting point
- (More capabilities can be added)

## Installation

### Current Build Dependencies

#### System Requirements
- Python>=3.11,<4
- Inference Model, Base URL, API Key

#### Python Packages (See requirements.txt)
- `ag-ui-protocol`==0.1.10
- `agno`==2.3.21
- `agno-infra`==1.0.4
- `ddgs`==.10.0
- `fastapi[standard]`==0.121.3
- `litellm`>=1.80.0
- `mcp`>=1.21.2
- `psycopg2`>=2.9.11
- `sqlalchemy`>=2.0.44
- `uvicorn[standard]`==0.38.0

Note: Some packages are added here but not used in the example project. These are added to further use in next development cycles. 

## Setup
1. Clone the repository
    ```bash
    git clone git@github.com:shahchiragh/agno-agent.git
    cd agno-agent
    ```
2. Create and activate a Python virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure environment variables and source it:
    ```bash
    # LLM CONFIG
    MODEL_NAME={YOUR_MODEL_NAME}
    BASE_URL={YOUR_BASE_URL}
    API_KEY={YOUR_API_KEY}
    ```

## Usage

Start the Agent in interactive mode:

```bash
cd app/
python main.py
```