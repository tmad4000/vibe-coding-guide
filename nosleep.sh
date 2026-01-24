#!/bin/bash
# nosleep - Prevent Mac from sleeping for a specified duration
# Useful for keeping Mac awake with lid closed while running long tasks

set -e

show_help() {
    cat << 'EOF'
nosleep - Prevent Mac from sleeping (including with lid closed)

USAGE:
    nosleep [OPTIONS] [DURATION]

DURATION:
    Time in seconds to keep awake. Default: 1800 (30 minutes)

    Examples:
        nosleep          # 30 minutes (default)
        nosleep 3600     # 1 hour
        nosleep 7200     # 2 hours
        nosleep 28800    # 8 hours

OPTIONS:
    -h, --help       Show this help message
    -s, --status     Show current sleep status
    -on, --on        Disable sleep indefinitely (until -off is run)
    -off, --off      Re-enable sleep

NOTES:
    - Press Ctrl+C to cancel and re-enable sleep
    - Requires passwordless sudo for pmset (see setup below)
    - Safe to close laptop lid while running

SETUP:
    To run without password prompts, add to sudoers:

    echo 'YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/pmset' | sudo tee /etc/sudoers.d/pmset
    sudo chmod 0440 /etc/sudoers.d/pmset

EOF
}

show_status() {
    echo "Current sleep settings:"
    sudo pmset -g | grep -E "(SleepDisabled|sleep|disablesleep)"
}

case "${1:-}" in
    -h|--help)
        show_help
        exit 0
        ;;
    -s|--status)
        show_status
        exit 0
        ;;
    -on|--on)
        echo "Disabling sleep indefinitely..."
        sudo pmset -a disablesleep 1
        echo "Sleep disabled. Run 'nosleep --off' to re-enable."
        exit 0
        ;;
    -off|--off)
        echo "Re-enabling sleep..."
        sudo pmset -a disablesleep 0
        echo "Sleep re-enabled."
        exit 0
        ;;
esac

DURATION=${1:-1800}

# Validate duration is a number
if ! [[ "$DURATION" =~ ^[0-9]+$ ]]; then
    echo "Error: Duration must be a number (seconds)" >&2
    echo "Run 'nosleep --help' for usage" >&2
    exit 1
fi

MINUTES=$((DURATION / 60))
HOURS=$((MINUTES / 60))

if [ $HOURS -gt 0 ]; then
    echo "Disabling sleep for ${HOURS}h $((MINUTES % 60))m..."
else
    echo "Disabling sleep for ${MINUTES} minutes..."
fi

sudo pmset -a disablesleep 1

# Trap to ensure sleep is re-enabled on exit (Ctrl+C, etc)
cleanup() {
    echo ""
    echo "Re-enabling sleep..."
    sudo pmset -a disablesleep 0
    exit 0
}
trap cleanup INT TERM

sleep $DURATION

echo "Time's up. Re-enabling sleep..."
sudo pmset -a disablesleep 0
