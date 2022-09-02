<template>
  <div class="main-wrapper">
    <!-- 板块1 -->
    <div class="box box1">
      <div class="title">在这里，你将体验到：</div>
      <ul class="list">
        <li v-for="(item, index) in list1" :key="index">
          <div class="imgs">
            <img :src="item.src" alt=""/>
          </div>
          <div class="msg">
            <div class="tit">{{ item.title }}</div>
            <div class="desc">{{ item.desc }}</div>
          </div>
        </li>
      </ul>
    </div>
    <!-- 板块2 -->
    <div class="box box2">
      <div class="title">我们的日常</div>
      <div class="desc">自由灵活的自学与交流模式，自由灵活的自学与交流模式</div>
      <ul class="list">
        <li v-for="(item, index) in list2" :key="index">
          <div class="imgs">
            <img :src="item.src" alt=""/>
          </div>
          <div class="title">{{ item.title }}</div>
          <div class="desc">
            {{ item.desc }}
          </div>
        </li>
      </ul>
    </div>
    <!-- 板块3 -->
    <div class="box box3">
      <div class="top">
        <div class="location">
          <img src="../../assets/images/location.png" alt=""/>
        </div>

        <!-- 位置 -->
        <div class="title">
          <!-- 开关 -->
          <div class="switch">
            <el-switch
              v-model="value"
              active-color="#13ce66"
              inactive-color="#ff4949"
            >
            </el-switch>
          </div>
          <p v-if="value">泰达</p>
          <p v-else>河西</p>
          <p style="position: relative; left: -147px">imaker实验室</p>
        </div>
        <div class="desc">
          <div style="font-size: 42px">大活玻璃屋120</div>
          <div style="position: relative">
            纳新群已开放，欢迎进群来玩！
            <div class="btn">进群</div>
          </div>
        </div>
      </div>
      <div class="mid">
        <div class="imgs imgs1">
          <img src="../../assets/images/location1.png" alt=""/>
        </div>
        <ul class="btns">
          <li
            v-for="(item, index) in list3"
            :key="index"
            @click="changeitem(index)"
            :class="item.ref ? 'active' : ''"
          >
            {{ item.content }}
          </li>
        </ul>
        <div class="imgs imgs2">
          <img src="../../assets/images/location1.png" alt=""/>
        </div>
      </div>
      <p>自由灵活的自学与交流模式，自由灵活的自学与交学与交学与交流模式</p>
      <p>自由灵活的自学与交流模式，自由灵活的自学与交流模式</p>
      <p>自由灵活的自学与交流模式</p>
    </div>
    <!-- 板块4 -->
    <div class="box box4">
      <dan></dan>
    </div>
    <!-- 板块5 -->
    <div class="box box5">
      <div class="title">- 更多小游戏 -</div>
      <div style="display: flex" class="content">
        <div class="list">
          <li>
            <div class="imgs">
              <img src="../../assets/images/timg.jpg" alt=""/>
            </div>
            <p>
              <a href="http://home.ustc.edu.cn/~zzzz/lifegame/lifegame.html" target="_blank">生命游戏</a>
            </p>
          </li>
          <li>
            <div class="imgs">
              <img src="../../assets/images/timg.jpg" alt=""/>
            </div>
            <p>
              <a href="http://home.ustc.edu.cn/~zzzz/lifegame/lifegame.html" target="_blank">生命游戏</a>
            </p>
          </li>
        </div>
        <div class="advise">
          <div class="desc">
            <p style="min-width: 250px;line-height: 40px;width: 50%;">
              如果有什么疑问/有趣的建议请到提问箱留言吧~
            </p>
            <div class="imgs">
              <img src="../../assets/images/message.png" alt=""/>
            </div>
          </div>
          <div class="btn" @click="goOthers('/joinUs')">Join&nbsp;Us &gt;</div>
        </div>
      </div>
    </div>
    <bottom></bottom>
  </div>
</template>

<script>
import bottom from "../base/bottom";
import dan from "./Dan.vue";
import img1 from "../../assets/images/team.png";
import img2 from "../../assets/images/tool.png";
import img3 from "../../assets/images/match.png";
import img4 from "../../assets/images/effect.png";
import img5 from "../../assets/images/summary.png";
import img6 from "../../assets/images/share.png";
import img7 from "../../assets/images/brain.png";

