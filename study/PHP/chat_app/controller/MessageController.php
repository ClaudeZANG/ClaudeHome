<?php
session_start();
require_once '../model/DBConnect.php'; // 注意目录名称的更新为model
require_once '../model/FileUpload.php'; // 引用FileUpload类

if (isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
    $db = new DBConnect();
    $conn = $db->getConnection();
    $userID = $_SESSION["UserID"];
    $messageText = isset($_POST["message"]) ? trim($_POST["message"]) : "";
    $fileLink = null;

    // 处理文件上传
    if (isset($_FILES["media"]) && $_FILES["media"]["error"] == 0) {
        try {
            $uploader = new FileUpload();
            $fileLink = $uploader->upload($_FILES["media"]); // 使用FileUpload处理上传
        } catch (Exception $e) {
            die($e->getMessage()); // 出错时打印错误消息
        }
    }

    $messageText = htmlspecialchars($messageText, ENT_QUOTES, 'UTF-8');

    // 插入消息到数据库，包括文本和文件链接
    $sql = "INSERT INTO messages (UserID, MessageText, FileLink) VALUES (?, ?, ?)";
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("iss", $userID, $messageText, $fileLink);
        if (!$stmt->execute()) {
            echo "Error: " . $stmt->error;
        } else {
            // 可能在此处添加更多逻辑
            header("Location: ../view/chatroom.php"); // 发送成功后重定向回聊天室页面
            exit; // 确保重定向后停止脚本执行
        }
        $stmt->close();
    } else {
        echo "Database error.";
    }
    $conn->close();
} else {
    // 重定向到登录页面
    header("Location: ../view/login.html");
    exit;
}
?>
