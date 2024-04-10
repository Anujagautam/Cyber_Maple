// video.js

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;

if (navigator.getUserMedia) {
  navigator.getUserMedia({ video: true }, handleVideo, videoError);
}

function handleVideo(stream) {
  var video = document.getElementById("videoElement");
  video.srcObject = stream;
}

function videoError(e) {
  console.error("Error accessing webcam:", e);
}
