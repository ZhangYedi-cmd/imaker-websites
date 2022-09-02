<template>
  <!--设计-->
  <transition appear name="animate__animated animate__bounce" enter-active-class="animate__fadeIn">
    <div class="box">
      <!-- 板块1 -->
      <div class="bg1"><img src="../../assets/images/pybg.png" alt=""/></div>

      <!-- 板块2 -->
      <!--    <div class="box2 commonbox">-->
      <!--      <div class="content">-->
      <!--        <p class="title">Python</p>-->
      <!--        <p>print("Hello world!")</p>-->
      <!--        <p>爬虫</p>-->
      <!--        <p>机器学习</p>-->
      <!--        <p>深度学习</p>-->
      <!--        <p>人生苦短，我要学Python</p>-->
      <!--      </div>-->
      <!--      <div class="img">-->
      <!--        <img src="../../assets/images/python-1.png" alt="" />-->
      <!--      </div>-->
      <!--    </div>-->

      <!-- 板块2 -->
      <div class="box2 commonbox" style="background: none">
        <div class="img">
          <img src="../../assets/images/python-2.png" alt=""/>
        </div>
        <div class="content">
          <p style="font-size: 30px;color: yellow">python能做什么？</p>
          <p>
          <p>
            <img
              src="../../assets/images/bigoo.png"
              alt=""
              style="width: 30px; vertical-align: middle"
            />
            1、AI
          </p>

          <p><img
            src="../../assets/images/bigoo.png"
            alt=""
            style="width: 30px; vertical-align: middle"
          />2、爬虫</p>
          <p><img
            src="../../assets/images/bigoo.png"
            alt=""
            style="width: 30px; vertical-align: middle"
          />3、自动化</p>
          <p><img
            src="../../assets/images/bigoo.png"
            alt=""
            style="width: 30px; vertical-align: middle"
          />4、数据分析</p>
          <p><img
            src="../../assets/images/bigoo.png"
            alt=""
            style="width: 30px; vertical-align: middle"
          />5、web</p>
          <p><img
            src="../../assets/images/bigoo.png"
            alt=""
            style="width: 30px; vertical-align: middle"
          />6、脚本</p>
          <p><img
            src="../../assets/images/bigoo.png"
            alt=""
            style="width: 30px; vertical-align: middle"
          />7、GUI界面</p>
        </div>
      </div>

      <!-- 板块4 -->
      <div class="box4 commonbox">
        <div class="title">作品展示</div>
        <div class="list">
          <div>
            <img src="../../assets/images/python2-1.png" alt=""/>
            <div class="mask">
              <div class="title1">HERO VS ROGUE游戏</div>
              <div class="desc1">
                一款格斗类游戏，算法随机生成10个相连的地图，主角在其中进行格斗
              </div>
            </div>
          </div>

          <div>
            <img src="../../assets/images/python2-2.png" alt=""/>
            <div class="mask">
              <div class="title1">表白神神器</div>
              <div class="desc1">
                基于Python中的pygame模板制作的跨年表白神器，快去表白！
                <a href="https://blog.csdn.net/weixin_51390582">大佬博客</a>
              </div>
            </div>
          </div>
          <div>
            <img src="../../assets/images/Seq_3.jpg" alt=""/>
            <div class="mask">
              <div class="title1">神经风格迁移</div>
              <div class="desc1">
                用于将两个图像各自的内容（内容参考图像）和风格（风格参考图像）混合
              </div>
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
  name: "python",
  components: {bottom},
};
</script>

<style scoped lang="less">
.box {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  color: white;
  background: url(../../assets/images/c2.jpg) no-repeat center/cover;

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
    box-sizing: border-box;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 40px;
  }

  .box2 {
    background: url(../../assets/images/pybg2.png) no-repeat center/cover;
    height: 600px;

    .img {
      > img {
        border-radius: 10px;
      }
    }

    .content {
      width: 40%;
      min-width: 300px;

      > p {
        line-height: 30px;
        font-size: 24px;
        margin-top: 10px;
      }

      .title {
        font-size: 40px;
        min-width: 300px;
      }
    }

    .img {
      width: 40%;

      > img {
        width: 100%;
        height: 100%;
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
      //height: 400px;
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

