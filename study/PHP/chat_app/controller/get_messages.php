<?php
session_start();
require_once '../model/DBConnect.php';

if (isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
    $db = new DBConnect();
    $conn = $db->getConnection();

    $sql = "SELECT messages.*, users.username FROM messages JOIN users ON messages.UserID = users.UserID ORDER BY messages.created_at ASC";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            // 先显示时间，时间和消息之间空一行
            echo "<div class='message-time'><small>Sent on " . date("Y-m-d H:i:s", strtotime($row["created_at"])) . "</small></div>";
            echo "<div class='message'><strong>" . htmlspecialchars($row["username"]) . ":</strong><br>" . htmlspecialchars($row["MessageText"]);
            if (!empty($row["FileLink"])) {
                echo "<br><a href='../" . htmlspecialchars($row["FileLink"]) . "' target='_blank'>View File</a>";
            }
            echo "</div><br>"; // 在消息后添加额外的空行
        }
    } else {
        echo "No messages.";
    }
    $conn->close();
} else {
    echo "User not logged in.";
}
?>
