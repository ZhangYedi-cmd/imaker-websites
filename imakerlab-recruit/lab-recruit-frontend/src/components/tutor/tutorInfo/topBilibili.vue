<style scoped>
  body {
    margin: 0;
    padding: 0;

  }

  header {
    height: 160px;
    position: relative;
    overflow: hidden;
    /*这里定义一个变量,可以通过Var()函数访问到*/
    --percentage: 0.5;
  }

  /*主轴交叉轴居中显示*/
  /*把几张图片摆到一行*/
  header .media,
  header .tree {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  header img,
  header video {
    position: absolute;
    display: block;
    width: 120%;
    height: 100%;
    object-fit: cover;
    /*    自适应*/
  }

  /*先从早上到晚上*/
  header .morning {
    z-index: 20;
    /*根据js传参自动计算透明度*/
    opacity: calc(1 - (var(--percentage) - 0.25) / 0.25);
  }

  header .afternoon {
    z-index: 10;
    opacity: calc(1 - (var(--percentage) - 0.5) / 0.5);
  }

  header .media {
    transform: translateX(calc(var(--percentage) * 100px));
  }

  /*树动起来*/
  header .tree {
    transform: translateX(calc(var(--percentage) * 50px));
    filter: blur(3px);
    /*    filter属性设置高斯模糊*/
  }

  header .morning .media,
  header .morning .tree,
  header .morning .morning,
  header .morning .afternoon {
    transition: none;
  }

  header .window-cover {
    opacity: calc((var(--percentage) - 0.9) / 0.1);
  }


</style>
<template>
  <el-row>
    <header>
      <div class="media">
        <!--        图片-->
        <img src="https://assets.codepen.io/2002878/bilibili-winter-view-1.jpg" class="morning" alt="">
        <img src="https://assets.codepen.io/2002878/bilibili-winter-view-2.jpg" class="afternoon" alt="">
        <!--        火焰遮罩效果-->
        <video autoplay loop muted class="evening">
          <source src="https://assets.codepen.io/2002878/bilibili-winter-view-3.webm" type="video/webm"/>
        </video>
        <img src="https://assets.codepen.io/2002878/bilibili-winter-view-3-snow.png" class="window-cover" alt="">
      </div>
<!--      <div class="tree">-->
<!--        &lt;!&ndash;        树&ndash;&gt;-->
<!--        <img src="https://assets.codepen.io/2002878/bilibili-winter-tree-1.png" class="morning" alt="">-->
<!--        <img src="https://assets.codepen.io/2002878/bilibili-winter-tree-2.png" class="afternoon" alt="">-->
<!--        <img src="https://assets.codepen.io/2002878/bilibili-winter-tree-3.png" class="evening" alt="">-->
<!--      </div>-->
    </header>
  </el-row>
</template>

<script>
  import $ from 'jquery'
  export default {
    name: "overView",
    methods: {
      init() {
        this.initDom()
      },
      initDom() {
        let startingPoint;
        $("header").on("mouseout", (e) => {
          $("header").css("--percentage", 0.5);

        });
        // 划入时自动计算位置            传入event,获取鼠标位置
        $("header").on("mouseenter", (e) => {
          console.log("话进来了")
          startingPoint = e.clientX
        })
        // 移动时动态传参
        $("header").on("mousemove", (e) => {
          console.log("话进来了")
          let percentage = (e.clientX - startingPoint) / window.outerWidth + 0.5;
          $("header").css("--percentage", percentage)
        })
      }
    },
    mounted() {
      this.init();
    }
  }
</script>


