<template>
  <!--web前端-->
  <transition appear name="animate__animated animate__bounce" enter-active-class="animate__fadeIn">
  <div class="box">
 <!-- 板块1 -->
    <div class="bg1"><img src="../../assets/images/前端.jpg" alt="" /></div>
     <!-- 板块2 -->
    <div class="box2 commonbox">
      <div class="content">
        <p class="title">前端</p>
        <p>&lt;body&gt;Hello world!&lt;/body&gt;</p>
        <p>实现你对网页设计的奇思妙想</p>
        <p>满足你制作小程序的愿望</p>
        <p>在这里不仅仅是网页这么简单</p>
        <p>我们是设计师更是艺术家</p>
      </div>
      <div class="img">
        <img src="../../assets/images/web-1.png" alt="" />
      </div>
    </div>


 <!-- 板块2 -->
    <div class="box2 commonbox">
       <div class="img">
        <img src="../../assets/images/web-2.jpg" alt="" />
      </div>
      <div class="content">
       <p><img
            src="../../assets/images/right.png"
            alt=""
            style="width: 40px; vertical-align: middle"
          />就业方向广，需求广泛，多领域多岗位都可就业</p>
          <p><img
            src="../../assets/images/right.png"
            alt=""
            style="width: 40px; vertical-align: middle"
          />职业前景好，人才长期稀缺，未来发展持续看好</p>
          <p><img
            src="../../assets/images/right.png"
            alt=""
            style="width: 40px; vertical-align: middle"
          />学习门槛低，前端从业者背景多样，没有限制</p>
      </div>

    </div>


     <!-- 板块4 -->
    <div class="box4 commonbox">
      <div class="title">作品展示</div>
      <div class="list">
        <div>
          <img src="../../assets/images/flushbonading2-1.png" alt="" />
          <div class="mask">
            <div class="title1">超声波避障小车</div>
            <div class="desc1">基于Arduino开发的超声波避障小车</div>
          </div>
        </div>

        <div>
          <img src="../../assets/images/flushbonading2-2.png" alt="" />
          <div class="mask">
            <div class="title1">垃圾自动分拣系统</div>
            <div class="desc1">这是描述这是描述</div>
          </div>
        </div>
        <div>
          <img src="../../assets/images/design2-6.png" alt="" />
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
  name: "webfront",
  components: {bottom}
}

</script>

<style scoped lang="less">
.box {  width: 100%;
  color: white;
  display: flex;
  flex-direction: column; //主轴方向竖直
  align-items: center; //子元素居中对齐
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
    box-sizing: border-box; //转化为盒子模型
    display: flex;
    justify-content: space-around; //弹性容器对齐方式
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 40px;
  }

  .box2 {
    .content {
      width: 30%;
      min-width: 300px;
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
          top:80%;
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
    .box2 {
      .content {
        width:100%;
        margin-bottom: 40px;
      }
      .img {
        width:100%;
      }
    }
    .box4 {
      .list {
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        > div {
          width: 100%;
          margin-bottom: 30px;
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
