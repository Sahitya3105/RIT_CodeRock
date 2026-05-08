# 🦞 RADAR — Research & Autonomous Deployment Analytics Robot

> **The World's First Autonomous Research-to-PR Pipeline for Enterprise Intelligence**
> *Built for the Samsung PRISM Hackathon by Team CodeRock*

---

## 📋 Important Documents

| Document | Description |
|----------|-------------|
| 🎬 [DEMO.md](./DEMO.md) | **Live demo video link** — watch RADAR in action ,Kindly download the video to view in best quality|
| 📄 [RIT_CODEROCK.pdf](./RIT_CODEROCK.pdf) | Full project proposal, team details & technical architecture |
| 🤖 [OpenClaw_AI_Disclosure.docx](./OpenClaw_AI_Disclosure.docx) | AI tool usage disclosure as required by competition guidelines |
| 🏗️ [Architecture Diagram](./radar_architecture_diagram_1777053872297.png) | Visual system architecture of the full RADAR pipeline |
| ⚙️ [OpenClaw Setup Guide](./README_OPENCLAW.md) | Detailed OpenClaw agent configuration reference |

---

## 🚨 The Problem

Samsung and other enterprise technology companies publish research and ship products at extreme velocity. But the gap between **what global academia discovers** and **what engineering teams implement** is growing every year.

Today, a breakthrough paper on **NPU quantization** or **on-device LLM inference** is published on ArXiv. Samsung's engineers may not see it for weeks — or ever. Meanwhile, competitors like **Google DeepMind, Qualcomm, and Apple** are already acting on it.

**The cost of this gap:**
- Missed optimization opportunities in production codebases
- Delayed response to competitor moves
- Engineering teams manually scanning hundreds of papers with no systematic process
- No automated link between academic breakthroughs and actionable code changes

> *"By the time a human researcher reads, evaluates, and proposes implementation of a research paper — the window of competitive advantage has already closed."*

---

## 💡 Our Solution

RADAR is a **fully autonomous multi-agent system** that monitors the global AI research landscape and takes immediate action — no human intervention required. It:

1. **Harvests** breakthroughs from ArXiv and Semantic Scholar across domains relevant to Samsung (NPU, Mobile AI, Security, IoT).
2. **Analyzes** papers using LLMs to map research opportunities to specific Samsung repositories.
3. **Acts** by autonomously generating production-quality code and opening Pull Requests.
4. **Broadcasts** real-time strategic alerts and competitor threat intelligence via Telegram.
5. **Schedules** itself to repeat this pipeline every 24 hours — forever — without any human trigger.

---

## 🏗️ System Architecture

```
                        ┌─────────────────────────────────────┐
                        │         RADAR HEARTBEAT             │
                        │         (python main.py)            │
                        └──────────────┬──────────────────────┘
                                       │
          ┌────────────────────────────┼─────────────────────────────┐
          │                            │                             │
    ┌─────▼──────┐            ┌────────▼───────┐            ┌───────▼──────┐
    │  MEMBER 1  │            │   MEMBER 2     │            │  MEMBER 3    │
    │  Strategy  │            │  The Harvester │            │  The Brain   │
    │            │            │                │            │              │
    │org_scanner │            │ paper_fetcher  │            │process_papers│
    │            │            │ fetch_threats  │            │trend_analyzer│
    └─────┬──────┘            │ fetch_trends   │            └───────┬──────┘
          │                   └────────┬───────┘                    │
          │   org_profile.json         │   incoming_papers.json     │   pending_actions.json
          │                            │   threat_papers.json       │   live_trends.json
          └────────────────────────────┴────────────────────────────┘
                                       │
                              ┌────────▼───────┐
                              │   MEMBER 4     │
                              │ The Communicator│
                              │                │
                              │  auto_pr.py    │──────► GitHub Pull Requests
                              │  send_alert.py │──────► Telegram Alerts
                              │  trend_broadcast│─────► Telegram Trend Cards
                              └────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Core Language** | Python 3.10+ |
| **Orchestration** | OpenClaw (Agentic Gateway & Scheduler) |
| **Primary LLM** | Google Gemini 2.5 Flash |
| **Fallback LLM** | Groq (Llama 3.3 / 3.1) |
| **Tertiary LLM** | OpenRouter (Nemotron, Gemma — Free Tier) |
| **ML Clustering** | Sentence-Transformers + Scikit-Learn KMeans |
| **Research APIs** | ArXiv API, Semantic Scholar API |
| **Integrations** | GitHub API (PyGithub), Telegram Bot API |
| **Scheduling** | OpenClaw Cron + Windows Task Scheduler |

---

## 🚀 Quick Start — Run the Pipeline

### Step 1: Clone the Repository
```bash
git clone https://github.com/Sahitya3105/RIT_CodeRock.git
cd RIT_CodeRock
git checkout demo-recording
```

### Step 2: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
```bash
# Copy the example file
cp .env.example .env
```

Open `.env` and fill in your credentials:
```env
# AI Providers (at least one required)
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here

