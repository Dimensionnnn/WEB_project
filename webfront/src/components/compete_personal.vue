<template>
    <div class="personal_bg">
      <el-row class="card-list">
        <div v-for="(item,index) in card_list" :key="key" :id="item.id">
          <el-col :span="8">
            <div class="card">
              <div class="card-logo-box">
                <div class="card-pictrue">
                  <img :src="item.src" class="card-logo">
                </div>
              </div>
              <div class="card-title">
                <div class="card-header">{{item.name}}</div>
                <div class="card-number">{{item.num}}</div>
              </div>
            </div>
          </el-col>
        </div>
      </el-row>
      <el-row class="graph-list">
        <el-col :span="12">
          <div class="graph">
            <div id="charts1" class="charts1"></div>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="graph">
            <div id="charts2" class="charts2"></div>
          </div>
        </el-col>
      </el-row>
      <div class="radar-list">
        <div class="radar-box">
          <div class="capacity" id="radar1"></div>
        </div>
        <div class="statistic-box">
          <div class="personal-card1"></div>
          <div class="personal-card2"></div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "compete_personal",
        data(){
          return {
            card_list:[
              {id:'1',name:'历史胜率',src:'/static/picture/achieve.png',num:76},
              {id:'2',name:'平均成绩',src:'/static/picture/statistic.png',num:89},
              {id:'3',name:'测试次数',src:'/static/picture/test-tube.png',num:23}
            ],
            history_record:[90,95,85,80,93,90,95],
            history_test:[2,3,1,5,3,2,1]
          }
        },
        methods:{
            Init_charts:function () {
                var that = this;
                var option = {
                    title: {
                        text: '近七天平均成绩'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['平均成绩']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '平均成绩',
                            type: 'line',
                            stack: '总量',
                            data: that.history_record,
                            itemStyle:{
                              normal:{
                                color:'#409EFF',
                                lineStyle:{
                                  color: '#409EFF'
                                }
                              }
                            }
                        }
                    ]
                };
                var Mychart1 = this.$echarts.init(document.getElementById('charts1'));
                Mychart1.setOption(option);

                var option1 = {
                    title: {
                        text: '近七天测试次数'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['测试次数']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '平均成绩',
                            type: 'line',
                            stack: '总量',
                            data: that.history_test,
                            itemStyle:{
                              normal:{
                                color:'#67C23A',
                                lineStyle:{
                                  color: '#67C23A'
                                }
                              }
                            }
                        }
                    ]
                };
                var Mychart2 = this.$echarts.init(document.getElementById('charts2'));
                Mychart2.setOption(option1);

                var option2 = {
                    title: {
                        text: '个人学习能力分析'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        left: 'center',
                        data: ['个人能力', '答题分析']
                    },
                    radar: [
                        {
                            indicator: [
                                {text: '党史知识', max: 100},
                                {text: '基本理论', max: 100},
                                {text: '政治素养', max: 100},
                                {text: '创新思维', max: 100}
                            ],
                            center: ['28%', '60%'],
                            radius: 80
                        },
                        {
                            indicator: [
                                {text: '客观题', max: 100},
                                {text: '主观题', max: 100},
                                {text: '简答题', max: 100},
                                {text: '论述题', max: 100},
                                {text: '分析题', max: 100}
                            ],
                            radius: 80,
                            center: ['78%', '60%'],
                        },
                    ],
                    series: [
                        {
                            type: 'radar',
                            tooltip: {
                                trigger: 'item'
                            },
                            areaStyle: {

                            },
                            data: [
                              {
                                  value: [90, 73, 85, 60],
                                  name: '个人能力'
                              }
                            ],

                        },
                        {
                            type: 'radar',
                            radarIndex: 1,
                            tooltip: {
                                trigger: 'item'
                            },
                            areaStyle: {},
                            data: [
                                {
                                    value: [95, 80, 95, 90, 93],
                                    name: '答题分析'
                                }
                            ]
                        },

                    ]
                };

                var Mychart3 = this.$echarts.init(document.getElementById('radar1'));
                Mychart3.setOption(option2);
            }
        },
        mounted() {
           $(".personal_bg").css('min-height',(window.innerHeight-62+100).toString()+'px')
            this.Init_charts();
        }
    }
</script>

<style scoped>
  .card-list{
    width: 100%;
    height: 180px;
  }
  .personal_bg{
    background: #f7f7f7;
  }
  .card{
    width: 80%;
    height: 100px;
    margin-top: 40px;
    margin-left: 10%;
    background: #fff;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
    cursor: pointer;
    transition: all .3s;
  }
  .card:hover{
    box-shadow: 0 0 10px 10px rgba(153,153,153,0.2);
  }
  .card-pictrue{
    width: 50px;
    height: 50px;
    margin-top: 15px;
    margin-left: 15px;
  }
  .card-logo{
    width: 100%;
    height: 100%;
  }
  .card-title{
    float: left;
    margin-left: 90px;
    height: 100%;
    margin-top: 20px;
  }
  .card-header{
    color: #aaa;
    font-size: 18px;
    font-weight: bold;
  }
  .card-number{
    font-size: 20px;
    font-weight: bold;
    color: #888;
    margin-top: 8px;
  }
  .card-logo-box{
    width: 80px;
    height: 80px;
    float: left;
    margin-left: 15px;
    margin-top: 10px;
  }
  .graph-list{
    margin-top: 20px;
    width: 100%;
    height: 400px;
  }
  .graph{
    width: 90%;
    height: 300px;
    background: #fff;
    margin-left: 5%;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
    padding: 5px 5px;
  }
  .charts1{
    width: 100%;
    height: 100%;
  }
  .charts2{
    width: 100%;
    height: 100%;
  }
  .radar-list{
    margin-top: -80px;
    height: 300px;
    width: 100%;
  }
  .radar-box{
    width: 48%;
    height: 100%;
    background: #fff;
    margin-top: 10px;
    float: left;
    margin-left: 30px;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
  .capacity{
    width: 100%;
    margin: 0 auto;
    height: 100%;
    text-align: center;
  }
  .statistic-box{
    width: 40%;
    height: 100%;
    float: left;
    margin-left: 20px;
    padding: 10px 10px;
  }
  .personal-card1{
    margin-top: 30px;
    width: 100%;
    height: 100px;
    background: #fff;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
  .personal-card2{
    width: 100%;
    height: 100px;
    margin-top: 30px;
    background: #fff;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
</style>
