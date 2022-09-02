<template>
  <div class="home">
    <div class="title">弹幕互动区</div>
    <div class="desc">发条弹幕试试？欢迎留下你的足迹</div>
    <div
      style="
        height: 400px;
        width: 100%;
        position: relative;
        margin: 0px auto;
        background: #244147;
      "
    >
      <!-- <video controls
             src="@/assets/1.mp4"
             autoplay
             style="width:100%;height:100%;z-index:2;" /> -->
      <!-- 确保父元素是相对定位，弹幕容器是绝对定位 -->
      <v-barrage :arr="arr" :isPause="isPause" :percent="100"></v-barrage>
    </div>
    <div class="barrage-control">
      <input
        type="text"
        v-model="sendContent"
        placeholder="回车发送"
        id="sendContent"
        @keyup.enter="sendBarrage"
      />
      <button
        id="sendBarrageBtn"
        style="margin-left: 25px"
        @click="sendBarrage"
      >
        发送
      </button>

      <select style="margin: 0px 12px" v-model="direction" v-if="false">
        <option value="default">默认</option>
        <option value="top">顶部</option>
      </select>
      <input type="checkbox" v-if="false" v-model="isJs"/>

      <button id="pauseBtn" v-if="false">@click="isPause=true">暂停</button>
      <button id="startBtn" v-if="false">@click="isPause=false">开始</button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import VBarrage from "../VBarrage/index.vue";

export default {
  components: {
    VBarrage,
  },
  data() {
    return {
      arr: [],
      isPause: false,
      sendContent: null,
      isJs: false,
      direction: "default",
    };
  },
  mounted() {
    this.initTestData();
  },
  methods: {
    // 初始化模拟弹幕数据
    initTestData() {
      let arr = [
        "PHP是世界上最好的语言",
        "Java是最好的语言！",
        "yyds",
        "卷王就是我！",
        "人生苦短，，我学Python"
      ];
      for (let i = 0; i < 6; i++) {
        for (let index = 0; index < 1000; index++) {
          this.arr.push({
            direction: "default",
            content: arr[parseInt(Math.random() * arr.length)],
          });
        }
      }
    },
    // 发送弹幕
    sendBarrage() {
      if (
        this.arr.length > 1 &&
        this.sendContent != "" &&
        this.sendContent != null
      ) {
        this.arr.unshift({
          content: this.sendContent,
          direction: this.direction,
          isSelf: true,
          style: {
            color: "red",
            fontSize: "25px",
          },
          isJs: this.isJs,
        });
      } else {
        this.arr.push({
          content: this.sendContent,
          direction: this.direction,
          isSelf: true,
          style: {
            color: "red",
          },
          isJs: this.isJs,
        });
      }
      this.sendContent = null;
    },
  },
};
</script>
<style lang="less" scoped>
.barrage-control {
  text-align: center;
  margin: 10px 0px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.title {
  font-size: 36px;
  font-family: DengXian;
  font-weight: bold;
  color: #ffffff;
  margin-bottom: 40px;
}

.desc {
  font-size: 18px;
  font-family: DengXian;
  font-weight: bold;
  color: #ffffff;
  margin-bottom: 40px;
}

#sendContent {
  width: 85%;
  height: 43px;
  background: rgba(#eeeeee, .49);
  border-radius: 10px;
  color: white;
  outline: none;
  padding-left: 20px;
  box-sizing: border-box;
  box-sizing: border-box;
}

#sendBarrageBtn {
  width: 10%;
  height: 43px;
  background: #eeeeee;
  border-radius: 10px;
  min-width: 42px;

  font-family: DengXian;
  font-weight: bold;
  color: #000000;

}
</style>
