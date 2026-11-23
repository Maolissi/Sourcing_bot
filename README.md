# Telegram Sourcer Bot

Interactive AI-assisted sourcing workspace in Telegram.

## MVP scope
- AI Match Score
- Boolean Search
- Candidate Database
- Outreach Drafts
- Daily Search Reports

The bot is interactive: the recruiter reviews strategies and results and explicitly starts each search. Outreach is drafted, never sent automatically.

## Stack
Python 3.12+, aiogram 3, PostgreSQL, SQLAlchemy 2, Alembic, Redis (reserved for background jobs), OpenAI API.

## Local setup
1. Copy `.env.example` to `.env`.
2. Add your Telegram bot token to `.env`.
3. Start infrastructure: `docker compose up -d postgres redis`.
4. Install: `python -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"`.
5. Start: `python -m sourcer_bot`.

Never commit `.env`, bot tokens, API keys, passwords, or private candidate data.

## Development principles
- Keep Telegram handlers thin; business logic belongs in service modules.
- Isolate source adapters under `integrations/`.
- Minimize candidate data, preserve source provenance, and support correction/deletion.
- Respect platform terms, API limits, and access controls. Do not bypass authentication or restrictions.
