<template>
    <div>



    <section class="hero">
        <div class="container">
            <div class="row">
                <div class="col-lg-7 col-12">
                    <h1>Appoint Your Vaccination Schedule with HANAbook</h1>
                    <p class='fs-4'>Get your appointment schedule at the closest clinic by only a click.</p>

                    <div class="buttons-cta">
                        <nuxt-link :to="{name: 'auth-register'}" class="btn btn-primary shadow">Register Now</nuxt-link>
                    </div>
                </div>
                <div class="col-lg-5 col-12">
                    <div>
                        <img src="@/assets/images/bg/vector.png" id="hero-vector" alt="Vaccination illustration">
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="features-section">
        <div class="container">
            <h1 class="mb-5">Features</h1>
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
        <div class="container">
            <div class="row">
                <div class="col-lg-5 col-12">
                    <iframe class = "map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d975.8113900679374!2d103.68173161688698!3d1.3473190376878703!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31da0f0a99014463%3A0xb8bb0800c52d8219!2sNanyang%20Technological%20University!5e0!3m2!1sen!2smy!4v1614425870333!5m2!1sen!2smy" width="400" height="500" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
                </div>
                <div class="col-lg-6 offset-lg-1 col-12">
                    <h1>Contact us</h1>
                    <p class='fs-4'>If you have trouble booking a vaccine appointment, we will always help you.</p>

                    <form action="">
                        <div class="mb-3">
                            <label for="name">Name</label>
                            <input type="text" id="name" name="name" class='form-control'>
                        </div>
                        <div class="mb-3">
                            <label for="number">Phone Number</label>
                            <input type="text" id="number" name="number" class="form-control">
                        </div>
                        <div class="mb-3">
                            <label for="message">Message</label>
                            <textarea name="message" id="message" cols="30" rows="5"  class="form-control"></textarea>
                        </div>

                        <input type="submit" class="btn btn-primary float-end" value="Send message" >
                    </form>
                </div>
            </div>

        </div>
    </section>

</div>

</template>

<style lang="scss">
    @import "@/assets/scss/pages/landing.scss";
</style>

<script>
export default {
    mounted() {

    }
}
</script>