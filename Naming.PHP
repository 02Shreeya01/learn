<?php
$host = "localhost";
$user = "root";
$password = '';
$db_name = "login details";
$con = mysql_connection($host, $password, $db_name,$_REQUEST,$);
if (mysql_connection_errno()) {
    die("Filed to Connect with PHPSQL:" . mysqli_connect_errno());
}
