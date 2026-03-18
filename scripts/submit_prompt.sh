#!/bin/zsh

SOLUTION_FILE="$1"
LEETCODE_DIR="$HOME/Dev/Leetcode"
EXT="${SOLUTION_FILE##*.}"
DATE=$(date +"%Y-%m-%d")
TIME_NOW=$(date +"%H:%M:%S")
TIME_SAFE=$(date +"%H-%M-%S")

GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[0;36m'
BOLD='\033[1m'
YELLOW='\033[1;33m'
RESET='\033[0m'

# ── Extract problem number + slug from filename ───────
BASENAME=$(basename "$SOLUTION_FILE" ".$EXT")
PROBLEM_NUM=$(echo "$BASENAME" | cut -d'.' -f1)
PROBLEM_SLUG=$(echo "$BASENAME" | cut -d'.' -f2)
PROBLEM_DIR="$LEETCODE_DIR/${PROBLEM_NUM}_${PROBLEM_SLUG}"
mkdir -p "$PROBLEM_DIR"

# ── Comment character ─────────────────────────────────
case "$EXT" in
    py|rb|sh)            CMT="#"  ;;
    js|ts|cpp|c|java|cs) CMT="//" ;;
    *)                   CMT="#"  ;;
esac

SEP="${CMT} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
DIV="${CMT} ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─"

echo ""
echo "${CYAN}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo "${CYAN}${BOLD}  LeetCode Submission Logger${RESET}"
echo "${CYAN}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo "${CYAN}  Problem : #${PROBLEM_NUM} ${PROBLEM_SLUG}${RESET}"
echo "${CYAN}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo ""
echo "${BOLD}Paste full submission result, then press Enter twice:${RESET}"
echo ""

# ── Read pasted block ─────────────────────────────────
PASTED=""
while IFS= read -r line; do
    [[ -z "$line" ]] && break
    PASTED+="$line"$'\n'
done

# ── Parse result ──────────────────────────────────────
if echo "$PASTED" | grep -qi "accepted"; then
    STATUS="accepted"
elif echo "$PASTED" | grep -qi "wrong\|failed\|error\|time limit\|memory limit\|runtime error"; then
    STATUS="failed"
else
    STATUS="unknown"
fi

# ── Parse stats (accepted) ────────────────────────────
CASES=$(echo "$PASTED"     | grep -oi '[0-9]*/[0-9]* cases passed'    | grep -oE '[0-9]+/[0-9]+')
RUNTIME=$(echo "$PASTED"   | grep -oi '[0-9]* ms'                      | head -1)
RUNTIME_BEAT=$(echo "$PASTED" | grep -oi 'runtime beats [0-9.]*'       | grep -oE '[0-9.]+')
MEMORY=$(echo "$PASTED"    | grep -oE '[0-9.]+ MB'                     | head -1)
MEMORY_BEAT=$(echo "$PASTED"  | grep -oi 'memory usage beats [0-9.]*'  | grep -oE '[0-9.]+')

# ── Parse test case (failed) ──────────────────────────
TC_INPUT=$(echo "$PASTED"    | grep -i "input"    | sed 's/.*[Ii]nput[^:]*:[[:space:]]*//' | head -1)
TC_EXPECTED=$(echo "$PASTED" | grep -i "expected" | sed 's/.*[Ee]xpected[^:]*:[[:space:]]*//' | head -1)
TC_GOT=$(echo "$PASTED"      | grep -i "output"   | sed 's/.*[Oo]utput[^:]*:[[:space:]]*//' | head -1)