export default {
  name: "introduce",
  components: {
    bottom,
    dan,
  },
  data() {
    return {
      list1: [
        {
          src: img1,
          title: "团队合作",
          desc: "在这里你可以迅速找到与自己 志同道合的新朋友",
        },
        {
          src: img2,
          title: "提供丰富而全面的实验器材",
          desc: "我们拥有丰富而全面的实验器材， 可以充分发挥你的动手能力",
        },
        {
          src: img3,
          title: "参与比赛",
          desc: "最快最新的比赛咨询，对于参 加比赛经验丰富",
        },
        {
          src: img4,
          title: "出色的效率",
          desc: "高效的团队执行力，使每周都能 学到新东西，进度不停歇",
        },
      ],
      list2: [
        {
          src: img5,
          title: "月度项目总结",
          desc: "为用户量身定制可执行、可落地 的解决方案，提供场景案例分享 与答疑",
        },
        {
          src: img6,
          title: "分享会",
          desc: "为用户量身定制可执行、可落地 的解决方案，提供场景案例分享 与答疑",
        },
        {
          src: img7,
          title: "头脑风暴",
          desc: "为用户量身定制可执行、可落地 的解决方案，提供场景案例分享 与答疑",
        },
      ],
      list3: [
        {ref: true, content: "c/c++"},
        {ref: false, content: "java"},
        {ref: false, content: "Python"},
        {ref: false, content: "Rust"},
        {ref: false, content: "嵌入式"},
        {ref: false, content: "前端"},
      ],
      value: true,
    };
  },
  methods: {
    changeitem(index) {
      for (let i = 0; i < this.list3.length; i++) {
        if (i == index) {
          this.list3[i].ref = true;
        } else {
          this.list3[i].ref = false;
        }
      }
    },
    goOthers(url) {
      this.$router.push(url);
    },
  },
};
</script>

<style lang="less" scoped>

@media screen and (max-width: 768px ) {
  .box {
    width: 90% !important;

    .title {
      font-size: 28px !important;
    }
  }

  .box1 {
    .list {
      margin-top: 80px !important;

      > li {
        padding-left: 0 !important;

        .tit {
          font-size: 20px !important;
        }
      }
    }
  }

  .box2 {
    .list {
      > li {
        width: 90% !important;
        margin-bottom: 40px;
      }
    }
  }

  .box3 {
    .top {
      .desc {
        display: none !important;
      }

      .location {
        margin: 0 !important;
        height: 150px !important;
        width: 170px !important;
      }

      .title {
        .switch {
          margin-top: 0 !important;
        }

        p {
          font-size: 26px !important;
        }

        p:last-child {
          left: 0 !important;
        }
      }
    }

    .mid {
      .imgs1 {
        display: none;
      }

      .imgs2 {
        width: 70% !important;
      }
    }

    > p {
      margin-bottom: 30px !important;
    }
  }

  .box5 {
    .content {

      flex-direction: column;

      .list {
        width: 90%;
      }

      .advise {
        .btn {
          width: 130px;
        }
      }
    }
  }
}

/*屏幕宽度 大于700px 且 小于900px 时*/
@media screen and (min-width: 768px) and (max-width: 992px ) {

}

/*屏幕宽度 大于900px 且 小于1200px 时*/
@media screen and (min-width: 992px) and (max-width: 1200px ) {

}

/*屏幕宽度 大于1200px 时*/
@media screen and (min-width: 1200px ) {

}

@import "../../styles/introduce.css";

* {
  margin: 0;
  padding: 0;
}

