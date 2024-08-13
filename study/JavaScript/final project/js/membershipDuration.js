function calculateDuration() {
    var startDate = new Date(document.getElementById('startDate').value);
    var today = new Date();
    var duration = new Date(today - startDate);
    
    var years = duration.getUTCFullYear() - 1970; // 因为getUTCFullYear()返回的是从1970年开始的年数
    var months = duration.getUTCMonth(); // 获取月份差
    var days = duration.getUTCDate() - 1; // 获取天数差

    var resultText = `Your membership duration is ${years} years, ${months} months, and ${days} days.`;
    document.getElementById('result').innerText = resultText;
}
