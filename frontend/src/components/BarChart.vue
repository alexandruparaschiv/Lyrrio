/* eslint-disable */

<template>
   <div>
     <apexchart  id="chart" width="400" type="bar" :options="chartOptions" :series="series"></apexchart>
   </div>
</template>

<script>

export default {
  name: "BarChart",
  components: {
   },
   props:['probabilities'],


   data: function() {
     return {
       bar:{
         horizontal:true,
       },
       showtext:false,
       info:null,
       chartOptions: {
         toolbar: {
           show: false,
           tools:{
             download:false,
           },
         },
         grid: {
           borderColor: 'white',
           strokeDashArray: 1,
           },


         colors: ["#02fae5"],

         xaxis: {
           type: "category",
           categories: ['Country', 'Hip Hop', 'Latin', 'Pop', 'Rock'],
           labels: {
             show:true,
             style:{
               colors:'white',
             },
           },
           title: {
             text:'',
             style:{
               color:'white',
               fontSize:'20px',
             },
           },
         },
         dataLabels: {
           enabled: false
         },
         yaxis: {
          labels: {
            show:true,
            formatter: function (value) {
              return value.toFixed(2);
            },
            style: {
              colors:'white',
            }
          },
          title:{
            text:'Genre',
            style:{
              color:'white',
              fontSize:'20px',
            },
          },
          },
          title:{
            text:'',
            style: {
              color:'white',
              fontSize:'20px',
            },
          },
          tooltip:{
            theme:false,
          }
     },
       series: [{
         name: 'Probability',
         data: [0,0,0,0,0],
       }]
     }
   },
   methods: {
     updateChart: function () {
          this.series = [{
                        name: 'Probability',
                        data: this.probabilities,
                        }];
     },
   },
   watch: {
     probabilities: function() {
       this.updateChart();
     }
   },
};
</script>
<style scoped>
#chart {
  max-width:500px;
  margin: 15px auto;

}
.chart .a.apexcharts-menu-icon {
  background: #1B213B;
  color: #fff;
}
.apexcharts-menu-icon{
  display:none;
}
</style>
