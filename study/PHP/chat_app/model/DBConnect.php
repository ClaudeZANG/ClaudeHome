<?php
class DBConnect {
    private $server = "localhost";
    private $username = "ss"; // 使用你的实际数据库用户名
    private $password = "7147"; // 使用你的实际数据库密码
    private $dbname = "chat_app"; // 确认数据库名称

    public function getConnection() {
        $conn = new mysqli(
            $this->server, 
            $this->username, 
            $this->password, 
            $this->dbname
        );

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        return $conn;
    }
}
?>
