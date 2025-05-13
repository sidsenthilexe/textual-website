
function updateClock(elementId, timeZone, city) {
    const now = new Date();
    const timeOptions = {
        timeZone: timeZone,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    };
    const dateOptions = {
        timeZone: timeZone,
        year: 'numeric',
        month: 'short',
        day: '2-digit',
    };
    const timeFormat = new Intl.DateTimeFormat('en-US', timeOptions);
    const dateFormat = new Intl.DateTimeFormat('en-US', dateOptions);

    const timeFormatted = timeFormat.format(now);
    const dateFormatted = dateFormat.format(now);

    const nowMs = now.getMilliseconds();
    const hundredths = Math.floor(nowMs / 100);
    document.getElementById(elementId).textContent = `I am currently in ${city}, and it is ${timeFormatted}.${hundredths} local time on ${dateFormatted}`;
    
}

setInterval(() => {
    updateClock('city-time', 'America/Los_Angeles', 'Sunnyvale, CA')
}, 100)