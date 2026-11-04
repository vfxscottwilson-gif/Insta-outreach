# 02 Architecture

No software lives here. The spec describes a queue-based system: Google Sheets as the data layer, Gmail API for sending with threading, short scheduled runs on GitHub Actions, and an API-agnostic AI layer for drafts. Details: spec section 2. Implementations: see the table in `README.md`.
