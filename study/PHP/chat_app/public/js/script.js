function loadMessages() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '../controller/get_messages.php', true);
    xhr.onload = function() {
        if (this.status == 200) {
            var messagesDiv = document.getElementById('messages');
            messagesDiv.innerHTML = this.responseText;
            // 滚动到div的底部
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
    };
    xhr.send();
}

// 定时刷新消息
setInterval(loadMessages, 1000); // 每1秒刷新一次消息

// 页面加载时获取消息
document.addEventListener('DOMContentLoaded', loadMessages);
