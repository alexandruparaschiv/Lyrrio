<template>
  <div id="app">
          <div id="vp">
            <vue-particles color="#dedede"></vue-particles>
          </div>
        <LyricsForm />
        Created by Alexandru Paraschiv
  </div>
</template>

<script>
import LyricsForm from './components/LyricsForm.vue'

export default {
  name: 'App',
  components: {
    LyricsForm
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#vp {    position : absolute;
    width:100%;
    height:100%;
    z-index:-1;
}

body{
/*background: rgb(2,0,36);
background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 11%, rgba(0,212,255,1) 100%);*/
background:#16191c;}
</style>
