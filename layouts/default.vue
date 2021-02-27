<template>
    <div class='main-layout'>
        <nav class="navbar navbar-expand-lg navbar-light ">
            <div class="container">
                <a class="navbar-brand" href="#">
                    <img class = "toplogoimg" src="@/assets/images/logo/logo.png" alt="Shape of a head and body with a text beside saying HANAbook">
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About Us</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Contact Us</a>
                    </li>
                </ul>
                </div>
            </div>
        </nav>
        <Nuxt/>

        
        <section class = "footer">
            <div class="container">
                <div class="d-flex justify-content-between align-items-center">
                    <div class="copyright">
                        <p class='mb-0'>&copy; Copyright by Fishy Duck Services</p>
                    </div>
                    <div class = "socials">
                        <a href=""><i class="bi bi-facebook"></i></a>
                        <a href=""><i class="bi bi-instagram"></i></a>
                        <a href=""><i class="bi bi-twitter"></i></a>
                    </div> 
                </div>
            </div>
        </section>
    </div>
</template>