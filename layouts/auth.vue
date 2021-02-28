<template>
    <div class="row h-100" id="auth">
        <div class="col-lg-5 col-12">
            <Nuxt/>
        </div>
        <div class="col-lg-7 d-none d-lg-block">
            <div id="auth-right">

            </div>
        </div>
    </div>
</template>
<style scoped>
#auth {
    background-color: #fff;
    height: 100vh;
    overflow-x: hidden;
}

#auth-right {
    height: 100%;
    background:  url(~assets/images/bg/4853433.jpg),linear-gradient(90deg,#2d499d,#3f5491);
}
</style>