# GitHub Integration
GITHUB_TOKEN=your_github_personal_access_token_here
GITHUB_ORG=Samsung-PRISM-EdgeAI
GITHUB_REPO=Samsung-PRISM-EdgeAI/core-inference-engine

# Telegram Notifications
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
```

### Step 4: Run the Full Pipeline
```bash
python main.py
```

Watch the `contracts/` folder populate in real time:
- `org_profile.json` — Samsung repo intelligence
- `incoming_papers.json` — 60+ harvested research papers
- `threat_papers.json` — Competitor intelligence from ArXiv
- `pending_actions.json` — AI-mapped optimization opportunities
- `live_trends.json` — ML-clustered research trend report

---

## 🔑 How to Get API Keys

### Google Gemini (Primary LLM)
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click **Get API Key** → **Create API key**
3. Copy the key into `GOOGLE_API_KEY`

### Groq (Fast Fallback LLM)
1. Go to [Groq Console](https://console.groq.com/keys)
2. Create a new API Key (free tier available)
3. Copy the key into `GROQ_API_KEY`

### OpenRouter (Free Tertiary Fallback)
1. Go to [OpenRouter](https://openrouter.ai/keys)
2. Create an account and generate a key
3. Copy the key into `OPENROUTER_API_KEY`

### GitHub Personal Access Token
1. Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
2. Generate a new **Classic Token**
3. Select scopes: `repo`, `read:org`, `workflow`
4. Copy into `GITHUB_TOKEN`

### Telegram Bot
1. Message `@BotFather` on Telegram → `/newbot`
2. Copy the token into `TELEGRAM_BOT_TOKEN`
3. Add your bot to a group/channel and make it **Admin**
4. Message `@userinfobot` to get your `TELEGRAM_CHAT_ID`

---

## 🦞 OpenClaw Setup Guide (Autonomous Scheduling)

OpenClaw transforms RADAR from a script into a **fully autonomous, always-on** research agent.

### Step 1: Install OpenClaw
```bash
npm install -g openclaw
```

### Step 2: Initialize in the Project Directory
```bash
cd RIT_CodeRock
npx openclaw init
```

### Step 3: Configure the AI Model
Open `~/.openclaw/openclaw.json` and set your model:
```json
"model": {
  "primary": "groq/llama-3.1-8b-instant"
}
```
> **Note:** Ensure `GROQ_API_KEY` is set as a **system environment variable** (not just in `.env`) so the gateway can access it.

### Step 4: Start the Gateway
```bash
npx openclaw gateway start
```

### Step 5: Open the Control Dashboard
```bash
npx openclaw dashboard
```
Navigate to `http://127.0.0.1:18789` in your browser.

- **Chat Tab**: Talk to RADAR (`/radar-run`, `/radar-status`, `/radar-pr`)
- **Cron Tab**: View and manually trigger scheduled jobs
- **Logs Tab**: Watch the agent's real-time reasoning

