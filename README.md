# PokeBot

Python + Playwright automation scaffolding.

## Run Tests Locally

```bash
./scripts/run_tests.sh
```

The script uses `.venv/bin/python` when it exists, defaults browser runs to headless mode, and writes timestamped logs to `logs/`.

## Cron Setup

Edit `cron/pokebot-tests.crontab.example` if you want a different schedule, then install it with:

```bash
crontab cron/pokebot-tests.crontab.example
```

The included example runs tests daily at 7:00 AM local time.
