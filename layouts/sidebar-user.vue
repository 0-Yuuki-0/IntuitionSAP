<template>
  <div id="app">
      <div id="sidebar" class="active">
          <SidebarUser></SidebarUser>
      </div>
      <div id="main" class='layout-navbar'>
          <Header></Header>
          <Nuxt/>
          <Footer></Footer>
      </div>
  </div>
</template>
<script>
export default {
    
}
</script>