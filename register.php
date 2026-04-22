<?php
include "db.php";
if(isset($_POST['submit'])){
$name=$_POST['name'];
$email=$_POST['email'];
$password=$_POST['password'];
$sql="INSERT INTO students(name,email,password)
VALUES('$name','$email','$password')";
if($conn->query($sql)==TRUE){
echo "Registration Successful";
}
}
?>

<!DOCTYPE html>
<html>
<head>
<title>Register</title>
<link rel="stylesheet" href="style.css">
<script src="script.js"></script>
<style>
body {
    background-color: <?php echo "white" ?>;
}
</style>
</head>
<body>
<div class="container">
<h2>Registration Form</h2>
</form>
</div>
<form method="POST" onsubmit="return validateForm()">
<input type="text" name="name" placeholder="Enter Name" required>
<input type="email" name="email" placeholder="Enter Email" required>
<input type="password" name="password" placeholder="Enter Password" required><br>
<button type="submit" name="submit">Register</button>
</body>
</html>