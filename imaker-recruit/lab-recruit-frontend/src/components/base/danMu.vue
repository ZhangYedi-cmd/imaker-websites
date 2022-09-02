<template>
  <div class="box">
    <div class="location">
      <img src="../../assets/images/location.png" alt="">
    </div>
    <div class="nav">
      <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="transparent"
        text-color="#fff"
        active-text-color="#9ac8f0"
      >
        <el-menu-item class="el-menu-item" index="C / C++">C/C++</el-menu-item>
        <el-menu-item class="el-menu-item" index="Java">Java</el-menu-item>
        <el-menu-item class="el-menu-item" index="Python">Python</el-menu-item>
        <el-menu-item class="el-menu-item" index="设计">设计</el-menu-item>
        <el-menu-item class="el-menu-item" index="前端">前端</el-menu-item>
        <el-menu-item class="el-menu-item" index="嵌入式">嵌入式</el-menu-item>
      </el-menu>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      group: "C / C++",
      url: "../barry.html",
      activeIndex: "1",
      activeIndex2: "1",
    };
  },

  methods: {
    handleSelect(key, keyPath) {
      console.log(key);
      switch (key) {
        case "Java":
          this.$router.push("/group/java");
          break;
        case "rust":
          this.$router.push("/group/rust");
          break;
        case "C / C++":
          this.$router.push("/group/c");
          break;
        case "Python":
          this.$router.push("/group/python");
          break;
        case "设计":
          this.$router.push("/group/design");
          break;
        case "前端":
          this.$router.push("/group/webfront");
          break;
        case "嵌入式":
          this.$router.push("/group/flushbonading");
          break;
      }
    },
  },
};
</script>

<style scoped lang="less">
  .box{
    width: 100%;
    height: 400px;
    background: url(../../assets/images/group-common.png) no-repeat center/cover;
    padding-top: 80px;
    position: relative;
    .nav{
      width: 100%;
      position: absolute;
      bottom: 0;
      font-size: 30px;
      .el-menu-demo{
        width: 100%;
        display: flex;
        justify-content: space-around;
        border: none;
        flex-wrap: wrap;
        text-align: center;
        .el-menu-item{
          font-size: 26px;
        }
      }
    }
  }
</style>
