<?php include 'db.php'; ?>

<!DOCTYPE html>
<html>
<head>
    <title>Student List</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; } 
    </style>
</head>
<body>

<h2>Student Records</h2>

<form method="GET" action="">
    <input type="text" name="search" placeholder="Search by First Name...">
    <input type="submit" value="Search">
    <a href="index.php">Reset</a>
</form>
<br>
<a href="create.php">Add New Student</a>
<br><br>

<table>
    <tr>
        <th>ID</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>CGPA</th>
        <th>Semester</th>
        <th>Actions</th>
    </tr>
    <?php
    // Search Logic 
    if (isset($_GET['search'])) {
        $filtervalues = $_GET['search'];
        // Using LIKE for partial matches 
        $sql = "SELECT * FROM student WHERE Fname LIKE '%$filtervalues%'";
    } else {
        $sql = "SELECT * FROM student"; // Default: Show all 
    }

    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Loop through results 
        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row['id'] . "</td>";
            echo "<td>" . $row['Fname'] . "</td>"; 
            echo "<td>" . $row['Lname'] . "</td>";
            echo "<td>" . $row['cgpa'] . "</td>";
            echo "<td>" . $row['semester'] . "</td>";
            // Action Links 
            echo "<td>
                    <a href='edit.php?id=" . $row['id'] . "'>Edit</a> |
                    <a href='delete.php?id=" . $row['id'] . "' onclick=\"return confirm('Are you sure?');\">Delete</a>
                  </td>";
            echo "</tr>";
        }
    } else {
        echo "<tr><td colspan='6'>No records found</td></tr>";
    }
    ?>
</table>

</body>
</html>