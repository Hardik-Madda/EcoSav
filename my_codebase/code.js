const container = document.querySelector(".container"),
      pwShowHide = document.querySelectorAll(".showHidePw"),
      pwFields = document.querySelectorAll(".password"),
      signUp = document.querySelector(".signup-link"),
      login = document.querySelector(".login-link"),
      navbar = document.querySelector(".navbar"),
      searchBox = document.querySelector(".search-box .bx-search");
    
    
    pwShowHide.forEach(eyeIcon =>{
        eyeIcon.addEventListener("click", ()=>{
            pwFields.forEach(pwField =>{
                if(pwField.type ==="password"){
                    pwField.type = "text";

                    pwShowHide.forEach(icon =>{
                        icon.classList.replace("uil-eye-slash", "uil-eye");
                    })
                }else{
                    pwField.type = "password";

                    pwShowHide.forEach(icon =>{
                        icon.classList.replace("uil-eye", "uil-eye-slash");
                    })
                }
            }) 
        })
    })

    signUp.addEventListener("click", ( )=>{
        container.classList.add("active");
    });
    login.addEventListener("click", ( )=>{
        container.classList.remove("active");
    });

     function auth(){
        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;
        if(email== "dawghardik@gmail.com" && password=="Daviel@69"){
            window.location.assign("homepage.html");
            alert("Login successful");
        } 
        else{
            alert("Invalid information");
            return;
        }
     }

     searchBox.addEventListener("click", ()=>{
        navbar.classList.toggle("showInput");
        if(navbar.classList.contains("showInput")){
          searchBox.classList.replace("bx-search" ,"bx-x");
        }else {
          searchBox.classList.replace("bx-x" ,"bx-search");
        }
      });
      
      let navLinks = document.querySelector(".nav-links");
      let menuOpenBtn = document.querySelector(".navbar .bx-menu");
      let menuCloseBtn = document.querySelector(".nav-links .bx-x");
      menuOpenBtn.onclick = function() {
      navLinks.style.left = "0";
      }
      menuCloseBtn.onclick = function() {
      navLinks.style.left = "-100%";
      }
      
      let htmlcssArrow = document.querySelector(".htmlcss-arrow");
      htmlcssArrow.onclick = function() {
       navLinks.classList.toggle("show1");
      }
      let moreArrow = document.querySelector(".more-arrow");
      moreArrow.onclick = function() {
       navLinks.classList.toggle("show2");
      }
      let jsArrow = document.querySelector(".js-arrow");
      jsArrow.onclick = function() {
       navLinks.classList.toggle("show3");
      }