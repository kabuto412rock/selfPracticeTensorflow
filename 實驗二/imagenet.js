const download = require('image-downloader')
var fs = require('fs')
fs.readFile('ok_urls.json', 'utf8', function (err, data) {
  var ok_urls = JSON.parse(data)
  console.log('ok_urls:', ok_urls)

  for (var i = 0; i < ok_urls.length; i++) {
    options = {
      url: ok_urls[i],
      dest: 'dog' + i + '.jpg' // Save to /path/to/dest/photo.jpg 
    }

    download.image(options)
      .then(({ filename, image }) => {
        console.log('File saved to', filename)
      }).catch((err) => {
      errCount += 1
      console.log('errCount = ', errCount)
    })
  }
  console.log('End... ')
})
