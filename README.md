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

## 🦞 OpenClaw Integration
RADAR is fully integrated as an **OpenClaw Agent**. This provides:
- **Autonomous Scheduling**: Cron-based heartbeats for continuous background operation.
- **Control Dashboard**: A web-based UI (`http://127.0.0.1:18789`) to trigger runs and monitor AI logs.
- **Skill System**: Native commands like `/radar-run`, `/radar-status`, and `/radar-pr`.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- **Python 3.10+** installed.
- **Node.js 18+** (for the OpenClaw Gateway).
- A **GitHub Personal Access Token** (with `repo` scopes).

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Sahitya3105/RIT_CodeRock.git
cd RIT_CodeRock

# Install dependencies
pip install -r requirements.txt

# Initialize OpenClaw
npm install -g openclaw
npx openclaw init
```

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
