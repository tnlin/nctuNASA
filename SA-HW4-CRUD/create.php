<?php
 if ( !empty($_POST)) {
 	require 'database.php';
        $name = $_POST['name'];
        $email = $_POST['email'];
        $mobile = $_POST['mobile'];
        $pdo = Database::connect();
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql="INSERT INTO customers(name,email,mobile) VALUES (?,?,?)";
        $q = $pdo->prepare($sql);
        $q->execute(array($name,$email,$mobile));
        Database::disconnect();
	header("location:index.php");
 }
?>

<!DOCTYPE html>
<html lang="zh-tw">
<?php require('_head.php')?>
<body>
<div class="container">
<div class="row">
   <form  class="form-horizontal" action="create.php" method="post" enctype="multipart/form-data">
     <div class="col-lg-6 col-offset-2">
	<div class="form-group">
	    <label class="col-lg-2 control-label">名字</label>
	    <div class="col-lg-10">
    	    	<input class="form-control" name="name" placeholder="請輸入您的大名" required>
	    </div>
	</div>
	<div class="form-group">
	    <label class="col-lg-2 control-label">信箱</label>
	    <div class="col-lg-10">
		<input type="email" class="form-control" name="email" placeholder="請輸入信箱" required>
	    </div>
	</div>

	<div class="form-group">
	    <label class="col-lg-2 control-label">手機</label>
	    <div class="col-lg-10">
	    	    <input name="mobile" class="form-control" placeholder="請輸入手機號碼" required>
	    </div>
	</div>
	<div class="form-group">
	    <div class="col-sm-offset-2 col-sm-10">
	      	<button type="submit" name="submit" class="btn btn-primary">Create </button>
		<a class="btn btn-default" href="index.php">Back</a>
	    </div>
	</div>
     </div>
   </form>
</div>

</div><!--Container-->
</body>

</html>
