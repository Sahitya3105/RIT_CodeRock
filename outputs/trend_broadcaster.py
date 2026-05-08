"""
Member 4 – The Communicator | outputs/trend_broadcaster.py
===========================================================
Reads `contracts/live_trends.json` produced by Member 3's Trend Engine
and fires a beautifully formatted Markdown card to the Telegram channel.

Card design:
    🔴 LIVE TREND DETECTED: [Cluster Name]
    📊 17 New Papers in last 14 days
    🔬 Key Competitors acting: [Institutions]
    ⚠️  Implication: [Summary]

Usage
-----
1. Install dependency (if not already installed):
       pip install python-telegram-bot

2. Set credentials as environment variables (recommended) OR edit the
   constants block below:
       TELEGRAM_BOT_TOKEN  – Token from @BotFather
       TELEGRAM_CHAT_ID    – Target chat / channel ID

3. Run from the SAMSUNG_PRISM root directory:
       python outputs/trend_broadcaster.py
"""

import asyncio
import json
import os
import sys
import io

# Force UTF-8 for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
from pathlib import Path

from telegram import Bot
from telegram.constants import ParseMode
from dotenv import load_dotenv

# Load environment variables from .env in project root
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# ---------------------------------------------------------------------------
# Configuration – set via environment variables or edit directly here
# ---------------------------------------------------------------------------
TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
TELEGRAM_CHAT_ID: str = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

# Path to contract (relative to this script)
SCRIPT_DIR        = Path(__file__).parent          # outputs/
CONTRACTS_DIR     = SCRIPT_DIR.parent / "contracts"
LIVE_TRENDS_PATH  = CONTRACTS_DIR / "live_trends.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_live_trends() -> list[dict]:
    """Load the trend list from contracts/live_trends.json."""
    if not LIVE_TRENDS_PATH.exists():
        print(f"[ERROR] Contract file not found: {LIVE_TRENDS_PATH}")
        sys.exit(1)
    with open(LIVE_TRENDS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        print("[ERROR] live_trends.json must contain a JSON array.")
        sys.exit(1)
    return data


def _escape(text: str) -> str:
    """Escape all MarkdownV2 special characters in plain text."""
    special = r"\_*[]()~`>#+-=|{}.!"
    for ch in special:
        text = text.replace(ch, f"\\{ch}")
    return text


def generate_insight(cluster_name: str, paper_count: int, competitors: list, implication: str) -> str:
    """Use OpenRouter to generate a unique strategic insight for this trend."""
    import urllib.request, json as _json
    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    if not openrouter_key:
        return "Steady growth detected. Focus is shifting from theoretical models to practical, on-device efficiency."

    prompt = (
        f"You are a strategic AI research analyst at Samsung R&D.\n"
        f"A research trend has been detected:\n"
        f"- Topic: {cluster_name}\n"
        f"- New papers in last 14 days: {paper_count}\n"
        f"- Key competitors active: {', '.join(competitors) if competitors else 'Various institutions'}\n"
        f"- Implication: {implication}\n\n"
        f"Write a single, punchy 1-2 sentence strategic insight for Samsung engineers. "
        f"Be specific, technical, and urgent. No fluff."
    )
    free_models = ["google/gemma-4-31b-it:free", "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openrouter_key}",
        "HTTP-Referer": "https://github.com/Samsung-PRISM-EdgeAI",
        "X-Title": "RADAR"
    }
    for model in free_models:
        try:
            payload = _json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}]}).encode()
            req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=payload, headers=headers)
            r = urllib.request.urlopen(req, timeout=30)
            resp = _json.loads(r.read())
            return resp["choices"][0]["message"]["content"].strip()
        except Exception:
            pass

    return f"Critical momentum detected in {cluster_name} — {paper_count} papers signal accelerating competition from {competitors[0] if competitors else 'leading labs'}."


