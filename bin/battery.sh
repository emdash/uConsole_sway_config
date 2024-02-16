case "$(cat /sys/class/power_supply/axp20x-battery/status)" in
    Charging) echo -n '⚡︎';;
    *)        echo -n '🔋';;
esac
     
cat /sys/class/power_supply/axp20x-battery/capacity
