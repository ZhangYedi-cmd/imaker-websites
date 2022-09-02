<template>
  <div class="top">
    <div class="logo">
      <img src="../../assets/images/logo.png" alt=""/>
    </div>
    <!-- 大屏显示 -->
    <div class="nav">
      <el-menu
        :default-active="activeIndex"
        text-color="white"
        active-text-color="white"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
      >
        <el-menu-item index="1" @click="goOthers('/home')"
        >情况概述
        </el-menu-item
        >
        <el-menu-item index="2" @click="goOthers('/joinUs')"
        >加入我们
        </el-menu-item
        >
        <el-menu-item index="3" @click="goOthers('/group')"
        >技术交流
        </el-menu-item
        >
        <el-menu-item index="4" @click="goOthers('/home')"
        >资料整合
        </el-menu-item
        >
        <el-menu-item index="5" @click="goOthers('/home')">提问箱</el-menu-item>
      </el-menu>
    </div>
    <!-- 小屏显示 -->
    <div class="smallnav">
      <div
        @click="drawer"
        style="
          height: 20%;
          background: none;
          border: none;
          width: 20%;
          box-sizing: border-box;
          float: right;
        "
      >
        <img
          :src="imgsrc"
          alt=""
          style="width: 100%"
        />
      </div>

      <div class="mask" v-if="ismask">
        <p
          v-for="(item, index) in list"
          :key="index"
          @click="gotopage(item)"
          style="text-align: center; cursor: pointer;line-height: 40px;"
        >
          {{ item.title }}
        </p>
      </div>
      <div class="masks" v-if="ismask"></div>
    </div>
  </div>
</template>
<script>
import img1 from "../../assets/images/fenlei.png";
import img2 from "../../assets/images/cha.png";

export default {
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
      ismask: false,
      imgsrc: img1,
      list: [
        {title: "情况概述", path: "/home"},
        {title: "加入我们", path: "/joinUs"},
        {title: "技术交流", path: "/group"},
        {title: "资料整合", path: "/home"},
        {title: "提问箱", path: "/home"},
      ],
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    goOthers(url) {
      this.$router.push(url);
    },
    gotopage(item) {
      this.$router.push(item.path);
      this.ismask = false;
      this.imgsrc = img1;
    },
    drawer() {
      this.ismask = !this.ismask;
      if (this.ismask) {
        this.imgsrc = img2;
      } else {
        this.imgsrc = img1;
      }
    }
  },
};
</script>
<style scoped lang="less">
.masks {
  position: absolute;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 60px;
  background: rgba(0, 0, 0, .6);
}

.mask {
  position: absolute;
  top: 60px;
  left: 0;
  width: 100%;
  background: white;
  z-index: 1;
}

.top {
  z-index: 99;
  box-sizing: border-box;
  padding: 0 5%;
  width: 100%;
  position: absolute;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;

  .nav {
    width: 60%;
    display: flex;

    .el-menu-demo {
      width: 100%;
      display: flex !important;
      justify-content: space-around !important;
    }
  }

  .logo {
    width: 15%;
    height: 80%;
    z-index: 1000;

    img {
      padding-top: 5%;
      width: 60%;
    }
  }
}

.el-menu-demo {
  background: transparent;
}

.el-menu-item {
  background: none !important;
}

.el-menu.el-menu--horizontal {
  border-bottom: none !important;
}

.smallnav {
  display: none;
}

@media screen and (max-width: 768px) {
  .nav {
    display: none !important;
  }

  .logo {
    width: 30% !important;
  }

  .smallnav {
    display: block;
  }
}

/*屏幕宽度 大于700px 且 小于900px 时*/
@media screen and (min-width: 768px) and (max-width: 992px) {
}

/*屏幕宽度 大于900px 且 小于1200px 时*/
@media screen and (min-width: 992px) and (max-width: 1200px) {
}

/*屏幕宽度 大于1200px 时*/
@media screen and (min-width: 1200px) {
}
</style>
