<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // 发送邮件（这只是一个示例，实际需要配置服务器支持邮件发送功能）
    $to = "restaurant@example.com";
    $subject = "New Order from $name";
    $body = "Name: $name\nEmail: $email\nMessage/Order Details:\n$message";

    if (mail($to, $subject, $body)) {
      echo "Order submitted successfully!";
    } else {
      echo "Failed to submit order.";
    }
  }
?>
