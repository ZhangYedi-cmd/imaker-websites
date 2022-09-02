<template>
  <!--C-->
  <transition appear name="animate__animated animate__bounce" enter-active-class="animate__fadeIn">
    <div class="box">
      <!-- 板块1 -->
      <div class="bg1"></div>
      <!-- 板块2 -->
      <div class="boxbg">

        <div class="box2 commonbox">
          <div class="content">
            <p class="title">C/C++</p>
            <P>cout &lt;&lt;"Hello world!" &lt;&lt;endl;</P>
            <p>C++是世界上最好的语言</p>
            <p>来学...来...</p>
            <p>学就完了，C++做什么都可以，C++yyds</p>
          </div>
          <div class="img">
            <img src="../../assets/images/CC3.png" alt="">
          </div>
        </div>

        <!-- 板块3 -->
        <div class="box3 commonbox">
          <div class="li">
            <div class="title">C语言自学书籍</div>
            <div class="imgs">
              <img src="../../assets/images/c-books.png" alt="">
            </div>
          </div>
          <div class="li">
            <div class="title">终极自学大招</div>
            <div class="imgs">
              <img src="../../assets/images/c-baidu.png" alt="">
            </div>
          </div>
        </div>

        <!-- 板块4 -->
        <div class="box4 commonbox">
          <div class="title">作品展示</div>
          <div class="list">

            <div>
              <img src="../../assets/images/C2-1.png" alt="">
              <div class="mask">
                <div class="title1">聊天室</div>
                <div class="desc1">
                  使用C语言制作的联网聊天室
                  <a href="https://blog.csdn.net/qq_51599283?spm=1001.2014.3001.5509">个人博客</a>
                </div>
              </div>
            </div>

            <div>
              <img src="../../assets/images/C2-2.png" alt="">
              <div class="mask">
                <div class="title1">2048</div>
                <div class="desc1">使用C语言制作的20448游戏</div>
              </div>
            </div>
            <div>
              <img src="../../assets/images/C2-3.png" alt="">
              <div class="mask">
                <div class="title1">万花尺</div>
                <div class="desc1">输入不同参数，生成不同图案</div>
              </div>
            </div>
          </div>
        </div>
        <bottom></bottom>
      </div>
    </div>
  </transition>

</template>

<script>
import bottom from "../base/bottom";

export default {
  name: "c",
  components: {bottom},
};
</script>

<style scoped lang="less">
.box {
  width: 100%;
  color: white;

  .bg1 {
    width: 100%;
    height: 120vh;
    background: url(../../assets/images/c.jpg) no-repeat center/cover;
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

  .boxbg {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: url(../../assets/images/c2.jpg) no-repeat center/cover;

    .box2 {
      .content {
        width: 40%;
        min-width: 300px;

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
        //height: 160px;

        > img {
          width: 100%;
          height: 100%;
        }
      }
    }

    .box3 {
      .li {
        margin-top: 40px;
        width: 40%;
        display: flex;
        flex-direction: column;
        align-items: center;

        .title {
          font-size: 30px;
          font-weight: bold;
          margin-bottom: 30px;
        }

        .imgs {
          width: 100%;
          //height: 250px;
          border-radius: 15px;
          overflow: hidden;

          > img {
            width: 100%;
            height: 100%;
          }
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
            //height: 180px;
          }
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
