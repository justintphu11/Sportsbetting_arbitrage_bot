# Sportsbetting arbitrage bot

Initial smoke test for sharing a simulated sportsbook line update through Cognee's local memory. No sportsbook connections or real bets are involved.

## Run the memory test

Use Python 3.10–3.14. Tested on macOS with Python 3.14 and Cognee 1.6.8.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python test_memory.py write
python test_memory.py read
```

Let the writer finish before starting the reader. The writer stores a simulated FanDuel Chargers moneyline change from +190 to +250. The reader runs in a separate process, retrieves that record, and exits with an error if `+250` is missing.

The script clears `LLM_API_KEY` and `OPENAI_API_KEY` in its own process to use local models. Models download on first use; network access may also be needed for model metadata checks on later runs. Local data lives in `.cognee/`, and model files live in `.local_models/`. Both are excluded from Git alongside `.venv/`.

See the [Cognee local quickstart](https://pypi.org/project/cognee/) for details.
