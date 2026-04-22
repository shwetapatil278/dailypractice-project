<?php
session_start();
if(!isset($_SESSION['email'])){
header("location:login.php");
}
?>

<!DOCTYPE html>
<html>
<head>
<title>Dashboard</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
<h1>Welcome</h1>
<p>You are logged in successfully</p>
<a href="logout.php">Logout</a>
</div>
</body>
</html>