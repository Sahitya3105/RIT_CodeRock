# 🎭 RADAR: Final Demonstration Strategy
**Winning the Demo with Autonomous Intelligence**

This document serves as your "Script" and "Checklist" for creating a high-impact demonstration video or live presentation.

---

## 📽️ 3-Minute Video Storyboard

| Time | Scene | Key Message |
| :--- | :--- | :--- |
| **0:00-0:45** | **Mission Control** (OpenClaw Dashboard) | "Meet RADAR: A living, thinking architect built on **OpenClaw**." Show the Skills Tab and the Cron list. |
| **0:45-1:30** | **The Waking Agent** (Triggering) | Trigger `/radar-run`. Show the logs as the agent uses tools to "Fetch" and "Analyze" research. |
| **1:30-2:15** | **Autonomous Impact** (GitHub) | Switch to GitHub. Show the **Issues** and **PRs** appearing in real-time. Highlight the "AI-Generated" code. |
| **2:15-2:45** | **The Pulse Alert** (Telegram) | Show the **Threat Alert** and **Trend Card** popping up on a mobile/desktop Telegram. |
| **2:45-3:00** | **The Persistence** (Steady State) | Run the agent again to show **Deduplication**. It reports "STEADY" instead of spamming. |

---

## 🛠️ Proof of Work: "The Smoking Guns"

### 1. Proof of OpenClaw Integration
*   **The Dashboard UI**: The judges will recognize the OpenClaw interface immediately.
*   **The Wrench (Skills)**: Click the wrench icon in the dashboard and show the `/radar-run` skill with its 🔬 emoji and metadata.
*   **Background Tasks**: Point out the "Task ID" and the "Process still executing" notifications from the Assistant.
*   **Variable Expansion**: Show the tool call log using `{{workspace}}` to prove OpenClaw is managing the environment.

### 2. Proof of Fetcher Activity (Member 2)
*   **The Raw Harvest**: Open `contracts/incoming_papers.json` to show the raw JSON data the agent just pulled from the web.
*   **Live Logs**: Highlight the terminal lines: `[FETCH] Searching ArXiv for 'On-Device LLM'...`
*   **Trend Velocity**: Show the **Trend Card** in Telegram and explain it's based on analyzing 90 days of historical fetch data.

### 3. Proof of Brain Resilience (Member 3)
*   **Batching Logs**: Show the terminal saying `Processing batch 1/4...`. Explain that the agent is smart enough to bypass AI rate limits.
*   **Multi-LLM Fallback**: Mention that we use **Gemini 2.0** for deep logic, with an automatic **Groq Llama-3.3** fallback for speed and reliability.

---

## 💡 Top Demo Tips
1.  **Split-Screen**: Use a split-screen (Terminal/Dashboard on left, GitHub/Telegram on right).
2.  **Explain the "Why"**: Don't just show a PR; explain that this paper was a **threat** to Samsung's IP, so the agent acted to secure it.
3.  **The Persistence**: The fact that it *doesn't* alert when nothing is new is actually your strongest feature. It shows the agent has "Memory."
4.  **Mention Patents**: Briefly mention that RADAR is designed to be upgraded with **Patent Checks** for the "IP Fortress" expansion.

---

## ✅ Final Success Checklist
- [ ] OpenClaw Gateway is started and linked.
- [ ] `.env` is configured correctly.
- [ ] GitHub Org is visible and empty (before run).
- [ ] Telegram Bot is active and group is ready.
- [ ] "Deep Focus" mode is verified (runs a 2nd time without spam).
