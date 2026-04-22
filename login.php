<?php
session_start();
include "db.php";
if(isset($_POST['login'])){
$email=$_POST['email'];
$password=$_POST['password'];
$sql="SELECT * FROM students WHERE email='$email'
AND password='$password'";
$result=$conn->query($sql);
if($result->num_rows>0){
$_SESSION['email']=$email;
header("location:dashboard.php");
}
else{
echo "Invalid Login";
}
}
?>

<!DOCTYPE html>
<html>
<head>
<title>Login</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
<h2>Login</h2>
<form method="POST">
<input type="email" name="email" placeholder="Enter Email" required>
<input type="password" name="password" placeholder="Enter Password" required>
<button type="submit" name="login">Login</button>
</form>
</div>
</body>
</html>