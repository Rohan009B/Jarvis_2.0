function DisplayMessage(message) {
    const $siriMessage = $(".siri-message");

    if ($siriMessage.length) {
        // Stop any ongoing typing animation
        if (window.typingInterval) {
            clearTimeout(window.typingInterval);
            window.typingInterval = null;
        }

        $siriMessage.text(""); // Clear previous text

        let i = 0;
        function typeEffect() {
            if (i < message.length) {
                $siriMessage.text($siriMessage.text() + message.charAt(i));
                i++;
                window.typingInterval = setTimeout(typeEffect, 50);
            }
        }

        typeEffect();

        // Optional: Hide after 3 seconds
        setTimeout(() => {
            $siriMessage.text("");
        }, 3000);
    }
}


function ShowHood() {
  console.log("ShowHood triggered");

  const mainContainer = document.getElementById("mainContainer");
  const siriWave = document.getElementById("siriWave");
  const jarvisHood = document.getElementById("jarvisHood");

  if (mainContainer) {
    mainContainer.removeAttribute("hidden");
  }

  if (siriWave) {
    siriWave.setAttribute("hidden", true);
  }

  if (jarvisHood) {
    jarvisHood.classList.add("animate-hood");
    setTimeout(() => {
      jarvisHood.classList.remove("animate-hood");
    }, 2000);
  }
}

eel.expose(ShowHood);


eel.expose(senderText)
function senderText(message){
  var chatbox = document.getElementById("chat-canvas-body");
  if (message.trim() != ""){
    chatbox.innerHTML += `<div class="row justify-contect-end mb-4">
    <div class="width-size">
    <div class="sender_message">${message}</div></div>`;

    chatbox.scrollTop = chatbox.scrollHeight;
  }
}

eel.expose(receiverMessage)
function receiverMessage(message){
  var chatbox = document.getElementById("chat-canvas-body");
  if (message.trim() != ""){
    chatbox.innerHTML += `<div class="row justify-contect-end mb-4">
    <div class="width-size">
    <div class="receiver_message">${message}</div></div>`;

    chatbox.scrollTop = chatbox.scrollHeight;
  }
}