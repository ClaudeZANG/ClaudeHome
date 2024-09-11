<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 获取表单数据
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $phone = htmlspecialchars($_POST['phone']);
    $address = htmlspecialchars($_POST['address']);
    $food = htmlspecialchars($_POST['food']);
    $quantity = intval($_POST['quantity']);
    $payment = htmlspecialchars($_POST['payment']);

    // 数据库连接信息
    $servername = "localhost";
    $username = "root";
    $password = ""; // 根据你的 MySQL 设置
    $dbname = "restaurant_orders"; // 确保已创建此数据库

    // 创建连接
    $conn = new mysqli($servername, $username, $password, $dbname);

    // 检查连接是否成功
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // 插入数据SQL语句
    $sql = "INSERT INTO orders (name, email, phone, address, food, quantity, payment) 
            VALUES ('$name', '$email', '$phone', '$address', '$food', $quantity, '$payment')";

    // 执行插入操作并检测是否成功
    if ($conn->query($sql) === TRUE) {
        echo "<h1>Thank you for your order, $name!</h1>";
        echo "<p>We have received your order of $quantity $food(s). The order will be delivered to $address. Payment will be done via $payment.</p>";
        echo "<p>If you have any questions, please contact us at $phone or via email: $email.</p>";
    } else {
        echo "<p>There was an error submitting your order. Please try again later or contact us if the issue persists.</p>";
        error_log("Error: " . $sql . "<br>" . $conn->error);  // 记录错误到服务器日志
    }

    // 关闭连接
    $conn->close();
}
?>
