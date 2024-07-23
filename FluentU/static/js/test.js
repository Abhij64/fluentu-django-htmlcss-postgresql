var skip = document.getElementById('skip');
var Score = document.getElementById('score');
var totalScore = document.getElementById('totalScore');
var countdown = document.getElementById('countdown');
var count = 0;
var scoreCount = 0;
var duration = 0;
var qaSet = document.querySelectorAll('.qa_set');
var qaAnsRow = document.querySelectorAll('.qa_set .qa_ans_row input');

skip.addEventListener('click', function () {
    step();
    duration = 10;
});

qaAnsRow.forEach(function (qaAnsRowSingle) {
    qaAnsRowSingle.addEventListener('click', function () {
        setTimeout(function () {
            step();
            duration = 10;
        }, 500);

        var valid = this.getAttribute("valid");
        if (valid == "valid") {
            scoreCount += 20;
            Score.innerHTML = scoreCount; // Update the displayed score
            totalScore.innerHTML = scoreCount;
        } else {
            scoreCount -= 20;
            Score.innerHTML = scoreCount; // Update the displayed score
            totalScore.innerHTML = scoreCount;
        }

    });
});


function step() {
    count += 1;
    for (var i = 0; i < qaSet.length; i++) {
        qaSet[i].className = 'qa_set';
    }
    qaSet[count].className = 'qa_set active';
    if (count == 5) {
        skip.style.display = 'none';
        clearInterval(durationTime);
        countdown.innerHTML = 0;
        showResult();
    }
}

var durationTime = setInterval(function () {
    if (duration == 10) {
        duration = 0;
    }
    duration += 1;
    countdown.innerHTML = duration;
    if (countdown.innerHTML == "10") {
        step();
    }
}, 1000);

function showResult() {
    var resultText = "";
    if (scoreCount < 60) {
        resultText = "Beginner Level";
    } else if (scoreCount >= 61 && scoreCount <= 150) {
        resultText = "Intermediate Level";
    } else {
        resultText = "Advanced Level";
    }
    
    // Print the result in the designated location
    var resultLocation = document.getElementById('result');
    if (resultLocation) {
        resultLocation.innerHTML = resultText;
        // Show the "Re-Take" and "Go Back" buttons
        var endButtons = document.getElementById('endButtons');
        if (endButtons) {
            endButtons.style.display = 'block';
        }
    } else {
        console.log(resultText);
    }
}

