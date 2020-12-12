// let cloudinaryWidget = cloudinary.createUploadWidget({
//         cloudName: 'pixpimedia',
//         uploadPreset: 'widget-example',
//     },
//     function (error, result) {
//         console.log(error, result)
//     });

    // in the base head meta include the script src for the cloudinary widget
// add button with an onclick for cloudinaryWidget.open() in the view template for uploading to profile

// resource type indicates image/video/raw set to auto if cloudinary is to decide but preferable allow users to save to theit video or image or documents folders the type will be included in the asset url


// Cloudinary::Uploader.upload("sample_spreadsheet.xls",
// : resourse_type => :raw)
// : resourse_type => :auto)

// Cloudinary::Uploader.upload("sample.jpg",
// : resourse_type => :image,
// :folder => "user_uploads/admin/photos/nathan"
// :public_id => "sample_id" //specified filename 
// :use_filename => true, //use the current filename 
// :unique_filename => false)// don't add a suffix
// url
// https://res.cloudinary.com/pixpimedia/image/uplaod/sample.jpg

// images and videos can have transformatios done on them but raw files are returned as they are
//'https://res.cloudinary.com/pixpimedia/video/upload/v1607092605/Esse/user_uploads/sue/videos/nathan/1st_day_gr1.mov'