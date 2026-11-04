# local-drafter hand-over (2026-11-03)
- Repo: D:\All Automations Records\Local Draft File\local-drafter (4 commits, not pushed). Read its CLAUDE.md "Status / next step".
- Built + 231 pytest tests pass; verified only with the MOCK backend (no Ollama/LM Studio installed on this PC).
- Finding: nvidia-smi on this PC = RTX 2060 SUPER 8 GB (brief said RTX 5060 Ti 16 GB). Model advice in START_HERE.md covers both.
- Verified 2026-11-03: qwen3:14b 9.3 GB, qwen3:8b 5.2 GB, gemma3:12b 8.2 GB, gemma3:4b 3.4 GB (ollama.com/library);
  YouTube search.list now has its own 100 calls/day bucket; Sheets API 60 req/min/user, overage charges "planned later in 2026".
- Waiting on user: model install, service-account JSON + sheet sharing, --test-handoff with Apps Script.
