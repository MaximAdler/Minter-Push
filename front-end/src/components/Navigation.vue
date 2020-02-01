<template lang="html">
  <div class="nav_main">
      <a class="nav_point active" href="#">Пополнение</a>
      <a class="nav_point" href="#">Подтверждение</a>
      <a class="nav_point" href="#">Поделиться</a>
  </div>
</template>

<script>
export default {
}

data: ()

</script>

<style lang="css" scoped>
  .nav_main {
    width: 591px;
    height: 34px;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin: 0 auto;
    border-bottom: 2px solid #D4D4D4;
  }
  .nav_point {
    width: 197px;
    height: 34px;
    text-decoration: none;
    color: black;
    font-family: 'PT Sans', sans-serif;
    font-size: 16px;
  }
  .active, .nav_point:hover {
    border-bottom: 2px solid #D15C22;
  }
</style>
