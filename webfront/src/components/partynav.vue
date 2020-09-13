<template>
    <div id="sp-header">
      <div class="header-wrapper">
        <div class="header-left">
          <img src="/static/picture/nav_title.png" class="logo-left">
          <div class="header-search">
            <img class="i-search" src="/static/picture/search.png">
            <input class="input-search" placeholder="输入您想要搜索的内容"></input>
            <div class="btn-search">搜索</div>
          </div>
          <div class="header-list">
            <div class="fl-list">
              <div class="fl-item-block">外交足迹</div>
              <div class="fl-item-block">前辈寄语</div>
              <div class="fl-item-block">组织生活窗</div>
              <div class="fl-item-block">模范党支部</div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
      name: "partynav",
    }
</script>

<style scoped>
  #sp-header{
    position: fixed;
    width: 100%;
    height: 65px;
    top: 0;
    box-sizing: border-box;
    left: 0;
    z-index: 3;
    background: #b01a16;
    border-bottom: 1px solid #dddddd;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,0.10);
    animation: header 1s forwards;
  }
  @keyframes header {
    0%{opacity: 0; top: -55px}
    100%{opacity: 1; top: 0}
  }
  @-webkit-keyframes header {
    0%{opacity: 0; top: -55px}
    100%{opacity: 1; top: 0}
  }
  .header-wrapper{
    width: 1328px;
    height: 100%;
    margin: 0 auto;
  }
  .header-left{
    height: 100%;
    box-sizing: border-box;
  }
  .logo-left{
    height: 50px;
    position: absolute;
    left: 20px;
    top: 4px;
  }
  .header-search{
    width: 401px;
    height: 46px;
    margin-top: 12px;
    margin-left: 250px;
    line-height: 46px;
    float: left;
    position: relative;
  }
  .i-search{
    width: 17px;
    position: absolute;
    left: 22px;
    top: 15px;
    z-index: 11;
  }
  .input-search{
    width: 235px;
    height: 44px;
    position: absolute;
    left: 0;
    top: 0;
    z-index: 10;
    font-size: 16px;
    outline: 0;
    padding: 0 10px 0 54px;
    border-top-left-radius: 46px;
    border-bottom-left-radius: 46px;
    border: 1px solid #ce0000;
    background-color: #f8f8f8;
    border-right-color: #ce0000;
    box-sizing: content-box;
  }
  .btn-search{
    width: 82px;
    height: 100%;
    position: absolute;
    right: 20px;
    top: 0;
    background: #ffcc33;
    line-height: 46px;
    font-size: 16px;
    text-align: center;
    color: #ce0000;
    border-radius: 0 27px 27px 0;
    z-index: 11;
    letter-spacing: 4px;
    cursor: pointer;
  }
  .header-list{
    height: 56px;
    box-sizing: border-box;
    padding-top: 11px;
  }
  .fl-list{
    float: left;
    margin-top: 5px;
    margin-left: 165px;
  }
  .fl-item-block{
    font-size: 18px;
    height: 34px;
    line-height: 34px;
    color: white;
    margin-right: 30px;
    display: inline-block;
    cursor: pointer;
  }
  .fl-item-block:hover{
    animation: font-big 0.5s forwards;
  }
  @keyframes font-big {
    0%{font-size: 18px;margin-right: 30px}
    100%{font-size: 20px;margin-right: 28px}
  }
  @-webkit-keyframes font-big {
    0%{font-size: 18px}
    100%{font-size: 20px}
  }
</style>
