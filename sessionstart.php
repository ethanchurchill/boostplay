<?php
session_start();
// Now we check if the data from the login form was submitted, isset() will check if the data exists.
if ( !isset($_POST['username'], $_POST['password']) ) {
	// Could not get the data that should have been sent.
	exit('Please fill both the username and password fields!');
}
$user_name = $_POST['username'];
$pass_word = $_POST['password'];
$command_exec = escapeshellcmd("python login_engine.py $user_name $pass_word");
$str_output = shell_exec($command_exec);
if ((int)$str_output > 999) {
	// Verification success! User has logged-in!
	// Create sessions, so we know the user is logged in, they basically act like cookies but remember the data on the server.
	session_regenerate_id();
	$_SESSION['loggedin'] = TRUE;
	$_SESSION['name'] = $_POST['username'];
	$_SESSION['id'] = $id;
	$_SESSION['userid'] = (int)$str_output;
	header('Location: home.php');
} else {
	echo 'Incorrect username and/or password!';
}
?>