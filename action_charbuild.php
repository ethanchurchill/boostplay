<?php
session_start();
if (!isset($_SESSION['loggedin'])) {
	header('Location: landing.html');
	exit;
}
$char['charid'] = $_SESSION['charid'];
if(isset($_POST['char-name'])){
	$char['name'] = $_POST['char-name'];
}
if(isset($_POST['progtype'])){
	$char['progtype'] = $_POST['progtype'];
}
$char_struct['chardata'] = json_encode($char);
$char_json = json_encode($char_struct);
$userid = $_SESSION['userid'];

$command_exec = escapeshellcmd("python characterbuilder.py " . $char_json . " " . $userid);
$str_output = shell_exec($command_exec);
// header("Location: characterbuilder.php");
?>
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
	  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <script src="jq_scripts.js"></script>
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <!--<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">-->
    <link href="styleM.css" rel="stylesheet" type="text/css"> 
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer">
    <title>BoostPlay</title>
  </head>
  <body>
  	<p style="color: red;"><?= $str_output ?></p>
  </body>
  </html>
