<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
<style scoped >
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}

/*屏幕宽度 小于700px 时*/
    @media screen and (max-width: 768px ){
        
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
