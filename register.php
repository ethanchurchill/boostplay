<?php
// Now we check if the data was submitted, isset() function will check if the data exists.
if (!isset($_POST['username'], $_POST['password'], $_POST['email'])) {
	// Could not get the data that should have been sent.
	exit('Please complete the registration form!');
}
// Make sure the submitted registration values are not empty.
if (empty($_POST['username']) || empty($_POST['password']) || empty($_POST['email'])) {
	// One or more values are empty.
	exit('Please complete the registration form');
}
if (!filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
	exit('Email is not valid!');
}
if (preg_match('/^[A-Za-z0-9]{4,16}$/', $_POST['username']) == 0) {
    exit('Username is not valid!');
}
if (preg_match('/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@!%&*?])[A-Za-z\d#$@!%&*?]{8,30}$/', $_POST['password']) == 0) {
	exit('Password does not meet all requirements!');
} 
// We need to check if the account with that username exists.
$user_name = $_POST['username'];
$pass_word = $_POST['password'];
$e_mail = $_POST['email'];
$command_exec = escapeshellcmd("python registration_engine.py $user_name $pass_word $e_mail");
$str_output = shell_exec($command_exec);
if ($str_output == "0") {
	header('Location: landing.html');
} else {
	echo 'User already exists. Choose different credentials.';
}
?>

