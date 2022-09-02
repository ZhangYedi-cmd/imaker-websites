<template>
  <div class="box">
    <transition-group appear name="animate__animated animate__bounce" enter-active-class="animate__zoomIn">
      <h1 class="title1" key="1">Imakerlab</h1>
      <h1 class="title2" key="2">安力群大学生创新实验室</h1>
      <p class="desc" key="3">创新是第一生产力，跟我们一起用自己的双手把想象投射现实</p>
    </transition-group>

    <!-- 探索按钮 -->
    <transition appear name="animate__animated animate__bounce" enter-active-class="animate__zoomIn">
      <div class="button">
        <button class="commonbtn" @click="goOthers('/joinUs')">Join&nbsp;Us &gt;</button>
        <button class="commonbtn btn2">Found&nbsp;Us</button>
      </div>
    </transition>
    <transition-group appear name="animate__animated animate__bounce" enter-active-class="animate__zoomIn">
      <div
        class="btn"
        v-for="(item, index) in list"
        :key="index"
        :style="{ right: item.right + 'px', bottom: item.bottom + 'px',userSelect:'none'}"
      >{{ item.content }}
      </div>
    </transition-group>
  </div>
</template>

<script>
import 'animate.css';
// 3dmax
export default {
  data() {
    return {
      list: [
        {right: 470, bottom: 300, content: "Java"},
        {right: 370, bottom: 423, content: "Vue"},
        {right: 315, bottom: 234, content: "CSS"},
        {right: 294, bottom: 466, content: "Html"},
        {right: 82, bottom: 354, content: "嵌入式"},
        {right: 410, bottom: 632, content: "PhotoShop"},
        {right: 170, bottom: 456, content: "Android"},
        {right: 94, bottom: 452, content: "Lua"},
        {right: 294, bottom: 542, content: "SolidWorks "},
        {right: 204, bottom: 122, content: "Rust"},
        {right: 202, bottom: 245, content: "Au"},
        {right: 512, bottom: 234, content: "UG"},
        {right: 215, bottom: 323, content: "OpenCV"},
        {right: 402, bottom: 198, content: "Matlab"},
        {right: 202, bottom: 532, content: "C/C++"},
        {right: 312, bottom: 422, content: "Ae"},
        {right: 514, bottom: 345, content: "Pr"},
        {right: 315, bottom: 345, content: "设计"},
        {right: 402, bottom: 323, content: "UE4"},
        {right: 192, bottom: 634, content: "Unity"},
        {right: 425, bottom: 358, content: "OS"},
        {right: 295, bottom: 145, content: "C#"},
        {right: 450, bottom: 532, content: "JavaScript"},
        {right: 570, bottom: 252, content: "Python"},
      ],
    };
  },
  methods: {
    goOthers(url) {
      this.$router.push(url);
    },
  }
}

</script>

<style scoped lang="less">
.box {
  height: 800px;
  width: 100%;
  padding: 60px 4% 0;
  box-sizing: border-box;
  position: relative;
  background: url(../../assets/images/homebgc1.jpg) no-repeat center/cover;
  color: white;

  .title2 {
    margin-top: 40px;
    font-size: 50px;
  }

  .title1 {
    font-size: 40px;
    margin-top: 50px;
  }

  .desc {
    font-size: 20px;
    margin-top: 40px;
    font-weight: lighter;
  }

  .button {
    display: flex;
    flex-direction: column;

    .commonbtn {
      width: 150px;
      height: 60px;
      background: #4c8bf5;
      margin-top: 40px;
      font-family: DengXian;
      font-weight: 400;
      color: #ffffff;
      border: none;
    }

    .btn2 {
      background: none;
      color: #4c8bf5;
      border: 1px solid #4c8bf5;
    }
  }
}

.btn {
  position: absolute;
  padding: 10px;
  text-align: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  color: white;
}

@media screen and (max-width: 768px) {
  .box {
    height: 700px;

    .title1 {
      font-size: 28px;
    }

    .title2 {
      font-size: 30px;
    }

    .desc {
      line-height: 40px;
      font-size: 16px;
    }

    .button {
      .commonbtn {
        margin-top: 30px;
      }
    }
  }

  .btn {
    display: none;
  }
}

/*屏幕宽度 大于768px 且 小于992px 时*/
@media screen and (min-width: 768px) and (max-width: 992px) {
  .btn {
    display: none;

  }

  .box {
    .title2 {
      font-size: 40px;
    }
  }
}

/*屏幕宽度 大于992px 且 小于1200px 时*/
@media screen and (min-width: 992px) and (max-width: 1200px) {
  .box {
    .title2 {
      font-size: 40px;
    }
  }
}

/*屏幕宽度 大于1200px 时*/
@media screen and (min-width: 1200px) {
}
</style>
