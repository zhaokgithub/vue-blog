<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import HeaderLayout from "./components/layout/HeaderLayout";
export default {
  name: "app",
  components: {
    HeaderLayout
  }
};
</script>

<style>
body,
html,
section {
  height: 100%;
  margin:0px;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}
</style>
