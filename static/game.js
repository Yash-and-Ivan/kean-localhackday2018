var currentReal;
var interval;
var current = 0;
var time_taken = 0.5;
var num_correct = 0;
var final_time = 0;

$(document).ready(function(){
    $("#flash").fadeOut(0);
    loadTweet(false);
    gameCountIn();
});
gameCountIn = function(){
  window.setTimeout(function(){
      $("#counter").text("2");
  }, 1000);
  window.setTimeout(function(){
      $("#counter").text("1");
  }, 2000);
  window.setTimeout(function(){
      $("#white-overlay").fadeOut();
      setCountDown();
  }, 3000);
};

checkAnswer = function(val){
    if(currentReal === val){
        $("#flash").css({
            "background": "green"
        });
        num_correct += 1;
    } else {
        $("#flash").css({
            "background": "red"
        })
    }
    $("#flash").fadeIn(50).fadeOut(250);

    // set new tweet
    current++;

    $("#game-bar")
  .css("width", ((current)/(numq))*100 + "%")
  .attr("aria-valuenow", (current)*100/(numq));

    if(current > numq - 1){
        clearInterval(interval);
        if(final_time == 0) {
            final_time = time_taken;
        }
        console.log("Time Taken:" + time_taken);
        console.log("Number of questions correctly answered: " + num_correct);

        // scale to 100
        /*
            questions/time
            max_time = 0.5*questions
            max_score = 2
            (questions/2*time) * 100
         */

        var score = Math.round(((num_correct/final_time)/(2 * numq)) * 1000)/10;

        $("#counter").text("Final Score: " + score);
        $("#white-overlay").fadeIn(2000);


    } else {
        loadTweet(true);
    }
};

loadTweet = function(countdown){
    $.get("/gettweet", {

    }, function(data, status){
        data = JSON.parse(data);
        //$("#tweet-text").fadeOut(100);
        //$("#tweet-rts").fadeOut(100);
        //$("#tweet-likes").fadeOut(100);
        $("#tweet-text").fadeOut(function(){
            $("#tweet-text").text(data.text);
            $("#tweet-rts").text(data.retweets);
            $("#tweet-likes").text(data.favorites);
            $("#tweet-date").text(data.date);

            clearInterval(interval);
            setCountDown();

            // $("#tweet-text").fadeIn();
            // $("#tweet-rts").fadeIn();
            // $("#tweet-likes").fadeIn();
            $("#tweet-text").fadeIn(function(){
                clearInterval(interval);
                if(countdown)
                    setCountDown();
            })
        });
        currentReal = data.is_real;
    })
};

setCountDown = function(){
    $("#loading-bar")
  .css("width", "100%")
  .attr("aria-valuenow", 10);

    var current_progress = 100;
  interval = setInterval(function() {
      current_progress -= 100/(total_time/0.5);
      //console.log("YEAH: " + current_progress);
      $("#loading-bar")
      .css("width", current_progress + "%")
      .attr("aria-valuenow", current_progress);
      if (current_progress < 0) {
          clearInterval(interval);
          checkAnswer(!currentReal);
      }
      time_taken += 0.5;
  }, 500);
};