44<template>
  <div id="location_taida">
    <!--泰达位置-->
    <router-link to=""/>
    <div class="top_title">
      <div class="top_title_sub">
        <div id="location">位置|LOCATION</div>
        <div class="buttons">
          <router-link to="/location/hexi">
            <button>
              河西
            </button>
          </router-link>
          <router-link to="/location/taida">
            <button>
              泰达
            </button>
          </router-link>
        </div>
      </div>
    </div>

    <div class="main">
      <!-- 框1 -->
      <div class="map">
        <div class="map_box">
          <div class="map_title">
            <div class="map_title1">泰达实验室</div>
            <div class="map_title2">（西苑地图）</div>
          </div>
          <div class="map_text">*只需沿着西苑西门入口直走，在大自然食堂对面，便可见到大学生活动中心。</div>
          <a class="tips" href="#small"/>
          *点击查看小地图<br/>
          <img src="" alt="箭头图标">

        </div>
        <!--        <img src="../../assets/images/img-location/xiyuan-map.png" alt="西苑地图" width="500" >-->
      </div>

      <!-- 框2 -->
      <a name="small"/>
      <div class="map">
        <!--        <img src="../../assets/images/img-location/dahuo-map.png" alt="大活地图" width="500" >-->
        <div class="map_box">
          <div class="map_title">
            <div class="map_title1">大学生活动中心</div>
            <div class="map_title2">（小地图）</div>

            <div class="map_text">*手把手带您走向实验室</div>

            <a class="tips" href="#big"/>
            *点击查看大地图<br/>
            <img src="" alt="箭头图标">
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  export default {
    name: "taida"
  }
</script>

<style scoped>
  /*@import "../../styles/taida.css";*/

</style>
