<template>

    <div>

    <nav>
        <div class="logo">
            <img class = "toplogoimg" src="@/assets/images/logo/logo.png" alt="Shape of a head and body with a text beside saying HANAbook">
        </div>

        <ul class = "nav-links">
            <li><a href = '#'>Home</a></li>
            <li><a href = '#'>About Us</a></li>
            <li><a href = '#'>Features</a></li>
            <li><a href = '#'>Contact Us</a></li>
        </ul>

        <div class="burger">
            <div class="line1"></div>
            <div class="line2"></div>
            <div class="line3"></div>
        </div>
    </nav>


    <section class="hero">
        <div class="container">
            <div class="left-col">
                <div class="hero-cta">

                    <div class="imgcontainer">

                        <img class = "hana" src="@/assets/images/logo/just-logo.png" alt="Blue head purple body">

                        <img src="@/assets/images/bg/covidinject.jpg" class="hero-img" id = "herobro" alt="Doc giving someone an injection">

                        <div class="buttons">
                            <button type = "button" class = "buttontxt leftbtn">Register as a vaccine participant</button>
                            <button type = "button" class = "buttontxt rightbtn">Register your clinic</button>
                        </div>
                        
                    </div>

                </div>
            </div>
        </div>
    </section>

    <section class="features-section">
        <div class="container">
            <h2 class = "featuretxt">Features</h2>
            <ul class="features-list">
                <li>Find out if you are eligible for the vaccine</li>
                <li>Book your vaccine appointment as soon as possible</li>
                <li>Check in without physical contact</li>
                <li>Track your doses of vaccine and further appointments</li>
                <li>Get reminders for your upcoming appointments</li>
                <li>Obtain details of vaccine provider</li>
                <li>Healthcare clinics can fast track vaccine provision</li>
            </ul>
        </div>
    </section>

    <section class="contact-section v2cont">
        <div class="container navcontainer">
            <div class="contact-left">
                <h2>Contact us if you have trouble booking a vaccine appointment.</h2>

                <form action="">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name">

                     <label for="number">Phone Number</label>
                    <input type="text" id="number" name="number">

                    <label for="message">Message</label>
                    <textarea name="message" id="message" cols="30" rows="5"></textarea>

                    <input type="submit" class="sendmsg" value="Send message">
                </form>
            </div>
            <div class = "verticalcont">
                <iframe class = "map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d975.8113900679374!2d103.68173161688698!3d1.3473190376878703!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31da0f0a99014463%3A0xb8bb0800c52d8219!2sNanyang%20Technological%20University!5e0!3m2!1sen!2smy!4v1614425870333!5m2!1sen!2smy" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
            </div>

        </div>
    </section>

    <section class = "footer">

            <div class="logofooter">
                <img class = "footerlogoimg" src="@/assets/images/logo/logo.png" alt="Shape of a head and body with a text beside saying HANAbook">
            </div>

            <div class="copyright">
                <p>(C) Copyright by Fishy Duck Services</p>
            </div>

            <div class = "socials">
                <a target="_blank" href="#"><img class = "smallimg" src="@/assets/images/socialmedia/facebook.svg"></a>
                <a target="_blank" href="#"><img class = "smallimg" src="@/assets/images/socialmedia/insta.svg"></a>
                <a target="_blank" href="#"><img class = "smallimg" src="@/assets/images/socialmedia/twitter.svg"></a>
            </div> 

        </section>


    </div>

</template>

<style>
    @import "@/assets/scss/pages/landing.scss";
</style>

<script>
export default {
    mounted() {
        const fadeinNavMenu = () => {
            const burger = document.querySelector(".burger");
            const nav = document.querySelector(".nav-links");

            burger.addEventListener('click', () => {
               nav.classList.toggle("nav-active"); 
            });
        }

        fadeinNavMenu();
    }
}
</script>