<?php
$hostName = "localhost";
$dbUser = "root";
$dbPassword = "";
$dbName = "reg";
$conn = mysqli_connect("localhost","root",$dbPassword,"reg");
if (!$conn) {
    die("Something went wrong;");
}

?>