let selectedOptions = [];

document.getElementById('addFeedbackOption').addEventListener('click', function() {
    const select = document.getElementById('feedbackOptions');
    const selectedValue = select.value;
    if (!selectedOptions.includes(selectedValue)) {
        selectedOptions.push(selectedValue);
        updateSelectedOptionsDisplay();
    }
});

function updateSelectedOptionsDisplay() {
    const display = document.getElementById('selectedOptions');
    display.innerHTML = `Selected options: ${selectedOptions.join(', ')}`;
}

document.getElementById('feedbackForm').addEventListener('submit', function(e) {
    e.preventDefault();

    var name = document.getElementById('name').value;
    var postalCode = document.getElementById('postalCode').value;
    if (!/^\d{6}$/.test(postalCode)) {
        alert('Invalid postal code. It should be 6 digits.');
        return;
    }

    alert('Thank you for your feedback!');
    // 这里可以添加代码将表单数据发送到服务器
});
