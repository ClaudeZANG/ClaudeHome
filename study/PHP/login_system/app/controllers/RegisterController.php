<?php
// RegisterController.php

require_once '../../config/db_connect.php'; // 更正路径

class RegisterController {
    private $db;

    public function __construct($dbConnection) {
        $this->db = $dbConnection;
    }

    public function register() {
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $username = $_POST['username'];
            $password = $_POST['password'];

            // 对密码进行加密
            $passwordHash = password_hash($password, PASSWORD_DEFAULT);

            // 将用户信息存储到数据库
            $stmt = $this->db->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
            $stmt->bind_param("ss", $username, $passwordHash);

            if ($stmt->execute()) {
                // 注册成功，自动跳转到登录页面
                header("Location: /public/login.html"); // 确保这个路径与你的项目结构匹配
                exit;
            } else {
                // 注册失败，显示错误信息
                echo "注册失败：" . $this->db->error;
            }
        }
    }
}

// 假设$db是你已经成功建立的数据库连接实例
$registerController = new RegisterController($conn);
$registerController->register();
?>
