# Integrating LLMs into DevOps Pipelines  
### Automatically analyzing CI/CD failures using Claude (Anthropic LLM)

This repository demonstrates how an LLM can be integrated directly into a CI/CD pipeline to automatically analyze and explain build or test failures.

---

## Project Overview
In this experiment, the CI/CD pipeline:
1. Executes a simple Python project that intentionally triggers a threading-related error.
2. Captures the pipeline logs on failure.
3. Sends those logs to the **Claude LLM (`claude-opus-4.1`)** via API.
4. Receives a human-readable explanation of the issue and possible fixes — right within the pipeline run.

This approach simulates how **AI can assist in DevOps debugging**, making failure analysis faster and more intuitive.

---

## Repository Structure
app.py → Sample Python script (introduces a race condition)
test_app.py → Test that fails due to threading issue
analyse_logs.py → Sends logs to Claude API for analysis
azure-pipelines.yml → Azure DevOps pipeline configuration

---

## How It Works
1. The `test_app.py` intentionally fails due to a race condition.  
2. The Azure DevOps pipeline catches the failure and triggers `analyse_logs.py`.  
3. The script uses the Anthropic API to send the log to Claude:
   ```python
   client = anthropic.Anthropic(api_key="YOUR_API_KEY")
   response = client.messages.create(
       model="claude-opus-4-1-20250805",
       max_tokens=300,
       temperature=0,
       messages=[{"role": "user", "content": log_text}]
   )
4. Claude responds with a detailed explanation and suggestions to fix the issue.
