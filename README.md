# IBM watsonx Orchestrate MCP Backend

A FastMCP-based backend server for IBM watsonx Orchestrate that provides climate risk assessment and mitigation planning tools.

## Features

- **Climate Risk Assessment**: Get risk assessments for different locations
- **Mitigation Planning**: Generate customized mitigation plans based on risk types

## Project Structure

```
watsonx-mcp-backend/
├── server.py           # Main MCP server implementation
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration for IBM Cloud Code Engine
├── venv/             # Virtual environment (not committed)
└── README.md         # This file
```

## Local Development Setup

### Prerequisites

- Python 3.11 or higher
- pip

### Installation

1. **Activate the virtual environment:**

   Windows (PowerShell):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   Windows (Command Prompt):
   ```cmd
   .\venv\Scripts\activate.bat
   ```

   Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```bash
   python server.py
   ```

   Or with uvicorn:
   ```bash
   uvicorn server:mcp.app --host 0.0.0.0 --port 8080
   ```

## Available Tools

### 1. get_climate_risk

Get climate risk assessment for a location.

**Input:**
- `location` (string): Location name (e.g., "Mumbai", "Delhi")

**Output:**
- Risk assessment string

**Example responses:**
- Mumbai → "High Flood Risk"
- Delhi → "Severe Heatwave"
- Others → "Low Risk"

### 2. generate_mitigation_plan

Generate mitigation advice based on risk type.

**Input:**
- `risk_type` (string): Type of risk (e.g., "Flood", "Heatwave")

**Output:**
- Detailed mitigation plan with actionable steps

## Docker Deployment

### Build the Docker image:

```bash
docker build -t watsonx-mcp-backend .
```

### Run locally with Docker:

```bash
docker run -p 8080:8080 watsonx-mcp-backend
```

## IBM Cloud Code Engine Deployment

### Prerequisites

- IBM Cloud account
- IBM Cloud CLI installed
- Code Engine plugin installed

### Deployment Steps

1. **Login to IBM Cloud:**
   ```bash
   ibmcloud login
   ```

2. **Target your Code Engine project:**
   ```bash
   ibmcloud ce project select --name <your-project-name>
   ```

3. **Build and deploy:**
   ```bash
   ibmcloud ce application create \
     --name watsonx-mcp-backend \
     --build-source . \
     --port 8080 \
     --min-scale 1 \
     --max-scale 5
   ```

4. **Get the application URL:**
   ```bash
   ibmcloud ce application get --name watsonx-mcp-backend
   ```

## API Endpoints

Once deployed, the MCP server exposes standard MCP protocol endpoints:

- Health check: `GET /health`
- MCP protocol: `POST /mcp`

## Environment Variables

- `PORT`: Server port (default: 8080)
- `HOST`: Server host (default: 0.0.0.0)

## Development Notes

- The server uses mock data for climate risk assessments
- In production, integrate with real climate data APIs
- Extend with additional tools as needed for watsonx Orchestrate

## License

MIT License