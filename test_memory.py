import asyncio
import os
import sys
from pathlib import Path

# Keep this smoke test local even if the terminal has a provider key set.
os.environ.pop("LLM_API_KEY", None)
os.environ.pop("OPENAI_API_KEY", None)
os.environ["HF_HOME"] = str(Path(__file__).parent / ".local_models")

import cognee

MEMORY_ROOT = Path(__file__).resolve().parent / ".cognee"
cognee.config.system_root_directory(str(MEMORY_ROOT / "system"))
cognee.config.data_root_directory(str(MEMORY_ROOT / "data"))

DATASET = "sportsbook_demo"


async def write_update():
    await cognee.remember(
        "Simulated Ravens vs. Chargers game. The FanDuel watcher saw "
        "the Chargers moneyline move from +190 to +250.",
        dataset_name=DATASET,
    )
    print("FanDuel watcher saved its update.")


async def read_update():
    results = await cognee.recall(
        "What was the new FanDuel Chargers moneyline?", datasets=[DATASET]
    )
    print("Scanner retrieved:")
    for result in results:
        print(result)
    if "+250" not in str(results):
        raise SystemExit("Memory check failed: retrieval did not contain +250.")


if __name__ == "__main__":
    commands = {"write": write_update, "read": read_update}
    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        raise SystemExit("Usage: python test_memory.py write|read")
    asyncio.run(commands[sys.argv[1]]())
