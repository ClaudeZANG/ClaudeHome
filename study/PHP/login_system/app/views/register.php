<?php
// 假设这是在处理注册请求的PHP文件中
require_once '../../config/db_connect.php'; // 根据实际路径调整

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 获取用户提交的数据
    $username = $_POST['username'];
    $password = $_POST['password']; // 注意：实际操作中应该对输入数据进行验证和清洗

    // 对密码进行加密
    $passwordHash = password_hash($password, PASSWORD_DEFAULT);

    // 将用户信息存储到数据库
    $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $passwordHash);

    if ($stmt->execute()) {
        // 注册成功，可以重定向到登录页面或显示成功消息
        echo "注册成功！<a href='login.html'>点击这里登录</a>";
    } else {
        // 注册失败，显示错误信息
        echo "注册失败：" . $conn->error;
    }
}
?>
