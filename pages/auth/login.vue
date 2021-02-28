<template>
    <div>
        <div id="auth-left">
            <div class="auth-logo">
                <a href="index.html"><img src="@/assets/images/logo/logo.png" alt="Logo"></a>
            </div>
            <h1 class="auth-title">Log in.</h1>
            <p class="auth-subtitle mb-5">Log in with your data that you entered during registration.</p>
            <div class="alert alert-success" v-if="$route.query.success">Success register! Please login</div>
            <div class="alert alert-danger" v-if="error">{{error}}</div>
            <form action="index.html">
                <div class="form-group position-relative has-icon-left mb-4">
                    <input type="text" class="form-control form-control-xl" placeholder="Username" v-model="email">
                    <div class="form-control-icon">
                        <i class="bi bi-person"></i>
                    </div>
                </div>
                <div class="form-group position-relative has-icon-left mb-4">
                    <input type="password" class="form-control form-control-xl" placeholder="Password" v-model="password">
                    <div class="form-control-icon">
                        <i class="bi bi-shield-lock"></i>
                    </div>
                </div>
                <div class="form-check form-check-lg d-flex align-items-end">
                    <input class="form-check-input me-2" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label text-gray-600" for="flexCheckDefault">
                        Keep me logged in
                    </label>
                </div>
                <button class="btn btn-primary btn-block btn-lg shadow-lg mt-5" type="button" @click="login">Log in</button>
            </form>
            <div class="text-center mt-5 text-lg fs-4">
                <p class="text-gray-600">Don't have an account? <nuxt-link :to="{name: 'auth-register'}"
                        class="font-bold">Sign
                        up</nuxt-link>.</p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    layout: 'auth',
    data() {
        return {
            email: '',
            password: '',
            error: false,
        }
    },
    methods: {
        login() {
            this.$axios.post('/api/token/', {email: this.email, password: this.password})
                .then(res => {
                    this.$store.commit('setToken', res.data.access);
                    console.log(res)

                    this.$axios.defaults.headers.common['Authorization'] = `Bearer ${res.data.access}`;
                    
                    this.$axios.get('/api/token/get_user', {headers: {Authorization: `Bearer ${this.$store.state.token}`}})
                        .then(resUser => {
                            console.log(resUser.data);
                            this.$store.commit('updateUser', resUser.data[0])

                            if(resUser.data[0].is_clinic) {
                                this.$router.push("/clinic");
                            }else if(resUser.data[0].is_patient){
                                this.$router.push("/user");
                            }else{
                                this.$router.push("/user");
                            }
                        });

                }).catch(err => { 
                    console.log(err)
                    this.error = err.response.data.detail
                });
        }
    }
}
</script>

<style lang="scss" scoped>
body {
    background-color: white;
}
#auth {
    height: 100vh;
    overflow-x: hidden;
    
    #auth-right {
        height: 100%;
        background:  url(~assets/images/bg/4853433.jpg),linear-gradient(90deg,#2d499d,#3f5491);
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
}
</style>