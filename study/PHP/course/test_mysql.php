<?php
$mysqli = new mysqli("localhost", "ss", "7147", "world");

if ($mysqli->connect_error) {
  die("fail: " . $mysqli->connect_error);
}
echo "good";
?>
