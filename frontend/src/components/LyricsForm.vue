<template>
  <div class='genre'>
    <div class="container midway">
      <span class="text_1">Type in some lyrics :).</span>
       <form id="app"  @submit.prevent="predictGenre">
       <textarea id="name" v-model="lyrics" type="text" name="lyrics"
          rows="10" cols="33">
        </textarea>
        <p>
          <button class="btn btn-lg btn-primary  text-uppercase" type="submit">Guess genre</button>
        </p>
  </form>
     </div>
     {{genre}}
     <BarChart :probabilities="probabilities" />
  </div>
</template>

<script>
import axios from 'axios';
import BarChart from './BarChart.vue';
export default {
  name: "LyricsForm",
  components: {
    BarChart,
  },
  data: function(){
    return{
      lyrics:'',
      genre:'',
      probabilities:[10,0,0,0,0],
    }
  },

   methods: {
     predictGenre: function () {
         const self = this;
         axios({
           method: 'post',
           url: 'https://lyrbackend.herokuapp.com:/predict',
           data: {lyrics:this.lyrics},
           headers: {'Content-Type': 'multipart/form-data' }
           })
           .then(function (response) {
             self.genre = response['data']['genre'];
             self.updateProbs(response['data']['probabilities']);
           })
           .catch(function (response) {
             console.log(response);
           });
     },
     updateProbs: function(probs){
         const self = this;
         self.probabilities = probs;
     },
   },
}
</script>
<style scoped>

.btn {
  width:290px;
  height:200px;
  text-align: center;
  margin-top:8px;
  height:40px;
  font-family: Arial;
  background-color:purple;
  color:white;
  font-size:20px;
  border-radius: 20px;
  border:none;
  background-color: orange;
}

.btn:hover{
  background-color: #d4b85b;
}

input {
    margin-top: 5px;
    margin-bottom: 5px;
    display:inline-block;
    zoom:1;
    margin-left:20px;
    width:400px;
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    width: 100%;
    font-size: 36px;

resize: vertical;
}

label {
  color:white;
}

textarea{
  width: 600px;
	height: 120px;
	border: 3px solid #cccccc;
	padding: 5px;
	font-family: Tahoma, sans-serif;
	background-position: bottom right;
	background-repeat: no-repeat;
  background-color:white;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;
  resize: none;
  font-size:14px;
  font-weight:100;
}

table {
  text-align:center;
  margin-left:auto;
  margin-right:auto;
  margin-top:20px;
  margin-bottom:-65px;
  width:140px;
  border-collapse:separate;
  border-spacing:0 10px;
  background-color:#7c7e82;
  padding: 10px 10px 60px 10px;
  border-radius:15px;
}

tr {
  margin-top:20px;
  margin-bottom:20px;
}

.genre{
  color:white;
  font-size: 27px;
  font-weight: 200;
}



@keyframes typewriter {
  0%, 100% {
    width: 0;
  }
  20%, 80% {
    width: 10.2em;
  }
}

@keyframes caret {
  0%, 100% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
}

.text_1 {
  overflow: hidden;
  white-space: nowrap;
  animation: typewriter;
  display: inline-block;
  position: relative;
  animation-duration: 10s;
  animation-timing-function: steps(100, end);
  animation-iteration-count: infinite;
}

</style>
