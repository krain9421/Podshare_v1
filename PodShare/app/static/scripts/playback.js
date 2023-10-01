const audioPlayer = new Audio();
let currentPlayButton = null;

audioPlayer.addEventListener("ended", () => {
  pause(currentPlayButton);
});

async function play(playButton) {
  if (currentPlayButton) {
    pause(currentPlayButton);
  }
  currentPlayButton = playButton;
  playButton.querySelector("span").className = "fa fa-pause";
  if (audioPlayer.src.indexOf(playButton.dataset.audio) < 0) {
    audioPlayer.src = `/api/play/audio/${playButton.dataset.audio}`;
  }
  await audioPlayer.play();
}
async function pause(pauseButton) {
  pauseButton.querySelector("span").className = "fa fa-play";

  await audioPlayer.pause();
}

async function action(button) {
  if (button.querySelector("span").className == "fa fa-play") {
    await play(button);
  } else {
    await pause(button);
  }
}
