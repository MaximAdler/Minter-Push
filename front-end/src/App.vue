<template>
  <div id="app">
    <Main />
    <Navigation />
    <Qr />
  </div>
</template>

<script>
import Main from './components/Main';
import Navigation from './components/Navigation';
import Qr from './components/Qr';

export default {
  name: 'app',
  components: {
    Main,
    Navigation,
    Qr
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
