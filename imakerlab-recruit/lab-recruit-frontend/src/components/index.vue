<template>
  <div>
    <topNav></topNav>
    <div class="main" >
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import topNav from "./base/topNav";

export default {
  name: "index",
  components: {
    topNav
  }
}
</script>

<style scoped lang="less">

</style>
