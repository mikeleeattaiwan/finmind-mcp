# Fly.io deployment

This repository is prepared for Fly.io deployment with Docker.

## Expected endpoints

After deployment:

- Health check: `https://finmind-mcp-mikeleeattaiwan.fly.dev/health`
- MCP endpoint: `https://finmind-mcp-mikeleeattaiwan.fly.dev/mcp`

## One-time setup

Install and login to Fly.io CLI:

```bash
brew install flyctl
fly auth login
```

## Create the app

From this repository directory:

```bash
fly apps create finmind-mcp-mikeleeattaiwan --region nrt
```

If the app name is already taken, edit `fly.toml` and choose another globally unique app name.

## Optional FinMind token

If you have a FinMind API token:

```bash
fly secrets set FINMIND_TOKEN=your_token_here
```

The service can still run without a token, but FinMind API rate limits may be stricter.

## Deploy

```bash
fly deploy
```

## Verify

```bash
curl https://finmind-mcp-mikeleeattaiwan.fly.dev/health
```

Expected response:

```json
{"status":"healthy","service":"finmind-mcp"}
```
