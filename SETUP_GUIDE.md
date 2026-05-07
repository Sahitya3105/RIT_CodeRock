# 🛠️ RADAR: Global Setup & Deployment Guide
**Autonomous Research-to-PR Pipeline for Samsung PRISM**

This guide provides a step-by-step walkthrough to set up the RADAR autonomous pipeline on any Windows machine (teammate or judge).

---

## 1. Prerequisites
Ensure the following are installed:
*   **Python 3.9+**: [Download here](https://www.python.org/downloads/)
*   **Git**: [Download here](https://git-scm.com/)
*   **Node.js** (Required for the OpenClaw CLI): [Download here](https://nodejs.org/)

---

## 2. Repository Setup
Clone the repository and enter the project folder:
```bash
git clone https://github.com/Sahitya3105/RIT_CodeRock.git
cd RIT_CodeRock
```

---

## 3. Environment & Credentials
The pipeline requires four API keys to function. Create a `.env` file in the root directory by duplicating `.env.example`.

### A. Google Gemini API Key
1.  Go to [Google AI Studio](https://aistudio.google.com/).
2.  Click on **"Get API key"** in the left sidebar.
3.  Click **"Create API key in new project"**.
4.  Copy the key and paste it into `GOOGLE_API_KEY` in your `.env`.

### B. Groq API Key (High-Speed Fallback)
1.  Go to [Groq Console](https://console.groq.com/keys).
2.  Click **"Create API Key"**.
3.  Copy the key and paste it into `GROQ_API_KEY` in your `.env`.

### C. Semantic Scholar API Key
1.  Go to the [Semantic Scholar API Dashboard](https://www.semanticscholar.org/product/api).
2.  Sign up for a free developer account.
3.  Generate an API key from your profile settings.
4.  Copy the key and paste it into `SEMANTIC_SCHOLAR_API_KEY`.

### C. GitHub Personal Access Token
1.  Login to GitHub and go to **Settings** > **Developer settings**.
2.  Select **Personal access tokens** > **Tokens (classic)**.
3.  Click **Generate new token (classic)**.
4.  Give it a name and select the **`repo`** checkbox (required for creating PRs).
5.  Click **Generate token**, copy it, and paste it into `GITHUB_TOKEN`.

### D. Telegram Bot & Chat ID
1.  **Get the Bot Token**: Search for `@BotFather` on Telegram and send `/newbot`. Follow instructions to get your `HTTP API Token`.
2.  **Get the Chat ID**:
    *   Create a Telegram Group and add your new bot to it.
    *   Add `@userinfobot` to the group or send a message and then visit `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` to find the `chat: { id: -100... }`.
    *   Paste the token into `TELEGRAM_BOT_TOKEN` and the ID into `TELEGRAM_CHAT_ID`.

### E. GitHub Repository Targeting
1.  In your `.env`, set `GITHUB_ORG` to the name of your GitHub Organization or personal username.
2.  Set `GITHUB_REPO` to the specific repository where you want the "Core Engine" optimizations to be submitted (e.g., `MyOrg/core-engine`).

---

## 4. Install Dependencies
Run the following command to install all necessary Python libraries from the requirements file:
```bash
pip install -r requirements.txt
```

---

## 5. 🦞 OpenClaw: Autonomous Agent Setup

RADAR is designed to run as an autonomous agent using the **OpenClaw** framework. This allows the system to wake up on a schedule (Heartbeat) and execute skills end-to-end.

### Step 1: Installation
```bash
npm install -g openclaw
```

### Step 2: Initialize Workspace
Inside the `RIT_CodeRock` directory:
```bash
openclaw init
```
*When prompted for skills, ensure the path points to the `skills/` folder in the project.*

### Step 3: Start the Gateway
```bash
openclaw gateway start
```

### Step 4: Add the Daily Heartbeat
To make the agent wake up every day at 9 AM and run the full pipeline:
```bash
openclaw cron add --name "RADAR Daily Pipeline" --cron "0 9 * * *" --message "/radar-run"
```

### Step 5: Dashboard Monitoring
To see the agent thinking and executing in real-time:
```bash
openclaw dashboard
```

---

## 6. Testing the Flow
To verify everything is working immediately (without waiting for the heartbeat):

**Method A: CLI (Python Native)**
```bash
python main.py
```

**Method B: OpenClaw Dashboard (Agent Mode)**
1.  Run `openclaw dashboard`.
2.  In the chat window, type: `/radar-run`.
3.  Watch the agent fetch papers, analyze threats, generate code, and send the Telegram alert in real-time.

---

## ✅ Success Criteria
1.  **Autonomous Bootstrap**: The `contracts/` directory is created automatically on the first run.
2.  **New PR**: A Pull Request is opened on your GitHub repo with AI-generated optimization code.
3.  **New Alert**: A "Macro Trend Detected" card or "Critical Threat" alert appears in your Telegram chat.
4.  **Deduplication**: Running the script a second time should trigger the "Strategic Status: STEADY" report instead of repeating alerts.
