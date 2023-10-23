const logginn = document.getElementById("Login-Form");
const Reggisterr = document.getElementById("Register-Form");
const indicatorr = document.getElementById("indicator");
function Login(){
    indicatorr.style.transform = "translateX(18rem)";
    Reggisterr.classList.add("translate-x-1/2", "hidden");
    logginn.classList.add("translate-x-0");
    // logginn.classList.add("indicator");

    logginn.classList.remove("translate-x-1/2", "hidden");
    Reggisterr.classList.remove("translate-x-0");
    
}

function Register(){

 indicatorr.style.transform = "translateX(22.5rem)";
    logginn.classList.add("translate-x-1/2", "hidden");
    logginn.classList.remove("translate-x-0");
    Reggisterr.classList.add("translate-x-0");
    // Reggisterr.classList.add("indicator");

    Reggisterr.classList.remove("translate-x-1/2", "hidden");  
   
}