def format_trend_card(trend: dict, index: int, total: int) -> str:
    """Build a beautiful Markdown card for a single live trend."""
    CATEGORY_MAP = {
        "cs.CL": "Computation and Language (NLP)",
        "cs.AI": "Artificial Intelligence",
        "cs.LG": "Machine Learning",
        "cs.CV": "Computer Vision",
        "cs.NE": "Neural and Evolutionary Computing",
        "cs.RO": "Robotics",
    }

    cluster_raw = trend.get("cluster_name", "Unknown Cluster")
    for code, full_name in CATEGORY_MAP.items():
        if code in cluster_raw:
            cluster_raw = cluster_raw.replace(code, full_name)

    paper_count    = trend.get("papers_last_14_days", trend.get("paper_count", 0))
    timeframe_days = trend.get("timeframe_days", 14)
    competitors    = trend.get("key_competitors", [])
    implication    = trend.get("implication", "Strategic shift detected.")

    # Get top 3 papers
    all_papers = trend.get("papers", [])
    hot_papers = all_papers[:3]

    # AI-generated insight
    print(f"   [LLM] Generating insight for trend: {cluster_raw[:40]}...")
    insight = generate_insight(cluster_raw, paper_count, competitors, implication)

    # Escaped safe versions
    safe_cluster     = _escape(cluster_raw)
    safe_implication = _escape(implication)
    safe_competitors = _escape(", ".join(competitors) if competitors else "Unknown")
    safe_insight     = _escape(insight)

    lines = [
        f"🔴 *LIVE TREND DETECTED*",
        f"🎯 *Focus:* `{safe_cluster}`",
        "",
        f"📊 *{paper_count} New Papers* in last {timeframe_days} days",
        f"🔬 *Key Competitors:* {safe_competitors}",
        "",
        f"💡 *AI Insight:* {safe_insight}",
        f"⚠️ *Implication:* {safe_implication}",
        "",
        "🔥 *Hot Papers Currently:*",
    ]

    for p in hot_papers:
        title = _escape(p.get("title", "Research Paper"))
        url = p.get("url", "")
        if url:
            lines.append(f"• [{title}]({url})")
        else:
            lines.append(f"• {title}")

    lines += [
        "",
        f"━━━━━━━━━━━━━━━━━━━━━━━━",
        f"_RADAR Trend Digest · Alert {index}/{total}_",
    ]

    return "\n".join(lines)



# ---------------------------------------------------------------------------
# Core async broadcaster
# ---------------------------------------------------------------------------

async def broadcast_trends(token: str, chat_id: str, trends: list[dict]) -> None:
    """Send one Telegram card per trend."""
    bot = Bot(token=token)

    try:
        me = await bot.get_me()
        print(f"[INFO] Connected as @{me.username}. Broadcasting {len(trends)} trend(s)…")
    except Exception as exc:
        print(f"[ERROR] Could not authenticate with Telegram: {exc}")
        sys.exit(1)

    total = len(trends)
    for idx, trend in enumerate(trends, start=1):
        card = format_trend_card(trend, idx, total)
        try:
            await bot.send_message(
                chat_id=chat_id,
                text=card,
                parse_mode=ParseMode.MARKDOWN_V2,
                disable_web_page_preview=False,
            )
            print(f"[OK]   Trend {idx}/{total} sent: {trend.get('cluster_name', '?')}")
        except Exception as exc:
            print(f"[WARN] Failed to send trend {idx}/{total}: {exc}")

    print("[DONE] All trend cards dispatched.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print(
            "[ERROR] TELEGRAM_BOT_TOKEN is not set.\n"
            "        Export it as an environment variable:\n"
            "            $env:TELEGRAM_BOT_TOKEN = '<token>'  (PowerShell)\n"
            "            export TELEGRAM_BOT_TOKEN=<token>    (Linux/Mac)"
        )
        sys.exit(1)

    if TELEGRAM_CHAT_ID == "YOUR_CHAT_ID_HERE":
        print(
            "[ERROR] TELEGRAM_CHAT_ID is not set.\n"
            "        Export it as an environment variable:\n"
            "            $env:TELEGRAM_CHAT_ID = '<id>'  (PowerShell)\n"
            "            export TELEGRAM_CHAT_ID=<id>    (Linux/Mac)"
        )
        sys.exit(1)

    trends = load_live_trends()

    if not trends:
        print("[INFO] No trends found in live_trends.json. Nothing to broadcast.")
        return

    asyncio.run(broadcast_trends(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, trends))


if __name__ == "__main__":
    main()
