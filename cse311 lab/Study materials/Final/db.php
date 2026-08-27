<?php
$servername = "localhost";
$username = "root"; // Default XAMPP user 
$password = "";     // Default XAMPP password 
$dbname = "test1";  // Database from Week 7 PDF 

// Create connection using Object-Oriented style 
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection 
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error); // Stops script on error 
}
?>