# ════════════════════════════════════════════════════════
# ACCEPTED
# ════════════════════════════════════════════════════════
if [[ "$STATUS" == "accepted" ]]; then

    echo "${GREEN}${BOLD}✅ Accepted detected!${RESET}"

    # Warn if any stat missing
    WARN=0
    [[ -z "$CASES" ]]       && echo "${YELLOW}⚠ Could not parse cases passed${RESET}"       && WARN=1
    [[ -z "$RUNTIME" ]]     && echo "${YELLOW}⚠ Could not parse runtime${RESET}"            && WARN=1
    [[ -z "$RUNTIME_BEAT" ]] && echo "${YELLOW}⚠ Could not parse runtime beat %${RESET}"   && WARN=1
    [[ -z "$MEMORY" ]]      && echo "${YELLOW}⚠ Could not parse memory${RESET}"             && WARN=1
    [[ -z "$MEMORY_BEAT" ]] && echo "${YELLOW}⚠ Could not parse memory beat %${RESET}"     && WARN=1

    if [[ "$WARN" == "1" ]]; then
        echo ""
        echo "${YELLOW}Some stats could not be parsed. Fill in manually (or press Enter to skip):${RESET}"
        [[ -z "$CASES" ]]        && echo -n "Cases passed (e.g. 34/34): "   && read CASES
        [[ -z "$RUNTIME" ]]      && echo -n "Runtime (e.g. 45 ms): "        && read RUNTIME
        [[ -z "$RUNTIME_BEAT" ]] && echo -n "Runtime beats %: "             && read RUNTIME_BEAT
        [[ -z "$MEMORY" ]]       && echo -n "Memory (e.g. 16.2 MB): "       && read MEMORY
        [[ -z "$MEMORY_BEAT" ]]  && echo -n "Memory beats %: "              && read MEMORY_BEAT
    fi

    OUT="$PROBLEM_DIR/pass_${DATE}_${TIME_SAFE}.$EXT"

    {
        echo "$SEP"
        echo "${CMT} Problem  : ${PROBLEM_NUM} — ${PROBLEM_SLUG}"
        echo "${CMT} Status   : Accepted ✅"
        echo "${CMT} Date     : ${DATE} ${TIME_NOW}"
        echo "${CMT} Cases    : ${CASES}"
        echo "${CMT} Runtime  : ${RUNTIME} (beats ${RUNTIME_BEAT}%)"
        echo "${CMT} Memory   : ${MEMORY} (beats ${MEMORY_BEAT}%)"
        echo "$SEP"
        echo ""
        cat "$SOLUTION_FILE"
    } > "$OUT"

    cd "$LEETCODE_DIR"
    git add "${PROBLEM_NUM}_${PROBLEM_SLUG}/"
    git commit -m "✅ [$DATE] #${PROBLEM_NUM} ${PROBLEM_SLUG} | ${RUNTIME} | ${MEMORY} | beats ${RUNTIME_BEAT}%"
    git push origin main

    echo ""
    echo "${GREEN}${BOLD}✅ Saved, committed and pushed!${RESET}"
    echo "${GREEN}   $OUT${RESET}"

# ════════════════════════════════════════════════════════
# FAILED
# ════════════════════════════════════════════════════════
elif [[ "$STATUS" == "failed" ]]; then

    echo "${RED}${BOLD}❌ Failure detected!${RESET}"

    # Warn if test case missing
    WARN=0
    [[ -z "$TC_INPUT" ]]    && echo "${YELLOW}⚠ Could not parse input${RESET}"           && WARN=1
    [[ -z "$TC_EXPECTED" ]] && echo "${YELLOW}⚠ Could not parse expected output${RESET}" && WARN=1
    [[ -z "$TC_GOT" ]]      && echo "${YELLOW}⚠ Could not parse your output${RESET}"     && WARN=1

    if [[ "$WARN" == "1" ]]; then
        echo ""
        echo "${YELLOW}Fill in manually (or press Enter to skip):${RESET}"
        [[ -z "$TC_INPUT" ]]    && echo -n "Test input: "      && read TC_INPUT
        [[ -z "$TC_EXPECTED" ]] && echo -n "Expected output: " && read TC_EXPECTED
        [[ -z "$TC_GOT" ]]      && echo -n "Your output: "     && read TC_GOT
    fi

    OUT="$PROBLEM_DIR/fail_${DATE}_${TIME_SAFE}.$EXT"

    {
        echo "$SEP"
        echo "${CMT} Problem  : ${PROBLEM_NUM} — ${PROBLEM_SLUG}"
        echo "${CMT} Status   : Failed ❌"
        echo "${CMT} Date     : ${DATE} ${TIME_NOW}"
        echo "$DIV"
        echo "${CMT} Input    : ${TC_INPUT}"
        echo "${CMT} Expected : ${TC_EXPECTED}"
        echo "${CMT} Got      : ${TC_GOT}"
        echo "$SEP"
        echo ""
        cat "$SOLUTION_FILE"
    } > "$OUT"

    echo ""
    echo "${RED}${BOLD}❌ Saved failed attempt.${RESET}"
    echo "${RED}   $OUT${RESET}"

