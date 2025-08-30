document.addEventListener("DOMContentLoaded", function () {
  const siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 740,
    height: 300,
    speed: 0.1,
    amplitude: 1,
    autostart: true,
    style: 'ios9'
  });

  const micBtn = document.getElementById("micbtn");
  const ovel = document.getElementById("mainContainer");
  const siriWaveElement = document.getElementById("siriWave");
  const micSound = document.getElementById("micSound");

  micBtn.addEventListener("click", function () {
    eel.allCommands();
    if (ovel) ovel.hidden = true;
    if (siriWaveElement) siriWaveElement.hidden = false;
    if (micSound) {
      micSound.currentTime = 0;
      micSound.play();
    }
  });

  DisplayMessage("Hello, I am Jarvis 2.0. Ask me anything...");
});

eel.expose(DisplayMessage);

function DisplayMessage(message) {
  const siriMessage = document.querySelector(".siri-message");
  if (siriMessage) {
    if (window.typingInterval) {
      clearTimeout(window.typingInterval);
      window.typingInterval = null;
    }

    siriMessage.textContent = "";
    let i = 0;

    function typeEffect() {
      if (i < message.length) {
        siriMessage.textContent += message.charAt(i);
        i++;
        window.typingInterval = setTimeout(typeEffect, 50);
      }
    }

    typeEffect();

    setTimeout(() => {
      siriMessage.textContent = "";
    }, 3000);
  }
}

document.addEventListener('keyup', function (e) {
  if (e.key === 'j' && e.altKey) {
    const ovel = document.getElementById("mainContainer");
    const siriWaveElement = document.getElementById("siriWave");
    const micSound = document.getElementById("micSound");

    eel.allCommands();
    if (ovel) ovel.hidden = true;
    if (siriWaveElement) siriWaveElement.hidden = false;
    if (micSound) {
      micSound.currentTime = 0;
      micSound.play();
    }
  }
});


function PlayAssitant(message){
  if (message != ""){
    const ovel = document.getElementById("mainContainer");
    const siriWaveElement = document.getElementById("siriWave");
    const micSound = document.getElementById("micSound");

    eel.allCommands(message);
    if (ovel) ovel.hidden = true;
    if (siriWaveElement) siriWaveElement.hidden = false;
    if (chatbox) chatbox = "";
    if (micBtn) micBtn.hidden = false
    if (Sendbtn) Sendbtn.hidden =true
    if (micSound) {
      micSound.currentTime = 0;
      micSound.play();
    }
  }
}

function ShowHiddenButton(message) {
  const micBtn = document.getElementById("micbtn");
  const Sendbtn = document.getElementById("Sendbtn");

  if (message.length == 0) {
    if (micBtn) micBtn.hidden = false;
    if (Sendbtn) Sendbtn.hidden = true;
  } else {
    if (micBtn) micBtn.hidden = true;
    if (Sendbtn) Sendbtn.hidden = false;
  }
}

// Listen for typing inside chatbox
document.getElementById("chatbox").addEventListener("keyup", function(e) {
  let message = this.value; // same as $('#chatbox').val()
  ShowHiddenButton(message);
});

// Listen for Send button click
document.getElementById("Sendbtn").addEventListener("click", function(e) {
  let message = document.getElementById("chatbox").value;
  PlayAssitant(message);
});

document.getElementById("chatbox").addEventListener("keypress", function(e) {
  key = e.which;
  if (key == 13){
    let message = document.getElementById("chatbox").value;
    PlayAssitant(message);
  }
});