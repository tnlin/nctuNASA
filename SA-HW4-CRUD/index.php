<!DOCTYPE html>
<html lang="zh-tw">
<?php require('_head.php')?>
<body>
<div class="container">
<div class="row">
           <a class="btn btn-primary" href="create.php">Create</a>
	   <hr>
           <table class="table table-striped table-bordered">
             <tbody>
                     <tr>
			<th>ID</th>
			<th>Name</th>
			<th>Email</th>
			<th>Mobile</th>
			<th>Action</th>
                     </tr>
                     <?php
                           include 'database.php';
                           $pdo = Database::connect();
                           $sql = 'SELECT * FROM customers ORDER BY id DESC';
                           $q = $pdo->prepare($sql);
                           $q->execute();
                           foreach ($q as $row) {
                            echo '<tr>';
                            echo '<td>'. $row['id'] . '</td>';
                            echo '<td>'. $row['name'] . '</td>';
                            echo '<td>'. $row['email'] . '</td>';
                            echo '<td>'. $row['mobile'] . '</td>';
                            echo '<td>';
                            echo '<a class="btn btn-default"  href="read.php?id=' .$row['id']. '">Read</a> ';
                            echo '<a class="btn btn-success" href="update.php?id='.$row['id']. '">Update</a> ';
                            echo '<a class="btn btn-danger"  href="delete.php?id='.$row['id']. '">Delete</a> ';
                            echo '</td>';
                            echo '</tr>';
                           }
                           Database::disconnect();
                        ?>
              </tbody>
	    </table>
</div><!--row-->
</div><!--container-->
<body>
<html>
