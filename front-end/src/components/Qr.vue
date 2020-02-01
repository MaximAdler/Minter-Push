<template lang="html">
  <div class="qr_main">
    <div class="qr_code">
        <img src="../pictures/1.png" alt="">
    </div>
    <div class="qr_path">
      <p class="qr_status">Отправьте монеты на этот адрес</p>
      <p class="qr_hash">Mx4b07582bce440e86842a92b12cdefeb66e6caf74</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Qr'
}
</script>

<style lang="css" scoped>
  .qr_main {
    width: 587px;
    height: 156px;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    margin-top: 46px;
  }
  .qr_path {
    width: 406px;
    height: 55px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-left: 25px;
    margin-top: 28px;
  }
  .qr_status {
    color: #979797;
    font-family: 'PT Sans', sans-serif;
    font-size: 16px;
    margin-bottom: 11px;
  }
  .qr_hash {
    color: #D15C22;
    font-family: 'PT Sans', sans-serif;
    font-size: 18px;
    font-style: bold;
    font-weight: 700;
    margin: 0;
  }
</style>
