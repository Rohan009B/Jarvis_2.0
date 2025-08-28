// document.addEventListener("DOMContentLoaded", function () {
//   // Initialize SiriWave
//   const siriWave = new SiriWave({
//     container: document.getElementById("siri-container"),
//     width: 740,
//     height: 300,
//     speed: 0.1,
//     amplitude: 1,
//     autostart: true,
//     style: 'ios9'
//   });

//   // Mic button logic
//   const micBtn = document.getElementById("micbtn");
//   const ovel = document.getElementById("mainContainer");
//   const siriWaveElement = document.getElementById("siriWave");
//   const micSound = document.getElementById("micSound");

//   micBtn.addEventListener("click", function () {
//     eel.TakeCommand(); // Trigger Python voice recognition
//     if (ovel) ovel.hidden = true;
//     if (siriWaveElement) siriWaveElement.hidden = false;
//     if (micSound) {
//       micSound.currentTime = 0;
//       micSound.play();
//     }
//   });

//   // Default greeting on load
//   DisplayMessage("Hello, I am Jarvis 2.0. Ask me anything...");
// });

// // Expose DisplayMessage to Python
// eel.expose(DisplayMessage);

// // Typing effect for dynamic messages
// function DisplayMessage(message) {
//   const siriMessage = document.querySelector(".siri-message");
//   if (siriMessage) {
//     // Stop previous typing if any
//     if (window.typingInterval) {
//       clearTimeout(window.typingInterval);
//       window.typingInterval = null;
//     }

//     siriMessage.textContent = ""; // Clear previous text
//     let i = 0;

//     function typeEffect() {
//       if (i < message.length) {
//         siriMessage.textContent += message.charAt(i);
//         i++;
//         window.typingInterval = setTimeout(typeEffect, 50);
//       }
//     }

//     typeEffect();

//     // Optional: Clear message after 3 seconds
//     setTimeout(() => {
//       siriMessage.textContent = "";
//     }, 3000);
//   }
// }

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