# ════════════════════════════════════════════════════════
# UNKNOWN — could not detect result
# ════════════════════════════════════════════════════════
else
    echo "${YELLOW}${BOLD}⚠ Could not detect result from pasted text.${RESET}"
    echo "${YELLOW}  Make sure you copied the full submission result.${RESET}"
    echo ""
    echo -n "${BOLD}Result — [a] Accepted  [f] Failed: ${RESET}"
    read MANUAL
    if [[ "$MANUAL" == "a" ]]; then
        STATUS="accepted"
        echo -n "Cases passed: "   && read CASES
        echo -n "Runtime: "        && read RUNTIME
        echo -n "Runtime beats %: " && read RUNTIME_BEAT
        echo -n "Memory: "         && read MEMORY
        echo -n "Memory beats %: " && read MEMORY_BEAT

        OUT="$PROBLEM_DIR/pass_${DATE}_${TIME_SAFE}.$EXT"
        {
            echo "$SEP"
            echo "${CMT} Problem  : ${PROBLEM_NUM} — ${PROBLEM_SLUG}"
            echo "${CMT} Status   : Accepted ✅"
            echo "${CMT} Date     : ${DATE} ${TIME_NOW}"
            echo "${CMT} Cases    : ${CASES}"
            echo "${CMT} Runtime  : ${RUNTIME} (beats ${RUNTIME_BEAT}%)"
            echo "${CMT} Memory   : ${MEMORY} (beats ${MEMORY_BEAT}%)"
            echo "$SEP"
            echo ""
            cat "$SOLUTION_FILE"
        } > "$OUT"

        cd "$LEETCODE_DIR"
        git add "${PROBLEM_NUM}_${PROBLEM_SLUG}/"
        git commit -m "✅ [$DATE] #${PROBLEM_NUM} ${PROBLEM_SLUG} | ${RUNTIME} | ${MEMORY} | beats ${RUNTIME_BEAT}%"
        git push origin main

        echo "${GREEN}${BOLD}✅ Saved, committed and pushed!${RESET}"
        echo "${GREEN}   $OUT${RESET}"

    elif [[ "$MANUAL" == "f" ]]; then
        echo -n "Test input: "      && read TC_INPUT
        echo -n "Expected output: " && read TC_EXPECTED
        echo -n "Your output: "     && read TC_GOT

        OUT="$PROBLEM_DIR/fail_${DATE}_${TIME_SAFE}.$EXT"
        {
            echo "$SEP"
            echo "${CMT} Problem  : ${PROBLEM_NUM} — ${PROBLEM_SLUG}"
            echo "${CMT} Status   : Failed ❌"
            echo "${CMT} Date     : ${DATE} ${TIME_NOW}"
            echo "$DIV"
            echo "${CMT} Input    : ${TC_INPUT}"
            echo "${CMT} Expected : ${TC_EXPECTED}"
            echo "${CMT} Got      : ${TC_GOT}"
            echo "$SEP"
            echo ""
            cat "$SOLUTION_FILE"
        } > "$OUT"

        echo "${RED}${BOLD}❌ Saved failed attempt.${RESET}"
        echo "${RED}   $OUT${RESET}"
    fi
fi

echo ""
```

---

The flow is now:
```
1. Submit via extension
2. Cmd+A, Cmd+C on submission tab
3. Hit Option+Shift+S
4. Cmd+V in terminal → Enter twice

→ auto detects accepted/failed
→ auto parses all stats
→ warns + asks manually only if parsing fails
→ saves + commits