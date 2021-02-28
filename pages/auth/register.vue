<template>
    <div>
        <div id="auth-left">
            <div class="auth-logo">
                <a href="index.html"><img src="@/assets/images/logo/logo.png" alt="Logo"></a>
            </div>
            <h1 class="auth-title">Sign Up</h1>
            <p class="auth-subtitle mb-5">Input your data to register to our website.</p>

            <form @submit.prevent="submit">
                <div class="form-group position-relative has-icon-left mb-4">
                    <select name="" id="" v-model="register.as" class="form-control form-control-xl">
                        <option value="">Register as</option>
                        <option value="patient">Patient</option>
                        <option value="clinic">Clinic</option>
                    </select>
                    <div class="form-control-icon">
                        <i class="bi bi-person"></i>
                    </div>
                </div>
                <div class="form-group position-relative has-icon-left mb-4">
                    <input type="text" class="form-control form-control-xl" name="name" placeholder="Full name" v-model="register.name">
                    <div class="form-control-icon">
                        <i class="bi bi-person"></i>
                    </div>
                </div>
                <div class="form-group position-relative has-icon-left mb-4">
                    <input type="text" class="form-control form-control-xl" name="email" placeholder="Email" v-model="register.email">
                    <div class="form-control-icon">
                        <i class="bi bi-envelope"></i>
                    </div>
                </div>
                <div class="form-group position-relative has-icon-left mb-4">
                    <input type="password" class="form-control form-control-xl" placeholder="Password" v-model="register.password">
                    <div class="form-control-icon">
                        <i class="bi bi-shield-lock"></i>
                    </div>
                </div>
                <div class="form-group position-relative has-icon-left mb-4">
                    <textarea v-model="register.address"  class="form-control form-control-xl" placeholder="Address"></textarea>
                    <div class="form-control-icon">
                        <i class="bi bi-house"></i>
                    </div>
                </div>
                <div class="form-group position-relative has-icon-left mb-4">
                    <input type="number" class="form-control form-control-xl" v-model="register.postcode" placeholder="Postcode">
                    <div class="form-control-icon">
                        <i class="bi bi-code"></i>
                    </div>
                </div>
                <div class="form-group position-relative has-icon-left mb-4">
                    <input type="text" class="form-control form-control-xl" v-model="register.state" placeholder="State">
                    <div class="form-control-icon">
                        <i class="bi bi-geo-alt"></i>
                    </div>
                </div>

                <template v-if="register.as == 'patient'">
                    <label for="">Date of birth</label>
                    <div class="form-group position-relative has-icon-left mb-4">
                        <input type="date" class="form-control form-control-xl" v-model="register.date_of_birth" placeholder="Date of birth">
                        <div class="form-control-icon">
                            <i class="bi bi-calendar"></i>
                        </div>
                    </div>
                    <div class="form-group position-relative has-icon-left mb-4">
                        <label for="">Has disease?</label>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" value="0" v-model="register.has_disease_1">
                            <label class="form-check-label" for="flexRadioDefault1">
                                No
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" value="1" v-model="register.has_disease_1">
                            <label class="form-check-label" for="flexRadioDefault2">
                                Yes
                            </label>
                        </div>
                    </div>
                </template>
                <button class="btn btn-primary btn-block btn-lg shadow-lg mt-5">Sign Up</button>
            </form>
            <div class="text-center mt-5 text-lg fs-4">
                <p class='text-gray-600'>Already have an account? <nuxt-link :to="{name:'auth-login'}"
                        class="font-bold">Log
                        in</nuxt-link>.</p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    layout: 'auth',
    data: () => ({
        register: {
            as: '',
            email: '',
            name: '',
            password: '',
            address: '',
            postcode: '',
            state: '',
            date_of_birth: '',
            has_disease_1: '',
        }
    }),
    methods: {
        submit() {
            let url = this.register.as == 'patient' ? 'api/patients/' : 'api/clinics/';
            let postdata = {
                name: this.register.name,
                email: this.register.email,
                password: this.register.password,
                addr_line_1: this.register.address,
                addr_postcode: this.register.postcode,
                addr_state: this.register.state,
            }
            if(this.register.as == 'patient') {
                postdata.dob = this.register.date_of_birth;
                postdata.has_disease_1 = this.register.has_disease_1;
            }
            this.$axios.post(url, postdata)
                .then(res => {
                    console.log(res.data)

                    this.$router.push('/auth/login?success=true');
                })
        }
    }
}
</script>

<style lang="scss" scoped>
body {
    background-color: white;
}
    
    #auth-left {
        padding: 5rem 8rem;
        
        .auth-title {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        .auth-subtitle {
            font-size: 1.7rem;
            line-height: 2.5rem;
            color: #a8aebb;
        }
        .auth-logo {
            margin-bottom: 7rem;
            img {
                height: 2rem;
            }
        }
        @media screen and (max-width: 767px) {
            padding: 5rem ;
        }
    }

</style>