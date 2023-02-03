let mediaRecorder = NaN
let startBtn = document.getElementById("startBtn");
let stopBtn = document.getElementById("stopBtn");
let audioChunks = []

startBtn.onclick = async ()=>{
  await navigator.mediaDevices.getUserMedia({audio:true})
  .then((stream)=>{
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();
    audioChunks = [];

    mediaRecorder.addEventListener("dataavailable", (ev)=>{
      audioChunks.push(ev.data);
    });

    mediaRecorder.onstop = function(){
      let blob = new Blob(audioChunks, {'type':"audio/mp3"})
      audioChunks = [];
      let audioUrl = window.URL.createObjectURL(blob);
      var d = document.createElement('a');
      d.href = audioUrl;
      d.download = "myDownload";
      d.text = "Download"
      document.body.append(d);
    }
  }).catch((err)=>{
    window.alert(err.message);
  })
}

stopBtn.onclick = ()=>{
  mediaRecorder.stop();
}
