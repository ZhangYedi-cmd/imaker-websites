<template>
  <!--设计-->
  <transition appear name="animate__animated animate__bounce" enter-active-class="animate__fadeIn">
    <div class="box">

      <div class="box0"></div>
      <!-- 板块2 -->
      <div class="boxbg">
        <div class="box3  commonbox ">
          <div class="content">
            <p class="title">设计</p>
            <p>可能包含以下内容：</p>
            <p>PS PR AE AU XD全家桶</p>
            <p>unity UE游戏策划 编程 美工</p>
            <p>哔哩哔哩鸽子窝</p>
          </div>
          <div class="img">
            <img src="../../assets/images/design-1.jpg" alt="">
          </div>
        </div>

        <!-- 板块2 -->
        <div class="box2 commonbox">
          <div class="img">
            <img src="../../assets/images/design-2.jpg" alt="">
          </div>
          <div class="content">
            <p class="title">授课内容</p>
            <p>Week1：PS的基础工具</p>
            <p>Week2：视频简单制作</p>
            <p>Week3：PS进阶教程</p>
            <p>Week4：设计漫谈</p>
          </div>
        </div>


        <!-- 板块4 -->
        <div class="box4 commonbox">
          <div class="title">作品展示</div>
          <div class="list">

            <div>
              <img src="../../assets/images/design2-1.png" alt="">
              <div class="mask">
                <div class="title1">假如没有物联网</div>
                <div class="desc1">物理仿真实验 制作软件：UE4</div>
              </div>
            </div>

            <div>
              <img src="../../assets/images/design2-2.png" alt="">
              <div class="mask">
                <div class="title1">灯塔计划（游戏）</div>
                <div class="desc1">意识慢慢回笼，你迷迷糊糊的睁开眼，白炽灯的光刺痛了你的神经。</div>
              </div>
            </div>
            <div>
              <img src="../../assets/images/design2-3.png" alt="">
              <div class="mask">
                <div class="title1">CarryMeBack</div>
                <div class="desc1">一款2D故事驱动类跑酷游戏。游戏玩家控制角色——患有抑郁症的小女孩诺诺，寻找属于自己的温暖记忆。
                  <a href="https://www.bilibili.com/video/BV1154y1t7dt?spm_id_from=333.999.0.0">制作实录</a>
                </div>

              </div>
            </div>

            <div>
              <img src="../../assets/images/design2-4.png" alt="">
              <div class="mask">
                <div class="title1">3D建模室内设计</div>
                <div class="desc1">3D建模室内设计（渲染图）制作软件：3Dmax</div>
              </div>
            </div>

            <div>
              <img src="../../assets/images/design2-5.png" alt="">
              <div class="mask">
                <div class="title1">萌遇</div>
                <div class="desc1">萌遇APP的UI设计（部分）</div>
              </div>
            </div>
            <div>
              <video src="../../assets/images/design2-6.mp4" autoplay loop></video>
              <div class="mask">
                <div class="title1">魔法师模型展示【自制】</div>
                <div class="desc1">Live2D动态立绘</div>
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
  name: "design",
  components: {bottom}
}
</script>

<style scoped lang="less">


.box {
  width: 100%;
  color: white;
  display: flex;
  flex-direction: column; //主轴方向竖直
  align-items: center; //子元素居中对齐

  #longbox {
    width: 100%;
  }

  .box0 {
    height: 1400px;
    width: 100%;
    background: url(../../assets/images/real设计top.jpg) no-repeat top/cover;

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

  .boxbg {
    background: url(../../assets/images/real设计.jpg) no-repeat top/cover;
    width: 100%;
    color: white;
    display: flex;
    flex-direction: column; //主轴方向竖直
    align-items: center; //子元素居中对齐

    .box3 {
      //height: 600px;
      //margin-bottom: 40px;

      .content {
        width: 40%;
        min-width: 300px;
        text-align: center;

        > p {
          line-height: 30px;
          font-size: 24px;
        }
      ;

        .title {
          font-size: 40px;
          min-width: 300px;
        }
      }

      .img {
        width: 40%;
        //height: 300px;

        > img {
          width: 100%;
          height: 100%;
          border-radius: 10px;
        }
      }
    }

    .box2 {
      .content {
        width: 40%;
        min-width: 300px;
        text-align: center;

        > p {
          line-height: 30px;
          font-size: 24px;
        }
      ;

        .title {
          font-size: 40px;
          min-width: 300px;
        }
      }

      .img {
        width: 40%;
        //height: 300px;

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

              > a {
                text-decoration: none;
                color: #66ccff;
              }
            }
          }
        }
      }
    }

  }


}


@media screen and (max-width: 768px ) {
  .box {
    .commonbox {
      width: 100%
    }

    .box0 {
      height: 400px;
    }

    .bg1 {
      height: 400px;
    }

    .boxbg {
      .box2 {
        .content {
          width: 80%;
          margin-bottom: 40px;
        }

        .img {
          width: 80%;

        }
      }

      .box3 {
        .li {
          width: 80%;

          .imgs {
            width: 100%;
            //height: 180px;
          }
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
            width: 80%;
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
}

/*屏幕宽度 大于700px 且 小于900px 时*/
@media screen and (min-width: 700px) and (max-width: 992px ) {
  .box {
    .commonbox {
      width: 100%
    }
  }
}

/*屏幕宽度 大于900px 且 小于1200px 时*/
@media screen and (min-width: 992px) and (max-width: 1200px ) {
  .box {
    .commonbox {
      width: 100%
    }
  }

}

/*屏幕宽度 大于1200px 时*/
@media screen and (min-width: 1200px ) {

}

</style>
