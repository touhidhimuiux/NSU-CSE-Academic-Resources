<?php
include 'db.php';

if (isset($_GET['id'])) { // Get ID from URL 
    $id = $_GET['id'];

    // Delete Query 
    $sql = "DELETE FROM student WHERE id = $id";

    if ($conn->query($sql) === TRUE) {
        header("Location: index.php");
    } else {
        echo "Error deleting record: " . $conn->error;
    }
}
?>