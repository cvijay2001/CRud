
// validating the image + giving preview image
function validateForm() {
    var fileInput = document.getElementById('eprofilephoto');
    var filePath = fileInput.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;

    if (!allowedExtensions.exec(filePath)) {
        alert('Please upload an image file (jpg, jpeg, png, gif) only.');
        fileInput.value = '';
        return false; 
    }
    else 
  {
    // Image preview
    if (fileInput.files && fileInput.files[0]) {
      var reader = new FileReader();
      reader.onload = function(e) {
        document.getElementById(
          'imagePreview').innerHTML = 
          '<img width="160" height="160" src="' + e.target.result
          + '"/>';
      };
      
      reader.readAsDataURL(fileInput.files[0]);
    }
  }
}