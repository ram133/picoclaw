// /picoclaw/microbilling/billing.js
let startTime;
let timerVar;
let isActive = false;
const ratePerSecond = 0.0025; // Example: $9.00 per hour rate

function toggleWork() {
    const btn = document.getElementById('action-btn');
    const status = document.getElementById('status-text');
    
    if (!isActive) {
        startTime = Date.now();
        isActive = true;
        btn.innerText = "Stop & Submit Work";
        btn.style.backgroundColor = "red";
        status.innerText = "RECORDING...";
        timerVar = setInterval(updateBilling, 1000);
        logAction("Session Started");
    } else {
        clearInterval(timerVar);
        submitWork(Date.now() - startTime);
        resetTerminal();
    }
}

function updateBilling() {
    let elapsed = (Date.now() - startTime) / 1000;
    let earned = elapsed * ratePerSecond;
    document.getElementById('live-billing').innerText = earned.toFixed(4);
}

function logAction(msg) {
    const log = document.getElementById('log-display');
    log.innerHTML += `<p>[${new Date().toLocaleTimeString()}] ${msg}</p>`;
}

function resetTerminal() {
    isActive = false;
    document.getElementById('action-btn').innerText = "Start Micro-Billing Task";
    document.getElementById('action-btn').style.backgroundColor = "";
    document.getElementById('status-text').innerText = "IDLE";
}

function submitWork(durationMs) {
    logAction(`Session Ended. Total Duration: ${(durationMs/1000).toFixed(2)}s`);
    // API call to update ray.services backend would go here
}
