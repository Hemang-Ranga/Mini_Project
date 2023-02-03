
navigator.mediaDevices.getUserMedia({audio:true})
.then((stream)=>{
  const mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.start();
  let chunks = [];

  mediaRecorder.addEventListener("dataavailable", (event)=>{
    chunks.push(event.data);
  });

  mediaRecorder.onstop = function(){
    const file = new File(chunks, 'test1.mp3');
    // const form = new FormData();
    // form.append("file", file);
    // fetch("",{
    //   method:"POST",
    //   body:form
    // })
    // let audioPlayer = document.getElementById("audioPlayer");
    // let startBtn = document.getElementById("startBtn");
    // let stopBtn = document.getElementById("stopBtn");
    let blob = new Blob(chunks,{'type':"audio/mp3"});
    chunks = [];
    let audioUrl = window.URL.createObjectURL(blob);
    // audioPlayer.src = audioUrl;
    // var x = document.createElement("AUDIO");
    // // x.src = audioUrl;
    // document.body.push(x);
    window.alert(audioUrl);
    var d = document.createElement('a');
    d.href = audioUrl;
    d.download = "myDownload";
    d.text = "Download"
    document.body.append(d);
  }
  setTimeout(function(){
    mediaRecorder.stop();
  },5000)
}).catch((err)=>{
  window.alert(err.message);
});
