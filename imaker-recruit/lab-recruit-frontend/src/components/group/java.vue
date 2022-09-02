<template>
  <transition appear name="animate__animated animate__bounce" enter-active-class="animate__fadeIn">
    <div class="box">
      <!-- 板块1 -->
      <div class="bg1"><img src="../../assets/images/javabg.png" alt=""/></div>
      <!-- 板块3 -->
      <div class="box3  commonbox">
        <div class="content">
          <p class="title">Java</p>
          <p>System.out.print("Hello world!");</p>
          <p>别听C++的，Java才是世界上最好的语言</p>
          <p>
            Java————一种创造与强大并存的语言，在这里每个人都可以找到自己的“对象”！
          </p>
          <p>
            加入我们，无需基础，你将学到：Java基础，网站建设，APP开发，网络爬虫等新奇有趣技能
          </p>
        </div>
        <div class="img">
          <img src="../../assets/images/design-1.jpg" alt="">
        </div>
      </div>
      <!-- 板块2 -->
      <div class="box2 commonbox">
        <div class="img">
          <img src="../../assets/images/java-2.png" alt=""/>
        </div>
        <div class="content">
          <p class="title">Java Programing</p>
          <p class="title">授课内容</p>
          <P>第一周：java基本语法</P>
          <p>第二周：java高级特性</p>
          <p>第三周：java灵活应用</p>
          <p>第四周：java实战</p>
        </div>
      </div>
      <!-- 板块4 -->
      <div class="box4 commonbox">
        <div class="title">作品展示</div>
        <div class="list">
          <div>
            <img src="../../assets/images/design2-4.png" alt=""/>
            <div class="mask">
              <div class="title1">3D建模室内设计</div>
              <div class="desc1">3D建模室内设计（渲染图）制作软件：3Dmax</div>
            </div>
          </div>

          <div>
            <img src="../../assets/images/design2-5.png" alt=""/>
            <div class="mask">
              <div class="title1">萌遇</div>
              <div class="desc1">萌遇APP的UI设计（部分）</div>
            </div>
          </div>
          <div>
            <img src="../../assets/images/design2-6.png" alt=""/>
            <div class="mask">
              <div class="title1">CarryMeBack</div>
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
  name: "java",
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

  .box3 {
    justify-content: space-around;

    .content {
      width: 40%;
      min-width: 300px;
      margin-left: 20px;



      > p {
        line-height: 30px;
        font-size: 24px;
      }

      .title {
        font-size: 40px;
        min-width: 300px;
      }

    }
    .img {
      > img {
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
          }
        }
      }
    }
  }
}

@media screen and (max-width: 768px) {
  .box {


    .box3 {
      height: auto;

      img {
        width: 100%;
      }

      .content {
        > p {
          font-size: 20px;
        }

        width: 80%;
        margin-left: 0;
        margin-bottom: 40px;
      }
    }

    .box2 {
      .content {
        width: 80%;
        margin-bottom: 40px;
      }

      .img {
        width: 100%;
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
