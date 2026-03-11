# https://github.com/ram133/picoclaw/cron.sh
# Path: picoclaw/cron.sh

(crontab -l 2>/dev/null; echo "00 09 * * * cd ~/picoclaw && /usr/bin/python3 realty.py") | crontab -
