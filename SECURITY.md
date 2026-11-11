# Cyber & Data Security Architecture

## Threat Model

- API key compromise
- Injection via external data feeds
- Unauthorized order placement
- Data exfiltration of portfolio or strategy logic
- Supply-chain risks in dependencies

## Controls

### Secrets Management
- All exchange API keys, webhook secrets, and encryption keys live exclusively in environment variables or a dedicated secrets manager (e.g., HashiCorp Vault, AWS Secrets Manager, 1Password CLI).
- `.env` files are gitignored and never committed.
- Example configuration provided in `config/example.env` with placeholder values only.

### Encryption
- Sensitive intermediate data (if persisted) encrypted at rest using AES-GCM via the `cryptography` library.
- In-memory secrets zeroized after use where feasible.

### Input Validation & Sanitization
- All external market data, news, and user inputs validated against strict schemas (Pydantic models).
- Rate limiting on data fetches to prevent abuse and respect exchange limits.

### Audit & Logging
- Structured JSON logging of all strategy signals, risk decisions, and simulated orders.
- Logs include timestamps, strategy ID, asset class, decision rationale, and confidence scores.
- No PII or raw API keys in logs.

### Execution Safety
- Live trading disabled by default (`LIVE_TRADING=false`).
- Multiple confirmation gates required to enable live mode.
- Maximum position size, daily loss limits, and circuit breakers enforced in `risk/` module.
- Paper trading mode simulates fills with realistic slippage models.

### Dependency & Runtime Security
- Pin dependencies in `requirements.txt`.
- Recommend running in isolated container (Dockerfile provided).
- Regular dependency scanning recommended (Dependabot, Safety, etc.).

### Network Security
- Prefer read-only API keys where possible.
- Outbound connections restricted to known exchange and data provider endpoints.
- TLS enforced for all external communications.

## Incident Response

1. Immediately revoke compromised API keys at the exchange.
2. Rotate all related secrets.
3. Review audit logs for anomalous activity.
4. Switch to paper-only mode.

For questions or to report a security issue, open a private security advisory on GitHub.
