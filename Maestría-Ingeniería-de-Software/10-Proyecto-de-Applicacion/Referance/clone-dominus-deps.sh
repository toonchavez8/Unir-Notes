#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

clone_or_update() {
  local url="$1"
  local name="$2"
  local target="${SCRIPT_DIR}/${name}"

  if [ -d "${target}/.git" ]; then
    echo "Updating ${name}..."
    git -C "${target}" pull --ff-only
  else
    echo "Cloning ${name}..."
    git clone "${url}" "${target}"
  fi
}

clone_or_update "https://github.com/unir-broker-tfm/dominus-broker.git" "dominus-broker"
clone_or_update "https://github.com/unir-broker-tfm/dominus-sdk.git" "dominus-sdk"
clone_or_update "https://github.com/unir-broker-tfm/consumer-example.git" "consumer-example"
clone_or_update "https://github.com/unir-broker-tfm/dominus-proto-definition.git" "dominus-proto-definition"

echo "Done."
