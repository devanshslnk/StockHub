window.onload = function() {
   var btnLogin = document.getElementById("btn-login");
   var btnSignup = document.getElementById("btn-signup");
   var formBody = document.getElementById("form-body");
   var loginContainer = document.getElementById("login-container");
   var signupContainer = document.getElementById("signup-container");
   
   btnLogin.addEventListener("click", function() {
       formBody.classList.add('hide');
       this.setAttribute('disabled', 'true');
       
       setTimeout(function() {
           formBody.style.background = "#EEE";
           formBody.style.padding = "0 40px";
           signupContainer.style.display = "none";
           loginContainer.style.display = "block";
       }, 500);
       
       setTimeout(function() {
                       formBody.classList.remove('hide');
       }, 500);
       
       setTimeout(function() {
           btnSignup.removeAttribute('disabled');
       }, 600);
   });
   
   btnSignup.addEventListener("click", function() {
       formBody.classList.add('hide');
       this.setAttribute('disabled', 'true');
       
       setTimeout(function() {
           formBody.style.background = "#EEE";
           formBody.style.padding = "0 15px";
           signupContainer.style.display = "block";
           loginContainer.style.display = "none";
       }, 500);
       
       setTimeout(function() {
           formBody.classList.remove('hide');
       }, 500);
       
       setTimeout(function() {
           btnLogin.removeAttribute('disabled');
       }, 600);
   });
   
};