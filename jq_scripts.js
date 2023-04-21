
function passwordKeyUpDown() {
	confirmPassword();
	passwordRequirements();
}

function confirmPassword() {
	var password = document.querySelector('input[id=password]');
	var confirm_password = document.querySelector('input[id=confirm_password]');
	var cp_label = document.querySelector('label[id=confirm_password_label]');
	var p_label = document.querySelector('label[id=password_label]');
	var p_label_style = window.getComputedStyle(p_label);
	if (confirm_password.value === password.value && p_label_style.getPropertyValue('background-color') === "rgb(63, 179, 49)") {
		confirm_password.setCustomValidity('');
		cp_label.style.backgroundColor = "#3FB331";

	} else {
		confirm_password.setCustomValidity('Passwords do not match.');
		cp_label.style.backgroundColor = "#b4423b";
  }
}

function passwordRequirements() {
	var password = document.querySelector('input[id=password]');
	var p_label = document.querySelector('label[id=password_label]');
	if (password.value.length >= 8 && password.value.length <= 30) {
		if(/[0-9]/.test(password.value) && /[a-z]/.test(password.value) 
		   && /[A-Z]/.test(password.value) && /[#$@!%&*?]/.test(password.value)) {
			password.setCustomValidity('');
			p_label.style.backgroundColor = "#3FB331";
		} else {
			password.setCustomValidity('Password missing required characters.');
			p_label.style.backgroundColor = "#b4423b";
		}
	} else {
		password.setCustomValidity('Password not 8-30 characters long.');
		p_label.style.backgroundColor = "#b4423b";
	}
}
function usernameRequirements() {
	var username = document.querySelector('input[id=username]');
	var u_label = document.querySelector('label[id=username_label]');
	if (username.value.length >= 4 && username.value.length <= 16) {
		if(/^[0-9a-zA-Z]+$/.test(username.value)) {
			username.setCustomValidity('');
			u_label.style.backgroundColor = "#3FB331";
		} else {
			username.setCustomValidity('Username has invalid characters.');
			u_label.style.backgroundColor = "#b4423b";
		}
	} else {
		username.setCustomValidity('Username not 4-16 characters long..');
		u_label.style.backgroundColor = "#b4423b";
	}
}
function emailRequirements() {
	var email = document.querySelector('input[id=email]');
	var e_label = document.querySelector('label[id=email_label]');
	if(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email.value)) {
		email.setCustomValidity('');
		e_label.style.backgroundColor = "#3FB331";
	} else {
		email.setCustomValidity('Email is not valid.');
		e_label.style.backgroundColor = "#b4423b";
	}
}
function openTab(evt, tabName) {
  
  if (evt.currentTarget.className.includes("active")){
    evt.currentTarget.className = evt.currentTarget.className.replace(" active", "");
	document.getElementById(tabName).classList.toggle('fade');
  }
  else{
    evt.currentTarget.className += " active";
	document.getElementById(tabName).classList.toggle('fade');
//	setTimeout(function(){document.getElementById(tabName).scrollIntoView({
//		behavior: 'smooth',
//		block: 'center'
//	});}, 500);
	
  }

}
function defaultTab(){
	document.getElementById("defaultOpen").click();
}

function sendData(val) {
    var data = {
        value: val
    };

    var xhr = new XMLHttpRequest();

    //👇 set the PHP page you want to send data to
    xhr.open("POST", "characterbuilder.php", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    //👇 what to do when you receive a response
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            alert(xhr.responseText);
        }
    };

    //👇 send the data
    xhr.send(JSON.stringify(data));
}