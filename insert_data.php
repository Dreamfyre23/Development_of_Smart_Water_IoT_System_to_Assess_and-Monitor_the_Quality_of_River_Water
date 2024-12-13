<?php
include ('./config.php');

date_default_timezone_set('Asia/Kolkata');
$dt = new DateTime();
// echo $dt->format('H:i:s');
// VALUES ('".$dt->format('H:i:s')."','".$_GET['temperature']."','".$_GET['turbidity']."','".$_GET['ph']."')");
// VALUES ('".$dt->format('H:i:s')."','".$_GET['temperature']."','".$_GET['turbidity']."','".$_GET['ph']."','".$_GET['solids']."','".$_GET['result']."','".$_GET['wqi']."','".$_GET['rating']."')");
// VALUES ('".$dt->format('H:i:s')."','".$_GET['temperature']."','".$_GET['turbidity']."','".$_GET['ph']."','".$_GET['solids']."','".$_GET['wqi']."','".$_GET['rating']."')");

$con = mysqli_connect('localhost',$username,$password) 
or die('Cannot connect to the DB');

mysqli_select_db($con, $database_name);

mysqli_query($con,"INSERT INTO reading (time,temperature,turbidity,ph,solids,result,wqi,rating)
  VALUES ('".$dt->format('H:i:s')."','".$_GET['temperature']."','".$_GET['turbidity']."','".$_GET['ph']."','".$_GET['solids']."','".$_GET['result']."','".$_GET['wqi']."','".$_GET['rating']."')");

mysqli_close($con);
echo "Successfully insert new data";

?>