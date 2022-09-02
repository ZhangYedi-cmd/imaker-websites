<template>
  <div class="container">
    <div class="box">
      <div class="list">
        <div class="title">概括简介</div>
        <li>河西组别</li>
        <li>泰达组别</li>
        <li>历史回廊</li>
      </div>
      <div class="list list1">
        <div class="title">技术交流</div>
        <ul style="color: white;padding: 0px;margin: 0;">
          <li>java</li>
          <li>前后端</li>
          <li>Python</li>
          <li>机器视觉</li>
          <li>c/c++</li>
          <li>Rust</li>
          <li>设计</li>
          <li>3D建模</li>
          <li>嵌入式</li>
          <li>视频后期</li>
        </ul>
      </div>
      <div class="list">
        <div class="title">资源整合</div>
        <li>自学平台</li>
        <li>开发软件</li>
        <li>常用工具</li>
        <li>优秀开源</li>
      </div>
      <div class="list3">
        <li>
          <span>联系我们</span>
          <img src="../../assets/images/email.png" alt="" />
          邮箱：service@imakerlab.cn
        </li>
        <li>
          <span>加入我们</span
          ><img src="../../assets/images/tel.png" alt="" />电话：xxxxxxx
        </li>
        <li>
          <span>提问箱</span>
          <img
            src="../../assets/images/wechat.png"
            alt=""
          />公众号：天科大创新实验室
        </li>
      </div>
    </div>
    <div class="copy">
      <span>Copyright ©2021 ONES.AI 深圳复临科技有限公司 </span>
      <span>粤ICP备15032127号</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "bottom",
};
</script>

<style scoped lang="less">
.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: url(../../assets/images/mainbg2.png) no-repeat center/cover;
  padding: 40px;
  box-sizing: border-box;
}

.box {
  width: 75%;
  min-height: 300px;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;

  li {
    list-style: none;
  }

  .list {
    min-width: 130px;
    text-align: center;
    max-width: 150px;

    .title {
      font-size: 16px;
      font-family: DengXian;
      font-weight: bold;
      color: #d7d8d9;
      line-height: 50px;
      border-bottom: 1px solid #d2d7d8;
    }

    > li {
      font-size: 12px;
      font-family: DengXian;
      font-weight: 400;
      color: #9b9ea0;
      margin-top: 10px;
    }
  }

  .list1 {
    > ul {
      display: flex;
      flex-wrap: wrap;
      width: 100%;

      > li {
        color: #9b9ea0;
        font-size: 12px;
        width: 50%;
        margin-top: 10px;
      }
    }
  }

  .list3 {
    margin-top: 50px;

    li {
      font-size: 12px;
      font-family: DengXian;
      font-weight: 400;
      color: #9b9ea0;
      margin-top: 10px;

      img {
        width: 20px;
        height: 20px;
        vertical-align: middle;
        margin-right: 10px;
      }
    }
  }
}

.copy {
  margin-top: 40px;
  display: flex;
  flex-wrap: wrap;

  > span {
    font-size: 12px;
    font-family: DengXian;
    font-weight: bold;
    color: #646060;
  }
}

 @media screen and (max-width: 768px ){
        .container{
          .box{
            width: 90%;
          }
          .list{
            width: 100%;
          }
        }
    }

    /*屏幕宽度 大于700px 且 小于900px 时*/
    @media screen and (min-width: 768px) and (max-width: 992px ){
        
    }

    /*屏幕宽度 大于900px 且 小于1200px 时*/
    @media screen and (min-width: 992px) and (max-width: 1200px ){
        
    }

    /*屏幕宽度 大于1200px 时*/
    @media screen and (min-width: 1200px ){
        
    }
</style>
