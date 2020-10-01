// Paste this script inside console and see the magic :)
// From pinterest to insta, insta to magazines this script kills them all unless it's not CORS!
// If CORS policy is missing, shoot the payload!

var images = document.getElementsByTagName('img');
var i=0

while(images.length > i) {
	url = images[i].src
	name = images[i].alt
	i++;
	  
	
fetch(url)
  .then(resp => resp.blob())
  .then(blob => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    // the filename you want
    a.download = i+'.jpeg';
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    console.log(name); // or you know, something with better UX...
  })
  .catch(() => console.log('Failed'));
  function sleepThenAct(){ sleepFor(2000); console.log("hello js sleep !"); }
}
