<?php
// We need to use sessions, so you should always start sessions using the below code.
session_start();
// If the user is not logged in redirect to the login page...
if (!isset($_SESSION['loggedin'])) {
	  header('Location: landing.html');
	  exit;
}
$action = 'retrieve';
$userid = $_SESSION['userid'];
$command_exec = escapeshellcmd("python characterbuilder.py $action $userid");
$str_output = shell_exec($command_exec);
function writeMod($score){
	$mod = (int)(($score) / 2) - 5;
	if ($score > 9){
		return "(+{$mod})";
	}
	else{
		return "({$mod})";
	}
}
function checkNull($input, $catch){
	if ($input == null){
		return $catch;
	}
	else{
		return $input;
	}
}
?>
<!DOCTYPE html>
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
  <body style="color: red;">
	<nav class = "nav_bar" id="nb">
		<a href="home.php" id="boostplay" class="logo_a">
		  <img src="assets/BoostPlay.png" class="logo" col="g">
		  <img src="assets/BoostPlay_Neon.png" class="logo_none" col="b">
		</a>
		<ul class = "nav_ul nav_ul_left" >
			<li class = "nav_li"><a class = "nav_li_a" href="profile.php">Profile <i class="fas fa-user-circle"></i></a></li>
			<li class = "nav_li"><a class = "nav_li_a" href="about.html">About <i class="fa-solid fa-question"></i></a></li>
			<li class = "nav_li"><a class = "nav_li_a" href="characterbuilder.php">Builder</a></li>
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
	<div class="char-area">
		<h1 class="section-header-large">My Characters</h1>
		<form action="characterbuilder.php" method="post" class="dnd-add-form">
			<input type="submit" name="char-submit" class="dnd-add" value="new-char">
		</form>
		<form action="characterbuilder.php" method="post">
			<?php
			$chararray = json_decode($str_output, true);
			for ($i = 0; $i < count($chararray); $i++){
				$text = "<button class=\"char-box\" name= \"char-submit\" type=\"submit\" value=\"char-{$chararray[$i][0]}\">";
				$text .= "<img class=\"dnd-pfp\" src=\"assets/red-circle-300-300.png\">";
				$text .= "<table><tr>";
				$text .= "<td><p class=\"char-box-snippet\">" . checkNull($chararray[$i][1]['name'], 'Character name') . "</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score\">STR:</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score-num\">{$chararray[$i][1]['scores']['str']}" . writeMod($chararray[$i][1]['scores']['str']) . "</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score\">CHA:</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score-num\">{$chararray[$i][1]['scores']['cha']}" . writeMod($chararray[$i][1]['scores']['str']) . "</p></td>";
				$text .= "</tr><tr>";
				$text .= "<td><p class=\"char-box-snippet\">" . checkNull($chararray[$i][1]['species'], 'No Species') . "</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score\">DEX:</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score-num\">{$chararray[$i][1]['scores']['dex']}" . writeMod($chararray[$i][1]['scores']['str']) . "</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score\">WIS:</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score-num\">{$chararray[$i][1]['scores']['wis']}" . writeMod($chararray[$i][1]['scores']['str']) . "</p></td>";
				$text .= "</tr><tr>";
				$text .= "<td><p class=\"char-box-snippet\">" . checkNull($chararray[$i][1]['class'][0], 'No Class') . "</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score\">CON:</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score-num\">{$chararray[$i][1]['scores']['con']}" . writeMod($chararray[$i][1]['scores']['str']) . "</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score\">INT:</p></td>";
				$text .= "<td><p class=\"char-box-snippet-score-num\">{$chararray[$i][1]['scores']['int']}" . writeMod($chararray[$i][1]['scores']['str']) . "</p></td>";
				$text .= "</tr></table></button>";
				echo strip_tags($text, '<button><table><img><p><a><tr><td>');
			}
			?>
		</form>
	</div>
	
	<p style="color: red;"><?= $str_output ?></p>
  </body>
</html>