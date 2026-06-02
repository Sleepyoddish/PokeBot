#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/logs"
TIMESTAMP="$(date +"%Y%m%d-%H%M%S")"
LOG_FILE="${LOG_DIR}/pytest-${TIMESTAMP}.log"

mkdir -p "${LOG_DIR}"
cd "${ROOT_DIR}"

if [[ -x "${ROOT_DIR}/.venv/bin/python" ]]; then
  PYTHON="${ROOT_DIR}/.venv/bin/python"
else
  PYTHON="${PYTHON:-python3}"
fi

export HEADLESS="${HEADLESS:-true}"
export SLOWMO="${SLOWMO:-0}"

{
  echo "[$(date -Iseconds)] Starting PokeBot test run"
  echo "Project: ${ROOT_DIR}"
  echo "Python: $("${PYTHON}" --version)"
  echo
  "${PYTHON}" -m pytest "$@"
  status=$?
  echo
  echo "[$(date -Iseconds)] Finished with status ${status}"
  exit "${status}"
} 2>&1 | tee "${LOG_FILE}"
