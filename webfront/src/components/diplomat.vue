<template>
  <div id="container" style="height: 100%; box-sizing: border-box"></div>
</template>

<script>
    export default {
        name: "diplomat",
        data(){
          return{
            loadingState:true,
            geoCoordMap:{},
            BJData:[],
            series: [],
            dser: []
          }
        },
      methods:{
          ConvertData:function(data){
            var that = this;
            var res = [];
            for(var i = 0; i < data.length; i++) {
                var dataItem = data[i];
                var fromCoord = that.geoCoordMap[dataItem[1].name];
                var toCoord = that.geoCoordMap[dataItem[0].name];
                if(fromCoord && toCoord) {
                    res.push([fromCoord, toCoord])
                }
            }
            return res;
          },
          Init_map:function(){
            var that = this;
            [['北京', that.BJData]].forEach(function(item, i) {
                that.dser.push({
                type: 'effectScatter',
                coordinateSystem: 'geo',
                zlevel: 3,
                rippleEffect: {
                    brushType: 'stroke'
                },
                label: {
                    fontSize:24,
                    show: true,
                    position: 'right',
                    formatter: '{b}'
                },
                itemStyle: {
                    normal: {
                        color: '#f5f802'
                    }
                },
                data: item[1].map(function(dataItem) {
                    return {
                        name: dataItem[1].name,
                        value: that.geoCoordMap[dataItem[1].name],
                        symbolSize: dataItem[1].value / 4
                    };
                })
            },{
                type: 'effectScatter',
                coordinateSystem: 'geo',
                zlevel: 3,
                rippleEffect: {
                    brushType: 'stroke'
                },
                label: {
                    normal: {
                        show: true,
                        position: 'left',
                        fontSize:18,
                        formatter: '{b}'
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#ff0000'
                    }
                },
                data: [{
                    name: item[0],
                    value: that.geoCoordMap[item[0]],
                    symbolSize:parseInt(Math.random()*20+10),
                    label: {
                        normal: {
                            position: 'right'
                        }
                    }
                }]
            });
            that.series.push({
                    type: 'lines3D',
                    effect: {
                        show: true,
                        period: 3,//速度
                        trailLength: 0.1//尾部阴影
                    },
                    lineStyle: {//航线的视图效果
                        color: '#9ae5fc',
                        width: 1,
                        opacity: 0.6
                    },
                    data: that.ConvertData(item[1])// 特效的起始、终点位置，一个二维数组，相当于coords: convertData(item[1])
                })
            });
          },
          Init_Graph:function () {
            this.Init_map();
            var that = this;
            var canvas = document.createElement('canvas');

            var myChart = this.$echarts.init(canvas, null, {
                width: 4096,
                height: 2048
            });
            myChart.setOption({
              backgroundColor: 'rgba(3,28,72,0.3)',
              title: {
                  show:true
              },
              geo: {
                  type: 'map',
                  map: 'world',
                  left:0,
                  top:0,
                  right: 0,
                  bottom: 0,
                  boundingCoords: [[-180, 90], [180, -90]],
                  zoom:0,
                  roam: false,
                  itemStyle: {
                      borderColor:'#000d2d',
                      normal: {
                          areaColor: '#2455ad',
                          borderColor:'#000c2d'
                      },
                      emphasis: {
                          areaColor: '#357cf8'
                      }
                  },
                  label:{
                      fontSize:24
                  }
              },
              series:that.dser
          });
            myChart.on('click', function (e) {
              that.$message(e.name);
              console.log(e)
            });

          var option = {
              backgroundColor: 'rgba(0,0,0,0)',//canvas的背景颜色
              globe: {
                  baseTexture:myChart,
                  top: 'middle',
                  left: 'center',
                  displacementScale: 0,
                  environment:'/static/picture/starfield.jpg',
                  shading: 'color',
                  viewControl: {
                      distance:240,
                      autoRotate: true
                  },
                  click(res) {
                    this.$message(res)
                  }
              },
              series:that.series
          };

          this.$echarts.init(document.getElementById("container")).setOption(option, true);
        }
      },
      mounted() {

      },
      created() {
          let that = this;
          this.$axios.post('api/map').then(function (res) {
            let positions = res.data.data;
            for (let i=0; i<positions.length; i++){
              if (positions[i][0] !== '北京'){
                let list = [];
                list.push({name: '北京'});
                list.push({name: positions[i][0], value: 100});
                that.BJData.push(list)
              }
              that.geoCoordMap[positions[i][0]] = [positions[i][2], positions[i][1]]
            }
            that.Init_Graph()
          })
      }
    }
</script>

<style scoped>

</style>
