var player;
var index = 0;

function onYouTubePlayerAPIReady() {
        player = new YT.Player('player', {
          height: '0',
          width: '0',
          videoId: {{ songs[index]['videoid'] }},
          events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
          }
        });
    }

    // autoplay video
function onPlayerReady(event) {
        event.target.playVideo();
    }

    // when video ends
function onPlayerStateChange(event) {        
        if(event.data === 0) {            
            index += 1;
            onYoutubePlayerAPIReady();
        }
    }
