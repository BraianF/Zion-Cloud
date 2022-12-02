<template>
  <div id="home">
    <h1>Sorry, my home is a little messy</h1>
    <span>Pena que o trocadilho só funciona direito em inglês</span>
    <div>
    <img src="/img/patrick.webp" alt="Em construção">
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    // HelloWorld
  }
}
</script>

<style>
    #home {
        margin: auto;
        text-align: center;
    }

    #home span, #home div img {
        margin-top: 30px;
        margin-bottom: 30px;
    }
    #home h1 {
        font-size: 42px;
        margin-bottom: 30px;
        color: #222;
    }
</style>