<?php
// 引入数据库连接配置
require_once '../../config/db_connect.php';

class LoginController {
    private $conn;

    public function __construct($dbConnection) {
        $this->conn = $dbConnection;
    }

    public function login() {
        session_start(); // 开始会话

        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            if (isset($_POST["username"]) && isset($_POST["password"])) {
                $username = $_POST["username"];
                $submittedPassword = $_POST["password"];
                
                // 准备SQL查询，验证用户名
                $stmt = $this->conn->prepare("SELECT * FROM users WHERE username = ?");
                $stmt->bind_param("s", $username);
                $stmt->execute();
                $result = $stmt->get_result();
                
                if ($result->num_rows > 0) {
                    $user = $result->fetch_assoc();
                    // 验证密码
                    if (password_verify($submittedPassword, $user['password'])) {
                        // 登录成功，设置会话变量
                        $_SESSION["loggedin"] = true;
                        $_SESSION["username"] = $username; // 可以保存用户名或其他用户信息
                        
                        // 重定向到欢迎页面
                        header("Location: ../views/welcome.php");
                        exit;
                    } else {
                        // 密码不正确
                        header("Location: ../../public/login.html?error=invalid_credentials");
                        exit;
                    }
                } else {
                    // 用户名不存在
                    header("Location: ../../public/login.html?error=invalid_credentials");
                    exit;
                }
            } else {
                header("Location: ../../public/login.html?error=missing_credentials");
                exit;
            }
        } else {
            header("Location: ../../public/login.html");
            exit;
        }
    }
}

// 创建LoginController实例并传递数据库连接
$loginController = new LoginController($conn);

// 调用login方法
$loginController->login();
?>
