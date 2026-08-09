# Deployment

## Recommended path: Render Docker web service

This repository includes:

- `Dockerfile`
- `render.yaml`
- `server.py`
- `FINMIND_TOKEN` environment-variable support

Render can build and run this service directly from the GitHub repository.

## Deploy with Render Blueprint

1. Open Render Dashboard.
2. Create a new Blueprint / Infrastructure as Code project.
3. Connect this GitHub repository:

   ```text
   https://github.com/mikeleeattaiwan/finmind-mcp
   ```

4. Render should detect `render.yaml`.
5. Set the secret environment variable:

   ```text
   FINMIND_TOKEN=<your FinMind token>
   ```

6. Deploy.

After deployment, Render will provide an HTTPS URL similar to:

```text
https://finmind-mcp.onrender.com
```

The MCP endpoint should be exposed by FastMCP's HTTP transport on that service URL.

## Local smoke test

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
FINMIND_TOKEN="your-token" python server.py
```

Then connect an MCP client to the local HTTP endpoint.

## Docker smoke test

```bash
docker build -t finmind-mcp .
docker run --rm -p 8000:8000 -e FINMIND_TOKEN="$FINMIND_TOKEN" finmind-mcp
```
