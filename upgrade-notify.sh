#sudo nano /usr/local/bin/upgrade-notify.sh

#!/bin/bash
MESSAGE="$1"
if [ -z "$MESSAGE" ]; then
exit 1
fi
/usr/bin/wall "$MESSAGE"
