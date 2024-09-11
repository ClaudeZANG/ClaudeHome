<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Order Details - DESI Rasoi</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- Header Section -->
  <header>
    <div class="header-container">
      <img src="header-image.png" alt="Header Image" class="header-image">
      <h1>Order Details</h1>
    </div>
  </header>

  <!-- Back to Orders Button -->
  <div class="back-button-container">
    <a href="orders_history.php" class="back-button">Back to Orders</a>
  </div>

  <!-- Order Details Section -->
  <main>
    <div class="order-details-container">
      <h2>Order Information</h2>

      <?php
      // 获取订单 ID
      $order_id = $_GET['id'];

      // 数据库连接信息
      $servername = "localhost"; 
      $username = "root"; 
      $password = ""; 
      $dbname = "restaurant_orders"; 

      // 创建连接
      $conn = new mysqli($servername, $username, $password, $dbname);

      // 检查连接
      if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
      }

      // 查询指定 ID 的订单数据
      $sql = "SELECT * FROM orders WHERE id = $order_id";
      $result = $conn->query($sql);

      if ($result->num_rows > 0) {
        // 输出订单详细信息
        while($row = $result->fetch_assoc()) {
          echo "<p><strong>Order ID:</strong> " . $row["id"] . "</p>";
          echo "<p><strong>Name:</strong> " . $row["name"] . "</p>";
          echo "<p><strong>Email:</strong> " . $row["email"] . "</p>";
          echo "<p><strong>Phone:</strong> " . $row["phone"] . "</p>";
          echo "<p><strong>Address:</strong> " . $row["address"] . "</p>";
          echo "<p><strong>Food:</strong> " . $row["food"] . "</p>";
          echo "<p><strong>Quantity:</strong> " . $row["quantity"] . "</p>";
          echo "<p><strong>Payment Method:</strong> " . $row["payment"] . "</p>";
        }
      } else {
        echo "<p>Order not found.</p>";
      }

      // 关闭连接
      $conn->close();
      ?>

    </div>
  </main>

  <!-- Footer Section -->
  <footer>
    <p>© 2024 DESI Rasoi - Surrey. All rights reserved.</p>
  </footer>

  <!-- Styles for Order Details -->
  <style>
    .order-details-container {
      max-width: 600px;
      margin: 20px auto;
      padding: 20px;
      background-color: #f9f9f9;
      border: 1px solid #ddd;
      border-radius: 8px;
    }

    p {
      font-size: 18px;
      margin-bottom: 10px;
    }

    strong {
      font-weight: bold;
    }
  </style>

</body>
</html>
