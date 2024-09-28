
function updateDateTime() {
// Set locale to Persian
moment.locale('fa');

// Get the current time in Tehran's timezone
const tehranTime = moment().tz('Asia/Tehran');

// Convert the current time to Jalali (Persian) format
const persianDate = tehranTime.format('jYYYY/jMM/jDD');
const persianTime = tehranTime.format('HH:mm:ss');

// Set the date and time in the navbar
document.getElementById('persian-date').innerText = persianDate;
document.getElementById('persian-time').innerText = persianTime;
}

// Update the date and time every second
setInterval(updateDateTime, 1000);

// Run the function once the page loads
document.addEventListener("DOMContentLoaded", updateDateTime);
