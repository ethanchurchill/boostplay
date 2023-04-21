<?php
// We need to use sessions, so you should always start sessions using the below code.
session_start();
// If the user is not logged in redirect to the login page...
if (!isset($_SESSION['loggedin'])) {
	  header('Location: landing.html');
	  exit;
}

$val = $_POST['char-submit'];
$_SESSION['charid'] = $val;
$userid = $_SESSION['userid'];
$command_exec = escapeshellcmd("python characterbuilder.py $val $userid");
$str_output = shell_exec($command_exec);
$chararray = json_decode($str_output, true);

function checkNull($input, $catch){
	if ($input == null){
		return $catch;
	}
	else{
		return $input;
	}
}
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
  <body onpageshow="defaultTab()">
	<nav class = "nav_bar" id="nb">
		<a href="home.php" id="boostplay" class="logo_a">
		  <img src="assets/BoostPlay.png" class="logo" col="g">
		  <img src="assets/BoostPlay_Neon.png" class="logo_none" col="b">
		</a>
		<ul class = "nav_ul nav_ul_left" >
			<li class = "nav_li"><a class = "nav_li_a" href="profile.php">Profile <i class="fas fa-user-circle"></i></a></li>
			<li class = "nav_li"><a class = "nav_li_a" href="about.html">About <i class="fa-solid fa-question"></i></a></li>
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
	<!-- Tab links -->
	<!-- Tab content -->
	<div class="tabcontainer">
		<div class="tab">
			<div class="sidebar-nav">
				<button class="tablinks" name="overviewtab" onclick="openTab(event, 'Overview')" id="defaultOpen">Overview</button>
				<button class="tablinks" name="classtab" onclick="openTab(event, 'Class')" id="classtab">Class</button>
		 		<button class="tablinks" name="speciestab" onclick="openTab(event, 'Species')" id="speciestab">Species</button>
		 		<button class="tablinks" name="scorestab" onclick="openTab(event, 'Scores')" id="scorestab">Scores</button>
				<button class="tablinks" name="descriptiontab" onclick="openTab(event, 'Description')" id="descriptiontab">Description</button>
				<button class="tablinks" name="equipmenttab" onclick="openTab(event, 'Equipment')" id="equipmenttab">Equipment</button>
			</div>
		</div>
		<p style="color: red; text-align: center"><?= $str_output ?></p>
		<form action="action_charbuild.php" method="post" class="char-form">
			<input type="submit" name="char-save" class="dnd-save" value="Save">
			<div id="Overview" class="tabcontent">
				<div class=tabheader>
					<h1 class="tabheader_header">Overview</h1>
				</div>
				<div class="content-section">
					<h3 class="section-header">Character Name</h3>
					<?php
					if($chararray[0]['name'] == ""){
						$text = "<input type=\"text\" name=\"char-name\" placeholder=\"Name\" class=\"dnd-input\">";
					}
					else{
						$text = "<input type=\"text\" name=\"char-name\" placeholder=\"Name\" class=\"dnd-input\" value=\"{$chararray[0]['name']}\">";
					}
					echo strip_tags($text, '<input>');
					?>
				</div>
				<div class="content-section">
					<h3 class="section-header">Progression Type</h3>
					<p class="section-desc">Story-based progression / Experience-based progression</p>
					<select class="dnd-select" id="progtype" name="progtype">
						<option value="Milestone">Milestone</option>
						<option value="XP">XP</option>
					</select>
				</div>
				<div class="content-section">
					<h3 class="section-header">Hit Point Type</h3>
					<p class="section-desc">Increase Hit Points based on class fixed values / Manually inserted Hit Points</p>
					<select class="dnd-select" id="hptype">
						<option value="fixed">Fixed</option>
						<option value="manual">Manual</option>
					</select>
				</div>
				<div class="content-section">
					<h3 class="section-header">Encumbrance Type</h3>
					<p class="section-desc">Don't use Encumbrance rules / Use standard Encumbrance rules / Use more detailed optional Encumbrance rules</p>
					<select class="dnd-select" id="encumtype">
						<option value="noencum">No Encumbrance</option>
						<option value="useencum">Use Encumbrance</option>
						<option value="usevarencum">Use Variant Encumbrance</option>
					</select>
				</div>
			  	<div class="content-section">
					<h3 class="section-header">Ignore Coin Weight</h3>
				  	<p class="section-desc">Don't count coins in when calculating Encumbrance (50 coins is 1 lb.)</p>
					<div class="toggle-button-cover">
					  	<div class="button-cover">
							<div class="button r" id="button-1">
						  		<input type="checkbox" class="checkbox" />
						  		<div class="knobs"></div>
						  		<div class="layer"></div>
							</div>
					  	</div>
					</div>
				</div>
			</div>
			<div id="Class" class="tabcontent">
				<div class=tabheader>
					<h1 class="tabheader_header">Class</h1>
				</div>
				<div class="content-section">
					<ul class="classlist">
						<li id="artificer">Artificer</li>
						<li id="barbarian">Barbarian</li>
						<li id="bard">Bard</li>
						<li id="cleric">Cleric</li>
						<li id="druid">Druid</li>
						<li id="fighter">Fighter</li>
						<li id="monk">Monk</li>
					</ul>
					<ul class="classlist classlist_right">
						<li id="paladin">Paladin</li>
						<li id="ranger">Ranger</li>
						<li id="rogue">Rogue</li>
						<li id="sorcerer">Sorcerer</li>
						<li id="warlock">Warlock</li>
						<li id="wizard">Wizard</li>
					</ul>
				</div>
			</div>

			<div id="Species" class="tabcontent">
				<div class=tabheader>
					<h1 class="tabheader_header">Species</h1>
				</div>
				<div class="content-section">
				</div>
			</div>

			<div id="Scores" class="tabcontent">
				<div class=tabheader>
					<h1 class="tabheader_header">Scores</h1>
				</div>
			</div>
			
			<div id="Description" class="tabcontent">
				<div class=tabheader>
					<h1 class="tabheader_header">Description</h1>
				</div>
			</div>
			
			<div id="Equipment" class="tabcontent">
				<div class=tabheader>
					<h1 class="tabheader_header">Equipment</h1>
				</div>
			</div>
		</form>
	</div>
  </body>
</html>