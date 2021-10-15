function onScanSuccess(decodedText, decodedResult) {
    console.log(`Code scanned = ${decodedText}`, decodedResult);
    // $.post( "/postmethod", {
    //     data: JSON.stringify(decodedText)
    //   }, function(err, req, resp){
    //     window.location.href = "/description/"+resp["responseJSON"]["itemid"];  
    //   });
    const URL = '/postmethod'
    const xhr = new XMLHttpRequest();
    sender = JSON.stringify(decodedText)
    xhr.open('POST', URL);
    xhr.send(sender);
}

var html5QrcodeScanner = new Html5QrcodeScanner(
	"qr-reader", { fps: 10, qrbox: 250 });
html5QrcodeScanner.render(onScanSuccess);