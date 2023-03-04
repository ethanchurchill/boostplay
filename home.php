<?php
// We need to use sessions, so you should always start sessions using the below code.
session_start();
// If the user is not logged in redirect to the login page...
if (!isset($_SESSION['loggedin'])) {
	header('Location: landing.html');
	exit;
}
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <!--<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">-->
    <link href="styleM.css" rel="stylesheet" type="text/css"> 
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer">
	<link href="hvr.js" type="text/javascript">
    <title>BoostPlay</title>
  </head>
  <body>
	<nav class = "nav_bar">
		<a href="home.php" id="boostplay" class="logo_a" onmouseover="hvr(this, 'in')" onmouseleave="hvr(this, 'out')">
		  <img src="assets/BoostPlay.png" class="logo" col="g">
		  <img src="assets/BoostPlay_Neon" class="logo_none" col="b">
		</a>
		<ul class = "nav_ul nav_ul_left" >
			<li class = "nav_li"><a class = "nav_li_a" href="profile.php">Profile <i class="fas fa-user-circle"></i></a></li>
			<li class = "nav_li"><a class = "nav_li_a" href="about.html">About</a></li>
		</ul>
        <div class="dropdown">
            <button class="dropbtn">Settings
                <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
                <a class = "nav_li_a" href="logout.php">Sign out <i class="fas fa-sign-out-alt"></i></a>
            </div>
        </div>
	</nav>
  </body>
</html>