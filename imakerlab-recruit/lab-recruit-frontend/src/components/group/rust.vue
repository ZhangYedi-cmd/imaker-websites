<template>
  <div>
    <div class="bg">
      <div class="part">
        <div class="message">
          <span class="title">rust</span>
          <p class="title2">println!("Hello, world!");</p>
          <p>rust未来已来</p>
          <p>强大并发 简单内存管理</p>
          <p>区块链和操作系统</p>
          <p>分布式算法首选！ </p>
        </div>
        <div class="img">
          <img src="../../assets/images/c-Mooc.png" alt="">
        </div>
      </div>
    </div>
    <div class="bg">
      <div class="part">
        <div class="img" style="display: flex;align-items: center;flex-direction: column">
          <h2 style="font-size: 24px">C语言自学书籍 </h2>
          <div style="margin-top: 30px">
            <img src="../../assets/images/c-books.png" alt="" style="width: 75%">
          </div>
        </div>
        <div class="img" style="display: flex;align-items: center;flex-direction: column">
          <h2 style="font-size: 24px">
            终极自学大招
          </h2>

          <img src="../../assets/images/c-baidu.png" alt="" style="width: 75%">
        </div>
      </div>
    </div>
    <div class="bg ">
      <div class="part">
        <div class="parttile">
          <span class="midtitle">作品展示</span>
          <ul class="part2 introwork">
            <li class="video ">
              <div class="video-card-reco">
                <div class="info-box">
                  <img src="../../assets/images/C2-1.png"
                       alt="眼“色”游戏 （6）">
                  <div class="info">
                    <p class="mintitle ">聊天室</p>
                    <p class="intro">使用C语言制作的聊天室</p>
                  </div>
                </div>
              </div>
            </li>

            <li class="video">
              <div class="video-card-reco">
                <div class="info-box">
                  <img src="../../assets/images/C2-2.png"
                       alt="眼“色”游戏 （6）">
                  <div class="info">
                    <p class="mintitle ">2048</p>
                    <p class="intro">>使用C语言制作的2048游戏</p>
                  </div>
                </div>
              </div>
            </li>

            <li class="video">
              <a href="https://www.bilibili.com/video/BV1154y1t7dt" target="_blank">
                <div class="video-card-reco">
                  <div class="info-box">
                    <img src="../../assets/images/C2-3.png"
                         alt="#">
                    <div class="info">
                      <p class="mintitle ">万花尺</p>
                      <p class="intro">输入不同参数，生成不同图案</p>
                    </div>
                  </div>
                </div>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <bottom></bottom>
  </div>

</template>

<script>
import bottom from "../base/bottom";

export default {
  name: "design",
  components: {bottom}
}
</script>

<style scoped>
p {
  word-wrap: break-word;
  line-height: 32px;
  font-size: 24px;
  margin: auto;
}

.workname {
  padding: 4px;
}

.part {
  width: 100%;
  justify-content: center; /*实现水平居中*/
  align-items: center;
  display: grid;
  padding: 3vw 0 3vw 0;
  margin: auto;
  grid-template-columns: repeat(2, 1fr);
}

.part2 {
  justify-content: center; /*实现水平居中*/
  align-items: center;
  display: grid;
  padding-top: 12px;
  grid-template-columns: repeat(3, 1fr);
}

.parttile {
  display: grid;
  grid-column: 1/4;
  justify-content: center; /*实现水平居中*/
  align-items: center;
}

.black {
  background: url("../../assets/images/designbg.png") no-repeat;
  background-size: 100%;
  height: 800px;
  background-position: 0 100%;
}

.bg {
  display: block;
  width: 100%;
}

.title {
  font-size: 44px;
  line-height: 50px;
  color: white;
}

.midtitle {
  font-size: 32px;
  margin: auto;
  color: #ffffff;
}

.mintitle {
  font-size: 24px;
  margin: auto;
}

.title2 {
  font-size: 16px;
  line-height: 20px;
  color: #c5c5c5;
}

.intro {
  font-size: 16px;
  line-height: 20px;
}

.right {
  display: grid;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;

}

.img {
  overflow: hidden;
  float: right;
  width: 100%
}

.img img {
  max-width: 100%;
  max-height: 100%;
  display: block;
  margin: auto;
  border-radius: 10px;
}

#videoID {
  max-width: 120%;
  min-height: 110%;
  display: block;
  margin: auto;
}

.message {
  padding-right: 20px;
}

/*//////*/
.introwork {
  /*display: block;*/
  float: left;
  height: 220px;
  width: 100%;
}

.video {
  list-style: none;
  height: 300px;
  width: 320px;
  float: contour;
}

.video-card-reco {
  background-color: #fff;
  border-radius: 5px;
  overflow: hidden;
  position: relative;
  width: 290px;
  height: 170px;
  margin: 0 30px 30px 30px;
  box-sizing: border-box;
  /*text-align:center;*/
  vertical-align: middle;
  display: table-cell;
}

.video-card-reco:before {
  content: "";
  position: absolute;
  z-index: 1;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 48px;
  background-size: contain;
  background-repeat: repeat-x;
  border-radius: 0 0 2px 2px;
}

.van-watchlater span {
  display: none;
}

.video-card-reco:hover :before {
  opacity: 1;
}

.video-card-reco .info-box, .video-card-reco .info-box:before, .video-card-reco .info-box img {
  width: 100%;
  height: 170px;
}

.video-card-reco:hover {
  opacity: 1;
}

.watch-later-video:hover span {
  display: block;
}

.van-watchlater.black a {
  display: block;
  width: 20px;
  height: 20px;
}

.video-card-reco .info-box::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  background: rgba(0, 0, 0, .7);
  opacity: 0;
  transition: opacity .2s;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif;
  font-size: 12px;
  line-height: 1.5;
  color: #ffffff;
  background-color: #fff;
}

.video-card-reco:before {
  background-image: url(../../assets/images/bgblack.png);
  background-size: contain;
  background-repeat: repeat-x;
}

.video-card-reco:hover .info-box::before {
  opacity: 1;
}

a {
  color: #ffffff;
  transition: color .3s;
  outline: none;
  cursor: pointer;
}

a, a:hover {
  text-decoration: none;
}

img {
  vertical-align: middle;
  border-style: none;
}

.video-card-reco .info-box .info {
  position: absolute;
  z-index: 2;
  width: 95%;
  top: 121px;
  left: 0;
  transition: top .2s;
  padding: 16px 10px 10px;
}

.video-card-reco .info-box .info .title {
  font-size: 14px;
  line-height: 18px;
  height: 18px;
  color: #fff;
  margin-bottom: 6px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 500;
}

.video-card-reco .info-box .info, .video-card-reco .info-box .info {
  font-size: 12px;
  color: #ffffff;
  margin-bottom: 3px;
  line-height: 15px;
}

.video-card-reco:hover .info {
  top: -4%;
  opacity: 1;
  position: absolute;
}

.info {
  width: 50px;
  padding: 10px;
  /*opacity: 0;*/
  transition: opacity .2s;
}
.parttop{
  padding: 10vw 0 3vw 0;
}
.bgbottom {
  background-image: linear-gradient(#000000, #27214b);
}
</style>
