(function() {

    var width = 450; // We will scale the photo width to this
    var height = 0; // This will be computed based on the input stream

    var streaming = false;

    var video = null;


    function startup() {

        video = document.getElementById('video');
        canvas = document.getElementById('canvas');

        navigator.mediaDevices.getUserMedia({
                video: true,
                audio: false
            })
            .then(function(stream) {
                video.srcObject = stream;
                video.play();
            })
            .catch(function(err) {
                console.log("An error occurred: " + err);
            });




        video.addEventListener('canplay', function(ev) {
            if (!streaming) {
                height = video.videoHeight / (video.videoWidth / width);

                if (isNaN(height)) {
                    height = width / (4 / 3);
                }

                streaming = true;
            }
        }, false);

    }


    setInterval(takepicture, 10000); //take pic at every 10 sec

    function takepicture() {
        var context = canvas.getContext('2d');
        if (width && height) {

            canvas.width = width;
            canvas.height = height;

            context.drawImage(video, 0, 0, width, height);

            var data = canvas.toDataURL('image/png');




            var imgbase64data = data.replace('data:image/png;base64,', '');
            // create data
            senduserimg(imgbase64data)





            // call the api




        }
    }

    function senduserimg(data){
    var imgUrl = 'http://' + document.domain + ':' + location.port + '/getimg'; //uri

            var cameraData = {
                "imageFile": data
            };


            var imgheader = {

                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(cameraData),
                method: 'POST'
            }


             fetch(imgUrl, imgheader)
                .then(response => response.text())
                .then(data => console.log(data));

    }

    window.addEventListener('load', startup, false);
})();