.main-wrapper {
  background: url(../../assets/images/mainbg.png) no-repeat center/cover;
  color: white;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.box {
  width: 80%;
  min-height: 300px;
  margin-bottom: 20px;
}

/* box1 */
.box1 {
  .title {
    font-size: 36px;
    font-family: DengXian;
    font-weight: bold;
    color: #ffffff;
  }

  .list {
    display: flex;
    width: 100%;
    flex-wrap: wrap;
    margin-top: 100px;

    > li {
      width: 50%;
      display: flex;
      justify-content: flex-start;
      padding-left: 40px;
      box-sizing: border-box;
      margin-bottom: 40px;
      min-width: 400px;

      .imgs {
        margin-right: 10px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: white;
        display: flex;
        justify-content: center;
        align-items: center;

        > img {
          width: 80%;
          height: 80%;
        }
      }

      .msg {
        .tit {
          font-size: 24px;
          font-family: DengXian;
          font-weight: bold;
          color: #ffffff;
          line-height: 18px;
          margin-bottom: 20px;
        }

        .desc {
          font-size: 16px;
          font-family: DengXian;
          font-weight: bold;
          color: #ffffff;
          max-width: 60%;
          white-space: pre-wrap;
          line-height: 26px;
        }
      }
    }
  }
}

/* box2 */
.box2 {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;

  .title {
    font-size: 36px;
    font-family: DengXian;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 30px;
  }

  .desc {
    font-size: 24px;
    font-family: DengXian;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 30px;
  }

  .list {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    width: 100%;

    > li {
      width: 25%;
      min-height: 300px;
      background: #274656;
      border-radius: 10px;
      box-sizing: border-box;
      padding: 20px;
      display: flex;
      flex-direction: column;

      .imgs {
        width: 85px;
        height: 85px;
        background: #ffffff;
        opacity: 0.22;
        border-radius: 10px;
        padding: 20px;
        box-sizing: border-box;
        margin-bottom: 20px;

        > img {
          width: 100%;
          height: 100%;
        }
      }

      .title {
        font-size: 24px;
        font-family: DengXian;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 20px;
      }

      .desc {
        font-size: 16px;
        font-family: DengXian;
        font-weight: bold;
        color: #ffffff;
        line-height: 26px;
      }
    }
  }
}

/* box3 */
.box3 {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;

  > p {
    margin-bottom: 40px;
  }

  .mid {
    width: 100%;
    margin-top: 20px;
    margin-bottom: 40px;
    display: flex;
    justify-content: space-around;

    .imgs {
      width: 40%;
      height: 240px;
      border-radius: 10px;
      overflow: hidden;

      > img {
        width: 100%;
        height: 100%;
      }
    }

    .btns {
      display: flex;
      flex-direction: column;
      justify-content: flex-start;

      > li {
        display: block;
        width: 60px;
        border-radius: 10px;
        height: 30px;
        line-height: 30px;
        margin-bottom: 10px;
        background: white;
        color: black;
        text-align: center;
        cursor: pointer;
      }

      > li:hover {
        background: #ec6941;
        color: white;
      }

      .active {
        background: #ec6941;
        color: white;
      }
    }
  }

  .top {
    width: 100%;
    display: flex;
    justify-content: flex-start;

    .location {
      margin: 30px 30px;

      > img {
        width: 100%;
        height: 100%;
      }
    }

    .title {
      display: flex;
      flex-direction: column;
      justify-content: flex-start;

      .switch {
        margin-top: 100px;
        margin-bottom: 20px;
      }

      p {
        font-size: 36px;
        font-family: DengXian;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 10px;
      }
    }

    .desc {
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      margin-left: -64px;

      > div {
        margin-bottom: 20px;
      }

      .btn {
        display: inline-block;
        width: 60px;
        height: 30px;
        text-align: center;
        line-height: 30px;
        background: #ec6941;
        color: white;
        border-radius: 10px;
      }
    }
  }
}

/* box4 */

/* box5 */
.box5 {
  .title {
    font-size: 24px;
    font-family: DengXian;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 50px;
  }

  .list {
    width: 40%;
    display: flex;
    flex-direction: column;

    > li {
      margin-bottom: 40px;
      margin-left: 60px;
      margin-right: 20px;
      display: flex;
      justify-content: flex-start;
      align-items: center;

      > p {
        > a {
          text-decoration: none;
          color: white;
        }
      }

      .imgs {
        width: 80px;
        height: 80px;
        overflow: hidden;
        border-radius: 10px;
        margin-right: 20px;
        background: #768489;
        padding: 10px;
        box-sizing: border-box;

        > img {
          width: 100%;
          height: 100%;
          border-radius: 5px;
        }
      }
    }
  }

  .advise {
    display: flex;
    flex-direction: column;

    .desc {
      display: flex;
      font-size: 18px;
      font-family: DengXian;
      line-height: 20px;
      font-weight: bold;
      color: #ffffff;
      margin-bottom: 30px;

      .imgs {
        width: 60px;
        height: 60px;
        margin-left: 20px;

        > img {
          width: 100%;
          height: 100%;
        }
      }
    }

    .btn {
      background: #4c8bf5;
      width: 200px;
      height: 60px;
      text-align: center;
      line-height: 60px;
      font-size: 26px;
    }
  }
}
</style>
