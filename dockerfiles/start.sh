#!/usr/bin/env bash
set -e

# Launch Jupyter Lab. Token-based auth is enabled by default; check container logs for the URL with token.
exec jupyter lab \
  --ServerApp.ip=0.0.0.0 \
  --ServerApp.port=8888 \
  --ServerApp.open_browser=false \
  --ServerApp.allow_origin="*" \
  --NotebookApp.notebook_dir=/workspace