### Step 6: Add Autonomous Cron Jobs
In the OpenClaw Dashboard → Cron Jobs → New Job:

| Job Name | Agent | Schedule | Description |
|----------|-------|----------|-------------|
| RADAR Daily Pipeline | radar | `0 9 * * *` | Full pipeline at 9AM daily |


### Available Agent Skills
| Command | Description |
|---------|-------------|
| `/radar-run` | Execute the full autonomous pipeline |
| `/radar-fetch` | Harvest new research papers only |
| `/radar-analyze` | Analyze papers and map to repos |
| `/radar-pr` | Generate and submit code PRs |
| `/radar-alert` | Send Telegram intelligence report |
| `/radar-status` | Check pipeline health and pending actions |

---

## 📁 Repository Structure

```
RIT_CodeRock/
│
├── main.py                    # Master pipeline orchestrator
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variable template
│
├── brain/                     # Member 3: The Brain
│   ├── llm_client.py          # Multi-provider LLM failover engine
│   ├── org_scanner.py         # GitHub organization intelligence
│   ├── process_papers.py      # Semantic paper → action mapping
│   └── trend_analyzer.py      # ML clustering & velocity analysis
│
├── fetchers/                  # Member 2: The Harvester
│   ├── paper_fetcher.py       # ArXiv + Semantic Scholar harvesting
│   ├── fetch_threats.py       # Competitor intelligence (ArXiv)
│   ├── fetch_historical_trends.py  # Trend data fetching
│   └── config.py              # Harvester configuration
│
├── outputs/                   # Member 4: The Communicator
│   ├── auto_pr.py             # Autonomous code generation + PR submission
│   ├── send_alert.py          # Telegram opportunity alerts
│   ├── trend_broadcaster.py   # Telegram trend intelligence cards
│   ├── github_dispatcher.py   # GitHub Issue creation
│   └── issue_manager.py       # Issue lifecycle management
│
├── contracts/                 # Live data exchange (git-ignored)
│   ├── org_profile.json       # Samsung repo context
│   ├── incoming_papers.json   # Harvested research papers
│   ├── threat_papers.json     # Competitor intelligence
│   ├── pending_actions.json   # AI-mapped action queue
│   └── live_trends.json       # ML trend analysis output
│
├── skills/                    # OpenClaw agent skill definitions
├── openclaw/                  # OpenClaw agent configuration
│
├── RIT_CODEROCK.pdf           # Project proposal & team details
├── OpenClaw_AI_Disclosure.docx # AI tool usage disclosure
└── radar_architecture_diagram_1777053872297.png  # System architecture
```

---

## ⚠️ Is the Code Ready to Pull and Run?

**Yes, with these prerequisites:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Python 3.10+ | Required | `pip install -r requirements.txt` |
| `.env` file | Required | Copy from `.env.example`, add your keys |
| Node.js 18+ | Optional | Only for OpenClaw dashboard |
| GPU/CUDA | Not required | CPU-only inference supported |

> **The pipeline runs end-to-end without OpenClaw.** Judges can simply run `python main.py` after configuring `.env`.

---

## 🎬 Demo Sequence

1. **Show Dashboard**: Open `http://127.0.0.1:18789` with RADAR agent
2. **Trigger Pipeline**: Type `/radar-run` or click Run on a Cron Job
3. **Show Live Data**: Watch `contracts/` folder fill in VS Code
4. **Show GitHub**: Open `github.com/Samsung-PRISM-EdgeAI` for new PRs
5. **Show Telegram**: Live intelligence alert on mobile
6. **Show Scheduling**: Cron jobs tab proving autonomous operation

---

## 👥 Team CodeRock

Built with ❤️ for the **Samsung PRISM Hackathon**

---

## ⚖️ License

MIT License — See [AI Disclosure](./OpenClaw_AI_Disclosure.docx) for AI tool usage details.
