button.onclick = function () {
    var startPos;
    var nudge = document.getElementById('nudge');
  
    var showNudgeBanner = function () {
      nudge.style.display = 'block';
    };
  
    var hideNudgeBanner = function () {
      nudge.style.display = 'none';
    };
  
    var nudgeTimeoutId = setTimeout(showNudgeBanner, 5000);
  
    var geoSuccess = function (position) {
      hideNudgeBanner();
      // We have the location, don't display banner
      clearTimeout(nudgeTimeoutId);
  
      // Do magic with location
      startPos = position;
      document.getElementById('startLat').innerHTML = startPos.coords.latitude;
      document.getElementById('startLon').innerHTML = startPos.coords.longitude;
    };
    var geoError = function (error) {
      switch (error.code) {
        case error.TIMEOUT:
          // The user didn't accept the callout
          showNudgeBanner();
          break;
      }
    };
  
    navigator.geolocation.getCurrentPosition(geoSuccess, geoError);
  };

  // check for Geolocation support
if (navigator.geolocation) {
    console.log('Geolocation is supported!');
  } else {
    console.log('Geolocation is not supported for this Browser/OS.');
  }