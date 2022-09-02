<template>
  <!--主页-->
  <div>
    <glide></glide>
    <introduce></introduce>
  </div>
</template>

<script>
  import glide from "../../home/glide";
  import introduce from "../../home/introduce";

  export default {
    name: "home",
    components: {
      glide,
      introduce
    }
  }
</script>

<style scoped>

</style>
