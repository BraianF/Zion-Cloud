<template>
    <div>
        <Preloader/>
        <Navbar/>
        <router-view/>
        <Footer/>
    </div>
</template>

<script>
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Preloader from "./components/Preloader.vue";

export default {
    components: {
        Navbar,
        Footer,
        Preloader,
    },
    data() {
        return {
        }
    },
}
</script>

<style>
</style>
