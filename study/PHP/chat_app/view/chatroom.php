<?php
session_start();

if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
    header("location: login.html");
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Room</title>
    <link rel="stylesheet" href="../public/css/styles.css">
</head>
<body>
    <div class="container">
        <h1>Welcome to the Chat Room, <?php echo htmlspecialchars($_SESSION["Username"]); ?>!</h1>

        <!-- 显示已发送消息的区域 -->
        <div id="messages"></div>

        <!-- 输入和发送消息的表单 -->
        <form id="chatForm" method="post" enctype="multipart/form-data">
            <input type="text" name="message" id="messageInput" placeholder="Type a message...">
            <input type="file" name="media" id="mediaInput" accept="image/*,video/*,audio/*">
            <button type="submit">Send</button>
        </form>
        
        <!-- 假设有JavaScript文件处理消息加载和发送 -->
        <script src="../public/js/script.js"></script>
    </div>

    <script>
    document.getElementById('chatForm').addEventListener('submit', function(e) {
        e.preventDefault();

        var formData = new FormData(this);
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '../controller/MessageController.php', true);
        xhr.onload = function() {
            if (this.status == 200) {
                loadMessages(); // 成功发送消息后重新加载消息
                document.getElementById('messageInput').value = ''; // 清空输入框
            }
        };
        xhr.send(formData);
    });

    function loadMessages() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '../controller/get_messages.php', true); // 确保这个路径正确
        xhr.onload = function() {
            if (this.status == 200) {
                document.getElementById('messages').innerHTML = this.responseText;
            }
        };
        xhr.send();
    }

    setInterval(loadMessages, 1000); // 每1秒刷新一次消息
    window.onload = loadMessages; // 页面加载时获取消息
    </script>
</body>
</html>
