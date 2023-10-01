const likes = document.querySelectorAll(".like");

likes.forEach((like) => {
  const post = like.dataset.post;

  like.addEventListener("click", () => {
    $.ajax({
      type: "POST",
      url: `/api/like/posts/${post}`,
      data: JSON.stringify({ post: true }),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      async: false,
      success: function (response) {
        console.log(response);
        like.querySelector('span').style.color = 'red';
      },
      error: function () {
        console.log("an error occurred");
      },
    });
  });
});
