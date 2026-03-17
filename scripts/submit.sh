#!/bin/bash

# ─── CONFIG ───────────────────────────────────────────
LEETCODE_DIR="$HOME/leetcode"
# ──────────────────────────────────────────────────────

PROBLEM_NAME="$1"
STATUS="$2"          # "accepted" or "failed"
RUNTIME="$3"         # e.g. "45 ms"
MEMORY="$4"          # e.g. "16.2 MB"
SCORE="$5"           # percentile e.g. "87.5"
SOLUTION_FILE="$6"   # full path to your solution file
TC_INPUT="$7"        # test case input (for failed)
TC_EXPECTED="$8"     # expected output (for failed)
TC_GOT="$9"          # your output (for failed)

PROBLEM_DIR="$LEETCODE_DIR/$PROBLEM_NAME"
DATE=$(date +"%Y-%m-%d")
TIME_NOW=$(date +"%H:%M:%S")
EXT="${SOLUTION_FILE##*.}"

mkdir -p "$PROBLEM_DIR"

if [ "$STATUS" == "accepted" ]; then

    cp "$SOLUTION_FILE" "$PROBLEM_DIR/solution.$EXT"

    cat > "$PROBLEM_DIR/meta.json" <<EOF
{
  "problem": "$PROBLEM_NAME",
  "status": "Accepted",
  "date": "$DATE",
  "time": "$TIME_NOW",
  "runtime": "$RUNTIME",
  "memory": "$MEMORY",
  "score_percentile": "$SCORE"
}
EOF

    cd "$LEETCODE_DIR"
    git add "$PROBLEM_NAME/"
    git commit -m "✅ [$DATE] Accepted: $PROBLEM_NAME | Runtime: $RUNTIME | Memory: $MEMORY | Beat: $SCORE%"
    git push origin main
    echo "✅ Committed and pushed: $PROBLEM_NAME"

elif [ "$STATUS" == "failed" ]; then

    FAILED_DIR="$PROBLEM_DIR/failed"
    mkdir -p "$FAILED_DIR"
    TIMESTAMP=$(date +%s)

    # Save the failed solution
    cp "$SOLUTION_FILE" "$FAILED_DIR/solution_${DATE}_${TIMESTAMP}.$EXT"

    # Save the failing test case details
    cat > "$FAILED_DIR/testcase_${DATE}_${TIMESTAMP}.txt" <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problem  : $PROBLEM_NAME
Date     : $DATE $TIME_NOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INPUT:
$TC_INPUT

EXPECTED:
$TC_EXPECTED

YOUR OUTPUT:
$TC_GOT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

    echo "❌ Saved failed attempt + test case: $FAILED_DIR"
fi