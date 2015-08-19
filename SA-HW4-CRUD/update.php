<?php
        require 'database.php';
        $id = null;
        if ( !empty($_GET['id'])) {
                $id = $_REQUEST['id'];
        }

        if ( null==$id ) {
                header("Location: index.php");
        }

        if ( !empty($_POST)) {
                $name = $_POST['name'];
                $email = $_POST['email'];
                $mobile = $_POST['mobile'];

                $pdo = Database::connect();
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                $sql = "UPDATE customers set name = ?, email = ?, mobile = ? WHERE id = ?";
                $q = $pdo->prepare($sql);
                $q->execute(array($name,$email,$mobile,$id));
                Database::disconnect();
                header("Location: index.php");
        } else {
                $pdo = Database::connect();
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                $sql = "SELECT * FROM customers where id = ?";
                $q = $pdo->prepare($sql);
                $q->execute(array($id));
                $data = $q->fetch(PDO::FETCH_ASSOC);
                $name = $data['name'];
                $email = $data['email'];
                $mobile = $data['mobile'];
                Database::disconnect();
        }
?>

<html lang="zh-tw">
<?php include '_head.php';?>
<body>
    <div class="container">
                <div class="col-lg-6 col-lg-offset-2">
                        <div class="row">
                                <h3>Update a Customer</h3>
                        </div>
                        <form class="form-horizontal" action="update.php?id=<?php echo $id?>" method="post">
                          	<div class="control-group <?php echo !empty($nameError)?'error':'';?>">
                                    <label class="control-label">Name</label>
                                    <div class="controls">
                                        <input name="name" type="text"  class="form-control" value="<?php echo !empty($name)?$name:'';?>" required>
                                   </div>
                                 </div>
                                 <div class="control-group <?php echo !empty($emailError)?'error':'';?>">
                                    <label class="control-label">Email Address</label>
                                    <div class="controls">
                                        <input name="email" type="text" class="form-control" value="<?php echo !empty($email)?$email:'';?>" required>
                                    </div>
                                  </div>
                                  <div class="control-group <?php echo !empty($urlError)?'error':'';?>">
                                    <label class="control-label">mobile</label>
                                    <div class="controls">
                                        <input name="mobile" type="text" class="form-control" value="<?php echo !empty($mobile)?$mobile:'';?>" required>
                                    </div>
                                  </div>
				  <hr>
                                  <div class="form-actions">
                                       <button type="submit" class="btn btn-success">Update</button>
                                       <a class="btn btn-default" href="index.php">Back</a>
                                  </div>
                         </form>
              </div>
   </div> <!-- /container -->
  </body>
</html>

