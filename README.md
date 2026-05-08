# 🦞 RADAR: Research & Autonomous Deployment Analytics Robot

> **The World's First Autonomous Research-to-PR Pipeline for Enterprise Intelligence.**

RADAR is a state-of-the-art autonomous system designed for the **Samsung PRISM** hackathon. It doesn't just "monitor" research; it **acts** on it. By bridging the gap between global academic breakthroughs and production-grade codebases, RADAR ensures that engineering teams stay ahead of the curve through automated intelligence harvesting, semantic analysis, and autonomous code generation.

---

## 📺 Project Overview
RADAR is a multi-agent autonomous system that:
1.  **Harvests**: Scans ArXiv and Semantic Scholar for breakthroughs in NPU optimization, Mobile AI, and Security.
2.  **Analyzes**: Uses Large Language Models (LLMs) to map research opportunities to specific Samsung repositories.
3.  **Acts**: Autonomously generates code, opens Pull Requests, and creates GitHub Issues.
4.  **Broadcasts**: Sends real-time strategic trend alerts and threat intelligence to Telegram.

---

## 🛠️ Tech Stack
*   **Core**: Python 3.10+
*   **Orchestration**: [OpenClaw](https://openclaw.ai) (Agentic Gateway & Dashboard)
*   **LLMs**: Groq (Llama 3.3/3.1), Google Gemini 2.5 Flash, OpenRouter (Fallback Layer)
*   **Intelligence**: Sentence-Transformers (ML Clustering), Scikit-Learn
*   **Integrations**: GitHub API, Telegram Bot API, ArXiv API, Semantic Scholar API

---

## 🏗️ System Architecture
RADAR follows a modular "Member-based" architecture:
- **Member 1 (Strategy)**: Discovers organization context and maps repo structures.
- **Member 2 (The Harvester)**: Fetches multi-dimensional data (ArXiv, Scholar, Newsroom).
- **Member 3 (The Brain)**: Performs semantic relevance filtering and ML-based trend clustering.
- **Member 4 (The Communicator)**: Handles autonomous GitHub PRs, Issues, and Telegram Alerts.

---

## 🦞 Intensive OpenClaw Setup Guide

RADAR is powered by the **OpenClaw Multi-Agent Orchestrator**. Follow these steps to set up the autonomous control center.

### 1. Installation & Initialization
First, install the OpenClaw CLI globally and initialize your workspace:
```bash
# Install CLI
npm install -g openclaw

# Initialize OpenClaw in your project directory
npx openclaw init
```

### 2. Model Selection (AI Brain)
OpenClaw needs an AI model to understand your commands. You can choose between **Groq** (fastest) or **Gemini**.

**To configure your model:**
1. Open `~/.openclaw/openclaw.json` (or `C:\Users\<User>\.openclaw\openclaw.json` on Windows).
2. Set your primary model. 

**Recommended (Groq - Llama 3.1):**
```json
"model": {
  "primary": "groq/llama-3.1-8b-instant"
}
```
*(Note: Ensure your `GROQ_API_KEY` is set in your system Environment Variables for the gateway to see it.)*

### 3. Launching the Gateway
The Gateway is the background engine that runs your agents and cron jobs.
```bash
# Start the Gateway service
npx openclaw gateway start
```
*If you see a firewall prompt, click "Allow Access". The gateway runs on port `18789` by default.*

### 4. Setting up Autonomous Cron Jobs (Autonomy)
To make RADAR truly autonomous, add the scheduled heartbeats:
```bash
# Add a 9AM Daily Pipeline run
npx openclaw cron add --name "RADAR Daily Pipeline" --cron "0 9 * * *" --agent radar --message "/radar-run"

# Add a 6-Hour Strategic Scan
npx openclaw cron add --name "6-Hour Threat Scan" --cron "0 */6 * * *" --agent radar --message "/radar-alert"
```

### 5. Accessing the Control Dashboard
The Dashboard is where you interact with RADAR, see logs, and monitor live research runs.
```bash
# Open the Web UI
npx openclaw dashboard
```
*   **Chat Tab**: Talk to RADAR (type `/radar-status` to check health).
*   **Cron Tab**: See your scheduled jobs and run them manually for testing.
*   **Logs Tab**: Watch the AI's "Inner Monologue" as it analyzes Samsung's repos.

---

### 3. Environment Setup (.env)
Create a `.env` file in the root directory:
```env
# AI API Keys
GOOGLE_API_KEY=your_key
GROQ_API_KEY=your_key
OPENROUTER_API_KEY=your_key

# GitHub Integration
GITHUB_TOKEN=your_pat_token
GITHUB_ORG=Samsung
GITHUB_REPO=Sahitya3105/RIT_CodeRock

# Notifications
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_id
```

### 4. Running the Dashboard
To see RADAR in action through the GUI:
```bash
# Start the Gateway
npx openclaw gateway

# In a new terminal, open the Dashboard
npx openclaw dashboard
```

---

## ⚙️ How to obtain API Keys

### 1. Groq (Recommended for Speed)
1. Go to [Groq Console](https://console.groq.com/keys).
2. Create a free API Key.
3. Perfect for the fast-response dashboard chat.

### 2. Google Gemini
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Generate an API Key for `Gemini 1.5/2.5`.

### 3. Telegram (For Alerts)
1. Message `@BotFather` on Telegram to create a bot and get the `TOKEN`.
2. Message `@userinfobot` to get your `CHAT_ID`.

---

## 📅 Scheduling & Automation
RADAR uses OpenClaw Cron for true autonomy. Configuration lives in `~/.openclaw/cron/jobs.json`:

| Job Name | Schedule | Description |
|----------|----------|-------------|
| **Daily Pipeline** | `0 9 * * *` | Full research scan and PR submission at 9 AM daily. |
| **6-Hour Scan** | `0 */6 * * *` | Frequent threat detection and Telegram alerts. |
| **Weekly Trend** | `0 8 * * 1` | Strategic research digest every Monday. |

---

## 🧪 Demonstration Sequence
1. Open the **OpenClaw Dashboard**.
2. Type `/radar-run` in the chat.
3. Observe the `contracts/` directory in VS Code filling with live JSON data.
4. Watch the **Telegram** notification arrive.
5. Review the newly created **Pull Request** on GitHub.

---

## ⚖️ License
MIT License. Built with ❤️ by Sahitya & Team CodeRock for Samsung PRISM.
