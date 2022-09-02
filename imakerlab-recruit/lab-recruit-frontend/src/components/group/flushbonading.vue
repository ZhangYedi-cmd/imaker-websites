<template>
  <!--嵌入式-->
  <transition appear name="animate__animated animate__bounce" enter-active-class="animate__fadeIn">
  <div class="box">
    <!-- 板块1 -->
    <div class="bg1">
      <img src="../../assets/images/flushbonading.jpg" alt=""/>
    </div>

    <!-- 板块2 -->
    <div class="box2 commonbox">
      <div class="content">
        <p class="title">嵌入式</p>
        <p>Serial.println("Hello world!");</p>
        <p>
          来到嵌入式的世界，坐拥：智能寻路小车、相辅相成的智能
          家具，六度自由机械臂、只在游戏汇总见过的六足机械人、自由飞行的无人机。
          C/C++将为我们服务
        </p>
      </div>
      <div class="img">
        <img src="../../assets/images/flushbonading-1.png" alt=""/>
      </div>
    </div>

    <!-- 板块2 -->
    <div class="box2 commonbox">
      <div class="img">
        <img src="../../assets/images/flushbonading-2.png" alt=""/>
      </div>
      <div class="content">
        <p class="title">嵌入式的定义</p>
        <p>
          国内普遍认同的嵌入式系统定义是以应用为中心，以计算机技术为基础，软硬件可裁剪，适应应用系统对功能
          、可靠性、成本、体积、功耗等严格要求的专用计算机系统。从应用对象上加以定义来说，嵌入式系统是软件和
          硬件的综合体，还可以涵盖机械等附属装置。
        </p>
      </div>
    </div>

    <!-- 板块2 -->
    <div class="box2 commonbox">
      <div class="content">
        <p class="title">嵌入式的应用</p>
        <p>个人通信与娱乐产品：只能手环、PS5</p>
        <p>家电类产品：数字电视、扫地机器人、智能家电</p>
        <p>办公自动化产品：打印机、复印机、传真机</p>
        <p>医疗电子类产品：生化分析仪、血液分析仪</p>
      </div>
      <div class="img">
        <img src="../../assets/images/flushbonading-3.jpg" alt=""/>
      </div>
    </div>

    <!-- 板块4 -->
    <div class="box4 commonbox">
      <div class="title">作品展示</div>
      <div class="list">
        <div>
          <img src="../../assets/images/flushbonading2-1.png" alt=""/>
          <div class="mask">
            <div class="title1">超声波避障小车</div>
            <div class="desc1">基于Arduino开发的超声波避障小车</div>
          </div>
        </div>

        <div>
          <img src="../../assets/images/flushbonading2-2.png" alt=""/>
          <div class="mask">
            <div class="title1">垃圾自动分拣系统</div>
            <div class="desc1">这是描述这是描述</div>
          </div>
        </div>
        <div>
          <img src="../../assets/images/flushbonading2-2.png" alt=""/>
          <div class="mask">
            <div class="title1">垃圾自动分拣系统</div>
            <div class="desc1">这是描述这是描述</div>
          </div>
        </div>

      </div>
    </div>
    <bottom></bottom>
  </div>
  </transition>
</template>

<script>
import bottom from "../base/bottom";

export default {
  name: "flush",
  components: {bottom},
};
</script>

<style scoped lang="less">
.box {
  width: 100%;
  color: white;
  display: flex;
  flex-direction: column; //主轴方向竖直
  align-items: center; //子元素居中对齐
  background: url(../../assets/images/X.png) repeat;

  .bg1 {
    width: 100%;
    //height: 700px;
    > img {
      width: 100%;
      height: 100%;
    }
  }

  .commonbox {
    width: 80%;
    padding: 20px;
    box-sizing: border-box; //转化为盒子模型
    display: flex;
    justify-content: space-around; //弹性容器对齐方式
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 40px;
  }

  .box2 {
    .content {
      width: 40%;
      min-width: 300px;

      > p {
        line-height: 30px;
        font-size: 24px;
        margin:10px;
      }

      .title {
        font-size: 40px;
        min-width: 300px;
      }
    }

    .img {
      width: 40%;
      //height: 160px;
      > img {
        width: 100%;
        height: 100%;
        border-radius: 10px;
      }
    }
  }

  .box4 {
    .title {
      font-size: 40px;
      font-weight: bold;
      margin-bottom: 40px;
    }

    .list {
      width: 100%;;
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;

      > div:hover .mask {
        top: 0;
      }

      > div {
        margin-bottom: 20px;
        width: 30%;
        height: 220px;
        border-radius: 10px;
        overflow: hidden;
        position: relative;

        > img {
          width: 100%;
          height: 100%;
        }

        > video {
          width: 100%;
          height: 100%;
        }

        .mask {
          position: absolute;
          top: 80%;
          left: 0;
          width: 100%;
          height: 100%;
          background: rgba(0, 0, 0, .6);
          color: white;
          padding: 7px 20px;
          box-sizing: border-box;
          transition: top .6s;

          .title1 {
            font-size: 28px;
          }

          .desc1 {
            font-size: 20px;
          }
        }
      }
    }
  }
}

@media screen and (max-width: 768px) {
  .box {
    .bg1 {
    }

    .box2 {
      .content {
        width: 80%;
        margin-bottom: 40px;

      }

      .img {
        width: 80%;
      }
    }

    .box4 {
      .list {
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;

        > div {
          height: 180px;
          width: 100%;
          margin-bottom: 30px;

          .mask {
            top: 79%;
            padding: 4px 20px;

          }
        }
      }
    }
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
