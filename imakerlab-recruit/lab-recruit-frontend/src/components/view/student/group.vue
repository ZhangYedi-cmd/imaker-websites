<!--组别的公共页面-->
<template>
    <div class="main" >
      <danMu></danMu>
      <router-view></router-view>
    </div>
</template>

<script>
import bottom from "../../base/bottom";
import danMu from "../../base/danMu";
import flushbonading from "../../group/flushbonading";
import design from "../../group/design";

    export default {
        name: "group",
        components: {
          danMu,
          flushbonading,
          design,
          bottom
      }
    }
</script>

<style scoped>
  .main {
    display: grid;
  }
</style>
