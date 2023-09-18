$(
  $(".new-post").submit(function (e) {
    e.preventDefault();
  })
);

$(
  $(".post-button").click(function () {
    console.log("post button pressed");
    const audioFile = $(".audio-file")[0].files[0];
    const caption = $(".caption").val();

    const formData = new FormData();
    formData.append("audio", audioFile);
    formData.append("caption", caption);

    $.ajax({
      type: "POST",
      url: "/api/post",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        console.log(response);
        console.log("Successfully uploaded");
        showNotification(response.message)
      },
      error: function () {
        console.error("an Error occurred");
      },
    });
    setTimeout(() => {
      $(".audio-file").val("");
      $(".caption").val("");
    }, 10);
  })
);
